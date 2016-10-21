#!/usr/bin/python

import os, shutil, sys, time, fontforge, string, itertools, random

fontforge.setPrefs("AutoHint",False)
fontforge.setPrefs("ClearInstrsBigChanges",False)
fontforge.setPrefs("CopyTTFInstrs",False)

print "FontForge quick test install extension registered"

def genTestOTF(arg, ft):
   localFontdir='/.fonts/';
   fDir=os.path.expanduser("~")+localFontdir;
   ftActive=fontforge.activeFont();
   ftActive.save('temp.sfd');
   ft=fontforge.open('temp.sfd');
   aLayer=ft.layers[ft.activeLayer].name;
   ft.encoding='UnicodeBMP';
   ft.selection.all();
   for g in ft.selection.byGlyphs:
      g.removeOverlap();
      g.correctDirection();
      g.canonicalStart();
      g.canonicalContours();
   testname = 'test-' + time.strftime("%H-%M-%m-%d-%Y") + "-" + ft.fontname;
   ft.familyname = testname;
   ft.fullname = testname;
   ft.fontname = testname;
   # uniqueID
   # Fullname
   ft.appendSFNTName('English (US)', 'Version', testname);
   ft.appendSFNTName('English (US)', 'Descriptor', 'this is just a test version generated on' + time.strftime("%H-%M-%m-%d-%Y"));
   ft.appendSFNTName('English (US)', 'Compatible Full', testname );
   ft.appendSFNTName('English (US)', 'Preferred Family', testname );
   ft.appendSFNTName('English (US)', 'Fullname', testname );
   target=testname +'.otf';
   ft.generate(target, flags=('opentype','dummy-dsig','apple','no-hints','no-flex'),layer=aLayer)
   shutil.copy(target,fDir+target);
   ft.close();
   os.remove(target);
   os.remove('temp.sfd');
   print target + " generated and installed in ~/.fonts/ ";

if fontforge.hasUserInterface():
  #keyShortcut=""
  UIelement = ("Font","Glyph")
  menuText = "Generate test otf - drop in font folder"
  fontforge.registerMenuItem(genTestOTF,None,None,UIelement,keyShortcut,menuText);



