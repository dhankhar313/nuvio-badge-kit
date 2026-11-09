import re, sys
sys.path.insert(0, '.')
from spec import B
P = {x["id"]: re.compile(x["pattern"]) for x in B}
def hits(t): return sorted(k for k, p in P.items() if p.search(t))
cases = [
 ("Movie 2026 2160p UHD BluRay REMUX DV HDR10 HEVC TrueHD 7.1 Atmos-FGT | 💾 58.1 GB", {"remux","4k","dolby-vision","hdr10","hevc","truehd","atmos","7.1","bigfile"}),
 ("Movie 2026 1080p WEB H264-GRP | 💾 5.1 GB", {"web","1080p","avc"}),
 ("Movie 2026 2160p NF WEB-DL DDP5.1 Atmos DV H 265 | 💾 7.0 GB", {"netflix","webdl","4k","ddp","atmos","dolby-vision","dv-only","5.1","hevc"}),
 ("Show S01E01 1080p AMZN WEB-DL DDP2.0 H.264-NTb", {"amazon","webdl","1080p","ddp","2.0","avc"}),
 ("Movie 1080p BDRip x264 DD 5.1", {"bluray","1080p","avc","dd","5.1"}),
 ("Movie 2160p WEB-DL AV1 Opus 5.1 10bit HDR10+", {"webdl","4k","av1","opus","5.1","10bit","hdr10plus"}),
 ("Movie 2026 HDCAM 720p x264 Line Audio", {"cam","720p","avc","line-audio"}),
 ("Movie (2026) Hindi ORG 1080p WEB-DL Dual Audio [Hindi + English] DD+5.1 ESub", {"hindi","original","1080p","webdl","dual","english","ddp","5.1","esub"}),
 ("Avatar 2009 1080p BluRay 3D Half-SBS x264 DTS-HD MA 5.1", {"bluray","1080p","3d-hsbs","avc","dts-hd-ma","5.1"}),
 ("Movie 2026 1080p HC HDRip x264 AAC", {"hardsub","1080p","avc","aac"}),
 ("Movie IMAX Enhanced 2160p DSNP WEB-DL DDP 5 1 Atmos HDR", {"imax-enhanced","4k","disney","webdl","ddp","5.1","atmos","hdr"}),
 ("Movie Extended Directors Cut 1080p BluRay x265 10bit DTS-HD HRA 7.1", {"extended","directors-cut","1080p","bluray","hevc","10bit","dts-hd-hra","7.1"}),
 ("Star Sports 1 HD | IN: 🔴 LIVE", {"hd-feed","region-in","live"}),
 ("[RD+] Movie 2026 2160p HDR DV P8 MA WEB-DL", {"cached","realdebrid","4k","hdr","dolby-vision","dv-p8","movies-anywhere","webdl"}),
 ("[RD download] Movie 1080p WEBRip x264 AAC2.0", {"uncached","1080p","webrip","avc","aac","2.0"}),
 ("Movie 2026 Telugu 1080p HQ HDRip x264 AAC 2.0 ESubs - 2.0GB", {"telugu","1080p","hdrip","avc","aac","2.0","esub"}),
 ("Movie 1999 DVDRip XviD MP3 Stereo", {"dvdrip","xvid","mp3","2.0"}),
 ("Movie 2026 1080p WEB-DL Multi Sub", {"1080p","webdl","msubs"}),
 ("Show S02 Complete 1080p WEB-DL DDP5.1", {"season-pack","1080p","webdl","ddp","5.1"}),
 ("Movie 2026 4K Remaster 1080p BluRay x264", {"remastered","1080p","bluray","avc"}),
]
bad = 0
for t, exp in cases:
    h = set(hits(t))
    if h != exp:
        bad += 1
        print("TITLE:", t); print("  missing:", sorted(exp - h)); print("  extra:  ", sorted(h - exp))
print("failures:", bad, "of", len(cases))
