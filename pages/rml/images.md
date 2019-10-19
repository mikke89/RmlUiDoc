---
layout: page
title: RML Images
parent: rml
next: style_sheets
---

### \<img\>

The `<img>`{:.tag} element is used to include images or [sprites](../rcss/sprite_sheets.html) in the document.

_Attributes_

`src`{:.attr} = uri (CT)
: The source location of an image.

`sprite`{:.attr} = sprite (CS)
: The name of a sprite located in a sprite sheet in the current document. If this attribute is set, the `src`{:.attr} and `rect`{:.attr} attributes will be ignored.

`width`{:.attr} = number (CN)
: The width to force the element to, in pixels. If this is unspecified, it will default to the width of the sprite, rectangle, or image in that order.

`height`{:.attr} = number (CN)
: The height to force the element to, in pixels. If this is unspecified, it will default to the height of the sprite, rectangle, or image in that order.

`rect`{:.attr} = four numbers (CN)
: Crops the image to a sub-rectangle within the image file. Specified as a space-separated list of four (unit-less) values `x y width height`, where pixel units are implied. Will have no effect on sprites.
