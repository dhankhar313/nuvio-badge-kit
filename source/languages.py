# World language badges. Matching: English name, native name, safe ISO 639 codes, and flag emoji
# (only flags that point to one language). \b is added only next to ASCII letters, because
# JavaScript's \b ignores non-ASCII letters.
import re
def wrap(w):
    e = re.escape(w).replace(r"\-", "-").replace(r"\ ", r"[\s._-]?")
    a = r"\b" if w[0].isascii() and w[0].isalnum() else ""
    z = r"\b" if w[-1].isascii() and w[-1].isalnum() else ""
    return a + e + z

# (id, label, native suffix or None, words, codes, flags, on_by_default)
L = [
 # India & South Asia
 ("hindi","HINDI","हिन्दी",["hindi","हिन्दी","हिंदी"],["hin"],[],True),
 ("tamil","TAMIL","தமிழ்",["tamil","தமிழ்"],["tam"],[],True),
 ("telugu","TELUGU","తెలుగు",["telugu","తెలుగు"],["tel"],[],True),
 ("malayalam","MALAYALAM","മലയാളം",["malayalam","മലയാളം"],[],[],True),
 ("kannada","KANNADA","ಕನ್ನಡ",["kannada","ಕನ್ನಡ"],["kan"],[],True),
 ("bengali","BENGALI","বাংলা",["bengali","bangla","বাংলা"],[],["🇧🇩"],True),
 ("marathi","MARATHI","मराठी",["marathi","मराठी"],[],[],True),
 ("gujarati","GUJARATI","ગુજરાતી",["gujarati","ગુજરાતી"],["guj"],[],True),
 ("punjabi","PUNJABI","ਪੰਜਾਬੀ",["punjabi","panjabi","ਪੰਜਾਬੀ"],[],[],True),
 ("urdu","URDU","اردو",["urdu","اردو"],["urd"],["🇵🇰"],True),
 ("odia","ODIA","ଓଡ଼ିଆ",["odia","oriya","ଓଡ଼ିଆ"],[],[],True),
 ("assamese","ASSAMESE","অসমীয়া",["assamese","অসমীয়া"],[],[],True),
 ("bhojpuri","BHOJPURI","भोजपुरी",["bhojpuri","भोजपुरी"],[],[],True),
 ("nepali","NEPALI","नेपाली",["nepali","नेपाली"],[],["🇳🇵"],True),
 ("sinhala","SINHALA","සිංහල",["sinhala","sinhalese","සිංහල"],[],["🇱🇰"],True),
 # English & East Asia
 ("english","ENGLISH",None,["english"],["eng"],["🇬🇧","🇺🇸"],True),
 ("japanese","JAPANESE","日本語",["japanese","日本語"],["jpn","jap"],["🇯🇵"],True),
 ("korean","KOREAN","한국어",["korean","한국어"],["kor"],["🇰🇷"],True),
 ("chinese","CHINESE","中文",["chinese","mandarin","中文","国语","國語","普通话"],[],["🇨🇳","🇹🇼"],True),
 ("cantonese","CANTONESE","粵語",["cantonese","粤语","粵語"],[],["🇭🇰"],False),
 # Southeast Asia
 ("thai","THAI","ไทย",["thai","ภาษาไทย"],["tha"],["🇹🇭"],False),
 ("vietnamese","VIETNAMESE","TIẾNG VIỆT",["vietnamese","tiếng việt","tieng viet"],[],["🇻🇳"],False),
 ("indonesian","INDONESIAN","BAHASA",["indonesian","bahasa indonesia"],["indo"],["🇮🇩"],False),
 ("malay","MALAY","MELAYU",["malay","bahasa melayu"],[],["🇲🇾"],False),
 ("filipino","FILIPINO","TAGALOG",["filipino","tagalog"],[],["🇵🇭"],False),
 ("khmer","KHMER","ខ្មែរ",["khmer","ខ្មែរ"],[],["🇰🇭"],False),
 ("lao","LAO","ລາວ",["laotian","ພາສາລາວ"],[],["🇱🇦"],False),
 ("burmese","BURMESE","မြန်မာ",["burmese","myanmar","မြန်မာ"],[],["🇲🇲"],False),
 # Europe
 ("french","FRENCH","FRANÇAIS",["french","français","francais","truefrench","vff","vfq","vfi","vf2","vf"],["fre","fra"],["🇫🇷"],False),
 ("german","GERMAN","DEUTSCH",["german","deutsch"],["ger","deu"],["🇩🇪"],False),
 ("italian","ITALIAN","ITALIANO",["italian","italiano"],["ita"],["🇮🇹"],False),
 ("russian","RUSSIAN","РУССКИЙ",["russian","русский"],["rus"],["🇷🇺"],False),
 ("ukrainian","UKRAINIAN","УКРАЇНСЬКА",["ukrainian","українська"],["ukr"],["🇺🇦"],False),
 ("polish","POLISH","POLSKI",["polish","polski","lektor","pldub"],["pol"],["🇵🇱"],False),
 ("czech","CZECH","ČEŠTINA",["czech","čeština","cesky","česky"],["cze","ces"],["🇨🇿"],False),
 ("slovak","SLOVAK","SLOVENČINA",["slovak","slovenčina","slovensky"],["slk"],["🇸🇰"],False),
 ("hungarian","HUNGARIAN","MAGYAR",["hungarian","magyar"],["hun"],["🇭🇺"],False),
 ("romanian","ROMANIAN","ROMÂNĂ",["romanian","română","romana"],["rum","ron"],["🇷🇴"],False),
 ("bulgarian","BULGARIAN","БЪЛГАРСКИ",["bulgarian","български"],["bul"],["🇧🇬"],False),
 ("serbian","SERBIAN","SRPSKI",["serbian","srpski","српски"],["srp"],["🇷🇸"],False),
 ("croatian","CROATIAN","HRVATSKI",["croatian","hrvatski"],["hrv"],["🇭🇷"],False),
 ("slovenian","SLOVENIAN","SLOVENŠČINA",["slovenian","slovene","slovenščina"],["slv"],["🇸🇮"],False),
 ("bosnian","BOSNIAN","BOSANSKI",["bosnian","bosanski"],[],["🇧🇦"],False),
 ("macedonian","MACEDONIAN","МАКЕДОНСКИ",["macedonian","македонски"],["mkd"],["🇲🇰"],False),
 ("albanian","ALBANIAN","SHQIP",["albanian","shqip"],[],["🇦🇱"],False),
 ("greek","GREEK","ΕΛΛΗΝΙΚΑ",["greek","ελληνικά"],["gre","ell"],["🇬🇷"],False),
 ("turkish","TURKISH","TÜRKÇE",["turkish","türkçe","turkce"],["tur"],["🇹🇷"],False),
 ("dutch","DUTCH","NEDERLANDS",["dutch","nederlands","flemish","vlaams"],["dut","nld"],["🇳🇱"],False),
 ("swedish","SWEDISH","SVENSKA",["swedish","svenska"],["swe"],["🇸🇪"],False),
 ("danish","DANISH","DANSK",["danish","dansk"],[],["🇩🇰"],False),
 ("norwegian","NORWEGIAN","NORSK",["norwegian","norsk"],[],["🇳🇴"],False),
 ("finnish","FINNISH","SUOMI",["finnish","suomi"],[],["🇫🇮"],False),
 ("icelandic","ICELANDIC","ÍSLENSKA",["icelandic","íslenska"],[],["🇮🇸"],False),
 ("lithuanian","LITHUANIAN","LIETUVIŲ",["lithuanian","lietuvių"],[],["🇱🇹"],False),
 ("latvian","LATVIAN","LATVIEŠU",["latvian","latviešu"],[],["🇱🇻"],False),
 ("estonian","ESTONIAN","EESTI",["estonian","eesti"],[],["🇪🇪"],False),
 ("catalan","CATALAN","CATALÀ",["catalan","català"],[],[],False),
 ("basque","BASQUE","EUSKARA",["basque","euskara","euskera"],[],[],False),
 ("galician","GALICIAN","GALEGO",["galician","galego"],[],[],False),
 ("irish","IRISH","GAEILGE",["irish","gaeilge"],[],[],False),
 ("welsh","WELSH","CYMRAEG",["welsh","cymraeg"],[],[],False),
 ("belarusian","BELARUSIAN","БЕЛАРУСКАЯ",["belarusian","беларуская"],[],["🇧🇾"],False),
 # Middle East, Caucasus & Central Asia
 ("arabic","ARABIC","العربية",["arabic","العربية"],["ara"],["🇸🇦","🇪🇬","🇦🇪"],False),
 ("hebrew","HEBREW","עברית",["hebrew","עברית"],["heb"],["🇮🇱"],False),
 ("persian","PERSIAN","فارسی",["persian","farsi","فارسی"],[],["🇮🇷"],False),
 ("kurdish","KURDISH","KURDÎ",["kurdish","kurdî"],[],[],False),
 ("pashto","PASHTO","پښتو",["pashto","پښتو"],[],["🇦🇫"],False),
 ("georgian","GEORGIAN","ქართული",["georgian","ქართული"],[],["🇬🇪"],False),
 ("armenian","ARMENIAN","ՀԱՅԵՐԵՆ",["armenian","հայերեն"],[],["🇦🇲"],False),
 ("azerbaijani","AZERBAIJANI","AZƏRBAYCAN",["azerbaijani","azərbaycan"],[],["🇦🇿"],False),
 ("kazakh","KAZAKH","ҚАЗАҚ",["kazakh","қазақ"],[],["🇰🇿"],False),
 ("uzbek","UZBEK","OʻZBEK",["uzbek","o'zbek"],[],["🇺🇿"],False),
 ("mongolian","MONGOLIAN","МОНГОЛ",["mongolian","монгол"],[],["🇲🇳"],False),
 # Africa
 ("swahili","SWAHILI","KISWAHILI",["swahili","kiswahili"],[],["🇰🇪","🇹🇿"],False),
 ("amharic","AMHARIC","አማርኛ",["amharic","አማርኛ"],[],["🇪🇹"],False),
 ("afrikaans","AFRIKAANS",None,["afrikaans"],[],["🇿🇦"],False),
 ("yoruba","YORUBA","YORÙBÁ",["yoruba","yorùbá"],[],[],False),
 ("hausa","HAUSA",None,["hausa"],[],[],False),
 ("zulu","ZULU","ISIZULU",["zulu","isizulu"],[],[],False),
]

SPECIAL = {
 # Spanish (Spain) vs Latin American Spanish, Portuguese vs Brazilian: custom rules
 "spanish": ("SPANISH","ESPAÑOL", r"(?i)(?:\bspanish\b|\bcastellano\b|\bespa[ñn]ol\b(?![\s._-]?latino)|\besp\b|\bspa\b|🇪🇸)", False),
 "latino": ("LATINO","LATAM", r"(?i)(?:\blatino\b|\blatam\b|\blat\b|\bespa[ñn]ol[\s._-]?latino\b|🇲🇽)", False),
 "portuguese": ("PORTUGUESE","PORTUGUÊS", r"(?i)^(?=.*(?:\bportuguese\b|portugu[eê]s|\bpt[\s._-]?pt\b|🇵🇹))(?!.*(?:\bpt[\s._-]?br\b|\bbrazil|🇧🇷))", False),
 "brazilian": ("BRAZILIAN","PT-BR", r"(?i)(?:\bpt[\s._-]?br\b|\bbrazilian\b|\bdublado\b|🇧🇷)", False),
}

def pattern(words, codes, flags, lid):
    alts = [wrap(w) for w in words] + [r"\b" + c + r"\b" for c in codes] + flags
    p = "(?i)(?:" + "|".join(alts) + ")"
    if lid == "english":
        p = r"(?i)(?:\benglish\b|\beng\b)(?![\s._-]?subs?\b)|🇬🇧|🇺🇸"
    return p

# Country flag on each language badge (flag-icons codes, flags/1x1). The flag is where the
# language is mainly spoken; a language with no clear country flag keeps the language icon.
FLAG = {
    "hindi": "in", "tamil": "in", "telugu": "in", "malayalam": "in", "kannada": "in", "bengali": "in",
    "marathi": "in", "gujarati": "in", "punjabi": "in", "urdu": "pk", "odia": "in", "assamese": "in",
    "bhojpuri": "in", "nepali": "np", "sinhala": "lk", "english": "gb", "japanese": "jp", "korean": "kr",
    "chinese": "cn", "cantonese": "hk", "thai": "th", "vietnamese": "vn", "indonesian": "id", "malay": "my",
    "filipino": "ph", "khmer": "kh", "lao": "la", "burmese": "mm", "french": "fr", "german": "de",
    "italian": "it", "russian": "ru", "ukrainian": "ua", "polish": "pl", "czech": "cz", "slovak": "sk",
    "hungarian": "hu", "romanian": "ro", "bulgarian": "bg", "serbian": "rs", "croatian": "hr",
    "slovenian": "si", "bosnian": "ba", "macedonian": "mk", "albanian": "al", "greek": "gr", "turkish": "tr",
    "dutch": "nl", "swedish": "se", "danish": "dk", "norwegian": "no", "finnish": "fi", "icelandic": "is",
    "lithuanian": "lt", "latvian": "lv", "estonian": "ee", "catalan": "es-ct", "basque": "es-pv",
    "galician": "es-ga", "irish": "ie", "welsh": "gb-wls", "belarusian": "by", "spanish": "es",
    "latino": "mx", "portuguese": "pt", "brazilian": "br", "arabic": "sa", "hebrew": "il", "persian": "ir",
    "pashto": "af", "georgian": "ge", "armenian": "am", "azerbaijani": "az", "kazakh": "kz", "uzbek": "uz",
    "mongolian": "mn", "swahili": "ke", "amharic": "et", "afrikaans": "za", "yoruba": "ng", "hausa": "ng",
    "zulu": "za",
}

def entries():
    out = []
    for lid, label, native, words, codes, flags, on in L:
        out.append(dict(id=lid, label=label, sub=native, pattern=pattern(words, codes, flags, lid), on=on))
        if lid == "belarusian":  # keep Spanish/Portuguese next to the other European languages
            for k, (lab, nat, pat, o) in SPECIAL.items():
                out.append(dict(id=k, label=lab, sub=nat, pattern=pat, on=o))
    return out
