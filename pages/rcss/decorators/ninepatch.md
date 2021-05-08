---
layout: page
title: Ninepatch decorator
grandparent: rcss
parent: rcss/decorators
next: gradient
---


The `ninepatch`{:.prop} decorator splits a sprite into a 3x3 grid of patches by declaring another inner sprite. The corners of the ninepatch are rendered at their native size by default, while the inner patches are stretched so that the whole element is filled. In a sense, it can be considered a simplified and more performant version of the `tiled-box`{:.prop} decorator.

The decorator renders across the padded area of its element.

```css
decorator: ninepatch( <outer>, <inner>, <edge>? );
```

The `edge`{:.prop} property is optional.

### Properties


`outer`{:.prop}

Value: | \<string\>
Initial: | *empty*
Percentages: | N/A

This property defines a [sprite name](../sprite_sheets.html). The sprite declares the outer rectangle of the decorator. Image urls cannot be used in this decorator.

`inner`{:.prop}

Value: | \<string\>
Initial: | *empty*
Percentages: | N/A

This property defines a [sprite name](../sprite_sheets.html), and must be located in the same sprite sheet as `outer`{:.prop}. The inner sprite declares the inner rectangle of the decorator.

The area between the inner and outer rectangle defines the decorator's corners and edges. The corners are fixed in size, the edges only scale in one direction, while the center is stretched to cover the remaining area of the element's boundaries.

`edge`{:.prop}

Value: | \<number-length-percentage-box\>
Initial: | 0px 0px 0px 0px
Percentages: | relative to the size of the edge and current dp-ratio

The edge property is specified in the common `top-right-bottom-left`{:.value} box order. If the property is specified (not all 0px), the rendered size of each edge can be specified as a length, or number/percentage to scale it relative to the natural size of the image edge. The natural size is determined by the sprite's associated [`resolution`{:.prop} property](../sprite_sheets.html#resolution) and the current [dp-ratio](../syntax.html#dp-unit). The normal box shorthands are available, e.g., a single value will be replicated to all edges.


### Example

The decorator can be specified by two sprites, defining an outer and inner rectangle:
```css
@spritesheet my-button {
	src: button.png;
	button-outer: 247px  0px 159px 45px;
	button-inner: 259px 19px 135px  1px;
}
```
The inner rectangle defines the parts of the sprite that will be stretched when the element is resized. 

The `ninepatch`{:.prop} decorator is applied as follows:
```css
decorator: ninepatch( button-outer, button-inner );
```

Furthermore, the ninepatch decorator can have the rendered size of its edges specified manually.
```css
decorator: ninepatch( button-outer, button-inner, 19px 12px 25px 12px );
```
Percent and numbers can also be used, they will scale relative to the natural size of the given edge. Thus, setting
```css
decorator: ninepatch( button-outer, button-inner, 2.0 );
```
will double the size of all edges.
