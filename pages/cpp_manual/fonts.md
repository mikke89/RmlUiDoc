---
layout: page
title: Loading Fonts
parent: cpp_manual
next: input
---

TrueType and OpenType fonts can be loaded into RmlUi by the application. RmlUi has no default font, so at least one font must be loaded before text can be rendered.

To load a font, call one of the `Rml::LoadFontFace()` functions. The simplest of these takes a file name and optional fallback and weight parameters:

```cpp
// Adds a new font face to the font engine. The face's family, style and weight will be determined from the face itself.
// @param[in] file_name The file to load the face from.
// @param[in] fallback_face True to use this font face for unknown characters in other font faces.
// @param[in] weight The weight to load when the font face contains multiple weights, otherwise the weight to register the font as. By
// default it loads all found font weights.
// @return True if the face was loaded successfully, false otherwise.
bool LoadFontFace(const String& file_name, bool fallback_face = false, Style::FontWeight weight = Style::FontWeight::Auto);
```

This function will load the font file specified (opening it through the file interface). The font's family (the string you specify the font with using the `font-family`{:.prop} RCSS property), the style (normal or italic) and by default the weight are all fetched from the font file itself. RmlUi will generate the font data for specific sizes of the font as required by the application. Note that if you are loading a .ttc, only the first font will be registered.

If enabled, the `fallback_face` option will make the given font face be used for any unknown characters in other fonts. This is useful for example to provide a single font face for emojis, and another one providing characters for e.g. cyrillic or greek. Then these fonts will be used whenever characters encountered are not located in the fonts specified by the document. Multiple fallback faces can be used, and they will be prioritized in the order they were loaded.

When the `weight` parameter is `Auto`{:.value} the weight is automatically retrieved from the font. Further, if the font contains multiple weight variations then all of them are loaded. Any other value of `weight` is either used to override the registered weight, or when there are multiple weights in the face, choose which weight variation to load.

Overriding the default `weight` parameter can be done by one of `Rml::Style::FontWeight::Normal`{:.value}, `Bold`{:.value}, or any numeric value \[1,1000\] by casting, for example `(Rml::Style::FontWeight)850`{:.value}.

If you need to load a font face from memory, and override the family name, style or weight of the font, use the more complex `LoadFontFace()`:

```cpp
// Adds a new font face from memory to the font engine. The face's family, style and weight is given by the parameters.
// @param[in] data A pointer to the data.
// @param[in] data_size Size of the data in bytes.
// @param[in] family The family to register the font as.
// @param[in] style The style to register the font as.
// @param[in] weight The weight to load when the font face contains multiple weights, otherwise the weight to register the font as. By
// default it loads all found font weights.
// @param[in] fallback_face True to use this font face for unknown characters in other font faces.
// @return True if the face was loaded successfully, false otherwise.
// @lifetime The pointed to 'data' must remain available until after the call to Rml::Shutdown.
static bool LoadFontFace(const byte* data,
                         int data_size, 
                         const String& family,
                         Style::FontStyle style,
                         Style::FontWeight weight = Style::FontWeight::Auto,
                         bool fallback_face = false);
```

- When the provided `family` is empty, the font family and style is automatically retrieved from the font.
- `style` is one of `Rml::Style::FontStyle::Normal`{:.value} or `Italic`{:.value}.
- The `weight` and `fallback_face` parameters work exactly like in the above function.

The italic and bold versions of a font are selected with the `font-weight`{:.prop} and `font-style`{:.prop} RCSS properties.

In the following example, the font file at `data/trilobyte.ttf`{:.path} is loaded and registered with RmlUi with the family name, style and weight settings specified in the file itself.

```cpp
Rml::LoadFontFace("data/trilobyte.ttf");
```

In this example, the font file is loaded from memory with overrides for the name, style and weight.

```cpp
std::vector<unsigned char> trilobyte_b = MyAssetLoader("data/trilobyte_b.ttf");
Rml::LoadFontFace(trilobyte_b.data(), trilobyte_b.size(),
                  "Trilobyte",
                  Rml::Style::FontStyle::Normal,
                  Rml::Style::FontWeight::Bold);

/* ... */

// Note that the data must stay alive until after the call to Rml::Shutdown.
Rml::Shutdown();
trilobyte_b.clear();
```

These fonts would be specified in RCSS with the following rules (assuming 'trilobyte.ttf' registers a font of the family 'Trilobyte'):

```css
body
{
    font-family: Trilobyte;
}

strong
{
    font-weight: bold;
}
```