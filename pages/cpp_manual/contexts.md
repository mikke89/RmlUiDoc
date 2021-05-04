---
layout: page
title: Contexts
parent: cpp_manual
next: events
---

RmlUi contexts are independent collections of documents. All documents exist within a single context. Contexts are rendered, updated and given input independently of each other at the application's discretion.

### Uses of multiple contexts

Most games will feature a single context for the main interface. Multiple contexts could be used however for a number of different reasons.

#### Multiple desktops

A second or subsequent context could be used to store alternative 'desktops' that the user could switch to, in a similar fashion to many Linux desktops. This could be very useful for interface-heavy games where the user may have several windows open at once, more than could fit easily onto one screen.

#### In-world interfaces

Computer terminals or consoles in a 3D game world could themselves be RmlUi contexts. As they wouldn't necessarily be viewed parallel to the screen, mouse input would need to be projected onto the surface. When the context was rendered, it would need to be transformed correctly to fit onto the surface or rendered onto a texture.

### Creating a context

To create a new context, use the `Rml::CreateContext()` function.

```cpp
// Creates a new element context.
// @param[in] name The new name of the context. This must be unique.
// @param[in] dimensions The initial dimensions of the new context.
// @return The new context, or nullptr if the context could not be created.
Rml::Context* CreateContext(const Rml::String& name,
                                     const Rml::Vector2i& dimensions);
```

The context needs a unique string name and initial dimensions. The dimensions are used to generate relative lengths (for example, if a document has a percentage dimension), and sets the extents for the mouse cursor within the context.

To fetch a previously-constructed context, use the `GetContext()` function.

```cpp
// Fetches a previously constructed context by name.
// @param[in] name The name of the desired context.
// @return The desired context, or nullptr if no context exists with the given name.
Rml::Context* GetContext(const Rml::String& name);
```

### Releasing a context

A context can be manually removed by calling the following function.

```cpp
// Removes and destroys a context.
// @param[in] name The name of the context to remove.
// @return True if name is a valid context, false otherwise.
bool RemoveContext(const Rml::String& name);
```
All remaining contexts are destroyed during the call to `Rml::Shutdown()`.

### Update and rendering

If a context is active, it should have `Update()` called on it after the frame's input events have been sent to it.

```cpp
// Updates all elements in the context's documents.
bool Update();
```

To render a context, call `Render()` on it. Easy!

```cpp
// Renders all visible elements in the context's documents.
bool Render();
```

### Loading and creating documents

Documents are loaded through contexts. To load a document from an RML file into a context, call the `LoadDocument()` function on the appropriate context.

```cpp
// Load a document into the context.
// @param[in] document_path The path to the document to load.
// @return The loaded document, or nullptr if no document was loaded.
ElementDocument* LoadDocument(const Rml::String& document_path);
```

The `document_path` parameter will be given to RmlUi's [file interface](interfaces/file.html) to be open and read. If the document is loaded successfully, it will be added to the context and returned. Call `Show()` on the document to make it visible.

You can also load documents directly from a memory stream, this can be useful if you want to receive documents over the network or similar.

```cpp
/// Load a document into the context.
/// @param[in] document_rml The string containing the document RML.
/// @param[in] source_url Optional string used to set the document's source URL, or naming the document for log messages.
/// @return The loaded document, or nullptr if no document was loaded.
ElementDocument* LoadDocumentFromMemory(const String& document_rml, const String& source_url = "[document from memory]");
```

To create a new, empty document you can populate dynamically, use the `CreateDocument()` function.

```cpp
/// Creates a new, empty document and places it into this context.
/// @param[in] instancer_name The name of the instancer used to create the document.
/// @return The new document, or nullptr if no document could be created.
ElementDocument* CreateDocument(const String& instancer_name = "body");
```

The context will attempt to instance an element using the instancer specified by the caller, 'body' by default. If an `Rml::ElementDocument` is instanced, it will be added to the context and returned.

### Mouse cursor

Each context can propagate the mouse cursor name to the user through the [system interface](interfaces/system.html). The cursor name is set on an element through the  [`cursor`{:.prop} property](../rcss/user_interface.html#cursor). When the cursor name changes, the new name is sent though the interface. The client can then change the displayed cursor using the cursor facilities on their platform.

In the case of multiple contexts, it might be convenient for only a single context to handle the mouse cursor. The following function can be used to control this behavior:
```cpp
/// Enable or disable handling of the mouse cursor from this context.
/// When enabled, changes to the cursor name is transmitted through the system interface.
/// @param[in] show True to enable mouse cursor handling, false to disable.
void EnableMouseCursor(bool enable);
```
By default it is enabled.

### Media themes
{:#themes}

Media themes can be used to activate or deactive parts of a style sheet in combination with [media queries](../rcss/media_queries.html), using the `theme`{:.prop} media feature.

```cpp
/// Activate or deactivate a media theme. Themes can be used in RCSS media queries.
/// @param theme_name[in] The name of the theme to (de)activate.
/// @param activate True to activate the given theme, false to deactivate.
void ActivateTheme(const String& theme_name, bool activate);
/// Check if a given media theme has been activated.
/// @param theme_name The name of the theme.
/// @return True if the theme is activated.
bool IsThemeActive(const String& theme_name) const;
```

### Events

Event listeners can be attached to a context (rather than an element) to receive events sent to all elements within that context. As with elements, call `AddEventListener()` to attach a listener and `RemoveEventListener()` to detach.

```cpp
// Adds an event listener to the context's root element.
// @param[in] event The name of the event to attach to.
// @param[in] listener Listener object to be attached.
// @param[in] in_capture_phase True if the listener is to be attached to the capture phase, false for the bubble phase.
void AddEventListener(const Rml::String& event,
                      Rml::EventListener* listener,
                      bool in_capture_phase = false);

// Removes an event listener from the context's root element.
// @param[in] event The name of the event to detach from.
// @param[in] listener Listener object to be detached.
// @param[in] in_capture_phase True to detach from the capture phase, false from the bubble phase.
void RemoveEventListener(const Rml::String& event,
                         Rml::EventListener* listener,
                         bool in_capture_phase = false);
```

Note as for all raw pointers, they are non-owning. Thus, it is the user's responsibility to keep the event listener alive until it is removed, and then to clean it up.

### Input

See the section on [input](input.html) for detail on sending user input from your application into RmlUi contexts.

### Custom contexts

Contexts are created, like elements and decorators, through instancers. You can override the default context instancer if you want to create custom contexts. Generally, this is only required for adding support for scripting languages.

#### Creating a custom context

A custom context is a class derived from `Rml::Context`. There are no virtual methods on `Rml::Context`, so it cannot be specialised.

#### Creating a custom context instancer

A custom context instancer needs to be registered with the RmlUi factory in order to override the default instancer. A custom context instancer needs to be derived from `Rml::ContextInstancer`, and implement the required virtual methods:

```cpp
// Instances a context.
// @param[in] name Name of this context.
// @return The instanced context.
virtual Rml::ContextPtr InstanceContext(const Rml::String& name) = 0;

// Releases a context previously created by this context.
// @param[in] context The context to release.
virtual void ReleaseContext(Rml::Context* context) = 0;

// Releases this context instancer
virtual void Release() = 0;
```

`InstanceContext()` will be called whenever a new context is requested. It takes a single parameter, name, the name of the new context. If a context can be created, it should be initialised and returned wrapped in a `ContextPtr` which is a unique pointer with a custom deleter. Otherwise, return nullptr.

`ReleaseContext()` will be called whenever a context is released. The context instancer should destroy the context and free and resources allocated for it.

`Release()` will be called when RmlUi is shut down. The instancer should delete itself if it was dynamically allocated.

#### Registering an instancer

To register a custom instancer with RmlUi, call `RegisterContextInstancer()` on the RmlUi factory after RmlUi has been initialised.

```cpp
// The custom_instancer must be kept alive until after the call to Rml::Shutdown()
auto custom_instancer = std::make_unique<CustomContextInstancer>();
Rml::Factory::RegisterContextInstancer(custom_instancer.get());
```

Like for other instancers, it is the user's responsibility to manage the lifetime of the instancer. Thus, it must be kept alive until after the call to `Rml::Shutdown()`, and then cleaned up by the user.

#### Enumerating Contexts

All active contexts can be enumerated via the `Rml::GetNumContexts()` and `Rml::GetContext(int index)` function calls. 