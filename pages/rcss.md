---
layout: page
title: RCSS Cascading Style Sheets
short_title: RCSS
---

This document defines the *RCSS Cascading Style Sheets* language. RCSS is based on the [CSS2 specification](http://www.w3.org/TR/REC-CSS2/), with certain elements removed or altered to suit the needs of RmlUi. In some cases, elements have been taken from the [CSS3 working draft](http://www.w3.org/Style/CSS/current-work). This document provides an overview of RCSS and the differences between RCSS and CSS, and should be read in conjunction with the CSS2 specification.

RCSS interacts with RML in an identical fashion to CSS and HTML. Style properties declared in a RCSS are attached selectively to elements defined in RML to affect layout, positioning and other style attributes (such as font, color, text decoration, etc).

If you are familiar with CSS, a good place to start is the [property index](rcss/property_index.html), which outlines the properties and values supported in RCSS and the new functionality included. Next, read up on [decorators](rcss/decorators.html), the new, flexible way to skin elements.

If you are not, read through this documentation while consulting the CSS2 specification for detailed examples and technical details, or skip all this for now and play around with the samples!

### Contents

0. [Syntax and basic data types](rcss/syntax.html)
0. [Selectors](rcss/selectors.html)
0. [Assigning property values, cascading, and inheritance](rcss/cascade.html)
0. [Box model](rcss/box_model.html)
0. [Visual formatting model](rcss/visual_formatting_model.html)
0. [Visual formatting model details](rcss/visual_formatting_model_details.html)
0. [Visual effects](rcss/visual_effects.html)
0. [Colours, backgrounds, and rounded corners](rcss/colours_backgrounds.html)
0. [Fonts](rcss/fonts.html)
0. [Text](rcss/text.html)
0. [Tables](rcss/tables.html)
0. [User interface](rcss/user_interface.html)
0. [Flexboxes](rcss/flexboxes.html)
0. [Animations, transitions, and transforms](rcss/animations_transitions_transforms.html)
0. [Custom properties and variables](rcss/custom_properties.html)
0. [Media queries](rcss/media_queries.html)
0. [Sprite sheets](rcss/sprite_sheets.html)
0. [Decorators](rcss/decorators.html)
    * [Image](rcss/decorators/image.html)
    * [Tiled horizontal](rcss/decorators/tiled_horizontal.html)
    * [Tiled vertical](rcss/decorators/tiled_vertical.html)
    * [Tiled box](rcss/decorators/tiled_box.html)
    * [Ninepatch](rcss/decorators/ninepatch.html)
    * [Straight gradient](rcss/decorators/gradient.html)
    * [Linear gradient](rcss/decorators/linear_gradient.html)
    * [Radial gradient](rcss/decorators/radial_gradient.html)
    * [Conic gradient](rcss/decorators/conic_gradient.html)
    * [Shader](rcss/decorators/shader.html)
    * [Text](rcss/decorators/text.html)
0. [Masking](rcss/masking.html)
0. [Filters](rcss/filters.html)
0. [Font effects](rcss/font_effects.html)
    * [glow](rcss/font_effects/glow.html)
    * [outline](rcss/font_effects/outline.html)
    * [shadow](rcss/font_effects/shadow.html)
    * [blur](rcss/font_effects/blur.html)

### Appendix

* [Property index](rcss/property_index.html)
