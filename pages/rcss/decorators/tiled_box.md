---
layout: page
title: Tiled Box decorator
grandparent: rcss
parent: rcss/decorators
---

The _tiled-box_ decorator can render nine images, or subsections of images, across an element. One image is placed in each of the element's corners, one each stretched or tiled along the edges, and another stretched across the middle.

The decorator renders across the padded area of its element.

### Properties

#### Top-left corner

These properties specify the top-left corner image. They behave similarly to the properties in the [image decorator](image.html).

`<name>-top-left-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-top-left-image-s-begin`{:.prop}, `<name>-top-left-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-top-left-image-s-end`{:.prop}, `<name>-top-left-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Top-right corner

These properties specify the top-right corner image. They behave similarly to the properties in the [image decorator](image.html).

`<name>-top-right-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-top-right-image-s-begin`{:.prop}, `<name>-top-right-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-top-right-image-s-end`{:.prop}, `<name>-top-right-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Bottom-left corner

These properties specify the bottom-left corner image. They behave similarly to the properties in the [image decorator](image.html).

`<name>-bottom-left-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-bottom-left-image-s-begin`{:.prop}, `<name>-bottom-left-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-bottom-left-image-s-end`{:.prop}, `<name>-bottom-left-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Bottom-right corner

These properties specify the bottom-right corner image. They and behave similarly to the properties in the [image decorator](image.html).

`<name>-bottom-right-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-bottom-right-image-s-begin`{:.prop}, `<name>-bottom-right-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-bottom-right-image-s-end`{:.prop}, `<name>-bottom-right-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Top edge

These properties specify the top edge image. They behave similarly to the centre properties in the [tiled-horizontal decorator](tiled_horizontal.html).

`<name>-top-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-top-image-repeat`{:.prop}

Value: |  stretch \| clamp-stretch \| clamp-truncate \| repeat-stretch \| repeat-truncate
Initial: |  stretch
Percentages: |  N/A

`<name>-top-image-s-begin`{:.prop}, `<name>-top-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-top-image-s-end`{:.prop}, `<name>-top-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Right edge

These properties specify the right edge image. They behave similarly to the centre properties in the [tiled-vertical decorator](tiled_vertical.html).

`<name>-right-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-right-image-repeat`{:.prop}

Value: |  stretch \| clamp-stretch \| clamp-truncate \| repeat-stretch \| repeat-truncate
Initial: |  stretch
Percentages: |  N/A

`<name>-right-image-s-begin`{:.prop}, `<name>-right-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-right-image-s-end`{:.prop}, `<name>-right-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Bottom edge

These properties specify the bottom edge image. They behave similarly to the centre properties in the [tiled-horizontal decorator](tiled_horizontal.html).

`<name>-bottom-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-bottom-image-repeat`{:.prop}

Value: |  stretch \| clamp-stretch \| clamp-truncate \| repeat-stretch \| repeat-truncate
Initial: |  stretch
Percentages: |  N/A

`<name>-bottom-image-s-begin`{:.prop}, `<name>-bottom-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-bottom-image-s-end`{:.prop}, `<name>-bottom-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Left edge

These properties specify the left edge image. They behave similarly to the centre properties in the [tiled-vertical decorator](tiled_vertical.html).

`<name>-left-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-left-image-repeat`{:.prop}

Value: |  stretch \| clamp-stretch \| clamp-truncate \| repeat-stretch \| repeat-truncate
Initial: |  stretch
Percentages: |  N/A

`<name>-left-image-s-begin`{:.prop}, `<name>-left-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-left-image-s-end`{:.prop}, `<name>-left-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

#### Center

These properties specify the center image. They behave similarly to the centre properties in the [tiled-horizontal decorator](tiled_horizontal.html).

`<name>-center-image-src`{:.prop}

Value: |  \<string\>
Initial: |  not defined
Percentages: |  N/A

`<name>-center-image-repeat`{:.prop}

Value: |  stretch \| clamp-stretch \| clamp-truncate \| repeat-stretch \| repeat-truncate
Initial: |  stretch
Percentages: |  N/A

`<name>-center-image-s-begin`{:.prop}, `<name>-center-image-t-begin`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  0
Percentages: |  N/A

`<name>-center-image-s-end`{:.prop}, `<name>-center-image-t-end`{:.prop}

Value: |  \<number\> \| \<length\> \| \<percentage\>
Initial: |  1
Percentages: |  N/A

### Shorthands

`<name>-top-left-image-s`{:.prop}
: Shorthand for setting `<name>-top-left-image-s-begin`{:.prop} and `<name>-top-left-image-s-end`{:.prop}.

`<name>-top-left-image-t`{:.prop}
: Shorthand for setting `<name>-top-left-image-t-begin`{:.prop} and `<name>-top-left-image-t-end`{:.prop}.

`<name>-top-left-image`{:.prop}
: A shorthand property for setting `<name>-top-left-image-src`{:.prop}, `<name>-top-left-image-s-begin`{:.prop}, `<name>-top-left-image-t-begin`{:.prop}, `<name>-top-left-image-s-end`{:.prop} and `<name>-top-left-image-t-end`{:.prop}.

`<name>-top-right-image-s`{:.prop}
: Shorthand for setting `<name>-top-right-image-s-begin`{:.prop} and `<name>-top-right-image-s-end`{:.prop}.

`<name>-top-right-image-t`{:.prop}
: Shorthand for setting `<name>-top-right-image-t-begin`{:.prop} and `<name>-top-right-image-t-end`{:.prop}.

`<name>-top-right-image`{:.prop}
: A shorthand property for setting `<name>-top-right-image-src`{:.prop}, `<name>-top-right-image-s-begin`{:.prop}, `<name>-top-right-image-t-begin`{:.prop}, `<name>-top-right-image-s-end`{:.prop} and `<name>-top-right-image-t-end`{:.prop}.

`<name>-bottom-left-image-s`{:.prop}
: Shorthand for setting `<name>-bottom-left-image-s-begin`{:.prop} and `<name>-bottom-left-image-s-end`{:.prop}.

`<name>-bottom-left-image-t`{:.prop}
: Shorthand for setting `<name>-bottom-left-image-t-begin`{:.prop} and `<name>-bottom-left-image-t-end`{:.prop}.

`<name>-bottom-left-image`{:.prop}
: A shorthand property for setting `<name>-bottom-left-image-src`{:.prop}, `<name>-bottom-left-image-s-begin`{:.prop}, `<name>-bottom-left-image-t-begin`{:.prop}, `<name>-bottom-left-image-s-end`{:.prop} and `<name>-bottom-left-image-t-end`{:.prop}.

`<name>-bottom-right-image-s`{:.prop}
: Shorthand for setting `<name>-bottom-right-image-s-begin`{:.prop} and `<name>-bottom-right-image-s-end`{:.prop}.

`<name>-bottom-right-image-t`{:.prop}
: Shorthand for setting `<name>-bottom-right-image-t-begin`{:.prop} and `<name>-bottom-right-image-t-end`{:.prop}.

`<name>-bottom-right-image`{:.prop}
: A shorthand property for setting `<name>-bottom-right-image-src`{:.prop}, `<name>-bottom-right-image-s-begin`{:.prop}, `<name>-bottom-right-image-t-begin`{:.prop}, `<name>-bottom-right-image-s-end`{:.prop} and `<name>-bottom-right-image-t-end`{:.prop}.

`<name>-top-image-s`{:.prop}
: Shorthand for setting `<name>-top-image-s-begin`{:.prop} and `<name>-top-image-s-end`{:.prop}.

`<name>-top-image-t`{:.prop}
: Shorthand for setting `<name>-top-image-t-begin`{:.prop} and `<name>-top-image-t-end`{:.prop}.

`<name>-top-image`{:.prop}
: A shorthand property for setting `<name>-top-image-src`{:.prop}, `<name>-top-image-repeat`{:.prop}, `<name>-top-image-s-begin`{:.prop}, `<name>-top-image-t-begin`{:.prop}, `<name>-top-image-s-end`{:.prop} and `<name>-top-image-t-end`{:.prop}.

`<name>-right-image-s`{:.prop}
: Shorthand for setting `<name>-right-image-s-begin`{:.prop} and `<name>-right-image-s-end`{:.prop}.

`<name>-right-image-t`{:.prop}
: Shorthand for setting `<name>-right-image-t-begin`{:.prop} and `<name>-right-image-t-end`{:.prop}.

`<name>-right-image`{:.prop}
: A shorthand property for setting `<name>-right-image-src`{:.prop}, `<name>-right-image-repeat`{:.prop}, `<name>-right-image-s-begin`{:.prop}, `<name>-right-image-t-begin`{:.prop}, `<name>-right-image-s-end`{:.prop} and `<name>-right-image-t-end`{:.prop}.

`<name>-bottom-image-s`{:.prop}
: Shorthand for setting `<name>-bottom-image-s-begin`{:.prop} and `<name>-bottom-image-s-end`{:.prop}.

`<name>-bottom-image-t`{:.prop}
: Shorthand for setting `<name>-bottom-image-t-begin`{:.prop} and `<name>-bottom-image-t-end`{:.prop}.

`<name>-bottom-image`{:.prop}
: A shorthand property for setting `<name>-bottom-image-src`{:.prop}, `<name>-bottom-image-repeat`{:.prop}, `<name>-bottom-image-s-begin`{:.prop}, `<name>-bottom-image-t-begin`{:.prop}, `<name>-bottom-image-s-end`{:.prop} and `<name>-bottom-image-t-end`{:.prop}.

`<name>-left-image-s`{:.prop}
: Shorthand for setting `<name>-left-image-s-begin`{:.prop} and `<name>-left-image-s-end`{:.prop}.

`<name>-left-image-t`{:.prop}
: Shorthand for setting `<name>-left-image-t-begin`{:.prop} and `<name>-left-image-t-end`{:.prop}.

`<name>-left-image`{:.prop}
: A shorthand property for setting `<name>-left-image-src`{:.prop}, `<name>-left-image-repeat`{:.prop}, `<name>-left-image-s-begin`{:.prop}, `<name>-left-image-t-begin`{:.prop}, `<name>-left-image-s-end`{:.prop} and `<name>-left-image-t-end`{:.prop}.

`<name>-center-image-s`{:.prop}
: Shorthand for setting `<name>-center-image-s-begin`{:.prop} and `<name>-center-image-s-end`{:.prop}.

`<name>-center-image-t`{:.prop}
: Shorthand for setting `<name>-center-image-t-begin`{:.prop} and `<name>-center-image-t-end`{:.prop}.

`<name>-center-image`{:.prop}
: A shorthand property for setting `<name>-center-image-src`{:.prop}, `<name>-center-image-repeat`{:.prop}, `<name>-center-image-s-begin`{:.prop}, `<name>-center-image-t-begin`{:.prop}, `<name>-center-image-s-end`{:.prop} and `<name>-center-image-t-end`{:.prop}.


