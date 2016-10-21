# by MH

import sys, fontforge

print "FontForge stdout extension registered"

class logFile(object) :

    def __init__(self) :
        self.buf = ""

    def write(self, txt) :
        self.buf = self.buf + txt
        i = self.buf.find("\n")
        while i >= 0 :
            fontforge.logWarning(self.buf[0:i].replace("%","%%"))
            if i < len(self.buf) :
                self.buf = self.buf[i+1:]
            else :
                self.buf = ""
            i = self.buf.find("\n")

    def writelines(self, txts) :
        for t in txts:
            self.write(t)

if fontforge.hasUserInterface() :
    sys.stdout = logFile()
    sys.stderr = sys.stdout