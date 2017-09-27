class InfoLog:
    def __init__(self, length=50, inittext=""):
        self.inittext = inittext
        self.len = length
        self.contents = []

    def get(self, token='\n'):
        return token.join(self.contents)

    def add(self, text):
        self.contents.append(str(text))
        self.contents = self.contents[-self.len:]
        with open('infolog.dat', 'w') as log:
            log.write(self.get())


