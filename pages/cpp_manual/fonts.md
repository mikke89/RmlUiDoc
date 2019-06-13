---
layout: page
title: Loading Fonts
parent: cpp_manual
next: input
---

TrueType and OpenType fonts can be loaded into {{page.lib_name}} by the application. {{page.lib_name}} has no default font, so at least one font must be loaded before text can be rendered.

To load a font, call one of the `LoadFontFace()` functions on `{{page.lib_ns}}::Core::FontDatabase`. The simplest of these takes just a file name:

```cpp
// Adds a new font face to the database. The face's family, style and weight will be determined from the face itself.
// @param[in] file_name The file to load the face from.
// @return True if the face was loaded successfully, false otherwise.
static bool LoadFontFace(const {{page.lib_ns}}::Core::String& file_name);
```

This function will load the font file specified (opening it through the file interface). The font's family (the string you specify the font with using the `font-family`{:.prop} RCSS property), the style (normal or italic) and weight (normal or bold) are all fetched from the font file itself. {{page.lib_name}} will generate the font data for specific sizes of the font as required by the application.

Note that if you are loading a .ttc, only the first font will be registered.

If you need to override the family name, style or weight of the font, use the more complex `LoadFontFace()`:

```cpp
// Adds a new font face to the database, ignoring any family, style and weight information stored in the face itself.
// @param[in] file_name The file to load the face from.
// @param[in] family The family to add the face to.
// @param[in] style The style of the face (normal or italic).
// @param[in] weight The weight of the face (normal or bold).
// @return True if the face was loaded successfully, false otherwise.
static bool LoadFontFace(const {{page.lib_ns}}::Core::String& file_name,
                         const {{page.lib_ns}}::Core::String& family,
                         {{page.lib_ns}}::Core::Font::Style style,
                         {{page.lib_ns}}::Core::Font::Weight weight);
```

 * `style` is one of `{{page.lib_ns}}::Core::Font::STYLE_NORMAL` or `STYLE_ITALIC`;
 * `weight` is one of `{{page.lib_ns}}::Core::Font::WEIGHT_NORMAL` or `WEIGHT_BOLD`.

The italic and bold versions of a font are selected with the `font-weight`{:.prop} and `font-style`{:.prop} RCSS properties.

In the following example, the font file at `data/trilobyte.ttf`{:.path} is loaded and registered with {{page.lib_name}} with the family name, style and weight settings specified in the file itself.

```cpp
{{page.lib_ns}}::Core::FontDatabase::LoadFontFace("data/trilobyte.ttf");
```

In this example, the font file is loaded with overrides for the name, style and weight.

```cpp
{{page.lib_ns}}::Core::FontDatabase::LoadFontFace("data/trilobyte_b.ttf",
                                         "Trilobyte",
                                         {{page.lib_ns}}::Core::Font::STYLE_NORMAL,
                                         {{page.lib_ns}}::Core::Font::WEIGHT_BOLD);
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