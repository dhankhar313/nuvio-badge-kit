# Source

Everything in this kit is generated from these files.

| File | What it holds |
|---|---|
| `spec.py` | Every badge: label, icon, tier and matching pattern |
| `languages.py` | The 83 languages, their native names and match words |
| `render.py` | The 5 styles as CSS, and the renderer |
| `manifests.py` | Builds the Nuvio files |
| `test_world.py`, `test_node.mjs` | Pattern tests in Python and JavaScript |

## Rebuild

```
npm install
pip install playwright pillow && playwright install chromium
python3 render.py obsidian      # every badge as PNG into out/
python3 test_world.py && node test_node.mjs
python3 manifests.py https://raw.githubusercontent.com/YOU/YOUR-REPO/main webp ..
```

Images in the kit are the PNGs converted to WebP (quality 92).
