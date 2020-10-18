---
layout: page
title: Lottie plugin
parent: cpp_manual
---

Lottie is a popular format for rendering vector-based animations.

There is a plugin in RmlUi for serving such animations, located in the `lottie` sample. This plugin uses the [rlottie](https://github.com/Samsung/rlottie) library to render the animation.

Once the `lottie` plugin is initialized, the `<lottie>`{:.tag} element is available as a normal RML tag.


### \<lottie\>

The `<lottie>`{:.tag} element is used to include animations in the document.

_Attributes_

`src`{:.attr} = uri (CT)
: The source location of the JSON-file describing the Lottie animation.

![Lottie sample](../../assets/gallery/lottie.gif)

### Building the Lottie sample

First, we demonstrate how to download and build the [rlottie](https://github.com/Samsung/rlottie) dependency. Once this dependency is available, the RmlUi CMake configuration will automatically add the `lottie` sample to its project, when configured to build the included samples.

Open up a terminal and navigate to `RmlUi/Dependecies`{:.path}. Then execute the following commands.

```cmd
git clone --branch v0.2 https://github.com/Samsung/rlottie.git
cd rlottie
mkdir build
cd build
cmake -G -DBUILD_SHARED_LIBS=OFF ..
cmake --build . --target rlottie --config Debug
cmake --build . --target rlottie --config Release
```

You may want to adjust the CMake arguments to your preferences.

To build RmlUi with the `lottie` sample, [use CMake to generate](building_with_cmake.html) the RmlUi configuration as normal. Make sure to set the option `BUILD_SAMPLES=ON`. For example, in the `RmlUi/Build`{:.path} directory execute the following:

```cmd
cmake -G -DBUILD_SHARED_LIBS=OFF -DBUILD_SAMPLES=ON ..
```

This should automatically locate the `rlottie` library, and you can now build and run the included `lottie` sample as you would any other sample.


### Including the Lottie plugin

To include the Lottie plugin in your own project, simply copy the following files into your project.

```
RmlUi/Samples/basic/lottie/src/ElementLottie.h
RmlUi/Samples/basic/lottie/src/ElementLottie.cpp
RmlUi/Samples/basic/lottie/src/LottiePlugin.h
RmlUi/Samples/basic/lottie/src/LottiePlugin.cpp
```

Then link with the `rlottie` library, and add its header files to your include path.

To initialize the plugin, first add `#include "LottiePlugin.h"` to your cpp-file, then call `Rml::Lottie::Initialise()` just after the call to `Rml::Initialise()`.
