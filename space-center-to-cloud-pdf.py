# menuTitle : Space Center PDF Export to Cloud
# shortCut  : command+control+shift+e
"""
  Saves the current Space Center as a PDF in DropBox, so you can open it in an iPad app such as Notability and annotate / make markups.

  Inspired by / started with code from LettError and RafalBuchner.
  
  https://forum.robofont.com/topic/646/export-glyph-image-edit-on-ipad-reimport-as-background-image
  https://gist.github.com/LettError/d0d2688abe959595a88b3fdb85c18db3
"""

import datetime
import os
from os.path import expanduser
from mojo.UI import CurrentSpaceCenter, SpaceCenterToPDF

timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

home = expanduser("~")
# imagesDir = "Library/Mobile Documents/com~apple~CloudDocs/RoboFont/" # if you prefer iCloud
imagesDir = "Dropbox/RoboFont" # if you prefer DropBox

path = os.path.join(home, imagesDir)

if not os.path.exists(path):
        os.makedirs(path)
        
f = CurrentFont()
sp = CurrentSpaceCenter()

if f is not None and sp is not None:
    ufoName = os.path.basename(f.path)
    ufoName = ufoName.replace(".ufo", "_images")
    #print(ufoName)
    ufoImagesPath = os.path.join(path, ufoName)
    print("exporting to", ufoImagesPath)
    if not os.path.exists(ufoImagesPath):
        os.makedirs(ufoImagesPath)

    pdfName = os.path.join(ufoImagesPath, f"{ufoName}-space_center-{timestamp}.pdf")
    
    SpaceCenterToPDF(pdfName, spaceCenter=None, currentFontOnly=False)
