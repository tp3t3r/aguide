#! /bin/sh

### BEGIN INIT INFO
# Provides:		autoguider
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		
# Short-Description:	Autoguider
### END INIT INFO

set -e

. /lib/lsb/init-functions

case "$1" in
  start)
    cp -r /home/pi/aguide /tmp/
    cd /tmp/aguide/guider2
    ./main.py    
	;;
  stop)
    killall python
	;;

  status)
	if [ -z "$(pgrep python)" ]; then
        echo 'not running'
    else
        echo 'running'
    fi
	;;

  *)
	echo "Usage: /etc/init.d/autoguider {start|stop|status}" || true
	exit 1
esac

exit 0