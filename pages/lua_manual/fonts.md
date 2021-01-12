---
layout: page
title: Loading fonts
parent: lua_manual
next: attaching_to_events
---

The Lua plugin installs a global table `rmlui`, which provides a way to load supported font files from Lua. The function takes a single string as a parameter, the file name of the font to load.

```python
rmlui.LoadFontFace('../assets/LatoLatin-Regular.ttf')
rmlui.LoadFontFace('../assets/LatoLatin-Bold.ttf')
```

See the RmlUi [Lua API reference](api_reference.html#rmlui) for other things to do with this global.
