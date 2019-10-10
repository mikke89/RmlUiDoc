---
layout: page
title: RmlUi Changelog
---


## RmlUi 3.0


RmlUi 3.0 features a substantial amount of new features and bug fixes. One of the main efforts in RmlUi 3.0 has been on improving the performance of the library. Users should see a substantial performance increase when upgrading.

Changelog todo.





## RmlUi 2.0

A quick glance at some of the features and changes in {{page.lib_name}} 2.0 since libRocket.

### New Features

 * [Animations, transitions, and transforms](rcss/animations_transitions_transforms.html)
 * [Density-independent pixel (dp)](rcss/syntax.html#density-independent-pixel-dp)
 * [Image-color property](rcss/colours_backgrounds.html#image-colour-the-image-color-property)
 * [Pointer-events property](rcss/user_interface.html#pointer-events-the-pointer-events-property)
 * [Border property shorthand](rcss/box_model.html#border-shorthands)
 * [:checked pseudo class](rcss/selectors.html)

Other, smaller features include:

 * Elements with
```css
display: inline-block;
width: auto;
```
will now shrink to the width of their content, like in CSS.

 * The slider on the `input.range`{:.tag} element can be dragged from anywhere in the element.
 

### Breaking Changes

 * The namespace has changed from `Rocket` to `Rml`, include path from `<Rocket/...>` to `<RmlUi/...>`, and macro prefix from `ROCKET_` to `RMLUI_`.
 * `{{page.lib_ns}}::Core::SystemInterface::GetElapsedTime()` now returns `double` instead of `float`.
```cpp
virtual double GetElapsedTime();
```
 * The `font-size`{:.prop} property no longer accepts a unit-less `<number>`{:.value}, instead add the `px`{:.value} unit for equivalent behavior. The new behavior is consistent with CSS.
 
 * The [old functionality](https://barotto.github.io/libRocketDoc/pages/cpp_manual/contexts.html#cursors) for setting and drawing mouse cursors has been replaced by a new function call to the [system interface](cpp_manual/interfaces.html#the-system-interface), thereby allowing the user to set the system cursor.

 * Python support has been removed.