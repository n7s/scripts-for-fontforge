#!/usr/bin/env python

import fontforge
from subprocess import Popen, PIPE

print "FontForge open font folders extension: registered"

def folder (dummy,font):
    if os.path.isdir('/home/nico/.fonts/'):
        subprocess.Popen(['xdg-open', '/home/nico/.fonts/'], shell=False, stdin=subprocess.PIPE)
    elif os.path.isdir('/home/nico/.local/share/fonts/'):
        subprocess.Popen(['xdg-open', '/home/nico/.local/share/fonts/'], shell=False, stdin=subprocess.PIPE)
    else:
        fontforge.logWarning("You need to create your font folders first: ~.fonts and ~.local/share/fonts")


if fontforge.hasUserInterface():
    UIelement = ("Font","Glyph")
    keyShortcut="Ctrl-Shft-O"
    menuText = "Open user font folders"
    fontforge.registerMenuItem(folder,None,None,UIelement,keyShortcut,menuText)
