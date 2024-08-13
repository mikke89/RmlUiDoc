---
layout: page
title: Getting started
parent: lua_manual
next: embedding_script
---

The Lua plugin for RmlUi can be used in an application that extends or embeds Lua. Your application will still need to initialize the RmlUi core library and provide the necessary System and Render interfaces, see the [C++ manual](../cpp_manual.html) for details on how to initialize RmlUi.

For a full list of types and methods please see the RmlUi Lua [API Reference](api_reference.html).

### Requirements

- [Lua 5.1+](https://www.lua.org/)

Tested with Lua 5.3 which is the recommended version, but we aim for compatibility with Lua version 5.1 and newer, including support for LuaJIT. There is also an unofficial Lua plugin [RmlSolLua](https://github.com/LoneBoco/RmlSolLua) based on sol3 with Lua 5.1 compatibility.

### Lua plugin integration

Perform the following steps to integrate the Lua plugin with RmlUi.

1. Install or build the Lua library, you may use the official [Lua.org](https://www.lua.org) implementation or [LuaJIT](http://luajit.org/luajit.html).
    - With the official implementation, we recommend to build the library as C++ rather than C so that the stack can be unwound properly in case of an error. When built as C, the Lua interpreter calls longjmp when an error occurs, which causes the destructors for local variables in any currently executing C++ extension functions to be skipped. Package managers typically provide Lua compiled as C only, so for this functionality you will have to build it as C++ yourself.

2. Build RmlUi with the Lua plugin enabled. See [Building with CMake](../cpp_manual/building_with_cmake.html) in the C++ manual for details.
    - Enable the option `RMLUI_LUA_BINDINGS` during the CMake configuration.
    - Set the option `RML_LUA_BINDINGS_LIBRARY` to the appropriate interpreter type: `lua_as_cxx`, `lua` \[as C], or `luajit`.
    - You may also need to guide CMake to find the Lua libraries by providing `LUA_DIR` set to the Lua directory.
    - We encourage you to also enable the samples by enabling the `RMLUI_SAMPLES` option, and try to build the `rmlui_sample_luainvaders` target to test that everything is working.

3. Link with the `rmlui_lua` library or the `RmlUi::Lua` CMake imported target, the same way you link to the core RmlUi library.

4. Within your application, setup and initialize RmlUi as you normally would, see [integrating RmlUi](../cpp_manual/integrating.html) in the C++ manual.

5. Include the Lua plugin headers in your C++ source files: `#include <RmlUi/Lua.h>`.

6. Finally, initialize the Lua library with the single call to `Rml::Lua::Initialise();`.
    - This call should happen just after the call to `Rml::Initialise();`.
    - It is also possible to provide your own lua state by calling `Rml::Lua::Initialise(lua_State* L);`.

Once you are done integrating the Lua plugin, you can start [embedding Lua scripts](embedding_script.html) inside your RML documents.
