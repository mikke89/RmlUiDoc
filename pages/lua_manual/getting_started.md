---
layout: page
title: Getting started
parent: lua_manual
next: embedding_script
---

The Lua plugin for RmlUi can be used in an application that extends or embeds Lua. Your application will still need to initialize the RmlUi core library and provide the necessary System and Render interfaces, see the [C++ manual](../cpp_manual.html) for details on how to initialize RmlUi.

For a full list of types and methods please see the RmlUi Lua [API Reference](api_reference.html).

### Requirements

- [Lua 5.x](https://www.lua.org/)

Tested with Lua 5.3, but other versions may work.

### Lua plugin integration

Perform the following steps to integrate the Lua plugin with RmlUi.

1. Download and build the Lua 5.x library, or install it with your system package manager.

2. Build RmlUi with the Lua plugin enabled. See [Building with CMake](../cpp_manual/building_with_cmake.html) in the C++ manual for details.
    - Enable the option `BUILD_LUA_BINDINGS` during the CMake configuration.
	- You may also need to guide CMake to find the Lua libraries by providing `LUA_DIR` set to the Lua directory.
	- We encourage you to also enable the samples, `BUILD_SAMPLES` options, and try to build the `luainvaders` sample application to test that everything is working.

3. Within your application, setup and initialize RmlUi as you normally would, see [integrating RmlUi](../cpp_manual/integrating.html) in the C++ manual.

4. Link with the `RmlLua` library just as you would link to `RmlCore`.

5. Include the Lua plugin headers in your C++ source files: `#include <RmlUi/Lua.h>`.

6. Finally, initialize the Lua library with the single call to `Rml::Lua::Initialise();`.
    - This call should happen just after the call to `Rml::Initialise();`.
	- It is also possible to provide your own lua state by calling `Rml::Lua::Initialise(lua_State* L);`.

Once you are done integrating the Lua plugin, you can start embedding Lua scripts inside your RML documents.
