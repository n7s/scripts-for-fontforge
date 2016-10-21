#!/usr/bin/python

import os, sys, time, fontforge

print "FontForge fea export extension registered"

font = fontforge.activeFont()

def feaexport (dummy,font):
    name = font.fontname + "-" + font.weight + "-" + "exported" + time.strftime("-%Y-%m-%d-%H-%M") + ".fea"
    font.generateFeatureFile(name)
    msg = "Exported OpenType code to " + name +  ".\n" + "Check copyright and license before reusing any smart font code."
    fontforge.logWarning(msg)

if fontforge.hasUserInterface():
    keyShortcut=""
    menuText = "Export OpenType to FEA file"
    fontforge.registerMenuItem(feaexport,None,None,"Font",keyShortcut,menuText);



