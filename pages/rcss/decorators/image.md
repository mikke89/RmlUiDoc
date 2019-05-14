---
layout: page
title: Image decorator
parent: rcss/decorators
---

The *image* decorator can render a single image or a rectangular subsection of a single image. 

### Properties

`<name>-image-src`{:.prop}

Value: | \<string\>
Initial: | not defined
Percentages: | N/A

This property defines the name (and, for file sources, the relative path) of the source image.

`<name>-image-s-begin`{:.prop}, `<name>-image-t-begin`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 0
Percentages: | N/A

`<name>-image-s-end`{:.prop}, `<name>-image-t-end`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1
Percentages: | N/A

These properties specify the texture coordinates to use when rendering the image.

### Values

`<number>`{:.value}
: Expected to be a floating-point number from 0 to 1, this is the raw texture coordinate.

`<length>`{:.value}
: Expected to be expressed in 'px' units and from 0 to the length of the appropriate texture axis. The texture will be rendered from (for -begin) or to (for -end) this pixel.

`<percentage>`{:.value}
: The texture will be rendered from (for -begin) ot to (for -end) this far across the appropriate texture axis. 

### Shorthands

`<name>-image-s`{:.prop}
: A shorthand property for setting `<name>-image-s-begin`{:.prop} and `<name>-image-s-end`{:.prop}.

`<name>-image-t`{:.prop}
: A shorthand property for setting `<name>-image-t-begin`{:.prop} and `<name>-image-t-end`{:.prop}.

`<name>-image`{:.prop}
: A shorthand property for setting
`<name>-image-src`{:.prop},
`<name>-image-s-begin`{:.prop},
`<name>-image-t-begin`{:.prop},
`<name>-image-s-end`{:.prop} and
`<name>-image-t-end`{:.prop}.

```css
/* Declares an image decorator. */
div#avatar
{
	avatar-decorator: image;
	avatar-image: player.png 0px 32px 32px 64px;
}
```

The image will be stretched or shrunk to render across the entire padded area of an element it is attached to.
