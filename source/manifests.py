"""Build Nuvio/Fusion badge manifests. python3 manifests.py <base_url> <ext>"""
import sys, os, json
sys.path.insert(0, os.path.dirname(__file__))
from spec import B, GROUPS

ORDER = ["delivery", "resolution", "hdr", "picture", "audio", "channels", "source", "language",
         "codec", "subtitles", "edition", "service", "flags"]
LIVE = ["live", "container"]
TIER_RANK = {"hero": 0, "warn": 1, "core": 2, "info": 3}
GNAME = dict(GROUPS)
STYLES = {"obsidian": "Obsidian", "prism": "Prism", "neon": "Neon", "cinema": "Cinema", "liquid": "Liquid"}

def fname(bid): return bid.replace(".", "_")

def build(style, base, ext, groups, enable):
    items = sorted([x for x in B if x["group"] in groups],
                   key=lambda x: (groups.index(x["group"]), B.index(x)))
    return {
        "groups": [{"id": g, "name": GNAME[g], "color": "#00000000", "borderColor": "#00000000", "isExpanded": True} for g in groups],
        "filters": [{
            "id": x["id"], "groupId": x["group"], "name": x["name"], "pattern": x["pattern"],
            "imageURL": f"{base}/{STYLES[style]}/{fname(x['id'])}.{ext}",
            "tagColor": "#00000000", "borderColor": "#00000000", "textColor": "#00000000",
            "tagStyle": "filled and bordered", "isEnabled": enable(x), "type": "filter"} for x in items],
    }

recommended = lambda x: x.get("on", True) if x["group"] == "language" else x["tier"] in ("hero", "core", "warn")
everything = lambda x: True

if __name__ == "__main__":
    base = sys.argv[1].rstrip("/"); ext = sys.argv[2] if len(sys.argv) > 2 else "webp"
    out = sys.argv[3] if len(sys.argv) > 3 else "kit"
    os.makedirs(out, exist_ok=True)
    for s, title in STYLES.items():
        for suffix, groups, rule in [("", ORDER, recommended), ("-full", ORDER, everything), ("-live", LIVE, everything)]:
            m = build(s, base, ext, groups, rule)
            p = os.path.join(out, f"{s}{suffix}.json")
            json.dump(m, open(p, "w"), indent=1, ensure_ascii=False)
            on = sum(f["isEnabled"] for f in m["filters"])
            print(f"{p}: {len(m['filters'])} badges, {on} on")
