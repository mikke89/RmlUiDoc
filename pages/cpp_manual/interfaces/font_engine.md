---
layout: page
title: Font engine interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
next: text_input_handler
---

The default font engine used in RmlUi provides an implementation based on the FreeType library. For users who want to render text using their own font system, a custom font engine interface can be constructed to replace the default implementation. In this case, the FreeType dependency can be removed entirely, see the [CMake option](../building_with_cmake.html#cmake-options) `RMLUI_FONT_ENGINE` for details.

Some of the most important functions for the font engine interface are given in the following.

```cpp
// Called by RmlUi when it wants to load a font face from file.
// @param[in] file_name The file to load the face from.
// @param[in] face_index The index of the font face within a font collection.
// @param[in] fallback_face True to use this font face for unknown characters in other font faces.
// @param[in] weight The weight to load when the font face contains multiple weights, otherwise the weight to register the font as.
// @return True if the face was loaded successfully, false otherwise.
virtual bool LoadFontFace(const String& file_name, int face_index, bool fallback_face, Style::FontWeight weight);

// Called by RmlUi when a font configuration is resolved for an element. Should return a handle that
// can later be used to resolve properties of the face, and generate string geometry to be rendered.
// @param[in] family The family of the desired font handle.
// @param[in] style The style of the desired font handle.
// @param[in] weight The weight of the desired font handle.
// @param[in] size The size of desired handle, in points.
// @return A valid handle if a matching (or closely matching) font face was found, NULL otherwise.
virtual FontFaceHandle GetFontFaceHandle(const String& family, Style::FontStyle style, Style::FontWeight weight, int size);

// Called by RmlUi when a list of font effects is resolved for an element with a given font face.
// @param[in] handle The font handle.
// @param[in] font_effects The list of font effects to generate the configuration for.
// @return A handle to the prepared font effects which will be used when generating geometry for a string.
virtual FontEffectsHandle PrepareFontEffects(FontFaceHandle handle, const FontEffectList& font_effects);

// Should return the font metrics of the given font face.
// @param[in] handle The font handle.
// @return The face's metrics.
virtual const FontMetrics& GetFontMetrics(FontFaceHandle handle);

// Called by RmlUi when it wants to retrieve the width of a string when rendered with this handle.
// @param[in] handle The font handle.
// @param[in] string The string to measure.
// @param[in] text_shaping_context Additional parameters that provide context for text shaping.
// @param[in] prior_character The optionally-specified character that immediately precedes the string. This may have an impact on the string
// width due to kerning.
// @return The width, in pixels, this string will occupy if rendered with this handle.
virtual int GetStringWidth(FontFaceHandle handle, StringView string, const TextShapingContext& text_shaping_context, Character prior_character = Character::Null);

// Called by RmlUi when it wants to retrieve the meshes required to render a single line of text.
// @param[in] render_manager The render manager responsible for rendering the string.
// @param[in] face_handle The font handle.
// @param[in] font_effects_handle The handle to the prepared font effects for which the geometry should be generated.
// @param[in] string The string to render.
// @param[in] position The position of the baseline of the first character to render.
// @param[in] colour The colour to render the text.
// @param[in] opacity The opacity of the text, should be applied to font effects.
// @param[in] text_shaping_context Additional parameters that provide context for text shaping.
// @param[out] mesh_list A list to place the meshes and textures representing the string to be rendered.
// @return The width, in pixels, of the string mesh.
virtual int GenerateString(RenderManager& render_manager, FontFaceHandle face_handle, FontEffectsHandle font_effects_handle, StringView string,
    Vector2f position, ColourbPremultiplied colour, float opacity, const TextShapingContext& text_shaping_context, TexturedMeshList& mesh_list);
```

The `LoadFontFace()` function is called when the user wants to load a font face. When an element is constructed, or some of its font-related properties are changed, it retrieves a `FontFaceHandle` through `GetFontFaceHandle()`. The font engine should then return a unique handle for the given family, style, weight and size.

If any font effects are applied to a given element, a list of such effects are submitted through `PrepareFontEffects()`. It is up to the font engine interface to decide how to handle them. A handle should be returned for the given list of font effects, this handle will later be used during the call to `GenerateString()`. If font effects are not used, there is no need to implement this function.

`GetFontMetrics()` is among several functions that should be implemented to allow RmlUi to query properties of the given font face.

During layouting, it is necessary to know the width of a given string without actually rendering it. Then, `GetStringWidth()` is called by RmlUi, expecting the interface to return the pixel width of the provided string for the given handle. Note that the string is encoded in UTF-8; there are some helper functions in `RmlUi/Core/StringUtilities.h`{:.incl} to iterate over such strings, if desired.

Finally, `GenerateString()` is called to actually generate the geometry of a given string. The face handle and font effects handle previously generated by the interface are provided. The function should return a list of textured meshes, as well as its pixel width.

Example implementations of custom font engine interfaces exist in the `bitmap_font` and `harfbuzz` samples.
