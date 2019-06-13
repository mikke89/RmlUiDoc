---
layout: page
title: Tiled Vertical decorator
parent: rcss/decorators
grandparent: rcss
next: tiled_box
---

The _tiled-vertical_ decorator can render three images, or subsections of images, vertically across an element. One image is placed on the top edge, another on the bottom edge, and the last is stretched or repeated across the middle.

The decorator renders across the padded area of its element.

### Properties

#### Top image

These properties specify the top image. They behave similarly to the properties in the [image decorator](image.html).

`<name>-top-image-src`{:.prop}

Value: | \<string\>
Initial: | not defined
Percentages: | N/A

`<name>-top-image-s-begin`{:.prop}, `<name>-top-image-t-begin`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 0
Percentages: | N/A

`<name>-top-image-s-end`{:.prop}, `<name>-top-image-t-end`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1
Percentages: | N/A

#### Bottom image

These properties specify the bottom image. They behave similarly to the properties in the [image decorator](image.html). If only one side is defined, the other will be the vertical mirror of it. At least one side must be defined.

`<name>-bottom-image-src`{:.prop}

Value: | \<string\>
Initial: | not defined
Percentages: | N/A

`<name>-bottom-image-s-begin`{:.prop}, `<name>-bottom-image-t-begin`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 0
Percentages: | N/A

`<name>-bottom-image-s-end`{:.prop}, `<name>-bottom-image-t-end`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1
Percentages: | N/A

#### Center image

These properties specify the centre image. They behave similarly to the centre properties in the [tiled-horizontal decorator](tiled_horizontal.html).

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


### Shorthands

`<name>-top-image-s`{:.prop}
: Shorthand for setting `<name>-top-image-s-begin`{:.prop} and `<name>-top-image-s-end`{:.prop}.

`<name>-top-image-t`{:.prop}
: Shorthand for setting `<name>-top-image-t-begin`{:.prop} and `<name>-top-image-t-end`{:.prop}.

`<name>-top-image`{:.prop}
: A shorthand property for setting `<name>-top-image-src`{:.prop}, `<name>-top-image-s-begin`{:.prop}, `<name>-top-image-t-begin`{:.prop}, `<name>-top-image-s-end`{:.prop} and `<name>-top-image-t-end`{:.prop}.

`<name>-bottom-image-s`{:.prop}
: Shorthand for setting `<name>-bottom-image-s-begin`{:.prop} and `<name>-bottom-image-s-end`{:.prop}.

`<name>-bottom-image-t`{:.prop}
: Shorthand for setting `<name>-bottom-image-t-begin`{:.prop} and `<name>-bottom-image-t-end`{:.prop}.

`<name>-bottom-image`{:.prop}
: A shorthand property for setting `<name>-bottom-image-src`{:.prop}, `<name>-bottom-image-s-begin`{:.prop}, `<name>-bottom-image-t-begin`{:.prop}, `<name>-bottom-image-s-end`{:.prop} and `<name>-bottom-image-t-end`{:.prop}.

`<name>-center-image-s`{:.prop}
: Shorthand for setting `<name>-center-image-s-begin`{:.prop} and `<name>-center-image-s-end`{:.prop}.

`<name>-center-image-t`{:.prop}
: Shorthand for setting `<name>-center-image-t-begin`{:.prop} and `<name>-center-image-t-end`{:.prop}.

`<name>-center-image`{:.prop}
: A shorthand property for setting `<name>-center-image-src`{:.prop}, `<name>-center-image-repeat`{:.prop}, `<name>-center-image-s-begin`{:.prop}, `<name>-center-image-t-begin`{:.prop}, `<name>-center-image-s-end`{:.prop} and `<name>-center-image-t-end`{:.prop}.


