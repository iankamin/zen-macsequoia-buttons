# MacSequoia Window Buttons

Makes Zen's minimize, maximize and close buttons look like the traffic lights
of the MacSequoia-Dark Aurorae window decoration, so Zen matches the rest of
your Plasma desktop.

- Red, yellow and green circles, 16px with 10px spacing, as in the theme
- The symbol (×, –, maximize/restore arrows) appears on the button under the
  pointer, and the circle darkens while pressed
- All three turn grey when the window loses focus

The button artwork is taken from the theme's own SVGs, one image per state.
Which side the buttons sit on still follows your KWin button layout.

## Regenerating

If the theme is updated, run `tools/extract.py` and then `tools/gen.py`. They
read `~/.local/share/aurorae/themes/MacSequoia-Dark/` and rewrite
`chrome.css`. `tools/` isn't needed by Zen.

## Notes

These are Zen's own buttons, restyled. If you'd rather use KWin's real
titlebar instead, set `browser.tabs.inTitlebar` to `0` in `about:config` and
don't install this mod.

Artwork from the MacSequoia KDE theme by vinceliuice (GPL-3.0).
