import re, sys, json
sys.path.insert(0, '.')
from spec import B
from test_spec import cases as base_cases
extra = [
 ("Movie 2026 1080p WEB-DL Multi 🇬🇧 / 🇪🇸 / 🇫🇷 / 🇩🇪 / 🇮🇹 DDP5.1", {"1080p","webdl","multi","english","spanish","french","german","italian","ddp","5.1"}),
 ("Pelicula 2026 1080p WEB-DL Español Latino DD5.1", {"1080p","webdl","latino","dd","5.1"}),
 ("Filme 2026 1080p WEB-DL Dublado PT-BR", {"1080p","webdl","brazilian"}),
 ("Фильм 2026 1080p WEB-DL Русский AAC 2.0", {"1080p","webdl","russian","aac","2.0"}),
 ("Movie 2026 TRUEFRENCH 1080p BluRay x264", {"french","1080p","bluray","avc"}),
 ("Movie 2026 VOSTFR 1080p WEB", {"vostfr","1080p","web"}),
 ("Movie 2026 1080p WEB-DL Hindi-Tamil-Telugu-Malayalam-Kannada DD5.1", {"1080p","webdl","hindi","tamil","telugu","malayalam","kannada","dd","5.1"}),
 ("[SubsPlease] Anime - 01 (1080p) [JPN] FLAC", {"1080p","japanese","flac"}),
 ("Movie 2026 1080p WEB-DL Arabic Hebrew Persian Turkish", {"1080p","webdl","arabic","hebrew","persian","turkish"}),
 ("Movie 2026 2160p NF WEB-DL 中文 日本語 한국어 DDP5.1", {"4k","netflix","webdl","chinese","japanese","korean","ddp","5.1"}),
 ("Movie 2026 1080p MX Player WEB-DL Bhojpuri", {"1080p","mxplayer","webdl","bhojpuri"}),
 ("Movie 2026 1080p DSCP WEB-DL Polish Lektor", {"1080p","discovery","webdl","polish"}),
 ("Movie 2026 1080p WEB-DL Thai Vietnamese Indonesian Malay Filipino", {"1080p","webdl","thai","vietnamese","indonesian","malay","filipino"}),
 ("Movie 2026 Greek Ελληνικά Română Čeština 1080p", {"greek","romanian","czech","1080p"}),
]
cases = base_cases + extra
pats = [{"id": x["id"], "p": x["pattern"]} for x in B]
json.dump({"pats": pats, "cases": [[t, sorted(e)] for t, e in cases]}, open("_tests.json","w"), ensure_ascii=False)
P = {x["id"]: re.compile(x["pattern"]) for x in B}
bad = 0
for t, exp in cases:
    h = {k for k, p in P.items() if p.search(t)}
    if h != exp:
        bad += 1; print("PY", t, "\n  missing", sorted(exp-h), "\n  extra", sorted(h-exp))
print("python failures:", bad, "of", len(cases))
