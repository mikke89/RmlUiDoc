---
layout: page
title: Render interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
next: file
---


The render interface is how RmlUi sends its generated geometry through to the application to render. It also uses the interface to load textures from external sources and from internally generated pixel data (for font textures). Applications must install a render interface before initialising RmlUi.

The render interface is given in `<RmlUi/Core/RenderInterface.h>`{:.incl}. To develop a custom render interface, create a class derived from `Rml::RenderInterface` and provide function definitions for the pure virtual functions, and any of the others that you wish to provide functionality for.

### Rendering simple geometry

If you do not provide function definitions for compiling geometry, or do not compile some geometry, RmlUi will call the `RenderGeometry()` function with geometry to be displayed:

```cpp
// Called by RmlUi when it wants to render geometry that the application does not wish to optimise.
virtual void RenderGeometry(Rml::Vertex* vertices,
                            int num_vertices,
                            int* indices,
                            int num_indices,
                            Rml::TextureHandle texture,
                            const Rml::Vector2f& translation) = 0;
```

All geometry from RmlUi is given in this format of indexed triangles.
* `vertices`: an array of vertices making up the geometry; each vertex is a `Rml::Vertex` type, defined in `<RmlUi/Core/Vertex.h>`{:.incl}.
* `num_vertices`: the number of vertices in the array; no index will be equal to or higher than this number.
* `indices`: an array of integer indices, each indexing a single vertex from the vertex array.
* `num_indices`: the total number of indices in the array; as all geometry is given in triangles, this will always be a multiple of three.
* `texture`: the application-defined handle to the texture to be applied to the geometry; this will be NULL for untextured geometry.
* `translation`: the 2D translation to be applied to the geometry.

All physical coordinates (the vertex positions and the geometry translation) are given in pixel offsets from the top-left of the current context being rendered.

Geometry is rendered through the render interface in order, so while you don't necessary have to pass the geometry through to your rendering system immediately (if you're implementing some kind of geometry aggregation for example), it should still be rendered in the order it came through.

### Compiling and rendering geometry

RmlUi will give you the opportunity to compile all geometry it renders into a format optimal for your rendering system before it falls back to the `RenderGeometry()` function. It uses the following functions on the render interface to do this:

```cpp
// Called by RmlUi when it wants to compile geometry it believes will be static for the forseeable future.
virtual Rml::CompiledGeometryHandle CompileGeometry(Rml::Vertex* vertices, int num_vertices, int* indices, int num_indices, Rml::TextureHandle texture);

// Called by RmlUi when it wants to render application-compiled geometry.
virtual void RenderCompiledGeometry(Rml::CompiledGeometryHandle geometry, const Core::Rml::Vector2f& translation);

// Called by RmlUi when it wants to release application-compiled geometry.
virtual void ReleaseCompiledGeometry(Rml::CompiledGeometryHandle geometry);
```

RmlUi will call `CompileGeometry()` with any geometry it renders internally to give the application the choice to compile it. It provides the geometry in the same format as into the `RenderGeometry()` function above. The returned `Rml::CompiledGeometryHandle` is a void pointer type which can be any value you need to uniquely identify the compiled geometry. The NULL (0) value is reserved for the invalid handle, so be sure not to return this as a valid handle! If NULL is returned, the geometry is assumed to have not been compiled and will be rendered through `RenderGeometry()` instead. The application will only be asked once to compile each geometry.

If a compiled geometry handle is returned through `CompileGeometry()`, RmlUi will render the geometry through the `RenderCompiledGeometry()` function. It takes geometry, the handle previously returned from `CompileGeometry()`, and translation, the offset from the top-left of the current context the geometry should be rendered at.

If the compiled geometry alters or is otherwise not needed any further, RmlUi will call `ReleaseCompiledGeometry()` to request the application to release it.

### Configuring the scissor region

RmlUi relies on scissoring regions to clip an element's hidden content. Therefore, these two functions are required to be implemented on all render interfaces:

```cpp
// Called by RmlUi when it wants to enable or disable scissoring to clip content.
virtual void EnableScissorRegion(bool enable) = 0;

// Called by RmlUi when it wants to change the scissor region.
virtual void SetScissorRegion(int x, int y, int width, int height) = 0;
```

`EnableScissorRegion()` is called to enable to disable scissoring on RmlUi geometry.

`SetScissorRegion()` is called when RmlUi wants to define the current scissor region. The scissor region is given as a rectangle, x and y being the top-left corner (as a pixel offset from the top-left corner of the rendering context). width and height are the dimensions of the rectangle, in pixels. Until the scissor region is changed, all RmlUi geometry should be clipped to fall within this region.

For example implementations of the scissoring functions, see the sample shell (`/Samples/shell/`{:.path}) for an OpenGL approach.

### Generating and releasing textures

RmlUi makes calls to the render interface to load, generate and release textures. As this functionality is required by RmlUi, these functions must be implemented in all render interfaces.

```cpp
// Called by RmlUi when a texture is required by the library.
virtual bool LoadTexture(Rml::TextureHandle& texture_handle,
                         Rml::Vector2i& texture_dimensions,
                         const Rml::String& source) = 0;

// Called by RmlUi when a texture is required to be built from an internally-generated sequence of pixels.
virtual bool GenerateTexture(Rml::TextureHandle& texture_handle,
                             const Rml::byte* source,
                             const Rml::Vector2i& source_dimensions) = 0;

// Called by RmlUi when a loaded texture is no longer required.
virtual void ReleaseTexture(Rml::TextureHandle texture_handle) = 0;
```

`LoadTexture()` is called when RmlUi wants to load a texture from an external source (usually a file, but this is up to the application).
* `source`: the source name specified in the RML (for an image tag) or RCSS (for a decorator image reference).
* `source_path`: the path of the referencing document.
* `texture_handle`: a reference to a `Rml::TextureHandle` type. This is a `uintptr_t`, and can be set to whatever you need to uniquely identify the loaded texture, except 0 which is reserved for an invalid texture.
* `texture_dimensions`: should be set to the x- and y-dimensions of the loaded texture.

If the `LoadTexture()` function succeeds in loading the texture, it should return `true`. Otherwise it should return `false`.

`GenerateTexture()` is used by the font system to convert raw pixel data to a texture. The `texture_handle` parameter is a reference to a `Rml::TextureHandle` type to be set, as in `LoadTexture()`. The raw pixel data is given in source; this is an array of unsigned, 8-bit values in RGBA order. It is laid out in tightly-packed rows, so is exactly `(source_dimensions.x * source_dimensions.y * 4)` bytes in size. The source_dimensions variable is set to the dimensions of the raw texture data.

`ReleaseTexture()` is called with a texture handle once it is no longer required by RmlUi.

See the sample shell for an OpenGL texture implementations.

### Transforms

Transforms allow the rendered location and size of any geometry to be modified, and is necessary to support the `transform`{:.prop} RCSS property. RmlUi will call the following function when the transform matrix needs to change, and expects all geometry rendered afterwards to apply the given transform.

```cpp
// Called by RmlUi when it wants the renderer to use a new transform matrix.
// If no transform applies to the current element, nullptr is submitted. Then it expects the renderer to use an identity matrix or otherwise omit the multiplication with the transform.
// @param[in] transform The new transform to apply, or nullptr if no transform applies to the current element.
virtual void SetTransform(const Rml::Matrix4f* transform);
```

A nullptr will be submitted when RmlUi wants to set the transform back to identity. This function is never called if there are no `transform`{:.prop} properties present.
