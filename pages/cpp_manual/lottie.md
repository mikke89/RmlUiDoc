---
layout: page
title: Lottie plugin
parent: cpp_manual
---

Lottie is a popular format for rendering vector-based animations.

There is a plugin in RmlUi for serving such animations, located in the `lottie` sample. This plugin requires the [rlottie](https://github.com/Samsung/rlottie) library to render the animation.

Once the `lottie` plugin is initialized, the `<lottie>`{:.tag} element is available as a normal RML tag.


### \<lottie\>

The `<lottie>`{:.tag} element is used to include animations in the document.

_Attributes_

`src`{:.attr} = uri (CT)
: The source location of the JSON-file describing the Lottie animation.

![Lottie sample](../../assets/gallery/lottie.gif)

### Building the Lottie sample

First, we demonstrate how to download and build the [rlottie](https://github.com/Samsung/rlottie) dependency. Once this dependency is available, the RmlUi can be built with the Lottie plugin integrated.

Open up a terminal and navigate to `RmlUi/Dependecies`{:.path}. Then execute the following commands.

```cmd
git clone --branch v0.2 https://github.com/Samsung/rlottie.git
cd rlottie
mkdir build
cd build
cmake -DBUILD_SHARED_LIBS=OFF ..
cmake --build . --target rlottie --config Debug
cmake --build . --target rlottie --config Release
```

You may want to adjust the CMake arguments to your preferences.

Then, during [CMake configuration](building_with_cmake.html) of RmlUi, enable the option `ENABLE_LOTTIE_PLUGIN`. This will ensure that the Lottie plugin is integrated and built together with `RmlCore`.

To build RmlUi with the `lottie` sample, [use CMake to generate](building_with_cmake.html) the RmlUi configuration with the option `ENABLE_LOTTIE_PLUGIN` enabled. Also make sure to set the option `BUILD_SAMPLES=ON`. For example, in the `RmlUi/Build`{:.path} directory execute the following:

```cmd
cmake -DBUILD_SHARED_LIBS=OFF -DENABLE_LOTTIE_PLUGIN=ON -DBUILD_SAMPLES=ON ..
```

This should automatically locate the `rlottie` library, and you can now build and run the included `lottie` sample as you would any other sample.


### Including the Lottie plugin

To include the Lottie plugin in your own project, make sure you build RmlUi with the CMake option `ENABLE_LOTTIE_PLUGIN` enabled, and [integrate RmlUi into your project](integrating.html) as normal. In addition, you will need to link with the `rlottie` library.

The plugin is then automatically loaded during the call to `Rml::Initialise()`. If everything has worked out properly, the log will output a short message about the Lottie plugin being initialised. The `<lottie>`{:.tag} element should then be available for displaying animations.
