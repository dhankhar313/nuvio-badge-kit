# Source

Everything in this kit is generated from these files.

| File | What it holds |
|---|---|
| `spec.py` | Every badge: label, icon, tier and matching pattern |
| `languages.py` | The 83 languages, their native names and match words |
| `render.py` | The first 5 styles as CSS, and the renderer |
| `styles_extra.py` | Pixel, VHS, Keycap, Enamel, Glitch, Line, Dot and Glyph |
| `nuvio_size.py` | Makes the final images: bigger text, trimmed for Nuvio's 16dp badges |
| `manifests.py` | Builds the Nuvio files |
| `test_world.py`, `test_node.mjs` | Pattern tests in Python and JavaScript |

## Rebuild

```
npm install
pip install playwright pillow numpy && playwright install chromium
python3 nuvio_size.py out obsidian   # every badge as PNG into out/, sized for Nuvio
python3 test_world.py && node test_node.mjs
python3 manifests.py https://raw.githubusercontent.com/YOU/YOUR-REPO/main webp ..
```

Images in the kit are those PNGs converted to WebP (quality 92), in `v2/`.
