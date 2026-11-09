"""Makes the published badge images, sized for how Nuvio draws them.

Nuvio draws every badge image 16dp tall, at most 92dp wide (ContentScale.Fit), and rounds
its corners at 6dp. So each badge:
  * has bigger text inside the same badge (zoom on the text block),
  * is cropped tight around the solid badge body, keeping just enough margin that
    Nuvio's 6dp corner rounding never cuts into the badge, with shadows faded out softly,
  * stays within the 92dp cap where it can: language badges keep their native script if slightly
    smaller text fits, otherwise they drop it; anything still too wide steps its text down.

python3 nuvio_size.py <outdir> [styles...]      (IDS="4k dual ..." limits badges for a quick test)
"""
import sys, os, json, asyncio, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render  # loads styles_extra too
from render import STYLES, page, badge_html, ROOT
from spec import B
import numpy as np
from PIL import Image

DPR = 4
CAP = 92 / 16            # widest aspect ratio Nuvio shows at full height
NUVIO_R = 6 / 16         # Nuvio's corner radius as a share of the image height
ZOOMS = [1.2, 1.15, 1.1, 1.05, 1.0, 0.95, 0.9, 0.85, 0.8]
PUBLISHED = {"obsidian": "Obsidian", "prism": "Prism", "neon": "Neon", "cinema": "Cinema", "liquid": "Liquid",
             "pixel": "Pixel", "vhs": "VHS", "keycap": "Keycap", "enamel": "Enamel", "glitch": "Glitch",
             "line": "Line", "dot": "Dot", "glyph": "Glyph"}

STACK_DROP = {"neon": 0.15, "keycap": 0.15}   # these styles have thicker top edges

LARGE_CSS = """
.cell { --pad: 22px !important; }
.txt { zoom: var(--z, 1.2); }
.stack { zoom: calc(var(--z, 1.2) - var(--sd, 0.1)); }
.nosuf .div, .nosuf .suffix { display: none; }
"""

FIT_JS = """
([zooms, cap, guess]) => {
  const out = {};
  const first = document.querySelector('.badge');
  const radius = parseFloat(getComputedStyle(first).borderTopLeftRadius) || 0;
  for (const c of document.querySelectorAll('.cell')) {
    const b = c.querySelector('.badge');
    const lang = c.dataset.lang === '1';
    const fits = () => { const r = b.getBoundingClientRect(); return (r.width + 2 * guess) / (r.height + 2 * guess) <= cap * 0.985; };
    let z = zooms[0], ok = false, nosuf = false;
    const tryZ = (list) => { for (const zz of list) { z = zz; b.style.setProperty('--z', z); if ((ok = fits())) return; } };
    if (lang && b.querySelector('.suffix')) {
      // keep the native script if a slightly smaller text still fits, otherwise drop it and go big again
      tryZ(zooms.filter(v => v >= 1.1));
      if (!ok) { b.classList.add('nosuf'); nosuf = true; tryZ(zooms); }
    } else tryZ(zooms);
    out[c.dataset.id] = { z, nosuf, ok };
  }
  return { radius, fit: out };
}
"""

def margin_px(body_h, radius):
    """Smallest margin (CSS px) that keeps a corner of radius `radius` inside Nuvio's rounding."""
    r = min(radius, body_h / 2)
    m = 0.3754 * (NUVIO_R * body_h - r)          # from (R - r)(1 - 1/sqrt2) with R = NUVIO_R * (body_h + 2m)
    return max(m + 1.0, 2.0)

def crop_and_fade(png, radius):
    im = Image.open(png).convert("RGBA")
    a = np.asarray(im).astype(np.float32)
    alpha = a[..., 3]
    solid = alpha > 150
    ys, xs = np.where(solid)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    M = int(round(margin_px((y1 - y0) / DPR, radius) * DPR))
    Y0, Y1, X0, X1 = max(y0 - M, 0), min(y1 + M, im.height), max(x0 - M, 0), min(x1 + M, im.width)
    yy, xx = np.mgrid[Y0:Y1, X0:X1]
    dx = np.maximum(np.maximum(x0 - xx, xx - (x1 - 1)), 0)
    dy = np.maximum(np.maximum(y0 - yy, yy - (y1 - 1)), 0)
    fade = np.clip(1 - np.sqrt(dx ** 2 + dy ** 2) / max(M, 1), 0, 1)
    out = a[Y0:Y1, X0:X1].copy()
    out[..., 3] = out[..., 3] * fade
    Image.fromarray(out.round().astype(np.uint8), "RGBA").save(png)
    return (X1 - X0) / (Y1 - Y0)

async def shoot(style, outdir, ids=None):
    from playwright.async_api import async_playwright
    items = [x for x in B if not ids or x["id"] in ids]
    render.CUR = STYLES[style]
    cells = "".join(f'<div class="cell" data-id="{x["id"]}" data-lang="{1 if x["group"] == "language" else 0}">{badge_html(x)}</div>' for x in items)
    f = os.path.join(ROOT, f"_nuvio_{style}.html"); open(f, "w").write(page(style, cells, LARGE_CSS + f".badge {{ --sd: {STACK_DROP.get(style, 0.1)}; }}"))
    d = os.path.join(outdir, PUBLISHED.get(style, style)); os.makedirs(d, exist_ok=True)
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get("CHROME") or None, args=["--no-sandbox"])
        pg = await br.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=DPR)
        await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
        first = await pg.evaluate("parseFloat(getComputedStyle(document.querySelector('.badge')).borderTopLeftRadius) || 0")
        res = await pg.evaluate(FIT_JS, [ZOOMS, CAP, margin_px(60, first)])
        await pg.wait_for_timeout(200)
        report = {}
        for el in await pg.query_selector_all(".cell"):
            bid = await el.get_attribute("data-id")
            path = os.path.join(d, bid.replace(".", "_") + ".png")
            await el.screenshot(path=path, omit_background=True)
            aspect = crop_and_fade(path, res["radius"])
            report[bid] = dict(res["fit"][bid], aspect=round(aspect, 3))
        await br.close()
    json.dump({"radius": res["radius"], "badges": report}, open(os.path.join(d, "_report.json"), "w"), indent=1)
    wide = [k for k, v in report.items() if v["aspect"] > CAP]
    print(f"{style}: {len(report)} badges, radius {res['radius']}, margin {margin_px(60, res['radius']):.1f}px, "
          f"suffix dropped {sum(v['nosuf'] for v in report.values())}, zoom<1.2 {sum(v['z'] < 1.2 for v in report.values())}, "
          f"still too wide {len(wide)} {wide[:6]}")

if __name__ == "__main__":
    outdir = sys.argv[1]; styles = sys.argv[2:] or list(PUBLISHED)
    ids = set(os.environ["IDS"].split()) if os.environ.get("IDS") else None
    for s in styles:
        asyncio.run(shoot(s, outdir, ids))
