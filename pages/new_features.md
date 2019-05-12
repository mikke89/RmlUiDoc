---
layout: page
title: New Features and Changes
---

### New Features

A quick glance at some of the features added in {{page.lib_name}} since libRocket.

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

 * The slider on the `input.range` element can be dragged from anywhere in the element.
 


#### Breaking Changes

 * `{{page.lib_ns}}::Core::SystemInterface::GetElapsedTime()` now returns `double` instead of `float`.
```cpp
virtual double GetElapsedTime();
```
 * The `font-size` property no longer accepts a unit-less \<number\>, instead add the `px` unit for equivalent behavior. The new behavior is consistent with CSS.
 * The old functionality for setting and drawing mouse cursors has been replaced by a new function call to the [system interface](cpp_manual/interfaces.html#the-system-interface), thereby allowing the user to set the system cursor.
