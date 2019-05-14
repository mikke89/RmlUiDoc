---
layout: page
title: Tiled Horizontal decorator
parent: rcss/decorators
---

The _tiled-horizontal_ decorator can render three images, or subsections of images, horizontally across an element. One image is placed on the left edge, another on the right edge, and the last is stretched or repeated across the middle.

The decorator renders across the padded area of its element.

### Properties

#### Left image

These properties specify the left image. They behave similarly to the properties in the [image decorator](image.html).

`<name>-left-image-src`{:.prop}

Value: | \<string\>
Initial: | not defined
Percentages: | N/A

`<name>-left-image-s-begin`{:.prop}, `<name>-left-image-t-begin`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 0
Percentages: | N/A

`<name>-left-image-s-end`{:.prop}, `<name>-left-image-t-end`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1
Percentages: | N/A

#### Right image

These properties specify the right image. They behave similarly to the properties in the [image decorator](image.html). If only one side is defined, the other will be the horizontal mirror of it. At least one side must be defined.

`<name>-right-image-src`{:.prop}

Value: | \<string\>
Initial: | not defined
Percentages: | N/A

`<name>-right-image-s-begin`{:.prop}, `<name>-right-image-t-begin`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 0
Percentages: | N/A

`<name>-right-image-s-end`{:.prop}, `<name>-right-image-t-end`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1
Percentages: | N/A

#### Center image

These properties specify the centre image. They behave similarly to the properties in the [image decorator](image.html).

`<name>-center-image-src`{:.prop}

Value: | \<string\>
Initial: | not defined
Percentages: | N/A

`<name>-center-image-repeat`{:.prop}

Value: | stretch \| clamp-stretch \| clamp-truncate \| repeat-stretch \| repeat-truncate
Initial: | stretch
Percentages: | N/A

`<name>-center-image-s-begin`{:.prop}, `<name>-center-image-t-begin`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 0
Percentages: | N/A

`<name>-center-image-s-end`{:.prop}, `<name>-center-image-t-end`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1
Percentages: | N/A

##### Values

`stretch`{:.value}
: The image will be stretched to fit the centre of the decorator. 

`clamp-stretch`{:.value}
: The image will be clamped to the upper-left of the centre of the decorator. If the centre of the decorator is too small to fit the image, it will be scaled down to fit. 

`clamp-truncate`{:.value}
: The image will be clamped to the upper-left of the centre of the decorator. If the centre of the decorator is too small to fit the image, it will be truncated. 

`repeat-stretch`{:.value}
: The image will be repeated across the centre of the decorator. Any last repeat will be stretched across the remainder. 

`repeat-truncate`{:.value}
: The image will be repeated across the centre of the decorator. The last repeat will be truncated. 

### Shorthands

`<name>-left-image-s`{:.prop}
: Shorthand for setting `<name>-left-image-s-begin`{:.prop} and `<name>-left-image-s-end`{:.prop}.

`<name>-left-image-t`{:.prop}
: Shorthand for setting `<name>-left-image-t-begin`{:.prop} and `<name>-left-image-t-end`{:.prop}.

`<name>-left-image`{:.prop}
: A shorthand property for setting `<name>-left-image-src`{:.prop}, `<name>-left-image-s-begin`{:.prop}, `<name>-left-image-t-begin`{:.prop}, `<name>-left-image-s-end`{:.prop} and `<name>-left-image-t-end`{:.prop}.

`<name>-right-image-s`{:.prop}
: Shorthand for setting `<name>-right-image-s-begin`{:.prop} and `<name>-right-image-s-end`{:.prop}.

`<name>-right-image-t`{:.prop}
: Shorthand for setting `<name>-right-image-t-begin`{:.prop} and `<name>-right-image-t-end`{:.prop}.

`<name>-right-image`{:.prop}
: A shorthand property for setting `<name>-right-image-src`{:.prop}, `<name>-right-image-s-begin`{:.prop}, `<name>-right-image-t-begin`{:.prop}, `<name>-right-image-s-end`{:.prop} and `<name>-right-image-t-end`{:.prop}.

`<name>-center-image-s`{:.prop}
: Shorthand for setting `<name>-center-image-s-begin`{:.prop} and `<name>-center-image-s-end`{:.prop}.

`<name>-center-image-t`{:.prop}
: Shorthand for setting `<name>-center-image-t-begin`{:.prop} and `<name>-center-image-t-end`{:.prop}.

`<name>-center-image`{:.prop}
: A shorthand property for setting `<name>-center-image-src`{:.prop}, `<name>-center-image-repeat`{:.prop}, `<name>-center-image-s-begin`{:.prop}, `<name>-center-image-t-begin`{:.prop}, `<name>-center-image-s-end`{:.prop} and `<name>-center-image-t-end`{:.prop}.
