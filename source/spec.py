import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
# Full badge spec: art + regex for every badge in the master map.
# mode: 'suffix' = small text after a divider, 'kicker' = small text above the main label
SZ = r"(?!\s*(?:gb|mb|gib|mib|tb|kb)\b)"
CH = lambda d: r"(?:^|[^0-9.v])" + d + r"(?![0-9])" + SZ

GROUPS = [
 ("source", "Source"), ("resolution", "Resolution"), ("hdr", "HDR & Colour"), ("picture", "Picture & 3D"),
 ("codec", "Video Codec"), ("audio", "Audio Format"), ("channels", "Audio Channels"), ("language", "Language"),
 ("subtitles", "Subtitles"), ("edition", "Edition"), ("service", "Streaming Service"), ("flags", "Release Flags"),
 ("delivery", "Delivery & Cache"), ("live", "Live TV"), ("container", "Container"),
]
PACK = {"quality": ["source","resolution","hdr","picture","codec","audio","channels"],
        "details": ["delivery","language","subtitles","edition","service","flags"],
        "live": ["live","container"]}

B = []
def b(id, group, label, icon, tier, pattern, sub=None, mode="suffix", name=None, hue=None):
    B.append(dict(id=id, group=group, label=label, icon=icon, tier=tier, pattern=pattern, sub=sub,
                  mode=mode, name=name or (label + (" " + sub if sub else "")), hue=hue or group))

# ---------------- Source & release
b("remux","source","REMUX","diamond","hero", r"(?i)^(?!.*\bdvd[\s._-]?remux\b).*\bremux\b", name="REMUX")
b("full-disc","source","FULL DISC","hard-drives","info", r"(?i)\b(?:bdmv|br[\s._-]?disk|complete[\s._-]?(?:uhd[\s._-]?)?blu[\s._-]?ray|bd(?:25|50|66|100)|iso)\b")
b("uhd-bluray","source","UHD BLU-RAY","disc","core", r"(?i)^(?=.*\buhd[\s._-]?(?:blu[\s._-]?ray|bd(?:rip)?)\b)(?!.*\bremux\b)(?!.*\b(?:bdmv|br[\s._-]?disk|complete[\s._-]?(?:uhd[\s._-]?)?blu[\s._-]?ray)\b)", name="UHD Blu-ray")
b("bluray","source","BLU-RAY","disc","core", r"(?i)^(?=.*\b(?:blu[\s._-]?ray|bd[\s._-]?rip|br[\s._-]?rip)\b)(?!.*\bremux\b)(?!.*\buhd[\s._-]?(?:blu[\s._-]?ray|bd)\b)(?!.*\b(?:bdmv|br[\s._-]?disk|complete[\s._-]?blu[\s._-]?ray)\b)", name="Blu-ray")
b("dvd-remux","source","DVD REMUX","disc","info", r"(?i)\bdvd[\s._-]?remux\b")
b("webdl","source","WEB-DL","cloud-arrow-down","core", r"(?i)\bweb[\s._-]?dl\b")
b("web","source","WEB","globe-simple","core", r"(?i)\bweb\b(?![\s._-]?(?:dl|rip|series|scr)\b)")
b("webrip","source","WEBRIP","globe","core", r"(?i)\bweb[\s._-]?rip\b", name="WEBRip")
b("hdrip","source","HDRIP","file-video","info", r"(?i)^(?=.*\bhd[\s._-]?rip\b)(?!.*\bhc[\s._-]?hd[\s._-]?rip\b)", name="HDRip")
b("hdtv","source","HDTV","television-simple","info", r"(?i)\b(?:hdtv|pdtv|sdtv|dsr|dsrip)\b")
b("tvrip","source","TVRIP","broadcast","info", r"(?i)\b(?:tv[\s._-]?rip|sat[\s._-]?rip|dvb[\s._-]?rip|dth[\s._-]?rip)\b", name="TVRip / SATRip")
b("dvdrip","source","DVDRIP","disc","info", r"(?i)\bdvd[\s._-]?rip\b", name="DVDRip")
b("cam","source","CAM","video-camera","warn", r"(?i)\b(?:cam|cam[\s._-]?rip|hd[\s._-]?cam)\b")
b("telesync","source","TS","projector-screen","warn", r"(?i)\b(?:hd[\s._-]?ts|tele[\s._-]?sync|pre[\s._-]?dvd|pdvd)\b", sub="TELESYNC", name="Telesync")
b("telecine","source","TC","film-reel","warn", r"(?i)\b(?:hd[\s._-]?tc|tele[\s._-]?cine|tc)\b", sub="TELECINE", name="Telecine")
b("screener","source","SCR","eye","warn", r"(?i)\b(?:scr|dvd[\s._-]?scr|bd[\s._-]?scr|web[\s._-]?scr|screener)\b", sub="SCREENER", name="Screener")
b("hardsub","source","HC","subtitles","warn", r"(?i)\b(?:hc|hardsub(?:bed|s)?|hard[\s._-]?coded)\b", sub="HARD SUBS", name="Hard-coded subs")

# ---------------- Resolution
b("8k","resolution","8K","monitor-play","hero", r"(?i)\b(?:4320[pi]?|8k)\b")
b("4k","resolution","4K","monitor-play","hero", r"(?i)^(?=.*\b(?:2160[pi]?|4k|uhd)\b)(?!.*\b(?:4320[pi]?|8k)\b)(?!.*\b(?:1080|720|480)[pi]\b)")
b("1440p","resolution","1440P","monitor-play","core", r"(?i)\b(?:1440[pi]?|2k|qhd)\b")
b("1080p","resolution","1080P","monitor-play","core", r"(?i)\b(?:1080[pi]|fhd|full[\s._-]?hd)\b")
b("720p","resolution","720P","monitor-play","core", r"(?i)\b720[pi]\b")
b("576p","resolution","576P","monitor-play","info", r"(?i)\b(?:576|540)[pi]\b")
b("480p","resolution","480P","monitor-play","info", r"(?i)\b480[pi]\b")
b("lowres","resolution","360P","monitor-play","warn", r"(?i)\b(?:360|240|144)[pi]\b", name="Low res")

# ---------------- HDR & colour
b("dolby-vision","hdr","VISION","circle-half","hero", r"(?i)\b(?:dv|dovi|dolby[\s._-]?vision)\b", sub="DOLBY", mode="kicker", name="Dolby Vision", hue="dv")
b("dv-only","hdr","DV ONLY","warning","warn", r"(?i)^(?=.*\b(?:dv|dovi|dolby[\s._-]?vision)\b)(?!.*\b(?:hdr(?:10)?(?:\+|plus)?|hlg)(?![a-z]))", name="DV only (no fallback)")
b("dv-p7","hdr","DV","stack","info", r"(?i)\b(?:fel|mel|p7|dv7|dvp7|profile[\s._-]?7)\b", sub="P7", name="DV Profile 7", hue="dv")
b("dv-p8","hdr","DV","stack","info", r"(?i)\b(?:p8|dv8|dvp8|profile[\s._-]?8|dvhe\.08)\b", sub="P8", name="DV Profile 8", hue="dv")
b("hdr10plus","hdr","HDR10+","sparkle","core", r"(?i)\bhdr[\s._-]?10[\s._-]?(?:\+|plus\b|p\b)")
b("hdr10","hdr","HDR10","sun","core", r"(?i)^(?=.*\bhdr[\s._-]?10(?![\s._-]?(?:\+|plus\b|p\b|bits?\b)))(?!.*\bhdr[\s._-]?10[\s._-]?(?:\+|plus\b|p\b))")
b("hdr","hdr","HDR","sun","core", r"(?i)^(?=.*\bhdr(?![a-z0-9]|[\s._-]?10))(?!.*\bhdr[\s._-]?10(?![\s._-]?bits?\b))")
b("hlg","hdr","HLG","broadcast","core", r"(?i)\bhlg\b")
b("sdr","hdr","SDR","sun-dim","info", r"(?i)\bsdr\b")
b("fake-hdr","hdr","FAKE HDR","magic-wand","warn", r"(?i)\b(?:generated[\s._-]?(?:dynamic[\s._-]?)?hdr|fake[\s._-]?hdr|sdr[\s._-]?(?:to|2)[\s._-]?hdr|hdr[\s._-]?converted)\b", name="Fake HDR")
b("12bit","hdr","12-BIT","gradient","info", r"(?i)\b12[\s._-]?bits?\b")
b("10bit","hdr","10-BIT","gradient","info", r"(?i)\b(?:10[\s._-]?bits?|hi10p?)\b")
b("8bit","hdr","8-BIT","gradient","info", r"(?i)\b8[\s._-]?bits?\b")

# ---------------- Picture & 3D
b("imax-enhanced","picture","IMAX","arrows-out","hero", r"(?i)\bimax[\s._-]?enhanced\b", sub="ENHANCED", name="IMAX Enhanced")
b("imax","picture","IMAX","corners-out","core", r"(?i)^(?=.*\bimax\b)(?!.*\bimax[\s._-]?enhanced\b)")
b("3d","picture","3D","cube","core", r"(?i)^(?=.*\b3d\b)(?!.*\b(?:h[\s._-]?sbs|half[\s._-]?sbs|f[\s._-]?sbs|full[\s._-]?sbs|sbs|h[\s._-]?ou|half[\s._-]?ou|h[\s._-]?tab|half[\s._-]?tab|over[\s._-]?under|mvc|anaglyph)\b)")
b("3d-hsbs","picture","3D","columns","info", r"(?i)\b(?:h[\s._-]?sbs|half[\s._-]?sbs)\b", sub="HALF SBS", name="3D Half-SBS")
b("3d-fsbs","picture","3D","columns","info", r"(?i)^(?=.*\b(?:f[\s._-]?sbs|full[\s._-]?sbs|sbs)\b)(?!.*\b(?:h[\s._-]?sbs|half[\s._-]?sbs)\b)", sub="FULL SBS", name="3D Full SBS")
b("3d-ou","picture","3D","rows","info", r"(?i)\b(?:h[\s._-]?ou|half[\s._-]?ou|h[\s._-]?tab|half[\s._-]?tab|over[\s._-]?under)\b", sub="OVER-UNDER", name="3D Over-Under")
b("3d-mvc","picture","3D","cube-focus","info", r"(?i)\bmvc\b", sub="MVC", name="3D MVC")
b("anaglyph","picture","3D","eyeglasses","info", r"(?i)\banaglyph\b", sub="ANAGLYPH", name="Anaglyph")
b("open-matte","picture","OPEN","selection-all","info", r"(?i)\bopen[\s._-]?matte\b", sub="MATTE", name="Open Matte")
b("hfr","picture","HFR","gauge","info", r"(?i)\b(?:hfr|(?:48|50|60|120)[\s._-]?fps)\b", sub="60 FPS")
b("hybrid","picture","HYBRID","git-merge","info", r"(?i)\bhybrid\b")
b("upscaled","picture","UPSCALED","arrow-fat-lines-up","warn", r"(?i)\b(?:upscaled?|ai[\s._-]?upscaled?|topaz)\b")
b("bw","picture","B&W","drop-half","info", r"(?i)\b(?:black[\s._-]?(?:and|&|n)[\s._-]?(?:white|chrome)|b[\s._-]?&[\s._-]?w)\b", name="Black & White")

# ---------------- Video codec
b("av1","codec","AV1","cpu","core", r"(?i)\bav1\b")
b("vvc","codec","VVC","cpu","info", r"(?i)\b(?:x266|h[\s._-]?266|vvc)\b", sub="H.266")
b("hevc","codec","HEVC","cpu","info", r"(?i)\b(?:x265|h[\s._-]?265|hevc)\b", sub="H.265")
b("avc","codec","AVC","cpu","info", r"(?i)\b(?:x264|h[\s._-]?264|avc)\b", sub="H.264")
b("vp9","codec","VP9","cpu","info", r"(?i)\bvp9\b")
b("vc1","codec","VC-1","cpu","info", r"(?i)\bvc[\s._-]?1\b")
b("mpeg2","codec","MPEG-2","cpu","info", r"(?i)\bmpeg[\s._-]?2\b")
b("xvid","codec","XVID","cpu","warn", r"(?i)\b(?:xvid|divx)\b", name="XviD / DivX")

# ---------------- Audio format
b("atmos","audio","ATMOS","spiral","hero", r"(?i)\batmos\b", sub="DOLBY", mode="kicker", name="Dolby Atmos")
b("dtsx","audio","DTS:X","spiral","hero", r"(?i)\bdts[\s._:-]?x\b", name="DTS:X")
b("truehd","audio","TRUEHD","waveform","core", r"(?i)\btrue[\s._-]?hd\b", sub="DOLBY", mode="kicker", name="TrueHD")
b("dts-hd-ma","audio","DTS-HD","waveform","core", r"(?i)^(?=.*\bdts[\s._-]?(?:hd[\s._-]?)?ma\b)(?!.*\bdts[\s._:-]?x\b)", sub="MA", name="DTS-HD MA")
b("dts-hd-hra","audio","DTS-HD","waveform","core", r"(?i)\b(?:dts[\s._-]?hd[\s._-]?)?hra\b", sub="HRA", name="DTS-HD HRA")
b("dts-hd","audio","DTS-HD","waveform","core", r"(?i)^(?=.*\bdts[\s._-]?hd\b)(?!.*\bdts[\s._-]?(?:hd[\s._-]?)?(?:ma|hra)\b)(?!.*\bdts[\s._:-]?x\b)", name="DTS-HD")
b("lpcm","audio","LPCM","waveform","core", r"(?i)\bl?pcm\b")
b("flac","audio","FLAC","waveform","core", r"(?i)\bflac\b")
b("ddp","audio","DIGITAL+","speaker-high","core", r"(?i)(?:\bddp|\bdd\+|\be[\s._-]?ac[\s._-]?3\b|\bdolby[\s._-]?digital[\s._-]?plus\b)", sub="DOLBY", mode="kicker", name="Dolby Digital Plus")
b("dd","audio","DIGITAL","speaker-high","info", r"(?i)^(?=.*(?:\bdd(?:[\s._-]?[1-7][\s._][01])?\b|\bac[\s._-]?3\b|\bdolby[\s._-]?digital\b(?![\s._-]?plus)))(?!.*(?:\bddp|\bdd\+|\be[\s._-]?ac[\s._-]?3\b|dolby[\s._-]?digital[\s._-]?plus))", sub="DOLBY", mode="kicker", name="Dolby Digital")
b("dts-es","audio","DTS-ES","speaker-high","info", r"(?i)\bdts[\s._-]?es\b")
b("dts","audio","DTS","speaker-high","info", r"(?i)^(?=.*\bdts\b)(?!.*\bdts[\s._:-]?(?:hd|ma|hra|x|es|xll)\b)")
b("aac","audio","AAC","speaker-high","info", r"(?i)\baac(?![a-z])")
b("opus","audio","OPUS","speaker-high","info", r"(?i)\bopus(?![a-z])", name="Opus")
b("mp3","audio","MP3","speaker-simple-low","info", r"(?i)\bmp3\b")

# ---------------- Audio channels
b("7.1","channels","7.1","speaker-simple-high","core", "(?i)" + CH(r"[78][. ][01]"), name="7.1 Surround")
b("6.1","channels","6.1","speaker-simple-high","info", "(?i)^(?=.*" + CH(r"6[. ]1") + ")(?!.*" + CH(r"[78][. ][01]") + ")", name="6.1 Surround")
b("5.1","channels","5.1","speaker-simple-high","core", "(?i)^(?=.*" + CH(r"5[. ][01]") + ")(?!.*" + CH(r"[678][. ][01]") + ")", name="5.1 Surround")
b("2.0","channels","2.0","headphones","info", "(?i)^(?=.*(?:" + CH(r"2[. ]0") + r"|\bstereo\b))(?!.*" + CH(r"[5678][. ][01]") + ")", sub="STEREO", name="2.0 Stereo")
b("1.0","channels","1.0","speaker-simple-low","info", "(?i)^(?=.*(?:" + CH(r"1[. ]0") + r"|\bmono\b))(?!.*" + CH(r"[25678][. ][01]") + ")", sub="MONO", name="1.0 Mono")

# ---------------- Language
b("dual","language","DUAL AUDIO","translate","core", r"(?i)\bdual(?:[\s._-]?(?:audio|aud))?\b", name="Dual Audio")
b("multi","language","MULTI AUDIO","translate","core", r"(?i)\bmulti(?![\s._-]?subs?\b)(?:[\s._-]?(?:audio|lang\w*))?\b", name="Multi Audio")
b("original","language","ORG AUDIO","seal-check","core", r"(?i)\b(?:org|original[\s._-]?audio)\b", name="Original audio")
from languages import entries as _lang_entries
for _l in _lang_entries():
    b(_l["id"], "language", _l["label"], "translate", "core" if _l["on"] else "info", _l["pattern"], sub=_l["sub"], name=_l["label"].title())
    B[-1]["on"] = _l["on"]
b("dubbed","language","DUBBED","microphone","info", r"(?i)\b(?:dubbed|dub)\b")
b("line-audio","language","LINE AUDIO","microphone-slash","warn", r"(?i)\b(?:line[\s._-]?(?:audio|dubbed)|linedubbed|mic[\s._-]?dubbed|cam[\s._-]?audio)\b", name="Line / cam audio")

# ---------------- Subtitles
b("esub","subtitles","ESUB","subtitles","info", r"(?i)\b(?:esubs?|eng(?:lish)?[\s._-]?subs?)\b", name="ESub")
b("msubs","subtitles","MSUBS","subtitles","info", r"(?i)\b(?:msubs?|multi[\s._-]?subs?)\b", name="MSubs")
b("sdh","subtitles","SDH","ear","info", r"(?i)\b(?:sdh|closed[\s._-]?captions?)\b")
b("vostfr","subtitles","VOSTFR","subtitles","info", r"(?i)\bvostfr\b", sub="FR SUBS", name="VOSTFR (French subs)")
b("forced","subtitles","FORCED SUBS","subtitles","info", r"(?i)\bforced\b")

# ---------------- Edition
b("extended","edition","EXTENDED","film-slate","core", r"(?i)\bextended\b(?![\s._-]?(?:trailer|clip|scene))")
b("directors-cut","edition","DIRECTOR'S CUT","film-slate","core", r"(?i)\bdirector'?s?[\s._-]?cut\b", name="Director's Cut")
b("unrated","edition","UNRATED","prohibit","core", r"(?i)\b(?:unrated|uncut)\b")
b("theatrical","edition","THEATRICAL","film-slate","info", r"(?i)\btheatrical\b")
b("remastered","edition","REMASTERED","sparkle","core", r"(?i)\b(?:remaster(?:ed)?|restored|4k[\s._-]?restoration)\b")
b("criterion","edition","CRITERION","seal","core", r"(?i)\b(?:criterion|crit)\b")
b("special","edition","SPECIAL EDITION","star","info", r"(?i)\b(?:special[\s._-]?edition|anniversary(?:[\s._-]?edition)?|ultimate[\s._-]?(?:edition|cut))\b", name="Special / Anniversary")
b("uncensored","edition","UNCENSORED","eye","info", r"(?i)\buncensored\b")

# ---------------- Streaming service (case-sensitive short tags, no logos)
S = "play-circle"
b("netflix","service","NETFLIX",S,"info", r"\b(?:NF|NETFLIX|[Nn]etflix)\b")
b("amazon","service","PRIME VIDEO",S,"info", r"\b(?:AMZN|AMAZON|[Aa]mazon|[Pp]rime[\s._-]?[Vv]ideo)\b", name="Prime Video")
b("disney","service","DISNEY+",S,"info", r"\b(?:DSNP|DSNY|DISNEY|[Dd]isney)\b", name="Disney+")
b("appletv","service","APPLE TV+",S,"info", r"\b(?:ATVP|ATV|APTV)\b|[Aa]pple[\s._-]?TV", name="Apple TV+")
b("hbo","service","HBO MAX",S,"info", r"\b(?:HMAX|HBO(?:[\s._-]?MAX)?|MAX(?=[\s._-]WEB))\b", name="HBO Max")
b("hulu","service","HULU",S,"info", r"\b(?:HULU|[Hh]ulu)\b", name="Hulu")
b("peacock","service","PEACOCK",S,"info", r"\b(?:PCOK|[Pp]eacock)\b", name="Peacock")
b("paramount","service","PARAMOUNT+",S,"info", r"\b(?:PMTP|PMNT|[Pp]aramount)", name="Paramount+")
b("itunes","service","ITUNES",S,"info", r"\b(?:iT(?=[\s._-]WEB)|iTunes)\b", name="iTunes")
b("movies-anywhere","service","MOVIES ANYWHERE",S,"info", r"\bMA(?=[\s._-]WEB)|[Mm]ovies[\s._-]?[Aa]nywhere", name="Movies Anywhere")
b("jiohotstar","service","JIOHOTSTAR",S,"info", r"(?i)\b(?:jio[\s._-]?hotstar|hotstar|jio[\s._-]?cinema)\b", name="JioHotstar")
b("zee5","service","ZEE5",S,"info", r"(?i)\bzee[\s._-]?5\b")
b("sonyliv","service","SONYLIV",S,"info", r"(?i)\bsony[\s._-]?liv\b", name="SonyLIV")
b("sunnxt","service","SUN NXT",S,"info", r"(?i)\bsun[\s._-]?nxt\b", name="Sun NXT")
b("aha","service","AHA",S,"info", r"(?i)\baha(?:[\s._-]?video)?(?=[\s._-]web)", name="aha")
b("hoichoi","service","HOICHOI",S,"info", r"(?i)\bhoichoi\b", name="Hoichoi")
b("crunchyroll","service","CRUNCHYROLL",S,"info", r"\b(?:CR(?=[\s._-]WEB)|CRUNCHYROLL|[Cc]runchyroll)\b", name="Crunchyroll")
b("hidive","service","HIDIVE",S,"info", r"(?i)\bhidive\b")
b("viki","service","VIKI",S,"info", r"(?i)\bviki\b", name="Viki")
b("iqiyi","service","IQIYI",S,"info", r"(?i)\biqiyi\b", name="iQIYI")
b("tving","service","TVING",S,"info", r"(?i)\btving\b")
b("iplayer","service","IPLAYER",S,"info", r"\b(?:iP(?=[\s._-]WEB)|[Ii][Pp]layer)\b", name="BBC iPlayer")
b("itvx","service","ITVX",S,"info", r"(?i)\bitvx\b")
b("nowtv","service","NOW",S,"info", r"\bNOW(?=[\s._-]WEB)|\bNOW[\s._-]?TV\b", name="NOW")

b("stan","service","STAN",S,"info", r"\bSTAN\b", name="Stan")
b("roku","service","ROKU",S,"info", r"(?i)\broku\b", name="Roku")
b("googleplay","service","GOOGLE PLAY",S,"info", r"\b(?:PLAY(?=[\s._-]WEB)|[Gg]oogle[\s._-]?[Pp]lay)\b", name="Google Play")
b("crave","service","CRAVE",S,"info", r"\b(?:CRAV|CRAVE|[Cc]rave)\b", name="Crave")
b("cbc","service","CBC",S,"info", r"\bCBC\b")
b("discovery","service","DISCOVERY+",S,"info", r"\bDSCP\b|[Dd]iscovery\+", name="Discovery+")
b("shudder","service","SHUDDER",S,"info", r"\b(?:SHDR|SHUDDER|[Ss]hudder)\b", name="Shudder")
b("mubi","service","MUBI",S,"info", r"(?i)\bmubi\b", name="MUBI")
b("starz","service","STARZ",S,"info", r"\b(?:STZ|STARZ|[Ss]tarz)\b", name="Starz")
b("showtime","service","SHOWTIME",S,"info", r"\b(?:SHO(?=[\s._-]WEB)|SHOWTIME|[Ss]howtime)\b", name="Showtime")
b("amcplus","service","AMC+",S,"info", r"\bAMCP\b|\bAMC\+", name="AMC+")
b("mxplayer","service","MX PLAYER",S,"info", r"(?i)\bmx[\s._-]?player\b", name="MX Player")
b("erosnow","service","EROS NOW",S,"info", r"(?i)\beros[\s._-]?now\b", name="Eros Now")
b("hungama","service","HUNGAMA",S,"info", r"(?i)\bhungama\b", name="Hungama")
b("altbalaji","service","ALTT",S,"info", r"(?i)\b(?:alt[\s._-]?balaji|altt)\b", name="ALTBalaji / ALTT")
b("viu","service","VIU",S,"info", r"(?i)\bviu\b", name="Viu")
b("wetv","service","WETV",S,"info", r"(?i)\bwetv\b", name="WeTV")
b("youku","service","YOUKU",S,"info", r"(?i)\byouku\b", name="Youku")
b("wavve","service","WAVVE",S,"info", r"(?i)\bwavve\b", name="Wavve")
b("unext","service","U-NEXT",S,"info", r"(?i)\bu[\s._-]?next\b", name="U-NEXT")
b("tver","service","TVER",S,"info", r"(?i)\btver\b", name="TVer")
b("coupang","service","COUPANG",S,"info", r"\b(?:CPNG|[Cc]oupang)\b", name="Coupang Play")

# ---------------- Release flags
b("proper","flags","PROPER","check-circle","info", r"(?i)\bproper\b")
b("repack","flags","REPACK","package","info", r"(?i)\b(?:repack\d?|rerip)\b")
b("internal","flags","INTERNAL","lock-simple","info", r"(?i)\binternal\b")
b("limited","flags","LIMITED","hourglass","info", r"(?i)\blimited\b")
b("season-pack","flags","SEASON PACK","stack","info", r"(?i)\b(?:complete[\s._-]?(?:series|season)|season[\s._-]?pack|s\d{1,2}(?![\s._-]?e\d)(?:[\s._-]?-[\s._-]?s\d{1,2})?)\b", name="Season pack")
b("version","flags","V2","arrow-clockwise","info", r"(?i)\b(?:v[2-9]|batch)\b", name="Anime v2 / Batch")
b("sample","flags","SAMPLE","scissors","warn", r"(?i)\b(?:sample|extras?|trailer|featurette)\b", name="Sample / Extras")

# ---------------- Delivery & cache
b("cached","delivery","CACHED","lightning","hero", r"(?i)⚡|\[(?:rd|ad|pm|tb|dl|ed|oc|pk)\+\]|\b(?:cached|instant)\b", name="Cached")
b("uncached","delivery","UNCACHED","hourglass-medium","warn", r"(?i)⏳|\[(?:rd|ad|pm|tb|dl|ed|oc|pk)[\s._-]?download\]|\buncached\b", name="Uncached")
b("realdebrid","delivery","REAL-DEBRID","cloud","info", r"(?i)\[rd\+?\]|\breal[\s._-]?debrid\b", name="Real-Debrid")
b("torbox","delivery","TORBOX","cloud","info", r"(?i)\[tb\+?\]|\btorbox\b", name="TorBox")
b("alldebrid","delivery","ALLDEBRID","cloud","info", r"(?i)\[ad\+?\]|\balldebrid\b", name="AllDebrid")
b("premiumize","delivery","PREMIUMIZE","cloud","info", r"(?i)\[pm\+?\]|\bpremiumize\b", name="Premiumize")
b("usenet","delivery","USENET","newspaper","info", r"(?i)\b(?:usenet|easynews|nzb\w*)\b")
b("p2p","delivery","P2P","share-network","info", r"(?i)\bp2p\b")
b("direct","delivery","DIRECT","link","info", r"(?i)\b(?:http|direct[\s._-]?link|ddl)\b")
b("bigfile","delivery","50 GB+","database","info", r"(?i)(?:^|[^0-9.])(?:[5-9]\d|\d{3})(?:[.,]\d+)?\s?(?:gb|gib)\b", name="Big file 50 GB+")

# ---------------- Live TV
b("live","live","LIVE","record","hero", r"(?i)🔴|\[\s*live\s*\]|\(\s*live\s*\)|\blive[\s._-]?(?:now|tv|stream)\b|\blive$")
b("247","live","24/7","repeat","info", r"(?i)\b24[\s._-]?(?:/|x)[\s._-]?7\b")
b("ppv","live","PPV","ticket","core", r"(?i)\b(?:ppv|pay[\s._-]?per[\s._-]?view)\b")
b("hd-feed","live","HD FEED","television","core", r"(?i)(?:^|[\s|:\[(])hd(?=$|[\s|:\])])", name="HD feed")
b("sd-feed","live","SD FEED","television","info", r"(?i)(?:^|[\s|:\[(])sd(?=$|[\s|:\])])", name="SD feed")
b("raw","live","RAW FEED","aperture","info", r"(?i)\braws?\b")
b("live-hfr","live","60 FPS","gauge","info", r"(?i)\b(?:50|60)[\s._-]?fps\b", name="50/60 fps feed")
b("backup","live","BACKUP","arrows-clockwise","info", r"(?i)\b(?:backup|b/u|alt(?:ernate)?[\s._-]?feed)\b")
b("catchup","live","CATCH-UP","clock-counter-clockwise","info", r"(?i)\b(?:catch[\s._-]?up|replay)\b", name="Catch-up")
b("region-in","live","IN","map-pin","info", r"(?:^|[\s\[(|])IN(?=\s*[|:\])])", name="Region IN")
b("region-uk","live","UK","map-pin","info", r"(?:^|[\s\[(|])UK(?=\s*[|:\])])", name="Region UK")
b("region-us","live","US","map-pin","info", r"(?:^|[\s\[(|])US(?=\s*[|:\])])", name="Region US")
b("hls","live","HLS","broadcast","info", r"(?i)\b(?:m3u8|hls)\b")
b("mpegts","live","MPEG-TS","broadcast","info", r"(?i)\bmpeg[\s._-]?ts\b|\.ts$", name="MPEG-TS")

# ---------------- Container
b("mkv","container","MKV","file-video","info", r"(?i)\bmkv\b")
b("mp4","container","MP4","file-video","info", r"(?i)\bmp4\b")
b("m2ts","container","M2TS","file-video","info", r"(?i)\b(?:m2ts|bdav)\b")
b("avi","container","AVI","file-video","warn", r"(?i)\bavi\b")

if __name__ == "__main__":
    from collections import Counter
    print(len(B), Counter(x["tier"] for x in B))
    print(Counter(x["group"] for x in B))
    ids = [x["id"] for x in B]; assert len(ids) == len(set(ids))
