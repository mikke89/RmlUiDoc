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

The easiest way to build {{page.lib_name}} is by using CMake. You'll first need to download CMake or install it via the package manager of your choice on Linux. CMake is not a build system itself: its purpose is to generates Makefiles, Xcode projects and Visual Studio projects, among other formats.

If you haven't already done so, download a copy of RmlUi. You can download and extract the library as a zip file, or use git from your terminal or command prompt:

```
git clone https://github.com/mikke89/RmlUi.git
```


### Building on Windows

This section serves as an introduction for users of Visual Studio.

In addition to CMake, you need a copy of the FreeType library, version 2.10.0 is officially supported. You can find prebuilt dynamic Windows binaries [here](https://github.com/ubawurinna/freetype-windows-binaries). Create the directory `RmlUi/Dependencies/freetype`{:.path} if it does not exist, and copy the FreeType files here.

Next, start up `cmake-gui` and browse here to your RmlUi source code. Choose to build the binaries under `RmlUi/Build`{:.path}. Click configure and select your Visual Studio version. Now there will be a few options appearing. See below for a description of some of them. If you'd like to take a look at the included samples, enable the  `BUILD_SAMPLES` option. Finally, click `Generate`. If it was successful, your Visual Studio solution file should be located at `RmlUi/Build/RmlUi.sln`{:.path}.

![cmake-gui](../../assets/images/cmake-gui.png)

If you use the dynamic binary version of FreeType, copy the `RmlUi/Dependencies/freetype/win64/freetype.dll`{:.path} file into a place where the RmlUi applications can see it, such as  `RmlUi/Build`{:.path}. By default, this will be the working directory when starting applications from Visual Studio.

Open up the generated Visual Studio solution file. Now there should be several samples available in addition to the RmlCore, RmlControls, and RmlDebugger projects. Right click on `invaders`, click `Set as StartUp Project`. Then press `F5`, it will start building and open the invaders demo when done. Enjoy!

### Building on macOS and Linux

Before generating your build files you need to configure CMake. Open a terminal window and navigate to the {{page.lib_name}} folder. Then execute the following command.

```
buildbox:Build$ ccmake .
```

NOTE: You need the . to denote the current directory is where the `CMakeLists.txt`{:.path} is located.

This will open a a text mode application that lets you choose which parts of {{page.lib_name}} you want to build and how you want to build it. Before you can alter any options you'll need to press C so that CMake can scan your system configuration. Once its complete you will see a list of options. The most interesting options are most likely

* `BUILD_LUA_BINDINGS` - Build the required bingings for Lua support. You'll need Lua installed.
* `BUILD_SAMPLES` - Should the samples be built
* `BUILD_SHARED_LIBS` - Build as .so/.dylib as apposed to a .a file 
* `CMAKE_BUILD_TYPE` - Choose the build type between: Debug, Release, RelWithDebInfo, MinSizeRel, or None (passed in CMAKE_CXX_FLAGS flags are used).

Make your selection and press C again so that CMake can recalculate build settings based on your selection. Once CMake is happy you'll be able to press G to generate the build configuration and exit.

At this point you should be back at the terminal and your Makefile will have been created. You can now build {{page.lib_name}} by executing make.

```
buildbox:Build$ make -j 8
```

NOTE: The -j parameter specifies how many jobs to execute in parallel: you should normally set this to the number of threads supported by your CPU.

Once the build is complete, check out the samples.
