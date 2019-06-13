---
layout: page
title: Plugins
parent: cpp_manual
next: controls
---

{{page.lib_name}} has a simple, straightforward system for writing plugins. Plugins receive notification when contexts and elements are created and destroyed.

### Creating a plugin

All plugins derive from the `{{page.lib_ns}}::Core::Plugin` class. The virtual functions that can be overridden are:

```cpp
// Called when {{page.lib_name}} is initialised.
virtual void OnInitialise();
// Called when {{page.lib_name}} shuts down.
virtual void OnShutdown();

// Called when a document load request occurs, before the document's file is opened.
virtual void OnDocumentOpen(Context* context, const {{page.lib_ns}}::Core::String& document_path);
// Called when a document is successfully loaded from file or instanced, initialised and added to its context. This is called before the document's 'load' event.
virtual void OnDocumentLoad(ElementDocument* document);
// Called when a document is unloaded from its context. This is called after the document's 'unload' event.
virtual void OnDocumentUnload(ElementDocument* document);

// Called when a new context is created.
virtual void OnContextCreate({{page.lib_ns}}::Core::Context* context);
// Called when a context is destroyed.
virtual void OnContextDestroy({{page.lib_ns}}::Core::Context* context);

// Called when a new element is created.
virtual void OnElementCreate({{page.lib_ns}}::Core::Element* element);
// Called when an element is destroyed.
virtual void OnElementDestroy({{page.lib_ns}}::Core::Element* element);
```

#### {{page.lib_name}} engine events

The `OnInitialise()` function will be called on all registered plugins when {{page.lib_name}} is successfully initialised. If {{page.lib_name}} is already initialised when a plugin is registered, `OnInitialise()` will be immediately called on the plugin.

`OnShutdown()` is called on all registered plugins when {{page.lib_name}} is shut down, immediately after all the contexts and elements are destroyed. Plugins must release any resources they have allocated, including themselves, during this call.

#### Document events

`OnDocumentOpen()` is called when a RML stream is opened, `OnDocumentLoad()` and `OnDocumentUnload()` are global callbacks called before and after the documents load and unload respectively.

#### Context events

`OnContextCreate()` and `OnContextDestroy()` are called on every registered plugin when a context is successfully created or destroyed.

#### Element events

`OnElementCreate()` and `OnElementDestroy()` are called on every registered plugin when an element is successfully created or destroyed.

### Registering a plugin

To register a plugin, call the `RegisterPlugin()` function in `{{page.lib_ns}}::Core`.

```cpp
{{page.lib_ns}}::Core::Plugin* plugin = new CustomPlugin();
{{page.lib_ns}}::Core::RegisterPlugin(plugin);
```