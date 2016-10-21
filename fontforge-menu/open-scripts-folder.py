#!/usr/bin/env python

import fontforge
from subprocess import Popen, PIPE

print "FontForge open python scripts folder extension registered"

def folder (dummy,font):
    subprocess.Popen(['xdg-open', '/home/nico/.config/fontforge/python/'], shell=False, stdin=subprocess.PIPE)

if fontforge.hasUserInterface():
    UIelement = ("Font","Glyph")
    keyShortcut=""
    menuText = "Open python scripts folder"
    fontforge.registerMenuItem(folder,None,None,UIelement,keyShortcut,menuText)

