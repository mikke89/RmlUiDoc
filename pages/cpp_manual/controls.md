---
layout: page
title: Controls plugin
parent: cpp_manual
next: debugger
---

### Initialisation

To use the Controls plugin, include the main header `<{{page.lib_dir}}/Controls.h>`{:.incl} and call the `{{page.lib_ns}}::Controls::Initialise()` function after {{page.lib_name}} itself has been initialised. This will set up the instancers for the custom elements in the Controls package.

### Element packages

The Controls plugin includes the following element packages:

* [Form controls](controls/form.html): a comprehensive set of form controls.
* [Data grids](controls/data_grid.html): elements for positioning and rendering dynamic, tabulated data.
* [Tab sets](controls/tab_set.html): elements for partitioning content into panels.
* [Progress bar](controls/progress_bar.html): element for displaying progress.
