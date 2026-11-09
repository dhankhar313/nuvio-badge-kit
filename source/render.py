"""Badge renderer: builds HTML for each style, screenshots every badge as a transparent PNG,
and makes preview sheets. Usage: python3 render.py [styles...] [--preview-only]"""
import sys, os, re, json, asyncio, html
sys.path.insert(0, os.path.dirname(__file__))
from spec import B, GROUPS

ROOT = os.path.dirname(os.path.abspath(__file__))
NM = os.path.join(ROOT, "node_modules")
ICON_DIR = os.path.join(NM, "@phosphor-icons/core/assets")

HUES = {
 "source": ("#67e8f9", "#0891b2"), "resolution": ("#93c5fd", "#2563eb"), "hdr": ("#fde68a", "#f59e0b"),
 "dv": ("#f0abfc", "#a21caf"), "picture": ("#f9a8d4", "#db2777"), "codec": ("#6ee7b7", "#059669"),
 "audio": ("#c4b5fd", "#7c3aed"), "channels": ("#a5b4fc", "#4f46e5"), "language": ("#fdba74", "#ea580c"),
 "subtitles": ("#bae6fd", "#0284c7"), "edition": ("#fda4af", "#e11d48"), "service": ("#e5e7eb", "#6b7280"),
 "flags": ("#d4d4d8", "#52525b"), "delivery": ("#d9f99d", "#65a30d"), "live": ("#fca5a5", "#dc2626"),
 "container": ("#cbd5e1", "#475569"), "warn": ("#fca5a5", "#dc2626"),
}

def icon_svg(name, weight):
    p = os.path.join(ICON_DIR, weight, f"{name}-{weight}.svg" if weight != "regular" else f"{name}.svg")
    s = open(p).read()
    s = s.replace('opacity="0.2"', 'class="duo"')
    return s

FONTS = "".join(f'<link rel="stylesheet" href="file://{NM}/{p}">' for p in [
 "@fontsource-variable/geist/index.css", "@fontsource-variable/archivo/wdth.css",
 "@fontsource/noto-sans-devanagari/700.css", "@fontsource/noto-sans-tamil/700.css",
 "@fontsource/noto-sans-telugu/700.css", "@fontsource/noto-sans-malayalam/700.css",
 "@fontsource/noto-sans-kannada/700.css", "@fontsource/noto-sans-bengali/700.css",
 "@fontsource/noto-sans-jp/700.css", "@fontsource/noto-sans-kr/700.css", "@fontsource/noto-sans/700.css", "@fontsource/silkscreen/400.css", "@fontsource/silkscreen/700.css", "@fontsource-variable/pixelify-sans/index.css", "@fontsource/bebas-neue/400.css", "@fontsource/oswald/500.css", "@fontsource/oswald/700.css", "@fontsource/jetbrains-mono/700.css", "@fontsource/jetbrains-mono/800.css",
 "@fontsource/noto-sans-arabic/700.css", "@fontsource/noto-sans-hebrew/700.css", "@fontsource/noto-sans-thai/700.css", "@fontsource/noto-sans-sc/700.css", "@fontsource/noto-sans-tc/700.css", "@fontsource/noto-sans-gurmukhi/700.css", "@fontsource/noto-sans-gujarati/700.css", "@fontsource/noto-sans-oriya/700.css", "@fontsource/noto-sans-sinhala/700.css", "@fontsource/noto-sans-georgian/700.css", "@fontsource/noto-sans-armenian/700.css", "@fontsource/noto-sans-khmer/700.css", "@fontsource/noto-sans-lao/700.css", "@fontsource/noto-sans-myanmar/700.css", "@fontsource/noto-sans-ethiopic/700.css"])

FALLBACK = "'Noto Sans','Noto Sans Devanagari','Noto Sans Tamil','Noto Sans Telugu','Noto Sans Malayalam','Noto Sans Kannada','Noto Sans Bengali','Noto Sans Gurmukhi','Noto Sans Gujarati','Noto Sans Oriya','Noto Sans Sinhala','Noto Sans Arabic','Noto Sans Hebrew','Noto Sans Thai','Noto Sans Khmer','Noto Sans Lao','Noto Sans Myanmar','Noto Sans Georgian','Noto Sans Armenian','Noto Sans Ethiopic','Noto Sans JP','Noto Sans KR','Noto Sans SC','Noto Sans TC'"

BASE_CSS = f"""
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: transparent; }}
.cell {{ display: inline-block; padding: var(--pad, 10px); vertical-align: top; }}
.badge {{ position: relative; display: inline-flex; align-items: center; height: 60px; white-space: nowrap;
  font-family: 'Geist Variable', {FALLBACK}, sans-serif; color: #fff; }}
.main {{ font-weight: 800; font-size: 37px; letter-spacing: -0.5px; line-height: 1; }}
.stack {{ display: flex; flex-direction: column; justify-content: center; }}
.stack .main {{ font-size: 30px; }}
.kicker {{ font-weight: 750; font-size: 16px; letter-spacing: 2.6px; line-height: 1; margin-bottom: 2px; }}
.suffix {{ font-weight: 750; font-size: 19px; letter-spacing: 1.2px; line-height: 1; }}
.suffix.script {{ font-size: 23px; letter-spacing: 0; }}
.txt {{ display: flex; align-items: center; }}
.div {{ width: 2px; height: 28px; border-radius: 2px; margin: 0 11px 0 12px; flex: none; }}
.tile {{ flex: none; display: grid; place-items: center; position: relative; }}
.tile svg {{ display: block; }}
.duo {{ opacity: .38; }}
"""

STYLES = {}

STYLES["obsidian"] = dict(title="Obsidian", desc="Smoked glass, gradient icon tile, gold ring on Hero badges", icon="fill", pad=6, css="""
.badge { padding: 0 20px 0 7px; gap: 12px; border-radius: 17px; border: 1.5px solid transparent;
  background: radial-gradient(130% 170% at 0% 50%, var(--h2a) 0%, transparent 58%) padding-box,
              linear-gradient(180deg,#272b37 0%,#13151c 100%) padding-box,
              linear-gradient(180deg, rgba(255,255,255,.40) 0%, rgba(255,255,255,.07) 42%, var(--h2b) 100%) border-box;
  box-shadow: 0 2px 4px rgba(0,0,0,.30); }
.badge::after { content:''; position:absolute; inset:0; border-radius:16px; pointer-events:none;
  background: linear-gradient(180deg, rgba(255,255,255,.10) 0%, rgba(255,255,255,0) 48%); }
.tile { width: 45px; height: 45px; border-radius: 13px; background: linear-gradient(145deg,var(--h1),var(--h2));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), inset 0 -3px 6px rgba(0,0,0,.18), 0 2px 8px var(--h2a); }
.tile svg { width: 27px; height: 27px; color: #fff; filter: drop-shadow(0 1px 1px rgba(0,0,0,.25)); }
.main { background: linear-gradient(180deg,#ffffff 35%,#cdd3e0 100%); -webkit-background-clip:text; background-clip:text; color: transparent; }
.suffix, .kicker { color: var(--h1); }
.div { background: linear-gradient(180deg, transparent, var(--h1), transparent); opacity: .85; }
.t-info .tile { background: linear-gradient(145deg, var(--h2a), rgba(255,255,255,.04)); box-shadow: inset 0 0 0 1px var(--h2b), inset 0 1px 0 rgba(255,255,255,.18); }
.t-info .tile svg { color: var(--h1); filter: none; }
.t-hero { border-width: 2px; box-shadow: 0 0 6px rgba(240,196,92,.40), 0 2px 4px rgba(0,0,0,.30);
  background: radial-gradient(130% 170% at 0% 50%, var(--h2a) 0%, transparent 58%) padding-box,
              linear-gradient(180deg,#2b2a2a 0%,#15140f 100%) padding-box,
              linear-gradient(135deg,#fff4cf 0%,#e8bf57 22%,#8f6a1d 45%,#f6dc8c 62%,#b8892b 82%,#fff1c2 100%) border-box; }
.t-hero .main { background: linear-gradient(180deg,#fff9e6 15%,#f3d27a 62%,#d2a043 100%); -webkit-background-clip:text; background-clip:text; }
.t-hero .suffix, .t-hero .kicker { color: #f6d88a; }
.t-hero .div { background: linear-gradient(180deg, transparent, #f3cf73, transparent); }
.t-warn { background: radial-gradient(130% 170% at 0% 50%, rgba(220,38,38,.38) 0%, transparent 60%) padding-box,
              linear-gradient(180deg,#2f1c1f 0%,#170c0e 100%) padding-box,
              linear-gradient(180deg, rgba(255,160,150,.55) 0%, rgba(255,255,255,.06) 45%, rgba(220,38,38,.6) 100%) border-box; }
.t-warn .main { background: linear-gradient(180deg,#fff0ee 30%,#ffb4ab 100%); -webkit-background-clip:text; background-clip:text; }
""")

STYLES["prism"] = dict(title="Prism", desc="Glossy colour block joined to a dark label", icon="fill", pad=6, css="""
.badge { padding: 0 20px 0 0; gap: 15px; border-radius: 16px; overflow: hidden; background: linear-gradient(180deg,#1b1e27,#101218);
  box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.09), 0 2px 4px rgba(0,0,0,.30); }
.tile { width: 62px; height: 60px; background: linear-gradient(150deg,var(--h1) -10%,var(--h2) 85%);
  box-shadow: inset -1px 0 0 rgba(0,0,0,.30), inset 0 1.5px 0 rgba(255,255,255,.45); }
.tile::after { content:''; position:absolute; inset:0; background: linear-gradient(180deg, rgba(255,255,255,.22) 0%, rgba(255,255,255,0) 52%); }
.tile svg { width: 30px; height: 30px; color: #fff; filter: drop-shadow(0 1px 2px rgba(0,0,0,.3)); position: relative; z-index: 1; }
.main { color: #fff; }
.suffix, .kicker { color: var(--h1); }
.div { background: rgba(255,255,255,.18); }
.t-info .tile { background: linear-gradient(150deg, color-mix(in srgb, var(--h2) 55%, #2a2e39), color-mix(in srgb, var(--h2) 30%, #1a1d25)); }
.t-hero { box-shadow: inset 0 0 0 1.5px rgba(246,214,138,.75), 0 0 6px rgba(240,196,92,.35), 0 2px 4px rgba(0,0,0,.3);
  background: linear-gradient(180deg,#24211a,#121009); }
.t-hero .tile { background: linear-gradient(150deg,#fff1c2 -5%,#e7bb52 40%,#a77a22 100%); }
.t-hero .tile svg { color: #3b2a06; filter: drop-shadow(0 1px 0 rgba(255,255,255,.4)); }
.t-hero .main { background: linear-gradient(180deg,#fff9e6 15%,#f3d27a 62%,#d2a043 100%); -webkit-background-clip:text; background-clip:text; color: transparent; }
.t-hero .suffix, .t-hero .kicker { color: #f6d88a; }
.t-warn { background: linear-gradient(180deg,#2c1316,#170a0c); box-shadow: inset 0 0 0 1.5px rgba(255,120,110,.35), 0 2px 4px rgba(0,0,0,.3); }
.t-warn .tile { background: linear-gradient(150deg,#ff9a8c -10%,#dc2626 85%); }
""")

STYLES["neon"] = dict(title="Neon Tube", desc="Glowing tube on a smoked plate, readable on any artwork", icon="bold", pad=11, css="""
.badge { padding: 0 21px 0 15px; gap: 12px; border-radius: 18px; background: rgba(8,9,15,.86);
  border: 2px solid var(--h1); box-shadow: 0 0 4px var(--h1), 0 0 10px var(--h2), inset 0 0 9px var(--h2a); }
.tile svg { width: 28px; height: 28px; color: #fff; filter: drop-shadow(0 0 2px var(--h1)) drop-shadow(0 0 6px var(--h2)); }
.main { color: #fff; text-shadow: 0 0 1px #fff, 0 0 4px var(--h1), 0 0 10px var(--h2); }
.suffix, .kicker { color: var(--h1); text-shadow: 0 0 6px var(--h2); }
.div { background: var(--h1); box-shadow: 0 0 6px var(--h2); width: 2px; }
.t-info { border-width: 1.5px; box-shadow: 0 0 4px var(--h2), inset 0 0 6px var(--h2a); }
.t-info .main { text-shadow: 0 0 4px var(--h1), 0 0 10px var(--h2a); }
.t-hero { --h1:#ffe08a; --h2:#f59e0b; border-color: #ffe7a3; box-shadow: 0 0 4px #ffd36b, 0 0 11px #f59e0b, inset 0 0 10px rgba(245,158,11,.45); }
.t-warn { --h1:#ff8a80; --h2:#ef4444; }
""")

STYLES["cinema"] = dict(title="Cinema Spec", desc="Monochrome plaque, expanded type, like premium AV gear", icon="bold", pad=6, css="""
.badge { font-family: 'Archivo Variable', FALLBACK, sans-serif; font-stretch: 125%; padding: 0 19px 0 15px; gap: 12px; border-radius: 10px;
  border: 1.5px solid transparent;
  background: linear-gradient(180deg,#1a1b20 0%,#0a0a0c 100%) padding-box, linear-gradient(180deg,#f4f5f7 0%,#80858e 48%,#cfd3d9 100%) border-box;
  box-shadow: 0 2px 4px rgba(0,0,0,.30); }
.badge::after { content:''; position:absolute; inset:3.5px; border-radius:7px; border: 1px solid rgba(255,255,255,.07); pointer-events:none; }
.main { font-size: 30px; font-weight: 800; letter-spacing: .4px; background: linear-gradient(180deg,#ffffff 25%,#a9afb8 100%); -webkit-background-clip:text; background-clip:text; color: transparent; }
.stack .main { font-size: 25px; }
.kicker { font-size: 14px; letter-spacing: 3px; font-weight: 650; color: #a3a9b2; }
.suffix { font-size: 16px; letter-spacing: 2px; font-weight: 650; color: #a3a9b2; }
.div { width: 1.5px; background: linear-gradient(180deg, transparent, #9aa0aa, transparent); }
.tile svg { width: 27px; height: 27px; color: #dfe2e7; }
.t-info { background: linear-gradient(180deg,#16171b 0%,#0a0a0c 100%) padding-box, linear-gradient(180deg,#8d929a 0%,#3e4249 50%,#6f747c 100%) border-box; }
.t-info .main { background: linear-gradient(180deg,#e8eaee 25%,#9097a1 100%); -webkit-background-clip:text; background-clip:text; }
.t-hero { background: linear-gradient(180deg,#1d1a12 0%,#0b0a07 100%) padding-box, linear-gradient(135deg,#fff3cc 0%,#d9ad4f 30%,#7d5a17 52%,#f2d488 72%,#b0832a 100%) border-box; box-shadow: 0 0 6px rgba(230,186,90,.30), 0 2px 4px rgba(0,0,0,.30); }
.t-hero .main { background: linear-gradient(180deg,#fff8e1 20%,#e9c46a 70%,#c28f35 100%); -webkit-background-clip:text; background-clip:text; }
.t-hero .tile svg { color: #f1cf78; }
.t-hero .suffix, .t-hero .kicker { color: #d9b664; }
.t-warn { background: linear-gradient(180deg,#1f1011 0%,#0c0607 100%) padding-box, linear-gradient(180deg,#ffb3aa 0%,#b3261e 50%,#ff8a80 100%) border-box; }
.t-warn .main { background: linear-gradient(180deg,#ffe6e3 20%,#ff8a80 100%); -webkit-background-clip:text; background-clip:text; }
.t-warn .tile svg, .t-warn .suffix, .t-warn .kicker { color: #ff8a80; }
""".replace("FALLBACK", FALLBACK))

STYLES["liquid"] = dict(title="Liquid Glass", desc="Clear glass with a bright rim, made for posters and backdrops", icon="fill", pad=7, css="""
.badge { padding: 0 23px 0 7px; gap: 12px; border-radius: 999px;
  background: linear-gradient(180deg, rgba(255,255,255,.30) 0%, rgba(255,255,255,.10) 55%, rgba(255,255,255,.16) 100%), rgba(16,18,26,.38);
  border: 1.5px solid rgba(255,255,255,.55);
  box-shadow: inset 0 1.5px 0 rgba(255,255,255,.85), inset 0 -8px 16px rgba(255,255,255,.10), 0 2px 5px rgba(0,0,0,.25); }
.tile { width: 46px; height: 46px; border-radius: 50%; background: radial-gradient(120% 120% at 30% 20%, var(--h1) 0%, var(--h2) 75%);
  box-shadow: inset 0 1.5px 0 rgba(255,255,255,.7), inset 0 -4px 8px rgba(0,0,0,.18), 0 2px 6px rgba(0,0,0,.2); }
.tile svg { width: 26px; height: 26px; color: #fff; }
.main { color: #fff; text-shadow: 0 1px 2px rgba(0,0,0,.35); }
.suffix, .kicker { color: #fff; opacity: .85; text-shadow: 0 1px 2px rgba(0,0,0,.35); }
.div { background: rgba(255,255,255,.55); }
.t-info .tile { background: rgba(255,255,255,.22); box-shadow: inset 0 1px 0 rgba(255,255,255,.6); }
.t-hero { border-color: rgba(255,226,150,.95); background: linear-gradient(180deg, rgba(255,226,150,.38) 0%, rgba(255,200,90,.14) 60%, rgba(255,214,120,.22) 100%), rgba(30,22,8,.35);
  box-shadow: inset 0 1.5px 0 rgba(255,246,214,.95), 0 0 6px rgba(255,200,90,.45), 0 2px 5px rgba(0,0,0,.25); }
.t-hero .main { color: #fff8e6; }
.t-warn { border-color: rgba(255,150,140,.9); background: linear-gradient(180deg, rgba(255,120,110,.36), rgba(220,38,38,.18)), rgba(30,10,10,.35); }
""")

def badge_html(x):
    h1, h2 = HUES["warn"] if x["tier"] == "warn" else HUES[x["hue"]]
    style = f"--h1:{h1};--h2:{h2};--h2a:{h2}55;--h2b:{h2}aa"
    icon = icon_svg(x["icon"], CUR["icon"])
    lab = html.escape(x["label"])
    if x["sub"] and x["mode"] == "kicker":
        text = f'<div class="stack"><div class="kicker">{html.escape(x["sub"])}</div><div class="main">{lab}</div></div>'
    elif x["sub"]:
        sc = " script" if any(ord(c) > 0x590 for c in x["sub"]) else ""
        text = f'<div class="txt"><span class="main">{lab}</span><span class="div"></span><span class="suffix{sc}">{html.escape(x["sub"])}</span></div>'
    else:
        text = f'<div class="txt"><span class="main">{lab}</span></div>'
    return f'<div class="badge t-{x["tier"]}" style="{style}"><div class="tile">{icon}</div>{text}</div>'

def page(style_key, body, extra_css=""):
    global CUR
    CUR = STYLES[style_key]
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{FONTS}<style>{BASE_CSS}{CUR['css']}{extra_css}
.cell {{ --pad: {CUR['pad']}px; }}</style></head><body>{body}</body></html>"""

def all_badges_page(style_key):
    global CUR
    CUR = STYLES[style_key]
    cells = "".join(f'<div class="cell" data-id="{x["id"]}">{badge_html(x)}</div>' for x in B)
    return page(style_key, cells)

async def shoot_badges(styles, outdir):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        br = await p.chromium.launch(executable_path=os.environ.get("CHROME") or None, args=["--no-sandbox"])
        pg = await br.new_page(viewport={"width": 1400, "height": 900}, device_scale_factor=4)
        for s in styles:
            d = os.path.join(outdir, s); os.makedirs(d, exist_ok=True)
            f = os.path.join(ROOT, f"_page_{s}.html"); open(f, "w").write(all_badges_page(s))
            await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            for el in await pg.query_selector_all(".cell"):
                bid = await el.get_attribute("data-id")
                await el.screenshot(path=os.path.join(d, bid.replace(".", "_") + ".png"), omit_background=True)
            print("rendered", s, len(B))
        await br.close()

try:
    import styles_extra  # Pixel, VHS, Keycap, Enamel, Glitch
except ImportError:
    pass

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    styles = args or list(STYLES)
    asyncio.run(shoot_badges(styles, os.path.join(ROOT, "out")))
