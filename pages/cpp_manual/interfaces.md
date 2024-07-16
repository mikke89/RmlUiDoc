---
layout: page
title: Custom interfaces
parent: cpp_manual
next: plugins
---

There are five interfaces that RmlUi provides to control how it interacts with your application. 

* [System interface](interfaces/system.html)
* [Render interface](interfaces/render.html)
* [File interface](interfaces/file.html)
* [Font engine interface](interfaces/font_engine.html)
* [Text input handler interface](interfaces/text_input_handler.html)

Only the render interface is required to be implemented for all applications.

The system and file interfaces will use default implementations using standard library methods unless a custom one is installed first. A default font engine will also be installed, which loads fonts and renders glyphs using the FreeType library, unless the user provides their own.

The text input handler might be supplied by a [default platform implementation from the backend](../ime.html#default-implementation) or by an empty interface.

#### Custom Interface Installation

To install a custom interface, instance your interface and install it with the appropriate `Rml::Set*Interface()` (or `Rml::SetTextInputHandler()` for the text input handler) before you initialise RmlUi.

```cpp
auto file_interface = std::make_unique<CustomFileInterface>();
Rml::SetFileInterface(file_interface.get());

/* ... */

Rml::Initalise();

/* ... */

Rml::Shutdown();

file_interface.reset();

```

***Lifetime notice:*** RmlUi takes non-owning pointers to the interfaces, thus, make sure to keep the interface alive until after the call to `Rml::Shutdown()`, and clean it up afterwards.
