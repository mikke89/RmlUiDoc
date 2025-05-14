---
layout: page
title: Loading Fonts
parent: lua_manual
next: attaching_to_events
---

- [rmlui Lua API reference](api_reference.html#rmlui)
- [Loading Fonts C++ manual](../cpp_manual/fonts.html)

---

The Lua plugin installs a global table `rmlui`, which provides a way to load supported font files from Lua. The simplest way to load a font face is executing the `LoadFontFace()` function with a single string as a parameter, the file name of the font to load:

```python
rmlui.LoadFontFace('../assets/LatoLatin-Regular.ttf')
rmlui.LoadFontFace('../assets/LatoLatin-Bold.ttf')
```

However, you may provide two additional parameters (in this order):

- A `fallback` option as a `boolean` type. If enables, it makes the given font face be used for any unknown characters in other fonts. This is useful for example to provide a single font face for emojis, and another one providing characters for Cyrillic, Greek, and similar. These fonts will then be used whenever characters encountered are not located in the fonts specified by the document. Multiple fallback faces can be used, and they will be prioritized in the order they were loaded.
- A `face_index` parameter as an `integer` type. It allows selection of font faces within font collections. This is useful for loading a single font file with multiple faces.

In this example, different weights of the same font face are loaded, as they are all part of the same file (see [OpenType Font Variations](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview)), and a fallback for emojis is included:

```python
rmlui.LoadFontFace('data/NotoSansJP-VariableFont_wght.ttf', false, 0)
rmlui.LoadFontFace('data/NotoSansJP-VariableFont_wght.ttf', false, 1)
rmlui.LoadFontFace('data/NotoSansJP-VariableFont_wght.ttf', false, 2)
rmlui.LoadFontFace('seguiemj.ttf', true)
```
