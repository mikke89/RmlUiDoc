---
layout: page
title: Integrating RmlUi into your application
parent: cpp_manual
next: packages
---

This guide will help you get started when you are ready to integrate RmlUi into your own application.

If you haven't already done so, take a look at the sample applications in `/Samples/`{:.path}. There you can find a whole heap of useful examples of how to use and abuse {{page.lib_name}}. Also in there you can find the shell library we used to develop all the samples (in `/Samples/shell/`{:.path}), which can be great if you want to write a quick and dirty application of your own.

### Setting up the build environment

{{page.lib_name}} is developed following the C++14 standard and can be used on the following platforms:

* Windows 32/64bit, compiling with Microsoft Visual Studio 2015+.
* MacOS 32/64bit, compiling with GCC 5+.
* Linux, compiling with GCC 5+. 

#### Visual Studio

* Add the include path (`/Include/`{:.path} under the {{page.lib_name}} directory) to your include paths, found under `Project -> Properties -> C/C++ -> General -> Additional Include Directories`.
* Add `#include <{{page.lib_dir}}/Core.h>` in a source or header file.
* Add the {{page.lib_name}} library path (`Debug/`{:.path} and `Release/`{:.path} under the `RmlUi/Build/`{:.path} directory as appropriate) to your library paths.
* Link with `RmlCore.lib`{:.path}.
* If you have RmlUi built as a shared/dynamic library, copy the appropriate DLLs, ie. `Debug/RmlCore.dll`{:.path} for debug builds, `Release/RmlCore.dll`{:.path} for release builds from the `/Build/`{:.path} folder into the directory your executable will run from. 

#### MacOS and Linux

* Add the {{page.lib_name}} include path (`/Include/`{:.path} under the {{page.lib_name}} directory) and library path (`/lib/`{:.path}) to the paths in your build system.
* `#include <{{page.lib_dir}}/Core.h>` in your project.
* Link with RmlCore.
* Either copy the {{page.lib_name}} libraries into your application's working directory, or set a `LD_LIBRARY_PATH` (`DYLD_LIBRARY_PATH` for MacOS) environment variable. 

### Initialising {{page.lib_name}}

Before you can initialise {{page.lib_name}}, you'll need to set the [interfaces](interfaces.html) that the library uses to interact with your application. There are two compulsory interfaces, the system interface and the render interface.

#### The system interface

The system interface is defined in `<{{page.lib_dir}}/Core/SystemInterface.h>`{:.incl}. In order to create a valid system interface, you'll need to create a class that inherits from `{{page.lib_ns}}::Core::SystemInterface` and provides the function:

```cpp
virtual double GetElapsedTime();
```

The function should return the time (in seconds) since the start of the application. Install your system interface by calling `{{page.lib_ns}}::Core::SetSystemInterface()` with a pointer to the interface. Note that you must keep the system interface alive until after the call to `{{page.lib_ns}}::Core::Shutdown()` and destroy it afterwards. {{page.lib_name}} won't release your interfaces.

For more uses of the system interface, see the [documentation](interfaces.html#the-system-interface).

#### The render interface

The render interface is defined in `<{{page.lib_dir}}/Core/RenderInterface.h>`{:.incl}. It provides a way for {{page.lib_name}} to send its geometry into your application's rendering pipeline. If you want to get {{page.lib_name}} up and running as quickly as possible in your own application, you can copy the render interface defined in the sample shell if your application is using OpenGL (you can find this at `/Samples/shell/include/ShellRenderInterface.h`{:.path} and `/Samples/shell/src/ShellRenderInterface.cpp`{:.path}).

Once you have a render interface for your application, install it into {{page.lib_name}} by calling `{{page.lib_ns}}::Core::SetRenderInterface()`.

If you'd like to take an in-depth look at setting up your own render interface, please see the [documentation](interfaces.html#the-render-interface).

#### Initialising the library

Call the global function `{{page.lib_ns}}::Core::Initialise()` once you have installed the system and render interfaces and {{page.lib_name}} will start up.


### Creating a context

All elements within {{page.lib_name}} are part of a context. You must have at least one context in order to load, manipulate and render and interface elements. To create a context, use the `{{page.lib_ns}}::Core::CreateContext()` function, passing in the name of the new context and its initial dimensions like so:

```cpp
{{page.lib_ns}}::Core::Context* context = {{page.lib_ns}}::Core::CreateContext("default", {{page.lib_ns}}::Core::Vector2i(myScreenWidth, myScreenHeight));
```

You can release the context when you're done with it by calling `{{page.lib_ns}}::Core::RemoveContext(context->GetName())`.  All contexts will automatically be destroyed on shutdown.

#### Updating and rendering

Your application will need to update and render each context it maintains, as appropriate. Call the `Context::Update()` function on each context as often as necessary to update the context (usually after the frame's input has been injected), and `Context::Render()` at the appropriate place in your application's render loop.

### Loading fonts

RmlUi does not come integrated with any fonts (with the exception of the debugger plugin), they must be provided by the user. Font faces can be loaded through the `Rml::Core::LoadFontFace()` function.

```cpp
bool success = Rml::Core::LoadFontFace("assets/my_font_face.ttf");
```

### Loading a document

Once you have a valid context, you can load a document into the context with the `LoadDocument()` function. `LoadDocument()` takes a single parameter, a string with the document's file name. If the load is successful you'll get a pointer to a `{{page.lib_ns}}::Core::ElementDocument` back; call `Show()` on the document to make it visible.

```cpp
{{page.lib_ns}}::Core::ElementDocument* document = context->LoadDocument("../../assets/demo.rml");
if (document)
	document->Show();
```

Unload the document by calling `UnloadDocument()` on its parent context.

```cpp
document->GetContext()->UnloadDocument(document);
```

### Injecting input

Once you've got a document loading and rendering, the next step is to get your input into {{page.lib_name}}. The context object has a range of functions for sending mouse, keyboard and text input into the system:

```cpp
// Sends a key down event into this context.
void ProcessKeyDown({{page.lib_ns}}::Core::Input::KeyIdentifier key_identifier, int key_modifier_state);
// Sends a key up event into this context.
void ProcessKeyUp({{page.lib_ns}}::Core::Input::KeyIdentifier key_identifier, int key_modifier_state);

// Sends a single unicode character (code point) as text input into this context.
void ProcessTextInput({{page.lib_ns}}::Core::Character character);
// Sends a string of UTF-8 text input into this context.
void ProcessTextInput(const {{page.lib_ns}}::Core::String& string);

// Sends a mouse movement event into this context.
void ProcessMouseMove(int x, int y, int key_modifier_state);
// Sends a mouse-button down event into this context.
void ProcessMouseButtonDown(int button_index, int key_modifier_state);
// Sends a mouse-button up event into this context.
void ProcessMouseButtonUp(int button_index, int key_modifier_state);
// Sends a mouse-wheel movement event into this context.
void ProcessMouseWheel(int wheel_delta, int key_modifier_state);
```

Call the appropriate input functions to inject all relevant user input into your {{page.lib_name}} context each frame, before you call `Update()`. Note that {{page.lib_name}} does not translate key presses into text; this is up to the application. For more information, see the chapter on user input.

### Where next?

Now that you've had a (very!) brief introduction to {{page.lib_name}}, it is recommended you read the [packages guide](packages.html) and the [core overview](core_overview.html) to get an understanding of the composition of {{page.lib_name}}. From there, either work your way through the documentation, or dive on into the code and consult it as necessary. 
