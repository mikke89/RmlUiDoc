---
layout: page
title: Building RmlUi with CMake
parent: cpp_manual
next: integrating
---

The following will guide you through the process of building RmlUi. This is necessary before you can integrate it into your own application. If you are just getting started, we also encourage you to build the included samples and have a look at them.

Requirements:
- [RmlUi](https://github.com/mikke89/RmlUi)
- [CMake](http://cmake.org)
- [FreeType](https://www.freetype.org/)

The easiest way to build RmlUi is by using CMake. You'll first need to download CMake or install it via the package manager of your choice on Linux. CMake is not a build system itself: its purpose is to generates Makefiles, Xcode projects and Visual Studio projects, among other formats.

If you haven't already done so, download a copy of RmlUi. You can download and extract the library as a zip file, or use git from your terminal or command prompt:

```
git clone https://github.com/mikke89/RmlUi.git
```


### Building on Windows

This section serves as an introduction for users of Visual Studio.

In addition to CMake, you need a copy of the FreeType library, version 2.10.1 is officially supported. You can find prebuilt dynamic Windows binaries [here](https://github.com/ubawurinna/freetype-windows-binaries). Create the directory `RmlUi/Dependencies/freetype`{:.path} if it does not exist, and copy the FreeType files here.

Next, start up `cmake-gui` and browse here to your RmlUi source code. Choose to build the binaries under `RmlUi/Build`{:.path}. Click configure and select your Visual Studio version. Now there will be a few options appearing. See the CMake options in the section below for a description of some of them. If you'd like to take a look at the included samples, enable the `BUILD_SAMPLES` option. Finally, click `Generate`. If it was successful, your Visual Studio solution file should be located at `RmlUi/Build/RmlUi.sln`{:.path}.

![cmake-gui](../../assets/images/cmake-gui.png)

If you use the dynamic binary version of FreeType, copy the `RmlUi/Dependencies/freetype/win64/freetype.dll`{:.path} file into a place where the RmlUi applications can see it, such as  `RmlUi/Build`{:.path}. By default, this will be the working directory when starting applications from Visual Studio.

Open up the generated Visual Studio solution file. Now there should be several samples available in addition to the RmlCore, RmlControls, and RmlDebugger projects. If you set the CMake option to build the samples, you can now right click on `invaders`, and click `Set as StartUp Project`. Finally, press `F5` to start building and open the invaders demo when done. Enjoy!

### Building on macOS and Linux

Before generating your build files you need to configure CMake. Open a terminal window, navigate to the RmlUi folder and create a `Build` folder:

```
buildbox:RmlUi$ mkdir Build
buildbox:RmlUi$ cd Build
```

Then execute the following command:

```
buildbox:RmlUi/Build$ ccmake ..
```

_NOTE_: You need the `..` to denote the directory where the `CMakeLists.txt`{:.path} is located.

This will open a text mode application that lets you choose which parts of RmlUi you want to build and how you want to build it. Before you can alter any options you'll need to press `C` so that CMake can scan your system configuration. Once it's complete you will see a list of options. See the CMake options below for what the most relevant options do. If you'd like to take a look at the included samples, enable the `BUILD_SAMPLES` option.

Make your selection and press `C` again so that CMake can recalculate build settings based on your selection. Once CMake is happy you'll be able to press `G` to generate the build configuration and then exit.

At this point you should be back at the terminal and your `Makefile`{:.path} will have been created. You can now build RmlUi by executing make.

```
buildbox:RmlUi/Build$ make -j 8
```

_NOTE_: The -j parameter specifies how many jobs to execute in parallel: you should normally set this to the number of threads supported by your CPU.

Once the build is complete, you may want to have a look at the samples.


### CMake options


* `BUILD_SAMPLES` - Enable to build the included samples.
* `BUILD_SHARED_LIBS` - Build shared libraries (dynamic libraries, .so/.dylib/.dll) as opposed to static libraries (.a/.lib). If the library is compiled *without* this option, then users of the library must specify `#define RMLUI_STATIC_LIB` before including the library.
* `BUILD_LUA_BINDINGS` - Build the required bindings for Lua support. You'll need Lua installed.
* `CMAKE_BUILD_TYPE` - Choose the build type between: Debug, Release, RelWithDebInfo, MinSizeRel, or None (passed in CMAKE_CXX_FLAGS flags are used).
* `NO_FONT_INTERFACE_DEFAULT` removes the default font engine, thereby allowing users to completely remove the FreeType dependency. If set, a custom font engine must be created and set through `Rml::SetFontEngineInterface` before initialization. See the `bitmapfont` sample for an example implementation of a custom font engine.
* `NO_THIRDPARTY_CONTAINERS`: RmlUi now comes bundled with some third-party container libraries for improved performance. For users that would rather use the `std` counter-parts, this option is available. The option replaces the containers via a preprocessor definition. If the library is compiled with this option, then users of the library *must* specify `#define RMLUI_NO_THIRDPARTY_CONTAINERS` before including the library.
* `DISABLE_RTTI_AND_EXCEPTIONS` will try to configure the compiler to disable RTTI language support and exceptions. All internal use of RTTI (eg. dynamic_cast) will then be replaced by a custom solution. If set, users of the library must then `#define RMLUI_USE_CUSTOM_RTTI` before including the library.
* `ENABLE_PRECOMPILED_HEADERS` enables the use of precompiled headers on supported compilers for speeding up compilation times. This requires CMake version 3.16.0 or greater and is enabled by default.
* `ENABLE_TRACY_PROFILING`: RmlUi has parts of the library tagged with markers for profiling with [Tracy Profiler](https://bitbucket.org/wolfpld/tracy/src/master/). This enables a visual inspection of bottlenecks and slowdowns on individual frames. To compile the library with profiling support, add the Tracy Profiler library to `/Dependencies/tracy/`, enable this option, and compile.  Follow the Tracy Profiler instructions to build and connect the separate viewer. As users may want to only use profiling for specific compilation targets, then instead one can `#define RMLUI_ENABLE_PROFILING` for the given target.
