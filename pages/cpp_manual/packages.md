---
layout: page
title: Packages
parent: cpp_manual
---

{{page.lib_name}} ships with four libraries, all with full source code.

### RocketCore

RocketCore is the main {{page.lib_name}} library. It contains all the basic types, the basic element hierarchy, the style sheet and property system, the layout engine and the RML parser. RocketCore is all you need to display content from C++.

To use RocketCore, include `<{{page.lib_dir}}/Core.h>`{:.incl} in your application and link with RocketCore or RocketCore_d.

### RocketControls

RocketControls contains custom elements for form controls (radio buttons, range sliders, etc), data tables and tabbed windows. You are free to use the plugin as-is in your application, or use the elements as a starting point for more specialised controls in your application.

This package is a great place to look at for examples of creating new elements and writing custom XML parsing.

To use RocketControls, include `<{{page.lib_dir}}/Controls.h>`{:.incl} in your application and link with RocketControls or RocketControls_d.

### RocketDebugger

RocketDebugger is a visual debugger for {{page.lib_name}} elements, inspired by similar debuggers for Firefox. We strongly recommend you use this in your application during development!

To use RocketDebugger, include `<{{page.lib_dir}}/Debugger.h>`{:.incl} in your application and link with RocketDebugger or RocketDebugger_d.
