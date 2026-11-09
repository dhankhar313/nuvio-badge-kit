"""Extra styles: Pixel, VHS, Keycap, Enamel, Glitch, Line, Dot, Glyph."""
from render import STYLES, FALLBACK

STYLES["pixel"] = dict(title="Pixel", desc="Retro LED dot-matrix sign", icon="bold", pad=10, css="""
.badge { font-family: 'Pixelify Sans Variable', FALLBACK, monospace; padding: 0 18px; gap: 10px; border-radius: 6px;
  background: #07080b; border: 2px solid #20232c; box-shadow: inset 0 0 0 1px #000, inset 0 0 14px rgba(0,0,0,.9), 0 2px 4px rgba(0,0,0,.4); }
.badge::after { content:''; position:absolute; inset:2px; border-radius:4px; pointer-events:none;
  background-image: linear-gradient(rgba(255,255,255,.04) 50%, transparent 50%); background-size: 100% 4px; }
.tile { display: none; }
.main { font-weight: 500; font-size: 35px; letter-spacing: 2px; color: var(--h1); text-shadow: 0 0 2px var(--h1), 0 0 8px var(--h2a); }
.stack .main { font-size: 26px; }
.kicker { font-weight: 500; font-size: 15px; letter-spacing: 2px; color: color-mix(in srgb, var(--h1) 75%, #888); }
.suffix { font-weight: 500; font-size: 19px; letter-spacing: 1px; color: color-mix(in srgb, var(--h1) 75%, #888); text-shadow: 0 0 6px var(--h2); }
.suffix.script { font-family: FALLBACK, sans-serif; font-weight: 700; }
.div { width: 2px; background: #2b2f3a; }
.t-info .main { text-shadow: 0 0 3px var(--h2); color: color-mix(in srgb, var(--h1) 80%, #6b7280); }
.t-hero { border-color: #5b4710; } .t-hero .main { color: #ffd166; text-shadow: 0 0 2px #ffd166, 0 0 9px rgba(245,158,11,.6); }
.t-hero .suffix, .t-hero .kicker { color: #e6b955; }
.t-warn .main { color: #ff6b6b; text-shadow: 0 0 2px #ff6b6b, 0 0 9px rgba(220,38,38,.6); }
""".replace("FALLBACK", FALLBACK))

STYLES["vhs"] = dict(title="VHS", desc="Video-tape spine: retro stripes and a paper label", icon="fill", pad=8, css="""
.badge { font-family: 'Oswald', FALLBACK, sans-serif; padding: 0 7px 0 0; gap: 0; border-radius: 4px; background: linear-gradient(180deg,#1c1c20,#0e0e10);
  border: 1px solid #2c2c31; box-shadow: inset 0 1px 0 rgba(255,255,255,.07), 0 2px 4px rgba(0,0,0,.5); }
.tile { width: 54px; height: 58px; background: linear-gradient(118deg, transparent 0 16%, var(--h1) 16% 33%, var(--h2) 33% 50%, color-mix(in srgb, var(--h2) 55%, #000) 50% 67%, transparent 67%); }
.tile svg { display: none; }
.txt, .stack { background: linear-gradient(180deg,#f4f1e8,#e6e1d3); height: 44px; padding: 0 15px; border-radius: 2px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.08); }
.main { font-weight: 700; font-size: 31px; letter-spacing: .6px; color: #141414; text-transform: uppercase; }
.stack { justify-content: center; } .stack .main { font-size: 23px; line-height: .95; }
.kicker { font-weight: 500; font-size: 12px; letter-spacing: 2.4px; color: #5a5a5a; margin-bottom: 1px; }
.suffix { font-weight: 500; font-size: 17px; letter-spacing: 1px; color: #555; }
.suffix.script { font-family: FALLBACK, sans-serif; font-weight: 700; font-size: 19px; }
.div { width: 1.5px; height: 24px; background: rgba(0,0,0,.25); margin: 0 9px 0 10px; }
.t-info .tile { background: linear-gradient(118deg, transparent 0 16%, #8a909b 16% 33%, #5b616c 33% 50%, #353a42 50% 67%, transparent 67%); }
.t-info .txt, .t-info .stack { background: linear-gradient(180deg,#e2dfd7,#cfcbc0); }
.t-hero { border-color: #6b5520; } .t-hero .tile { background: linear-gradient(118deg, transparent 0 16%, #ffd166 16% 33%, #f78c40 33% 50%, #e63946 50% 67%, transparent 67%); }
.t-hero .txt, .t-hero .stack { background: linear-gradient(180deg,#fdf0c4,#f1d68a); } .t-hero .main { color: #2a1c02; }
.t-warn .txt, .t-warn .stack { background: linear-gradient(180deg,#fde4e1,#f6c9c4); } .t-warn .main { color: #861010; } .t-warn .suffix, .t-warn .kicker { color: #a32020; }
""".replace("FALLBACK", FALLBACK))

STYLES["keycap"] = dict(title="Keycap", desc="Mechanical keyboard keys; accent keys for Hero and warnings", icon="fill", pad=8, css="""
.badge { padding: 0 20px 7px 12px; gap: 11px; border-radius: 12px; background: linear-gradient(180deg,#1f2026,#121318);
  box-shadow: 0 3px 0 #08090b, 0 5px 8px rgba(0,0,0,.5); }
.badge::before { content:''; position:absolute; left:5px; right:5px; top:3px; bottom:10px; border-radius:9px;
  background: linear-gradient(180deg,#3b3e47 0%,#2b2d34 100%); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.12), inset 0 -2px 3px rgba(0,0,0,.25); }
.tile, .txt, .stack { position: relative; z-index: 1; }
.tile svg { width: 25px; height: 25px; color: var(--h1); }
.main { font-size: 32px; color: #f2f3f5; }
.stack .main { font-size: 27px; }
.suffix, .kicker { color: var(--h1); }
.div { background: rgba(255,255,255,.18); }
.t-info .tile svg { color: #9aa1ab; } .t-info .main { color: #c9cdd3; } .t-info .suffix, .t-info .kicker { color: #9aa1ab; }
.t-hero { background: linear-gradient(180deg,#a8781c,#7a5410); box-shadow: 0 3px 0 #4a3206, 0 0 9px rgba(242,193,78,.4), 0 5px 8px rgba(0,0,0,.5); }
.t-hero::before { background: linear-gradient(180deg,#ffe08a 0%,#f2c14e 100%); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.6), inset 0 -2px 3px rgba(120,80,0,.25); }
.t-hero .main { color: #2c1e02; } .t-hero .tile svg, .t-hero .suffix, .t-hero .kicker { color: #6b4a08; } .t-hero .div { background: rgba(44,30,2,.3); }
.t-warn { background: linear-gradient(180deg,#9c1c1c,#6e1010); box-shadow: 0 3px 0 #3e0707, 0 5px 8px rgba(0,0,0,.5); }
.t-warn::before { background: linear-gradient(180deg,#ef5350 0%,#d32f2f 100%); box-shadow: inset 0 1.5px 0 rgba(255,255,255,.35), inset 0 -2px 3px rgba(0,0,0,.2); }
.t-warn .main { color: #fff5f5; } .t-warn .tile svg, .t-warn .suffix, .t-warn .kicker { color: #ffd7d3; } .t-warn .div { background: rgba(255,255,255,.35); }
""")

STYLES["enamel"] = dict(title="Enamel", desc="Collectible enamel pins: glossy colour set in gold metal", icon="fill", pad=8, css="""
.badge { padding: 0 22px 0 7px; gap: 12px; border-radius: 999px; border: 3px solid transparent;
  background: linear-gradient(165deg, color-mix(in srgb, var(--h2) 78%, #000) 0%, color-mix(in srgb, var(--h2) 58%, #000) 55%, color-mix(in srgb, var(--h2) 38%, #000) 100%) padding-box,
              linear-gradient(135deg,#fff3c4 0%,#d9ab45 28%,#8a6420 50%,#f0d27a 70%,#b8892b 100%) border-box;
  box-shadow: 0 2px 4px rgba(0,0,0,.55), inset 0 -4px 7px rgba(0,0,0,.25); }
.badge::after { content:''; position:absolute; left:14px; right:14px; top:3px; height:42%; border-radius:999px; pointer-events:none;
  background: linear-gradient(180deg, rgba(255,255,255,.34), rgba(255,255,255,0)); }
.tile { width: 42px; height: 42px; border-radius: 50%; border: 2.5px solid transparent;
  background: radial-gradient(circle at 35% 30%, color-mix(in srgb, var(--h2) 60%, #000), color-mix(in srgb, var(--h2) 35%, #000)) padding-box,
              linear-gradient(135deg,#fff3c4,#c99a3a 45%,#f0d27a) border-box; }
.tile svg { width: 23px; height: 23px; color: #f6d88a; }
.main { background: linear-gradient(180deg,#fff8dc 10%,#f2d27a 55%,#c4962f 100%); -webkit-background-clip:text; background-clip:text; color: transparent;
  filter: drop-shadow(0 1.5px 0 rgba(0,0,0,.45)); }
.suffix, .kicker { color: #fbe6a6; filter: drop-shadow(0 1px 0 rgba(0,0,0,.4)); }
.div { background: linear-gradient(180deg,#fff3c4,#b8892b); opacity: .8; }
.t-info { background: linear-gradient(165deg,#4a4f59 0%,#30343c 55%,#1e2127 100%) padding-box, linear-gradient(135deg,#ffffff 0%,#b9c0c9 30%,#6b727c 50%,#e3e7ec 72%,#8d949e 100%) border-box; }
.t-info .tile { background: radial-gradient(circle at 35% 30%,#3a3f48,#1d2026) padding-box, linear-gradient(135deg,#fff,#8d949e 45%,#e3e7ec) border-box; }
.t-info .tile svg { color: #dfe3e8; }
.t-info .main { background: linear-gradient(180deg,#ffffff 10%,#d5dae1 55%,#9aa1ab 100%); -webkit-background-clip:text; background-clip:text; }
.t-info .suffix, .t-info .kicker { color: #dfe3e8; }
.t-hero { background: linear-gradient(165deg,#2a2f3d 0%,#141821 55%,#07090d 100%) padding-box, linear-gradient(135deg,#fff6d6 0%,#f0c95e 28%,#9a6d18 50%,#ffe39a 70%,#c99630 100%) border-box;
  box-shadow: 0 0 9px rgba(240,200,90,.45), 0 2px 4px rgba(0,0,0,.55); }
.t-hero .tile { background: radial-gradient(circle at 35% 30%,#2a2f3d,#07090d) padding-box, linear-gradient(135deg,#fff6d6,#c99630 45%,#ffe39a) border-box; }
.t-warn { background: linear-gradient(165deg,#f0605a 0%,#c62828 55%,#7f1414 100%) padding-box, linear-gradient(135deg,#ffffff 0%,#c2c8d0 30%,#6b727c 50%,#e3e7ec 72%,#8d949e 100%) border-box; }
.t-warn .tile { background: radial-gradient(circle at 35% 30%,#7f1414,#3e0808) padding-box, linear-gradient(135deg,#fff,#8d949e 45%,#e3e7ec) border-box; }
.t-warn .tile svg { color: #ffd7d3; }
.t-warn .main { background: linear-gradient(180deg,#ffffff 10%,#f1f3f5 55%,#c9ced5 100%); -webkit-background-clip:text; background-clip:text; }
.t-warn .suffix, .t-warn .kicker { color: #ffe3e0; }
""")

STYLES["glitch"] = dict(title="Glitch", desc="Cyberpunk terminal: RGB-split text and scanlines", icon="bold", pad=8, css="""
.badge { font-family: 'JetBrains Mono', FALLBACK, monospace; padding: 0 18px 0 13px; gap: 11px; border-radius: 3px;
  background: linear-gradient(180deg,#0d0e14,#07080c); border: 1px solid #23252f; border-left: 5px solid var(--h1);
  box-shadow: 0 2px 4px rgba(0,0,0,.5), -2px 0 8px var(--h2a); }
.badge::after { content:''; position:absolute; inset:0; pointer-events:none; border-radius: 2px;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,.035) 0 1px, transparent 1px 3px); }
.tile svg { width: 25px; height: 25px; color: var(--h1); filter: drop-shadow(-1.5px 0 0 rgba(255,0,90,.7)) drop-shadow(1.5px 0 0 rgba(0,229,255,.7)); }
.main { font-weight: 800; font-size: 32px; letter-spacing: -0.5px; color: #f5f7ff; text-shadow: -2px 0 rgba(255,0,90,.85), 2px 0 rgba(0,229,255,.85); }
.stack .main { font-size: 27px; }
.kicker { font-weight: 700; font-size: 14px; letter-spacing: 2px; color: var(--h1); }
.suffix { font-weight: 700; font-size: 18px; letter-spacing: .5px; color: var(--h1); }
.suffix.script { font-family: FALLBACK, sans-serif; }
.div { width: 2px; background: #2c2f3b; }
.t-info { border-left-color: #6b7280; box-shadow: 0 2px 4px rgba(0,0,0,.5); } .t-info .main { color: #c9cdd6; text-shadow: -1px 0 rgba(255,0,90,.5), 1px 0 rgba(0,229,255,.5); }
.t-hero { border-left-color: #ffd166; border-color: #4a3d15; box-shadow: 0 2px 4px rgba(0,0,0,.5), -2px 0 10px rgba(255,209,102,.5); }
.t-hero .main { color: #ffe9a8; text-shadow: -2px 0 rgba(255,60,120,.8), 2px 0 rgba(255,190,40,.8); } .t-hero .tile svg, .t-hero .suffix, .t-hero .kicker { color: #ffd166; }
.t-warn { border-left-color: #ff4d4d; } .t-warn .main { color: #ffdede; text-shadow: -2px 0 rgba(255,0,60,.95), 2px 0 rgba(255,140,0,.6); }
""".replace("FALLBACK", FALLBACK))

def css(s): return s.replace("FALLBACK", FALLBACK)

# Minimal: outline only, coloured by group, small line icon.
STYLES["line"] = dict(title="Line", desc="Minimal: thin coloured outline, line icon", icon="bold", pad=6, css=css("""
.badge { padding: 0 22px 0 16px; gap: 10px; border-radius: 12px; background: rgba(12,13,17,.6); border: 2.5px solid var(--h1); }
.tile { width: 28px; height: 28px; } .tile svg { width: 28px; height: 28px; color: var(--h1); }
.main { font-weight: 700; letter-spacing: -.2px; color: #fff; }
.kicker, .suffix { font-weight: 650; color: var(--h1); }
.div { width: 2px; background: color-mix(in srgb, var(--h1) 45%, transparent); }
.t-info { border-color: rgba(255,255,255,.30); } .t-info .tile svg, .t-info .kicker, .t-info .suffix { color: rgba(255,255,255,.6); }
.t-info .main { color: rgba(255,255,255,.78); }
.t-hero { border-color: #f6c453; } .t-hero .main { color: #f6c453; } .t-hero .tile svg, .t-hero .kicker, .t-hero .suffix { color: #f6c453; }
.t-warn { border-color: #ff6b6b; } .t-warn .main { color: #ff8585; } .t-warn .tile svg, .t-warn .kicker, .t-warn .suffix { color: #ff8585; }
"""))

# Minimal: soft pill with a coloured dot for the group.
STYLES["dot"] = dict(title="Dot", desc="Minimal: soft pill with a coloured dot", icon="fill", pad=6, css=css("""
.badge { padding: 0 24px 0 20px; gap: 13px; border-radius: 999px; background: rgba(30,32,40,.94); border: 1.5px solid rgba(255,255,255,.07); }
.tile { width: 13px; height: 13px; border-radius: 50%; background: var(--h2); box-shadow: 0 0 0 4px color-mix(in srgb, var(--h2) 28%, transparent); }
.tile svg { display: none; }
.main { font-weight: 650; letter-spacing: -.2px; color: #eef0f3; }
.kicker, .suffix { font-weight: 600; color: rgba(255,255,255,.5); }
.div { width: 2px; background: rgba(255,255,255,.14); }
.t-info .main { color: rgba(255,255,255,.7); } .t-info .tile { background: #8b93a3; box-shadow: 0 0 0 4px rgba(139,147,163,.22); }
.t-hero .tile { background: #f6c453; box-shadow: 0 0 0 4px rgba(246,196,83,.3); } .t-hero .main { color: #fff3d1; }
.t-warn .tile { background: #ff5a5a; box-shadow: 0 0 0 4px rgba(255,90,90,.3); } .t-warn .main { color: #ffb4b4; }
"""))

# Icon-led: the icon does the talking, big and coloured; the word is secondary.
STYLES["glyph"] = dict(title="Glyph", desc="Icon-led: a big coloured symbol first, the word second", icon="fill", pad=6, css=css("""
.badge { padding: 0 20px 0 0; gap: 12px; border-radius: 14px; background: rgba(18,20,26,.92); overflow: hidden; }
.tile { width: 60px; height: 60px; background: linear-gradient(150deg, var(--h1) -20%, var(--h2) 75%); }
.tile svg { width: 40px; height: 40px; color: #fff; filter: drop-shadow(0 1px 1px rgba(0,0,0,.3)); }
.main { font-weight: 700; letter-spacing: -.3px; color: #fff; font-size: 33px; }
.stack .main { font-size: 27px; }
.kicker { color: var(--h1); font-size: 14px; } .suffix { color: var(--h1); font-weight: 650; }
.div { width: 2px; background: rgba(255,255,255,.18); }
.t-info .tile { background: linear-gradient(150deg, #9aa3b2 -20%, #4b5262 75%); } .t-info .main { color: rgba(255,255,255,.78); }
.t-hero .tile { background: linear-gradient(150deg, #ffe08a -20%, #d99a1e 75%); } .t-hero .kicker, .t-hero .suffix { color: #f6c453; }
.t-warn .tile { background: linear-gradient(150deg, #ff9a9a -20%, #d93636 75%); } .t-warn .main { color: #ffb4b4; }
"""))

STYLES["vhs"]["flag_css"] = ".flag .tile { width: 46px; height: 46px; border-radius: 4px; margin-left: 6px; }"

STYLES["dot"]["flag_css"] = ".flag .tile { width: 32px; height: 32px; border-radius: 50%; box-shadow: 0 0 0 2px rgba(255,255,255,.15) !important; }"

STYLES["line"]["flag_css"] = ".flag .tile { width: 34px; height: 34px; border-radius: 7px; }"
