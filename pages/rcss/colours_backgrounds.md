---
layout: page
title: Colours and backgrounds
parent: rcss
next: fonts
---

### Foreground colour: the 'color' property

`color`{:.prop}

Value: | \<colour\>
Initial: | black
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property sets the colour of rendered text and text decorations.

### Background colour

In RCSS, an element's background can be set as a flat colour but not an image. This functionality (and much more!) instead lies with [decorators](decorators.html).

`background-color`{:.prop}

Value: | \<colour\>
Initial: | transparent
Applies to: | all elements
Inherited: | no
Percentages: | N/A

This property sets the color of the element's generated boxes. The background colour is rendered under a box's padded area.

`background`{:.prop}

An alias for `background-color`{:.prop}.

### Image colour: the 'image-color' property

`image-color`{:.prop}

Value: | \<colour\>
Initial: | transparent
Applies to: | \<img\> elements and [decorators](decorators.html)
Inherited: | no
Percentages: | N/A

An extension to CSS for RCSS which multiplies a colour with images in `<img>`{:.tag} tags and image decorators. Useful for `:hover`{:.cls} pseudo-class and for applying transparency.

Example:
```css
image-color: rgba(255, 160, 160, 200);
icon-decorator: image;
icon-image: background.png 34px 0px 66px 28px;
``` 