# Quick Proofs

Currently, just a single, simple RoboFont script to save the current Space Center into a PDF in a DropBox folder. 

This allows for you to easily open and markup a simple proof in an iPad application such as Notability.

This will probably improve over time.

## Usage

1. Place in your RoboFont scripts folder.
2. Open the Space Center, and type some text to proof.
3. Make your proof in the Space Center window by zooming and resizing the window. Whatever is in view (without scrolling) will be what exports to a PDF.
4. If you want, edit the `imageDir` variable in [lines 20–21](https://github.com/thundernixon/quick-proofs/blob/master/space-center-to-cloud-pdf.py#L20-L21) in the main script to point to whatever path you'd like the proof PDF to save to. Currently, you can choose to save in iCloud or Dropbox, which makes it easy to quickly open on a secondary device or share with a collaborator.


## Credits

Inspired by a script from LettError (Erik van Blokland): [Export glyph image, edit on iPad, reimport as background image](https://forum.robofont.com/topic/646/export-glyph-image-edit-on-ipad-reimport-as-background-image)
