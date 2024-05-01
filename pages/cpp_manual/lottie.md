---
layout: page
title: Lottie plugin
parent: cpp_manual
next: svg
---

Lottie is a popular format for rendering vector-based animations.

RmlUi comes integrated with the Lottie plugin for drawing Lottie animations. The plugin uses the [rlottie](https://github.com/Samsung/rlottie) library to render the animations.

When RmlUi is built with the Lottie plugin, the `<lottie>`{:.tag} element is available as a normal RML tag.


### \<lottie\>

The `<lottie>`{:.tag} element is used to include animations in the document.

_Attributes_

`src`{:.attr} = uri (CT)
: The source location of the JSON-file describing the Lottie animation.

![Lottie sample](../../assets/gallery/lottie.gif)


### Building with the Lottie plugin

The Lottie plugin is integrated and built with the Core RmlUi library once it is enabled. Then, the plugin is automatically loaded during the call to `Rml::Initialise()`.

First, we demonstrate how to download and build the required [rlottie](https://github.com/Samsung/rlottie) dependency. Open up a terminal and navigate to `RmlUi/Dependecies`{:.path}. Then execute the following commands.

```cmd
git clone --branch v0.2 https://github.com/Samsung/rlottie.git
cd rlottie
mkdir build
cd build
cmake -DBUILD_SHARED_LIBS=OFF ..
cmake --build . --target rlottie --config Debug
cmake --build . --target rlottie --config Release
```

You may need to adjust the CMake arguments to your generator and environment.

Then, during [CMake configuration](building_with_cmake.html) of RmlUi, set the option `RMLUI_LOTTIE_PLUGIN=ON`. This will ensure that the Lottie plugin is integrated and built together with the RmlUi core library. For example, in the `RmlUi/Build`{:.path} directory execute the following:

```cmd
cmake -B Build -S . -DBUILD_SHARED_LIBS=OFF -DRMLUI_SAMPLES=ON -DRMLUI_LOTTIE_PLUGIN=ON ..
```

This should automatically locate the `rlottie` library. You can now build and run the `rmlui_sample_lottie` target the same way you would with any other sample to try out the plugin.


### Including the Lottie plugin

To include the Lottie plugin in your own project, make sure you build RmlUi with the CMake option `RMLUI_LOTTIE_PLUGIN` enabled as described above, and [integrate RmlUi into your project](integrating.html) as normal. In addition, you will need to link with the `rlottie` library. For CMake projects, RmlUi should automatically declare the dependency to rlottie and link to it. Make sure that rlottie can be found by CMake, for example by setting the `rlottie_ROOT` variable to its build folder.

The plugin is then automatically loaded during the call to `Rml::Initialise()`. If everything has worked out properly, the log will output a short message about the Lottie plugin being initialised. The `<lottie>`{:.tag} element should then be available for displaying animations.
