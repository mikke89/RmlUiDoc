---
layout: page
title: Plugins
parent: cpp_manual
next: troubleshooting
---

RmlUi has a simple, straightforward system for writing plugins. Plugins receive notification when contexts, documents, elements, and data models are created and destroyed.

### Creating a plugin

All plugins derive from the `Rml::Plugin` class. The virtual functions that can be overridden are:

```cpp
// Called when RmlUi is initialised.
virtual void OnInitialise();
// Called when RmlUi shuts down.
virtual void OnShutdown();

// Called when a document load request occurs, before the document's file is opened.
virtual void OnDocumentOpen(Context* context, const Rml::String& document_path);
// Called when a document is successfully loaded, initialised, and added to its context. Called before the document's 'load' event.
virtual void OnDocumentLoad(ElementDocument* document);
// Called when a document is unloaded from its context. This is called after the document's 'unload' event.
virtual void OnDocumentUnload(ElementDocument* document);

// Called when a new context is created.
virtual void OnContextCreate(Rml::Context* context);
// Called when a context is destroyed.
virtual void OnContextDestroy(Rml::Context* context);

// Called when a new element is created.
virtual void OnElementCreate(Rml::Element* element);
// Called when an element is destroyed.
virtual void OnElementDestroy(Rml::Element* element);

// Called when a new data model is created on a context.
virtual void OnDataModelCreate(Rml::Context* context, const Rml::String& name);
// Called when a data model is about to be destroyed.
virtual void OnDataModelDestroy(Rml::Context* context, const Rml::String& name);
```

#### RmlUi engine events

The `OnInitialise()` function will be called on all registered plugins when RmlUi is successfully initialised. If RmlUi is already initialised when a plugin is registered, `OnInitialise()` will be immediately called on the plugin.

`OnShutdown()` is called on all registered plugins when RmlUi is shut down, immediately after all the contexts and elements are destroyed. Plugins must release any resources they have allocated, including themselves, during this call.

#### Document events

`OnDocumentOpen()` is called when a RML stream is opened, `OnDocumentLoad()` and `OnDocumentUnload()` are global callbacks called before and after the documents load and unload respectively.

#### Context events

`OnContextCreate()` and `OnContextDestroy()` are called on every registered plugin when a context is successfully created or destroyed.

#### Element events

`OnElementCreate()` and `OnElementDestroy()` are called on every registered plugin when an element is successfully created or destroyed.

#### Data model events

`OnDataModelCreate()` is called whenever a new [data model](../data_bindings.html) is successfully created on a context through `Context::CreateDataModel()`. Attempting to create a data model with a name that already exists does not fire the callback.

`OnDataModelDestroy()` is called when a data model is about to be destroyed, either explicitly through `Context::RemoveDataModel()`, or implicitly when the owning context is destroyed. The data model can still be resolved through `Context::GetDataModel()` during this callback, but it becomes unusable as soon as the callback returns.

### Filtering event classes

By default, a plugin receives all of the events listed above. A plugin can override `GetEventClasses()` to receive only a subset of them, by returning a combination of the `Rml::Plugin::EventClasses`{:.cls} flags:

Flag | Events
------------------------- | ------
`EVT_BASIC`{:.value}      | `OnInitialise`, `OnShutdown`, `OnContextCreate`, `OnContextDestroy`
`EVT_DOCUMENT`{:.value}   | `OnDocumentOpen`, `OnDocumentLoad`, `OnDocumentUnload`
`EVT_ELEMENT`{:.value}    | `OnElementCreate`, `OnElementDestroy`
`EVT_DATA_MODEL`{:.value} | `OnDataModelCreate`, `OnDataModelDestroy`
`EVT_ALL`{:.value}        | All of the above (the default).

For example, a plugin interested only in document events:

```cpp
int GetEventClasses() override {
	return Rml::Plugin::EVT_DOCUMENT;
}
```

### Registering a plugin

To register a plugin, call the `Rml::RegisterPlugin()` function.

```cpp
Rml::Plugin* plugin = new CustomPlugin();
Rml::RegisterPlugin(plugin);
```
