---
layout: page
title: Image decorator
parent: rcss/decorators
grandparent: rcss
next: tiled_horizontal
---

The `image`{:.prop} decorator can render a single sprite or image.

```css
decorator: image( <image-src> <image-orientation> <image-fit> <image-align-x> <image-align-y> );
```
Values must be specified in the given order, any unspecified properties will be left at their default values. See the 'demo' sample for usage examples.

The decorator renders across the padded area of its element.

### Properties

`image-src`{:.prop}

Value: | \<string\>
Initial: | *empty*
Percentages: | N/A

This property defines either a [sprite name](../sprite_sheets.html) or a relative path to an image file.

`image-orientation`{:.prop}

Value: | none \| flip-horizontal \| flip-vertical \| rotate-180
Initial: | none
Percentages: | N/A

Flips or rotates the image.

`image-fit`{:.prop}

Value: | fill \| contain \| cover \| scale-none \| scale-down
Initial: | fill
Percentages: | N/A

`fill`{:.value}
: The image is stretched to boundaries.

`contain`{:.value}
: The image is stretched to boundaries, keeping aspect ratio fixed, 'letter-boxed'.

`cover`{:.value}
: The image is stretched to cover the boundaries, keeping aspect ratio fixed.

`scale-none`{:.value}
: The image is never scaled.

`scale-down`{:.value}
: The image acts like 'scale-none' if smaller than boundaries, or like 'contain' otherwise.


`image-align-x`{:.prop}

Value: | left \| center \| right \| \<length-percentage\>
Initial: | center
Percentages: | relative to the element's padding width

Horizontally align or offset the image.

`image-align-y`{:.prop}

Value: | top \| center \| bottom \| \<length-percentage\>
Initial: | center
Percentages: | relative to the element's padding height

Vertically align or offset the image.
