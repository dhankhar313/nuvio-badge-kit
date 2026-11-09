"""Build Nuvio/Fusion badge manifests. python3 manifests.py <base_url> <ext>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from spec import B, GROUPS

ORDER = ["delivery", "resolution", "hdr", "picture", "audio", "channels", "source",
         "codec", "subtitles", "edition", "service", "flags"]
LIVE = ["live", "container"]
LAST = ["language"]  # many possible languages, so they go at the end of the row
LANG_FIRST = ["line-audio", "dual", "multi", "original", "dubbed"]
LANG_LEAD = ["english", "hindi"]  # first among the languages themselves

def lang_rank(x):
    """Order inside the language block: audio-track badges, English, Hindi, international
    languages, then the other Indian languages (there are many, so they go last)."""
    if x["id"] in LANG_FIRST: return (0, LANG_FIRST.index(x["id"]))
    if x["id"] in LANG_LEAD: return (1, LANG_LEAD.index(x["id"]))
    if x.get("flag") == "in": return (3, B.index(x))
    return (2, B.index(x))
TIER_RANK = {"hero": 0, "warn": 1, "core": 2, "info": 3}
GNAME = dict(GROUPS)
STYLES = {"obsidian": "Obsidian", "prism": "Prism", "neon": "Neon", "cinema": "Cinema", "liquid": "Liquid",
          "pixel": "Pixel", "vhs": "VHS", "keycap": "Keycap", "enamel": "Enamel", "glitch": "Glitch",
          "line": "Line", "dot": "Dot", "glyph": "Glyph"}

# Nuvio caches badge images forever by URL, so new artwork goes in a new folder.
# People who paste their link again get it; old links keep working from the old folders.
IMAGES = "v2/"

# Flag language badges are new artwork too, so they get their own file names.
def fname(x): return x["id"].replace(".", "_") + ("-flag" if x.get("flag") else "")

def build(style, base, ext, groups, enable):
    items = sorted([x for x in B if x["group"] in groups],
                   key=lambda x: (groups.index(x["group"]),) + (lang_rank(x) if x["group"] == "language" else (0, B.index(x))))
    return {
        "groups": [{"id": g, "name": GNAME[g], "color": "#00000000", "borderColor": "#00000000", "isExpanded": True} for g in groups],
        "filters": [{
            "id": x["id"], "groupId": x["group"], "name": x["name"], "pattern": x["pattern"],
            "imageURL": f"{base}/{IMAGES}{STYLES[style]}/{fname(x)}.{ext}",
            "tagColor": "#00000000", "borderColor": "#00000000", "textColor": "#00000000",
            "tagStyle": "filled and bordered", "isEnabled": enable(x), "type": "filter"} for x in items],
    }

recommended = lambda x: True if x["group"] == "language" else x["tier"] in ("hero", "core", "warn")
everything = lambda x: True

if __name__ == "__main__":
    base = sys.argv[1].rstrip("/"); ext = sys.argv[2] if len(sys.argv) > 2 else "webp"
    out = sys.argv[3] if len(sys.argv) > 3 else "kit"
    os.makedirs(out, exist_ok=True)
    for s, title in STYLES.items():
        for suffix, groups, rule in [("", ORDER + LIVE + LAST, everything)]:
            m = build(s, base, ext, groups, rule)
            p = os.path.join(out, f"{s}{suffix}.json")
            json.dump(m, open(p, "w"), indent=1, ensure_ascii=False)
            on = sum(f["isEnabled"] for f in m["filters"])
            print(f"{p}: {len(m['filters'])} badges, {on} on")
