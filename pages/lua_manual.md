---
layout: page
title: Lua Manual
---

The Lua interface to RmlUi has been designed to resemble Javascript as closely as possible. Due the nature of the language, this is more possible in Lua than C++.

The functionality of RmlUi is described fully in the [C++ Manual](cpp_manual.html); this manual defines the Lua interface to the {{page.lib_name}} objects described there. Not all aspects of RmlUi are accessible from Lua; for example, custom decorators can only be created in C++. However the vast majority is accessible, enabling you to easily and efficiently develop the functionality of your documents.

A good place to get started is the `luainvaders` sample included with the library, which demonstrates many of the functionalities of the Lua plugin.

### Integrating Lua

1. [Getting started](lua_manual/getting_started.html)
2. [Embedding script](lua_manual/embedding_script.html)
3. [Loading fonts](lua_manual/fonts.html)
4. [Attaching to Events](lua_manual/attaching_to_events.html) 

### Interfaces

1. [Elements](lua_manual/elements.html)
2. [Documents](lua_manual/documents.html)
3. [Contexts](lua_manual/contexts.html)
4. [Events](lua_manual/events.html)

### Appendix

1. [API reference](lua_manual/api_reference.html)
