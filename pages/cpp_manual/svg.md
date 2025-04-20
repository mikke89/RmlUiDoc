---
layout: page
title: SVG plugin
parent: cpp_manual
---

RmlUi comes integrated with the SVG plugin for rendering SVG vector images. The plugin uses the [LunaSVG](https://github.com/sammycage/lunasvg) library to render the SVG document.

When RmlUi is built with the SVG plugin, the `<svg>`{:.tag} element is available as a normal RML tag.


### \<svg\>

The `<svg>`{:.tag} element is used to include SVG vector images in the document.

_Attributes_

`src`{:.attr} = uri (CT)
: The source location of the SVG image.

`width`{:.attr} = number (CN)
: The width to force the element to, in pixels.

`height`{:.attr} = number (CN)
: The height to force the element to, in pixels.


![SVG sample](../../assets/gallery/svg_plugin.png)


### Building with the SVG plugin

The SVG plugin is integrated and built with the Core RmlUi library once it is enabled. Then, the plugin is automatically loaded during the call to `Rml::Initialise()`.

#### Building LunaSVG

First, we demonstrate how to download and build the required [LunaSVG](https://github.com/sammycage/lunasvg) dependency. If you're using vcpkg, you can install the library with `vcpkg install lunasvg`, and then go directly to the [configuring RmlUi](#configuring-rmlui) step below. Otherwise, you can build it manually as shown in the following.

Open up a terminal and navigate to `RmlUi/Dependencies`{:.path}. Then execute the following commands.

```cmd
git clone --recurse-submodules --branch v3.2.1 https://github.com/sammycage/lunasvg
cd lunasvg
cmake -B build -S . -DBUILD_SHARED_LIBS=OFF -DLUNASVG_BUILD_EXAMPLES=OFF
cmake --build build --target lunasvg --config Debug
cmake --build build --target lunasvg --config Release
```

You may need to adjust the CMake arguments to your generator and environment. The plugin is tested at the given version of LunaSVG, but other versions may work.

#### Configuring RmlUi

Next, during [CMake configuration](building_with_cmake.html) of RmlUi, set the option `RMLUI_SVG_PLUGIN=ON`. This will ensure that the SVG plugin is integrated and built together with the RmlUi core library. For example, in the `RmlUi`{:.path} directory execute the following:

```cmd
cmake -B Build -S . --preset samples -DBUILD_SHARED_LIBS=OFF -DRMLUI_SVG_PLUGIN=ON
```

If you built LunaSVG using the above procedure, you may need to additionally add `-Dlunasvg_ROOT="Dependencies/lunasvg/build"` to the CMake configure command. In some cases, you may need to provide the path to the PlutoVG dependency of LunaSVG as well, e.g.: `-Dplutovg_ROOT="Dependencies/lunasvg/build/plutovg"`.

Once it has been successfully configured, you can now try out the sample for the plugin. Build and run the included `rmlui_sample_svg` target the same way you would with any other sample.

### Including the SVG plugin

To include the SVG plugin in your own project, make sure you build RmlUi with the CMake option `RMLUI_SVG_PLUGIN` enabled as described above, and [integrate RmlUi into your project](integrating.html) as normal. In addition, you will need to link with the `lunasvg` library. For CMake projects, RmlUi should automatically declare the dependency to LunaSVG and link to it. Make sure that LunaSVG can be found by CMake, for example by setting the `lunasvg_ROOT` variable to its build folder.

The plugin is then automatically loaded during the call to `Rml::Initialise()`. If everything has worked out properly, the log will output a short message about the SVG plugin being initialised. The `<svg>`{:.tag} element should then be available for displaying vector images.
