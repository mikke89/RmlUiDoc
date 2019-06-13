---
layout: page
title: Contexts
parent: cpp_manual
next: events
---

{{page.lib_name}} contexts are independent collections of documents. All documents exist within a single context. Contexts are rendered, updated and given input independently of each other at the application's discretion.

### Uses of multiple contexts

Most games will feature a single context for the main interface. Multiple contexts could be used however for a number of different reasons.

#### Multiple desktops

A second or subsequent context could be used to store alternative 'desktops' that the user could switch to, in a similar fashion to many Linux desktops. This could be very useful for interface-heavy games where the user may have several windows open at once, more than could fit easily onto one screen.

#### In-world interfaces

Computer terminals or consoles in a 3D game world could themselves be {{page.lib_name}} contexts. As they wouldn't necessarily be viewed parallel to the screen, mouse input would need to be projected onto the surface. When the context was rendered, it would need to be transformed correctly to fit onto the surface or rendered onto a texture.

### Creating a context

To create a new context, use the `CreateContext()` function in `{{page.lib_ns}}::Core`.

```cpp
// Creates a new element context.
// @param[in] name The new name of the context. This must be unique.
// @param[in] dimensions The initial dimensions of the new context.
// @return The new context, or NULL if the context could not be created.
{{page.lib_ns}}::Core::Context* CreateContext(const {{page.lib_ns}}::Core::String& name,
                                     const {{page.lib_ns}}::Core::Vector2i& dimensions);
```

The context needs a unique string name and initial dimensions. The dimensions are used to generate relative lengths (for example, if a document has a percentage dimension), and sets the extents for the mouse cursor within the context.

To fetch a previously-constructed context, use the `GetContext()` function.

```cpp
// Fetches a previously constructed context by name.
// @param[in] name The name of the desired context.
// @return The desired context, or NULL if no context exists with the given name.
{{page.lib_ns}}::Core::Context* GetContext(const {{page.lib_ns}}::Core::String& name);
```

### Releasing a context

Contexts are reference counted, and begin with a reference count of one. Once you have finished with a context, call `RemoveReference()` to release it. It will be destroyed, and all of its documents released.

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
// @return The loaded document, or NULL if no document was loaded.
ElementDocument* LoadDocument(const {{page.lib_ns}}::Core::String& document_path);
```

The `document_path` parameter will be given to {{page.lib_name}}'s [file interface](interfaces.html#the-file-interface) to be open and read. If the document is loaded successfully, it will be added to the context and returned. Call `Show()` on the document to make it visible.

You can also load documents directly from a memory stream, this can be useful if you want to receive documents over the network or similar.

```cpp
// Load a document into the context.
// @param[in] string The string containing the document RML.
// @return The loaded document, or NULL if no document was loaded.
ElementDocument* LoadDocumentFromMemory(const {{page.lib_ns}}::Core::String& string);
```

To create a new, empty document you can populate dynamically, use the `CreateDocument()` function.

```cpp
// Creates a new, empty document and places it into this context.
// @param[in] tag The document type to create.
// @return The new document, or NULL if no document could be created.
ElementDocument* CreateDocument(const {{page.lib_ns}}::Core::String& tag = "document");
```

The context will attempt to instance an element using the 'body' instancer, with the tag name specified by the caller. If a `{{page.lib_ns}}::Core::ElementDocument` is instanced, it will be added to the context and returned.

### Mouse cursor

Each context can propagate the mouse cursor name to the user through the [system interface](interfaces.html#the-system-interface). The cursor name is set on an element through the  [`cursor`{:.prop} property](../rcss/user_interface.html#cursors-the-cursor-property). When the cursor name changes, the new name is sent though the interface.

In the case of multiple contexts, it might be convenient for only a single context to handle the mouse cursor. The following function can be used to control this behavior:
```cpp
/// Enable or disable handling of the mouse cursor from this context.
/// When enabled, changes to the cursor name is transmitted through the system interface.
/// @param[in] show True to enable mouse cursor handling, false to disable.
void EnableMouseCursor(bool enable);
```
By default it is enabled.


### Events

Event listeners can be attached to a context (rather than an element) to receive events sent to all elements within that context. As with elements, call `AddEventListener()` to attach a listener and `RemoveEventListener()` to detach.

```cpp
// Adds an event listener to the context's root element.
// @param[in] event The name of the event to attach to.
// @param[in] listener Listener object to be attached.
// @param[in] in_capture_phase True if the listener is to be attached to the capture phase, false for the bubble phase.
void AddEventListener(const {{page.lib_ns}}::Core::String& event,
                      {{page.lib_ns}}::Core::EventListener* listener,
                      bool in_capture_phase = false);

// Removes an event listener from the context's root element.
// @param[in] event The name of the event to detach from.
// @param[in] listener Listener object to be detached.
// @param[in] in_capture_phase True to detach from the capture phase, false from the bubble phase.
void RemoveEventListener(const {{page.lib_ns}}::Core::String& event,
                         {{page.lib_ns}}::Core::EventListener* listener,
                         bool in_capture_phase = false);
```

### Input

See the section on [input](input.html) for detail on sending user input from your application into {{page.lib_name}} contexts.

### Custom contexts

Contexts are created, like elements and decorators, through instancers. You can override the default context instancer if you want to create custom contexts. Generally, this is only required for adding support for scripting languages.

#### Creating a custom context

A custom context is a class derived from `{{page.lib_ns}}::Core::Context`. There are no virtual methods on `{{page.lib_ns}}::Core::Context`, so it cannot be specialised.

#### Creating a custom context instancer

A custom context instancer needs to be registered with the {{page.lib_name}} factory in order to override the default instancer. A custom context instancer needs to be derived from `{{page.lib_ns}}::Core::ContextInstancer`, and implement the required virtual methods:

```cpp
// Instances a context.
// @param[in] name Name of this context.
// @return The instanced context.
virtual {{page.lib_ns}}::Core::Context* InstanceContext(const {{page.lib_ns}}::Core::String& name) = 0;

// Releases a context previously created by this context.
// @param[in] context The context to release.
virtual void ReleaseContext({{page.lib_ns}}::Core::Context* context) = 0;

// Releases this context instancer
virtual void Release() = 0;
```

`InstanceContext()` will be called whenever a new context is requested. It takes a single parameter, name, the name of the new context. If a context can be created, it should be initialised and returned. Otherwise, return NULL (0).

`ReleaseContext()` will be called whenever a context is released. The context instancer should destroy the context and free and resources allocated for it.

`Release()` will be called when {{page.lib_name}} is shut down. The instancer should delete itself if it was dynamically allocated.

#### Registering an instancer

To register a custom instancer with {{page.lib_name}}, call `RegisterContextInstancer()` on the {{page.lib_name}} factory after {{page.lib_name}} has been initialised.

```cpp
{{page.lib_ns}}::Core::ContextInstancer* custom_instancer = new CustomContextInstancer();
{{page.lib_ns}}::Core::Factory::RegisterContextInstancer(custom_instancer);
custom_instancer->RemoveReference();
```

Like other instancers, context instancers are reference counted and begin with a single reference. The factory will add its own reference to the instancer once it is registered, so you must remove the initial reference afterwards.

#### Enumerating Contexts

All active contexts can be enumerated via the `{{page.lib_ns}}::Core::GetNumContexts()` and `{{page.lib_ns}}::Core::GetContext(int index)` function calls. 