# Builds ../chrome.css from the SVGs in tools/build/.
import os
from urllib.parse import quote
HERE=os.path.dirname(os.path.abspath(__file__))
btns={'close':'close','min':'minimize','max':'maximize','restore':'restore'}
sts=['normal','hover','pressed','inactive','hover-inactive']
def uri(f):
    s=open(os.path.join(HERE,'build',f)).read().replace('"',"'")
    return 'url("data:image/svg+xml,'+quote(s,safe=" '=:/;,.-()")+'")'
vars_=[]
for k,f in btns.items():
    for s in sts:
        vars_.append(f'  --tl-{k}-{s}: {uri(f"{f}-{s}.svg")};')
rules=[]
for k in btns:
    rules.append(f'''.titlebar-{k} {{ background-image: var(--tl-{k}-normal) !important; }}
.titlebar-{k}:hover {{ background-image: var(--tl-{k}-hover) !important; }}
.titlebar-{k}:hover:active {{ background-image: var(--tl-{k}-pressed) !important; }}
:root:-moz-window-inactive .titlebar-{k} {{ background-image: var(--tl-{k}-inactive) !important; }}
:root:-moz-window-inactive .titlebar-{k}:hover {{ background-image: var(--tl-{k}-hover-inactive) !important; }}''')
css=f'''/* MacSequoia Window Buttons
 * Draws Zen's minimize / maximize / close buttons as the traffic lights of
 * the MacSequoia-Dark Aurorae window decoration, so they match KWin's.
 * The button artwork is cut from that theme's close/minimize/maximize/
 * restore SVGs, one image per state. Regenerate with tools/extract.py then tools/gen.py if the theme
 * changes.
 */

:root {{
  --tl-button-size: 16px;   /* ButtonWidth / ButtonHeight in MacSequoia-Darkrc */
  --tl-button-gap: 10px;    /* ButtonSpacing */
{chr(10).join(vars_)}
}}

.titlebar-buttonbox {{
  align-items: center !important;
  gap: var(--tl-button-gap) !important;
  padding-inline: 8px !important;
}}

.titlebar-button {{
  appearance: none !important;
  align-self: center !important;
  width: var(--tl-button-size) !important;
  height: var(--tl-button-size) !important;
  min-width: var(--tl-button-size) !important;
  min-height: var(--tl-button-size) !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  border-radius: 0 !important;
  background-color: transparent !important;
  background-position: center !important;
  background-repeat: no-repeat !important;
  background-size: 100% 100% !important;
  opacity: 1 !important;
}}

/* The artwork includes the glyphs, so hide Zen's own icons */
.titlebar-button > image {{
  display: none !important;
}}

{chr(10).join(rules)}
'''
open(os.path.join(HERE,'..','chrome.css'),'w').write(css)
print(len(css))
