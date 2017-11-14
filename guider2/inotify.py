import ctypes, ctypes.util
import os
import select
import struct

#events as seen in <sys/inotify.h>
EventMask = {
    'IN_ACCESS' : 0x00000001,
    'IN_MODIFY' : 0x00000002,
    'IN_ATTRIB' : 0x00000004,
    'IN_CLOSE_WRITE' : 0x00000008,
    'IN_CLOSE_NOWRITE' : 0x00000010,
    'IN_OPEN' : 0x00000020,
    'IN_MOVED_FROM' : 0x00000040,
    'IN_MOVED_TO' : 0x00000080,
    'IN_CREATE' : 0x00000100,
    'IN_DELETE' : 0x00000200,
    'IN_DELETE_SELF' : 0x00000400,
    'IN_MOVE_SELF' : 0x00000800,
    'IN_ISDIR' : 0x40000000,
    'IN_UNMOUNT' : 0x00002000,
    'IN_Q_OVERFLOW' : 0x00004000,
    'IN_IGNORED' : 0x00008000

}

defaultMask = EventMask['IN_CLOSE_WRITE'] | \
              EventMask['IN_CLOSE_NOWRITE'] | \
              EventMask['IN_CREATE'] | \
              EventMask['IN_DELETE'] | \
              EventMask['IN_DELETE_SELF'] | \
              EventMask['IN_ISDIR'] | \
              EventMask['IN_MOVED_TO']


#glibc wrapper
def checkRet(value):
    if value < 0:
        error = os.strerror(ctypes.get_errno())
        raise Exception('Failed library call, returned %d. %s' % (value, error))
    return value

libc = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))

inotify_init = libc.inotify_init
inotify_init.argtypes = []
inotify_init.restype = checkRet

inotify_add_watch = libc.inotify_add_watch
inotify_add_watch.argtypes = [ ctypes.c_int, ctypes.c_char_p, ctypes.c_uint ]
inotify_add_watch.restype = checkRet

inotify_rm_watch = libc.inotify_rm_watch
inotify_rm_watch.argtypes = [ ctypes.c_int, ctypes.c_int ]
inotify_rm_watch.restype = checkRet

class Inotify:
    def __init__(self, period=1):
        self.inotify_fd = inotify_init()
        self.period = period
        self.epoll = select.epoll()
        self.epoll.register(self.inotify_fd, select.POLLIN)

        self.wdList = {} #dict key: path, val: fd
        self.eventbuf = ''

    def add_watch(self, path, recurse=False, mask = defaultMask):
        if not os.path.isdir(path):
            return -1
        wd = inotify_add_watch(self.inotify_fd, path, mask)
        if recurse:
            for paths,dirs,files in os.walk(path):
                self.add_watch(paths)
        self.wdList[path] = wd
        return wd

    def rm_wd(self, wd):
        inotify_rm_watch(self.inotify_fd, wd)

    def rm_watch(self, path, fname):
        wd = self.wdList[path + "/" + fname]
        if wd:
            del self.wdList[path + "/" + fname]

    def extractEvent(self, wd, e_type):
        HeaderFormat='iIII' # see <sys/inotify.h> for header structure
        HeaderSize=struct.calcsize(HeaderFormat)

        buf = os.read(wd, 2000)
        if not buf:
            return
        self.eventbuf += buf #add to existing buffer
        while True:
            if not self.eventbuf and len(self.eventbuf) < HeaderSize:
                return
            _wd, _mask, _cookie, _len = struct.unpack(HeaderFormat, self.eventbuf[:HeaderSize])
            if len(self.eventbuf) < HeaderSize + _len:
                return
            _fname = self.eventbuf[HeaderSize:_len+HeaderSize].rstrip('\0')
            self.eventbuf = self.eventbuf[HeaderSize + _len:] # already processed

            _path = ''
            for p_key,wd_val in self.wdList.iteritems():
                if wd_val == _wd:
                    _path = p_key
                    break
            self.doChanges(_mask, _path, _fname)
            yield (_mask, _path, _fname)

    def doChanges(self, mask, path, fname):
        if mask == EventMask['IN_CREATE'] | EventMask['IN_ISDIR']:
            self.add_watch(path + '/' + fname, True)
            return
        if mask == EventMask['IN_DELETE'] | EventMask['IN_ISDIR']:
            self.rm_watch(path, fname)
            return

    def getEventNames(self, event_mask):
        flags = []
        for key,value in EventMask.iteritems():
            if event_mask & value:
                flags.append(key)
        return flags

    def getEvents(self):
        while True:
            events = self.epoll.poll(self.period)
            for wd, e_type in events:
                for (mask, path, fname) in self.extractEvent(wd, e_type):
                    mask_list = self.getEventNames(mask)
                    yield(path + "/" +fname, mask_list)
            yield None


