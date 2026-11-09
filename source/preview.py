"""Preview sheets rendered from live HTML (fast). python3 preview.py [styles...]"""
import sys, os, asyncio
sys.path.insert(0, os.path.dirname(__file__))
import render
from render import STYLES, badge_html, page, ROOT
from spec import B
BY = {x["id"]: x for x in B}

ROWS = [
 ("Hero", "Best quality. Gold finish, max 2-3 per stream", ["4k","remux","dolby-vision","atmos","imax-enhanced","dtsx","cached","live"]),
 ("Core", "The facts people pick a stream by", ["1080p","webdl","web","bluray","hdr10plus","hdr10","hlg","truehd","ddp","dts-hd-ma","7.1","5.1","av1","dual","hindi","extended","3d"]),
 ("Info", "Quiet detail, often hidden", ["hevc","10bit","aac","opus","2.0","esub","tamil","japanese","3d-hsbs","netflix","jiohotstar","proper","realdebrid","mkv"]),
 ("Warn", "Low quality or a playback risk", ["cam","telesync","dv-only","upscaled","line-audio","uncached","xvid"]),
]

def sheet(style_key, rows=ROWS, title=None):
    st = STYLES[style_key]
    render.CUR = st
    poster = style_key == "liquid"
    rows_html = ""
    for name, desc, ids in rows:
        cells = "".join(f'<div class="cell">{badge_html(BY[i])}</div>' for i in ids)
        rows_html += f'<div class="row"><div class="lab"><b>{name}</b><span>{desc}</span></div><div class="grid">{cells}</div></div>'
    bg = ("radial-gradient(700px 420px at 15% 20%, #f59e0b 0%, transparent 60%), radial-gradient(800px 500px at 85% 25%, #0ea5e9 0%, transparent 62%),"
          "radial-gradient(900px 520px at 50% 95%, #be185d 0%, transparent 60%), linear-gradient(180deg,#2b2f45,#141621)") if poster else \
         "radial-gradient(900px 500px at 10% 0%, rgba(80,90,140,.18), transparent 60%), linear-gradient(180deg,#101218,#0a0b0f)"
    css = f"""
body {{ background: #0a0b0f; }}
.sheet {{ width: 1600px; padding: 48px 56px 40px; background: {bg}; font-family: 'Geist Variable', sans-serif; color: #fff; }}
h1 {{ font-size: 40px; font-weight: 800; letter-spacing: -.6px; }} h1 span {{ color: rgba(255,255,255,.5); font-weight: 600; }}
.sub {{ font-size: 18px; color: rgba(255,255,255,.62); margin: 8px 0 26px; }}
.row {{ display: flex; gap: 24px; padding: 18px 0; border-top: 1px solid rgba(255,255,255,.08); }}
.lab {{ width: 190px; flex: none; padding-top: 14px; }}
.lab b {{ display: block; font-size: 17px; letter-spacing: 2.5px; text-transform: uppercase; color: rgba(255,255,255,.85); }}
.lab span {{ display: block; font-size: 13.5px; color: rgba(255,255,255,.5); margin-top: 6px; line-height: 1.35; }}
.grid {{ zoom: .66; flex: 1; }}
.foot {{ margin-top: 18px; font-size: 14px; color: rgba(255,255,255,.45); }}
"""
    body = f'<div class="sheet"><h1>Nuvio Badge Kit <span>· {st["title"]}</span></h1><div class="sub">{st["desc"]}. {len(B)} badges in this style; a sample shown by tier.</div>{rows_html}<div class="foot">Original designs with plain-text labels, not official Dolby, DTS or IMAX logos.</div></div>'
    return page(style_key, body, css)

async def main(styles):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get("CHROME") or None, args=["--no-sandbox"])
        pg = await br.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=2)
        os.makedirs(os.path.join(ROOT, "previews"), exist_ok=True)
        for s in styles:
            f = os.path.join(ROOT, f"_prev_{s}.html"); open(f, "w").write(sheet(s))
            await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            el = await pg.query_selector(".sheet")
            await el.screenshot(path=os.path.join(ROOT, "previews", f"preview-{s}.png"))
            print("preview", s)
        await br.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:] or list(STYLES)))
