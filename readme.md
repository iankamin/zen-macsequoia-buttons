# MacSequoia Window Buttons

Makes Zen's minimize, maximize and close buttons look like the traffic lights
of the MacSequoia-Dark Aurorae window decoration, so Zen matches the rest of
your Plasma desktop.

- Red, yellow and green circles, 16px with 10px spacing, as in the theme
- The symbol (×, –, maximize/restore arrows) appears on the button under the
  pointer, and the circle darkens while pressed
- All three turn grey when the window loses focus

The symbols are taken from the theme's own SVGs. Which side the buttons sit
on still follows your KWin button layout.

## Options

Each colour accepts any CSS colour (`#ff5f57`, `rgb(255 95 87)`, `tomato`).
Leave a field empty to use the theme's colour.

- **Close button colour**: default `#e9524a`
- **Minimize button colour**: default `#f1ae1b`
- **Maximize button colour**: default `#59c837`, also used for restore
- **Button colour when the window is inactive**: default `#5d5d5d`

These settings only appear when the mod is installed through Zen's Mods
page. If you use `chrome.css` as your `userChrome.css` instead, change the
fallback colours near the top of the file.

## Regenerating

If the theme is updated, run `tools/extract.py` and then `tools/gen.py`. They
read `~/.local/share/aurorae/themes/MacSequoia-Dark/` and rewrite
`chrome.css` and `preferences.json`. `tools/` isn't needed by Zen.

## Notes

These are Zen's own buttons, restyled. If you'd rather use KWin's real
titlebar instead, set `browser.tabs.inTitlebar` to `0` in `about:config` and
don't install this mod.

Artwork from the MacSequoia KDE theme by vinceliuice (GPL-3.0).
