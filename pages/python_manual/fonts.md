---
layout: page
title: Loading fonts
parent: python_manual
---

The {{page.lib_name}} module exposes the `LoadFontFace()` function for loading a supported font file from Python. The function takes a single string as a parameter, the file name of the font to load.

```python
rocket.LoadFontFace("../assets/Delicious-Roman.ttf")
rocket.LoadFontFace("../assets/Delicious-Bold.ttf")
```
