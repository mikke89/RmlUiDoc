---
layout: page
title: Tiled Box decorator
grandparent: rcss
parent: rcss/decorators
next: ninepatch
---

The `tiled-box`{:.prop} decorator can render nine sprites or images across an element. One image is placed at a fixed size in each of the element's corners, one image is stretched along each edge, and a final image is stretched in both directions to cover the center region of the image.

The decorator renders across the padded area of its element.

```css
decorator: tiled-horizontal( 
	<top-left-image-src> <top-left-image-orientation>,
	<top-image-src> <top-image-orientation>,
	<top-right-image-src> <top-right-image-orientation>,
	
	<left-image-src> <left-image-orientation>,
	<center-image-src> <center-image-orientation>,
	<right-image-src> <right-image-orientation>,
	
	<bottom-left-image-src> <bottom-left-image-orientation>,
	<bottom-image-src> <bottom-image-orientation>,
	<bottom-right-image-src> <bottom-right-image-orientation>
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
