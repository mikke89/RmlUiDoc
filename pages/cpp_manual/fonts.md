---
layout: page
title: Loading Fonts
parent: cpp_manual
next: input
---

TrueType and OpenType fonts can be loaded into {{page.lib_name}} by the application. {{page.lib_name}} has no default font, so at least one font must be loaded before text can be rendered.

To load a font, call one of the `LoadFontFace()` functions in `{{page.lib_ns}}::Core`. The simplest of these takes a file name and an optional fallback parameter:

```cpp
// Adds a new font face to the font engine. The face's family, style and weight will be determined from the face itself.
// @param[in] file_name The file to load the face from.
// @param[in] fallback_face True to use this font face for unknown characters in other font faces.
// @return True if the face was loaded successfully, false otherwise.
bool LoadFontFace(const String& file_name, bool fallback_face = false);
```

This function will load the font file specified (opening it through the file interface). The font's family (the string you specify the font with using the `font-family`{:.prop} RCSS property), the style (normal or italic) and weight (normal or bold) are all fetched from the font file itself. {{page.lib_name}} will generate the font data for specific sizes of the font as required by the application. Note that if you are loading a .ttc, only the first font will be registered.

If enabled, the `fallback_face` option will make the given font face be used for any unknown characters in other fonts. This is useful for example to provide a single font face for emojis, and another one providing characters for e.g. cyrillic or greek. Then these fonts will be used whenever characters encountered are not located in the fonts specified by the document. Multiple fallback faces can be used, and they will be prioritized in the order they were loaded.

If you need to load a font face from memory, and override the family name, style or weight of the font, use the more complex `LoadFontFace()`:

```cpp
// Adds a new font face from memory to the font engine. The face's family, style and weight is given by the parameters.
// @param[in] data A pointer to the data.
// @param[in] data_size Size of the data in bytes.
// @param[in] family The family to register the font as.
// @param[in] style The style to register the font as.
// @param[in] weight The weight to register the font as.
// @param[in] fallback_face True to use this font face for unknown characters in other font faces.
// @return True if the face was loaded successfully, false otherwise.
static bool LoadFontFace(const byte* data,
                         int data_size, 
                         const {{page.lib_ns}}::Core::String& file_name,
                         const {{page.lib_ns}}::Core::String& family,
                         {{page.lib_ns}}::Core::Style::FontStyle style,
                         {{page.lib_ns}}::Core::Style::FontWeight weight,
                         bool fallback_face = false);
```

 * `style` is one of `{{page.lib_ns}}::Core::Style::FontStyle::Normal` or `Italic`;
 * `weight` is one of `{{page.lib_ns}}::Core::Style::FontWeight::Normal` or `Bold`.

The italic and bold versions of a font are selected with the `font-weight`{:.prop} and `font-style`{:.prop} RCSS properties.

In the following example, the font file at `data/trilobyte.ttf`{:.path} is loaded and registered with {{page.lib_name}} with the family name, style and weight settings specified in the file itself.

```cpp
{{page.lib_ns}}::Core::FontDatabase::LoadFontFace("data/trilobyte.ttf");
```

In this example, the font file is loaded from memory with overrides for the name, style and weight.

```cpp
std::vector<unsigned char> trilobyte_b = MyAssetLoader("data/trilobyte_b.ttf");
{{page.lib_ns}}::Core::FontDatabase::LoadFontFace(trilobyte_b.data(), trilobyte_b.size(),
                                         "Trilobyte",
                                         {{page.lib_ns}}::Core::Style::FontStyle::Normal,
                                         {{page.lib_ns}}::Core::Style::FontWeight::Bold);
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