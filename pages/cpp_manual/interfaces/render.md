---
layout: page
title: Render interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
next: file
---


The render interface is how RmlUi sends its generated geometry through to the application to render. It also uses the interface to load textures from external sources and from internally generated pixel data (for font textures). Applications must install a render interface before initialising RmlUi.

The render interface is given in `<RmlUi/Core/RenderInterface.h>`{:.incl}. To develop a custom render interface, create a class derived from `Rml::RenderInterface` and provide function definitions for the pure virtual functions, and any of the others that you wish to provide functionality for.


### Rendering conventions

Before implementing the rendering API in RmlUi, the user should understand the following rendering conventions and assumptions used by the library.

* Vertex position coordinates are in `pixel` units.
* The coordinate system of documents in RmlUi places the origin at the top-left corner of the window.
* Indices define sets of triangles in a counter-clockwise winding order.
* The generated textures in RmlUi use the convention that the origin is at the bottom left corner.
* To handle transforms correctly, see the [transforms](#transforms) section.

Other rendering assumptions.

* Alpha blending should be enabled.
* Vertex colors are given in the sRGB color space.
* Textures should have their fetched color multiplied by the vertex color.

#### Projection matrix 

The user must construct their own projection matrix while considering the above conventions, along with the conventions and settings used in their graphics API. Eg. the OpenGL convention is to place the origin at the bottom-left corner of the window. Thus, the user should flip the y-axis when constructing their projection matrix. The DirectX convention is to place the origin at the top-left corner of the window, thus, an orthographic projection matrix which follows this convention can be used.

#### Generated textures

The generated textures in RmlUi follow the OpenGL convention of placing the texture origin at the bottom-left corner. Other graphics APIs, including DirectX, use the top-left corner as the origin. Thus, textures can appear vertically flipped. In this case, the user can flip the texture y-coordinates provided by RmlUi.

#### Face culling

If face culling is enabled, make sure to get the culled face direction correct. Otherwise you will get a blank window. Eg. by default OpenGL defines front faces to be in a counter-clockwise winding direction, and will cull back faces. Thus, in terms of the geometry submitted by RmlUi these defaults can be used. On the other hand, the DirectX convention is to use clockwise winding direction for front faces, thus, if back face culling is enabled you will get a blank screen. The solution is to either disable face culling, or set the culling to cull front faces and not back faces.

#### Viewport

Make sure to properly setup the viewport in your graphics API. This should typically correspond to the dimensions set on the `Rml::Context` being rendered.


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
virtual void RenderCompiledGeometry(Rml::CompiledGeometryHandle geometry, const Rml::Vector2f& translation);

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
* `texture_handle`: a reference to a `Rml::TextureHandle` type. This is a `uintptr_t`, and can be set to whatever you need to uniquely identify the loaded texture, except 0 which is reserved for an invalid texture.
* `texture_dimensions`: should be set to the x- and y-dimensions of the loaded texture.
* `source`: the source name specified in the RML (for an image tag) or RCSS (for a decorator image reference), joined with the path of the referencing document.

If the `LoadTexture()` function succeeds in loading the texture, it should return `true`. Otherwise it should return `false`.

`GenerateTexture()` is used by the font system to convert raw pixel data to a texture. The `texture_handle` parameter is a reference to a `Rml::TextureHandle` type to be set, as in `LoadTexture()`. The raw pixel data is given in `source`; this is an array of unsigned, 8-bit values in RGBA order. It is laid out in tightly-packed rows, so exactly `(source_dimensions.x * source_dimensions.y * 4)` bytes in size. The `source_dimensions` variable is set to the dimensions of the raw texture data.

`ReleaseTexture()` is called with a texture handle once it is no longer required by RmlUi.

See the sample shell for an OpenGL texture implementations.

### Transforms

Transforms allow the rendered location and size of any geometry to be modified, and is necessary to support the `transform`{:.prop} RCSS property. RmlUi will call the following function when the transform matrix needs to change, and expects all geometry rendered afterwards to apply the given transform.

```cpp
// Called by RmlUi when it wants the renderer to use a new transform matrix.
// If no transform applies to the current element, nullptr is submitted. Then it expects the renderer to use
// an identity matrix or otherwise omit the multiplication with the transform.
// @param[in] transform The new transform to apply, or nullptr if no transform applies to the current element.
virtual void SetTransform(const Rml::Matrix4f* transform);
```

A nullptr will be submitted when RmlUi wants to set the transform back to identity. This function is never called if there are no `transform`{:.prop} properties present.

Important things to be aware of to get correct results:

- The `Matrix4f` type is in **column-major** ordering. If your graphics API of choice takes row-major matrices, the matrix must first be transposed before submitting it to the graphics API.
- When a draw call is received through one of the `Render...()` calls, the `translation` vector should first be applied to the position of the vertices. Then the resulting 2d-vector should be extended to a 4d-vector with elements `z = 0` and `w = 1` for correct results of the translation and perspective parts of the transform.
- The provided `transform` matrix does not include projection to the user's window, thus, the user should create their own projection matrix `project` and use the product of `project * transform` to produce the vertex position output.
- Make sure to set the *z*<sub>far</sub> and *z*<sub>near</sub> planes of your projection matrix sufficiently far away from the document plane (*z*=0) so that geometry is not clipped when it is rotated or translated into the *z*-axis.
- When both a transform and scissor region is active, the scissor region must also have the `transform` matrix applied for correct results. One solution to this is to draw a rectangle with the position and dimensions of the scissor region into a stencil buffer with the transform applied. Then, when rendering vertices, use this stencil buffer to reject pixels outside of the drawn parts of the stencil buffer.

Pseudo vertex shader code for the vertex positions:

```c
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
