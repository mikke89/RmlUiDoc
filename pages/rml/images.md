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
: The name of a sprite, or the location of an image. If the attribute matches a sprite name, it will use that sprite, otherwise it will treat the attribute as the location of an image.

`width`{:.attr} = number (CN)
: The width to force the element to, in pixels. If this is unspecified, it will default to the width of the image.

`height`{:.attr} = number (CN)
: The height to force the element to, in pixels. If this is unspecified, it will default to the height of the image.

`coords`{:.attr} = four numbers (CN)
: Coordinates within an image, specified as a space-separated list of four (unit-less) values `x y width height`. This specifies a rectangle within the image in pixel units, thereby allowing only parts of the image to be rendered. Will have no effect on sprites.
