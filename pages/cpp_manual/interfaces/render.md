---
layout: page
title: Render interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
next: system
---


The render interface is how RmlUi sends its generated geometry through to the application to render. It also uses the interface to load textures, and optionally for advanced rendering effects. Applications must install a render interface before initializing RmlUi.

The render interface is given in `<RmlUi/Core/RenderInterface.h>`{:.incl}. To develop a custom render interface, create a class derived from `Rml::RenderInterface` and provide function definitions for the pure virtual functions, and any of the others that you wish to provide functionality for.

For example implementations of the interface, please take a look the [included backends](https://github.com/mikke89/RmlUi/tree/master/Backends) in RmlUi and their respective renderers (`RmlUi_Renderer_[…].cpp`{:.path}). There is also a large set of visual tests, which can be very helpful as a reference to verify that the renderer acts as expected. Comparing the rendered result with one of our built-in renderers may be very valuable during implementation. Please see the [RmlUi Test Suite](https://github.com/mikke89/RmlUi/tree/master/Tests) for details, and in particular the `rmlui_visual_tests`{:.value} application, enabled with the `BUILD_TESTING`{:.value} [CMake option](../building_with_cmake.html).

**Contents**

- [Feature table](#feature-table)
- [Rendering conventions](#rendering-conventions)
- [Basic rendering](#basic-rendering)
    - [Geometry](#geometry)
    - [Textures](#textures)
    - [Scissor region](#scissor-region)
- [Advanced rendering](#advanced-rendering)
    - [Clip mask](#clip-mask)
    - [Transforms](#transforms)
    - [Layers](#layers)
    - [Render textures](#render-textures)
    - [Mask images](#mask-images)
    - [Filters](#filters)
    - [Shaders](#shaders)

### Feature table
{:#feature-table}

The following table lists various rendering features, together with the properties that require those features to be implemented by the renderer. Each feature in this list represents a set of render interface functions.

| Feature | Description | Required by properties |
| -- | -- | -- |
| [Basic rendering](#basic-rendering) | Rendering box geometry, images, text, and basic decorators. | Always required |
| [Clip mask](#clip-mask) | Proper clipping of transformed elements and elements with rounded borders. | `transform`{:.prop} and `perspective`{:.prop}, `border-radius`{:.prop} combined with `overflow: none`{:.value}, `box-shadow`{:.prop} |
| [Transforms](#transforms) | Apply arbitrary matrix transformations to rotate, scale, skew, or translate elements. | `transform`{:.prop} and `perspective`{:.prop} |
| [Layers](#layers) | Rendering to layers, and compositing, so that render effects can be applied in isolation. | `filter`{:.prop}, `backdrop-filter`{:.prop}, `mask-image`{:.prop}, `box-shadow`{:.prop} |
| [Render textures](#render-textures) | Allow a layer to be stored as a texture for later rendering. | `box-shadow`{:.prop} |
| [Mask images](#mask-images) | Allow a layer to be stored and later used as a mask. | `mask-image`{:.prop} |
| [Filters](#filters) | Applying filters during compositing. | `filter`{:.prop}, `backdrop-filter`{:.prop}, `box-shadow`{:.prop} with blur applied |
| [Shaders](#shaders) | Rendering geometry with special shaders. | The following `decorator`{:.prop} types: `shader`{:.value}, `linear-gradient`{:.value}, `radial-gradient`{:.value}, `conic-gradient`{:.value}, in addition to their `repeating-`{:.value} variants. |

The listed properties may not work at all, or work with reduced functionality, if their corresponding feature is not implemented. If a property is not listed here specifically, then it should have full support with only the basic rendering functions implemented.

### Rendering conventions

Before implementing the rendering API in RmlUi, the user should understand the following rendering conventions and assumptions used by the library.

* Vertex position coordinates are in `pixel` units.
* The coordinate system of documents in RmlUi places the origin at the top-left corner of the window.
* Indices define sets of triangles in a counter-clockwise winding order.
* The generated textures in RmlUi use the convention with the origin placed at the bottom-left corner.
* To handle transforms correctly, see the [transforms](#transforms) section.

Other rendering assumptions.

* Alpha blending should be enabled.
* Generated textures and vertex colors are given in the sRGB color space with premultiplied alpha.
* Textures should have their fetched color multiplied by the vertex color.

#### Blending

The library uses colors with premultiplied alpha to ensure correct blending when compositing multiple layers with transparency. When implementing the render interface, users should ensure that they use a blend function appropriate for premultiplied alpha. E.g. [in OpenGL](https://apoorvaj.io/alpha-compositing-opengl-blending-and-premultiplied-alpha/), one can use `glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA)`. When compositing the rendered GUI onto the final destination buffer, one can use this same function if the destination buffer is opaque. Otherwise, one may need to un-premultiply the colors before blending.

#### Projection matrix

The user must construct their own projection matrix while considering the above conventions, along with the conventions and settings used in their graphics API. E.g. the OpenGL convention is to place the origin at the bottom-left corner of the window. Thus, the user should flip the y-axis when constructing their projection matrix. The DirectX convention is to place the origin at the top-left corner of the window, thus, an orthographic projection matrix which follows this convention can be used.

#### Generated textures

The generated textures in RmlUi follow the OpenGL convention of placing the texture origin at the bottom-left corner. Other graphics APIs, including DirectX, use the top-left corner as the origin. Thus, textures can appear vertically flipped. In this case, the user can flip the texture y-coordinates provided by RmlUi.

#### Face culling

If face culling is enabled, make sure to get the culled face direction correct. Otherwise you will get a blank window. E.g. by default OpenGL defines front faces to be in a counter-clockwise winding direction, and will cull back faces. Thus, in terms of the geometry submitted by RmlUi these defaults can be used. On the other hand, the DirectX convention is to use clockwise winding direction for front faces, thus, if back face culling is enabled you will get a blank screen. The solution is to either disable face culling, swap the winding direction, or set the culling to cull front faces instead of back faces.

#### Viewport

Make sure to properly set up the viewport in your graphics API. This should typically correspond to the dimensions set on the `Rml::Context` being rendered.

### Basic rendering

The basic rendering functions are required to be implemented by all render interfaces. These are implemented as pure virtual functions, and thus must be overloaded before one can instantiate the implementation of the render interface.

Basic rendering allows the application to display a basic layout, including text, borders, textures, and some of the decorators. Advanced rendering functions, such as transforms, filters, and box shadows, require additional advanced rendering functions, documented further below.

#### Geometry

All geometry in RmlUi is first submitted to the application with a call to `CompileGeometry()`. This gives the application the opportunity to compile the geometry data into a format optimal for its rendering system, or to simply store the references to the data. All later use of this geometry is then referred to through a handle to it, as determined by the application.

```cpp
// Called by RmlUi when it wants to compile geometry to be rendered later.
virtual Rml::CompiledGeometryHandle CompileGeometry(Rml::Span<const Rml::Vertex> vertices, Rml::Span<const int> indices) = 0;
```

All geometry is given as indexed triangles.

- `vertices`: An array of vertices making up the geometry; each vertex is an `Rml::Vertex` type, defined in `<RmlUi/Core/Vertex.h>`{:.incl}.
- `indices`: An array of integer indices, each indexing a single vertex from the vertex array. As all geometry is given in triangles, the number of indices will always be a multiple of three.

When RmlUi calls this, the application should generate and return a `CompiledGeometryHandle`, which is a pointer-sized integer, to any value needed to uniquely identify the compiled geometry. RmlUi will use that returned value to refer to the same geometry during later calls to other render functions. The value *zero* (0) is reserved for invalid handles, so this value should only be returned to indicate an error.

*Note:* RmlUi keeps a copy of the geometry data during its lifetime. In particular, the library guarantees that the pointed-to vertex and index data are valid and immutable until `ReleaseGeometry()` is called with the same geometry handle. Thus, it is safe for the application to store the references (spans) to the geometry data if they need to refer to it later, within the lifetime of the geometry.


```cpp
// Called by RmlUi when it wants to render geometry.
virtual void RenderGeometry(Rml::CompiledGeometryHandle geometry, Rml::Vector2f translation, Rml::TextureHandle texture) = 0;
```

When RmlUi wants to render geometry, it calls `RenderGeometry()` with a geometry handle previously returned from the compile geometry call.

- `geometry`: The handle to the geometry to be rendered.
- `translation`: the 2D translation to be applied to the geometry.
- `texture`: The handle to the texture to be applied to the geometry, this will be zero for untextured geometry.

All physical coordinates (the vertex positions and the geometry translation) are given in pixel offsets from the top-left of the current context being rendered. Geometry is rendered through the render interface in order, so while you don't necessary have to pass the geometry through to your rendering system immediately (if you're implementing some kind of geometry aggregation for example), it should still be rendered in the order it came through.

```cpp
// Called by RmlUi when it wants to release geometry.
virtual void ReleaseGeometry(Rml::CompiledGeometryHandle geometry) = 0;
```

Once the geometry is not needed any further, RmlUi will call `ReleaseGeometry()` to request the application to release it.

- `geometry`: The handle to the geometry to be released.

After the call to this function, any references to the geometry data are invalidated.

#### Textures

RmlUi makes calls to the render interface to load, generate and release textures. As this functionality is required by RmlUi, these functions must be implemented in all render interfaces.

```cpp
// Called by RmlUi when a texture is required by the library.
virtual Rml::TextureHandle LoadTexture(Rml::Vector2i& texture_dimensions, const Rml::String& source) = 0;

// Called by RmlUi when a texture is required to be generated from a sequence of pixels in memory.
virtual Rml::TextureHandle GenerateTexture(Rml::Span<const Rml::byte> source, Rml::Vector2i source_dimensions) = 0;

// Called by RmlUi when a loaded or generated texture is no longer required.
virtual void ReleaseTexture(Rml::TextureHandle texture) = 0;
```

`LoadTexture()` is called when RmlUi wants to load a texture from an external source (usually a file, but this is up to the application).
- `texture_dimensions`: Should be set by the application to the x- and y-dimensions of the loaded texture.
- `source`: The source name specified in the RML (for an image tag) or RCSS (for a decorator image reference), joined with the path of the referencing document.

The `LoadTexture()` function should return a `Rml::TextureHandle` type. This is a `uintptr_t`, and can be set to whatever you need to uniquely identify the loaded texture. The value *zero* (0) is reserved for invalid handles, and should only be used to indicate an error while trying to load the texture.

`GenerateTexture()` is called from RmlUi when it has raw pixel data it wants to convert to a texture, such as for fonts. The raw pixel data is given in `source`; this is an array of unsigned, 8-bit values in RGBA order. It is laid out in tightly-packed rows, so exactly `source_dimensions.x * source_dimensions.y * 4` bytes in size. The `source_dimensions` variable is set to the dimensions of the raw texture data. The application should return a `Rml::TextureHandle` uniquely identifying the texture, just as in `LoadTexture()`.

`ReleaseTexture()` is called with a texture handle once it is no longer required by RmlUi.

#### Scissor region

RmlUi relies on scissoring regions to clip an element's hidden content. Therefore, these two functions are required to be implemented on all render interfaces:

```cpp
// Called by RmlUi when it wants to enable or disable scissoring to clip content.
virtual void EnableScissorRegion(bool enable) = 0;

// Called by RmlUi when it wants to change the scissor region.
virtual void SetScissorRegion(Rml::Rectanglei region) = 0;
```

`EnableScissorRegion()` is called to enable and disable scissoring of rendered geometry.

`SetScissorRegion()` is called when RmlUi wants to define the current scissor region. The scissor region is given as a rectangle in pixel units whose origin is located in the top-left corner of the rendering context. The scissor region is always given in window coordinates, which implies that it is not affected by any active transforms. Until the scissor region is changed, all RmlUi geometry should be clipped to fall within this region.

When [properties that require](#feature-table) clip masks are used in the document, the scissor region alone will not be sufficient to clip content correctly. The render interface must implement the [clip mask](#clip-mask) feature to support such layouts.


### Advanced rendering

Advanced rendering functions are all optional, allowing the application access to many additional rendering features. Each feature is implemented as a distinct set of virtual functions, enabling applications to incrementally implement the feature set they require at any given time.

#### Clip mask

Clipping is important to the RmlUi layout model, in particular so that overflow can be hidden from elements. This can normally be handled by the scissor region, which serves a similar purpose to the clip mask. However, the scissor region can only be an axis-aligned rectangular shape. When applying transforms, the clipping region can take other shapes due to rotation or projection. Additionally, when applying border-radius we want to clip overflow to the curved border. Clip masks allow the library to clip to any region, by using arbitrary geometry to define the clipping area.

The following two functions need to be implemented to enable this feature.

```cpp
// Called by RmlUi when it wants to enable or disable the clip mask.
virtual void EnableClipMask(bool enable);

// Called by RmlUi when it wants to set or modify the contents of the clip mask.
virtual void RenderToClipMask(Rml::ClipMaskOperation operation, Rml::CompiledGeometryHandle geometry, Rml::Vector2f translation);
```

RmlUi enables or disables the clip mask using `EnableClipMask()`. When enabled, the clip mask should hide any rendered contents outside the area of the mask. The clip mask applies exclusively to all other functions that render with a geometry handle, in addition to the layer compositing function while rendering to its destination.

When RmlUi wants to set a new clip mask, it makes one or more calls to `RenderToClipMask()`. This function takes a `geometry` handle and a `translation` vector, just like a call to `RenderGeometry()`. However, the clip mask render function should not be rendered like normal geometry, but rather it should apply to the *clip mask*. The additional `operation` parameter describes how the geometry should be applied to the clip mask, and takes one of the following values.

```cpp
enum class ClipMaskOperation {
	Set,        // Set the clip mask to the area of the rendered geometry, clearing any existing clip mask.
	SetInverse, // Set the clip mask to the area *outside* the rendered geometry, clearing any existing clip mask.
	Intersect,  // Intersect the clip mask with the area of the rendered geometry.
};
```

The clip mask applies globally, as if all layers share a single clip mask. Any active transform should be applied to the geometry, just like during a normal geometry rendering call. RmlUi does not define how the clip mask is implemented on the rendering side, but one approach is to use a *stencil buffer*.

#### Transforms

Transforms allow the rendered location and size of any geometry to be modified, and is necessary to support the `transform`{:.prop} RCSS property. RmlUi will call the following function when the transform matrix needs to change.

```cpp
// Called by RmlUi when it wants the renderer to use a new transform matrix.
virtual void SetTransform(const Rml::Matrix4f* transform);
```

The `transform` parameter is a pointer to the new transformation matrix. A `nullptr`{:.value} will be submitted when RmlUi wants to set the transform back to identity. This function is never called if there are no `transform`{:.prop} properties present.

Important consideration to achieve correct results:

- After being set, the transform should apply to all functions that render with a geometry handle, and only those. In particular, this implies that it does not apply to the scissor region, but does apply when rendering to the clip mask.
- The `Matrix4f` type is in **column-major** ordering. If your graphics API of choice takes row-major matrices, the matrix must first be transposed before submitting it to the graphics API.
- When a draw call is received through one of the `Render...()` calls, the `translation` vector should first be applied to the position of the vertices. Then the resulting 2d-vector should be extended to a 4d-vector with elements `z = 0` and `w = 1` for correct results of the translation and perspective parts of the transform.
- The provided `transform` matrix does not include projection to the user's window, thus, the user should create their own projection matrix `project` and use the product of `project * transform` to produce the vertex position output.
- Make sure to set the *z*<sub>far</sub> and *z*<sub>near</sub> planes of your projection matrix sufficiently far away from the document plane (*z*=0) so that geometry is not clipped when it is rotated or translated into the *z*-axis.

Pseudo vertex shader code for the vertex positions:

```glsl
input Vec2 vertex_pos;
input Vec2 translation;
input Mat4 transform;
input Mat4 project;

output Vec4 frag_pos;

void main() {
	Vec4 pos_document = Vec4(vertex_pos + translation, 0, 1);
	frag_pos = project * transform * pos_document;
}
```

#### Layers

In RmlUi, layers are used for several rendering effects. For instance, they are fundamental to applying filters to a collection of elements in isolation, and to allow compositing different parts that make up a box shadow.

Layers are placed within the *render stack*. Layers are always constructed by being pushed onto the stack, and destroyed by being popped from the stack. Stack operations always happen in an ordered fashion - i.e. last in, first out (LIFO) order.

Rendering should always be done on the layer on the top of the render stack. In addition, a layer can be composited (blended) together with another layer. The following functions need to be implemented for layer support in RmlUi.

```cpp
// Called by RmlUi when it wants to push a new layer onto the render stack, setting it as the new render target.
virtual Rml::LayerHandle PushLayer();

// Composite two layers with the given blend mode and apply filters.
virtual void CompositeLayers(Rml::LayerHandle source,
                             Rml::LayerHandle destination,
                             Rml::BlendMode blend_mode,
                             Rml::Span<const Rml::CompiledFilterHandle> filters);

// Called by RmlUi when it wants to pop the render layer stack, setting the new top layer as the render target.
virtual void PopLayer();
```

The `PushLayer()` function is called when RmlUi wants to push a new layer onto the render stack. Here, the application should return a `LayerHandle`. Just like the other interface handles, this is a pointer-sized integer that the application should set to a value uniquely identifying the new layer (i.e. the top of the stack). This handle is later used during compositing to refer to the layer. The new layer should be initialized to transparent black within the current scissor region.

The `CompositeLayers()` function is called when RmlUi wants to composite two layers. This can be called for any two layers within the render stack, not just the top layers. It takes a `source` and a `destination` layer, which should be blended together according to the given `blend_mode`.

```cpp
enum class BlendMode {
	Blend,   // Normal alpha blending.
	Replace, // Replace the destination colors from the source.
};
```

In normal `Blend` mode, the source should be alpha composited onto the destination layer (i.e. *source **over** destination* operation in composition terminology). Note that, the application should use composition with premultiplied alpha to ensure correct blending with (partially) transparent images, see the [blending conventions](#blending) above. On the other hand, in `Replace` mode, the source should simply be written to the destination as-is, without any alpha blending.

The `filters` parameter specifies a list of filters that RmlUi wants to use during composition. This is only necessary to handle for applications that want to support the *filters* rendering feature. If this list is populated, then the application should apply the filters in the listed order, as if applying the filters to a copy of the source layer. The filters should be applied just before compositing. Then the result of the filtering is composited onto the destination layer, according to the same blending rules as previously.

Note that, the source and destination can refer to the same layer. In this case, they should be composited as if the source is first copied to a temporary buffer, and the temporary buffer then being composited onto the destination. This can be used e.g. to apply filters to the current layer.

Also, note that the scissor region takes effect during the composition operation. Only destination pixels within the scissor region should be affected by this operation. Keep in mind that some filters (like blur) can be affected by source pixels outside the scissor region. The scissor region only applies during the final composition.

Finally, `PopLayer()` is called when RmlUi wants to pop the top layer from render stack. Any previous handle to that layer will no longer be used.

#### Render textures
{:#render-textures}

The current layer can be stored as a texture, so that RmlUi can re-use its contents in later rendering operations.

```cpp
// Called by RmlUi when it wants to store the current layer as a new texture to be rendered later with geometry.
virtual Rml::TextureHandle SaveLayerAsTexture();
```

The `SaveLayerAsTexture()` function is called by RmlUi to store the current layer to a texture. It should return an application-specific `TextureHandle` to the new texture, just like for other textures. RmlUi can then use this texture during normal geometry rendering.

The active scissor region applies to this operation. This implies that the texture should be extracted from the same region, so that the size of the new texture matches the size of the scissor region.

When RmlUi no longer needs this texture, `ReleaseTexture()` will be called with its handle, just like with other textures.

#### Mask images
{:#mask-images}

A mask can be used to hide parts of an element, or other rendered geometry. Mask images can gradually fade out contents, as opposed to clip masks. This feature is mainly used to implement the `mask-image`{:.prop} property. Any image can be used to specify the mask, allowing users to create interesting effects by fading out contents.

```cpp
// Called by RmlUi when it wants to store the current layer as a mask image, to be applied later as a filter.
virtual Rml::CompiledFilterHandle SaveLayerAsMaskImage();
```

The `SaveLayerAsMaskImage()` function is called by RmlUi to store the current layer, so that the contents of the layer can be used as a mask image. The application should return a handle to a new filter representing the stored mask image. When that same filter handle is provided during layer composition, the application should use the stored image as a mask. RmlUi only uses alpha masks, which implies that the alpha channel of the mask should be multiplied with the alpha channel of the source image.

When RmlUi no longer needs this mask image, `ReleaseFilter()` will be called with its handle, just like with other filters.

#### Filters

Filters are a way to add graphical effects to a collection of geometry, such as blur, drop shadow, and color changes. For example, an element, including all its children, can have a sepia toning filter applied to it. However, filters are also used internally to apply effects, like the blur that can be used on box shadows.

```cpp
// Called by RmlUi when it wants to compile a new filter.
virtual Rml::CompiledFilterHandle CompileFilter(const Rml::String& name, const Rml::Dictionary& parameters);

// Called by RmlUi when it no longer needs a previously compiled filter.
virtual void ReleaseFilter(Rml::CompiledFilterHandle filter);
```

A filter is first compiled using `CompileFilter()`, such that the renderer can prepare its pipeline for rendering, and also so that RmlUi can easily refer to the same filter and set of parameters later. The application should return a handle uniquely representing the filter and its parameters. The filters are applied during layer compositing, see the [documentation for `CompositeLayers()`](#layers) above. The filters apply their described effect just before the composition stage.

The provided `name` refers to a particular filter effect type, each of which has a given set of `parameters` that can be used to adjust the effect. RmlUi supports all [filters specified in CSS](https://www.w3.org/TR/filter-effects-1/#supported-filter-functions), and we refer to that specification for how to render each particular effect. The following table lists all the filter types, together with the parameters each one is provided with.

| Filter        | Parameters                                                                                    |
|---------------|-----------------------------------------------------------------------------------------------|
| `opacity`     | `float value`                                                                                 |
| `blur`        | `float sigma` (pixel length)                                                                  |
| `drop-shadow` | `float sigma` (pixel length)<br>`Rml::Colourb color`<br>`Rml::Vector2f offset` (pixel length) |
| `brightness`  | `float value`                                                                                 |
| `contrast`    | `float value`                                                                                 |
| `invert`      | `float value`                                                                                 |
| `grayscale`   | `float value`                                                                                 |
| `sepia`       | `float value`                                                                                 |
| `hue-rotate`  | `float value` (angle in radians)                                                              |
| `saturate`    | `float value`                                                                                 |

Unless otherwise noted, float values are normalized, unit-less factors indicating the strength of the effect. Note that, the application itself, or plugins, can provide other filter types with their own set of parameters. The above table lists the ones that are built-in to RmlUi. Of course, it is also possible for the application to define their own filters, see the [C++ filters documentation](../filters.html) for details.

As an example, for `brightness`, its `value` parameter can be fetched as follows:

```cpp
float brightness = Rml::Get(parameters, "value", 0.f);
```
Here, a value of `1` would have no effect on the image, a greater value would make the image brighter, while a lower value would make it darker. See the CSS specifications for how to interpret the different values, or take inspiration from the built-in [OpenGL3 renderer](https://github.com/mikke89/RmlUi/blob/master/Backends/RmlUi_Renderer_GL3.cpp) in RmlUi.

Finally, when RmlUi no longer has a need for a previously compiled filter, the `ReleaseFilter()` function will be called with the `handle` to the filter.

#### Shaders

In RmlUi, shaders are used for rendering geometry in a distinct manner to produce some desired effect. While filters apply effects to a layer, shaders instead allow geometry itself to be rendered in different ways. The core RmlUi library does not provide any shader code itself, but rather an abstraction describing how rendering with a given shader should behave. It is flexible, so that users can name their own shaders to be used however the application sees fit.

Shaders are compiled, rendered with, and released just like normal geometry. The main difference being the shader compilation process, and that rendering additionally takes a handle to a shader. The following functions should be implemented to support this feature.

```cpp
// Called by RmlUi when it wants to compile a new shader.
virtual Rml::CompiledShaderHandle CompileShader(const Rml::String& name, const Rml::Dictionary& parameters);

// Called by RmlUi when it wants to render geometry using the given shader.
virtual void RenderShader(Rml::CompiledShaderHandle shader,
                          Rml::CompiledGeometryHandle geometry,
                          Rml::Vector2f translation,
                          Rml::TextureHandle texture);

// Called by RmlUi when it no longer needs a previously compiled shader.
virtual void ReleaseShader(Rml::CompiledShaderHandle shader);
```

Shaders are compiled just like filters. A shader is first compiled using `CompileShader()`, such that the renderer can prepare its pipeline for rendering, and also so that RmlUi can easily refer to same shader and set of parameters later. The application should return a handle uniquely representing the shader and its parameters.

The provided `name` refers to a particular shader effect type, each of which has a given set of `parameters` that can be used to adjust the effect. RmlUi provides selected built-in shaders to represent certain effects, such as gradients. The following table lists all the shader types, together with the parameters each one is provided with.

| Shader | Parameters |
| --- | --- |
| `linear-gradient` | `bool repeating`{:.value}: True if the gradient is repeating.<br>`Rml::Vector2f p0`{:.value}: Starting point.<br>`Rml::Vector2f p1`{:.value}: Ending point.<br>`float length`{:.value}: The length of the gradient line (px).<br>`Rml::ColorStopList color_stop_list`{:.value}: Color stop list. |
| `radial-gradient` | `bool repeating`{:.value}: True if the gradient is repeating.<br>`Rml::Vector2f center`{:.value}: Center point.<br>`Rml::Vector2f radius`{:.value}: Two-dimensional radius.<br>`Rml::ColorStopList color_stop_list`{:.value}: Color stop list. |
| `conic-gradient`  | `bool repeating`{:.value}: True if the gradient is repeating.<br>`Rml::Vector2f center`{:.value}: Center point.<br>`float angle`{:.value}: Rotation of the gradient (rad).<br>`Rml::ColorStopList color_stop_list`{:.value}: Color stop list. |
| `shader`          | `Rml::String value`{:.value}: A user-specified value.<br>`Rml::Vector2f dimensions`{:.value}: Dimensions of the paint area. |

Note that, the application itself, or plugins, can provide other shader types using [custom decorators](../decorators.html#custom-decorators) with their own set of parameters. The above table lists the ones that are built-in to RmlUi.

The parameters for the various `[...]-gradient` shaders have already been processed such that they are in a form suitable for rendering. In particular, the color stop lists have already been resolved, such that each color stop is given as a position with a *number* unit, where zero represents the beginning of the gradient line and unity represents the end of the gradient line. Specifically, the `Rml::ColorStopList` is a vector of `ColorStop` structs, having `color`  and `position` members. The latter is specified as a `NumericValue` type whose unit is always a `NUMBER`{:.value}. Please see the CSS specifications for how to interpret these parameters: [`linear-gradient`{:.prop}](https://www.w3.org/TR/css-images-3/#linear-gradients), [`radial-gradient`{:.prop}](https://www.w3.org/TR/css-images-3/#radial-gradients), and [`conic-gradient`{:.prop}](https://www.w3.org/TR/css-images-4/#conic-gradients). Also, feel free to take a look at the built-in [OpenGL3 renderer](https://github.com/mikke89/RmlUi/blob/master/Backends/RmlUi_Renderer_GL3.cpp) in RmlUi, and how they are implemented there

The `shader` shader is a generic shader which can be given a meaning by the application. The `shader(<string>)`{:.value} decorator directly hands over the provided string as a parameter, allowing the application to render the geometry accordingly. The dimensions of the paint area is provided as a parameter, in addition, the texture coordinates of its accompanying geometry is normalized `[0, 1]` to the paint area of the decorator.

When RmlUi wants to render some geometry with a given shader, it calls `RenderShader()`. This works just like `RenderGeometry()`, except that it also takes a `shader` argument, which indicates which shader the geometry should be rendered with.

Finally, when RmlUi no longer has a need for a previously compiled shader, the `ReleaseShader()` function will be called with the `handle` to the shader.
