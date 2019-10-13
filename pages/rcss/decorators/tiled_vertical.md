---
layout: page
title: Tiled Vertical decorator
parent: rcss/decorators
grandparent: rcss
next: tiled_box
---

The `tiled-vertical`{:.prop} decorator can render three sprites or images, vertically across an element. One image is placed on the top edge, another on the bottom edge, and the last is stretched across the middle.

The decorator renders across the padded area of its element.

```css
decorator: tiled-horizontal( 
	<top-image-src> <top-image-orientation>,  
	<center-image-src> <center-image-orientation>,
	<bottom-image-src> <bottom-image-orientation>
);
```

The `<x-orientation>`{:.prop} properties can be omitted, which leaves them at their default values.


### Properties


`*x*-image-src`{:.prop}

Value: | \<string\>
Initial: | *empty*
Percentages: | N/A

This property defines either a [sprite name](../sprite_sheets.html) or a relative path to an image file.

`*x*-image-orientation`{:.prop}

Value: | none \| flip-horizontal \| flip-vertical \| rotate-180
Initial: | none
Percentages: | N/A

Flips or rotates the image.
