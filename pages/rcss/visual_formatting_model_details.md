---
layout: page
title: Visual formatting model details
parent: rcss
next: visual_effects
---

### Definition of 'containing block'

During layout, the containing block of an element is fixed when the element is encountered in the document tree. It is sized as follows:

1. For the root element of the document (the `body`{:.tag} element), the containing block is the size of the document's context.
2. For other elements (other than absolutely positioned elements), the containing block is the size of the nearest block ancestor's content area. If the block ancestor does not have a fixed height (ie, its `height`{:.prop} property is set to `auto`{:.value}), the height of the containing block is given by the height of the nearest block ancestor's fixed content area. This may end up as the height of the context.
3. If the element is positioned `fixed`{:.value} or `absolute`{:.value}, its containing block is given by the padded size of the nearest block element with a `position`{:.prop} other than `static`{:.value}, or the root if no such element exists. Like other elements, they will look further back in order to get a fixed height. 

### Content width: the 'width' property
{:#width}

`width`{:.prop}

Value: | \<length\> \| \<percentage\> \| auto
Initial: | auto
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | relative to the width of the containing block

This property only applies to block boxes and inline boxes with an intrinsic width. Other inline boxes are sized by their content.

Values have the following meaning:

`<length>`{:.value}
: Specifies a fixed width. 

`<percentage>`{:.value}
: Specifies a width relative to the width of the box's containing block. 

`auto`{:.value}
: The width depends on the values of other properties. See below. 

```css
/* Fixes the width of input elements of class 'text' to 12 times their line height. */
input.text
{
	width: 12em;
}
```

### Computing widths and margins

If any of a box's `width`{:.prop}, `margin-left`{:.prop} or `margin-right`{:.prop} are set to `auto`{:.value}, then they are evaluated when the box is sized. Depending on the box type, they are set as follows:

* For an inline non-replaced box, any `auto`{:.value} margins are set to '0'. `width`{:.prop} is ignored.
* For an inline replaced box, `auto`{:.value} margins are set to '0'. A `width`{:.prop} of `auto`{:.value} is set to the element's intrinsic width.
* For a block box, the formula `margin-left + border-left-width + padding-left + 'content width' + padding-right + border-right-width + margin-right = containing block width` must hold true. If `width`{:.prop} is `auto`{:.value}, then any `auto`{:.value} margins are set to '0' and the box width is set to the appropriate value. Otherwise, the inequality in the equation is split evenly between the auto-margins. 

This is different from the CSS equation in the following ways:

* The `left`{:.prop} and `right`{:.prop} properties cannot be set to `auto`{:.value}.
* Floating and positioned boxes are evaluated like normal boxes. 

### Minimum and maximum widths: 'min-width' and 'max-width'
{:#min-width}

`min-width`{:.prop}

Value: | \<length\> \| \<percentage\>
Initial: | 0px
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | relative to the width of the containing block

`max-width`{:.prop}
{:#max-width}

Value: | \<length\> \| \<percentage\>
Initial: | -1px
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | relative to the width of the containing block

Values have the following meaning:

`<length>`{:.value}
: Specifies a fixed minimum or maximum width. 

`<percentage>`{:.value}
: Specifies a minimum or maximum width relative to the width of the containing block. 

Note that there is no `auto`{:.value} value for `max-width`{:.prop}; instead, if it is a negative number there is no maximum width.

When evaluating `width`{:.prop}, if the computed width is greater than `max-width`{:.prop}, then the width is computed again, this time substituting `max-width`{:.prop} for `width`{:.prop}. If the computed value is less than `min-width`{:.prop}, the the width is computed again, this time substituting `min-width`{:.prop} for `width`{:.prop}.

### Content height: the 'height' property
{:#height}

`height`{:.prop}

Value: | \<length\> \| \<percentage\> \| auto
Initial: | auto
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | relative to the height of the containing block

This property only applies to block boxes and inline boxes with an intrinsic height. Other inline boxes are sized by their content.

Values have the following meaning:

`<length>`{:.value}
: Specifies a fixed height. 

`<percentage>`{:.value}
: Specifies a height relative to the height of the box's containing block. 

`auto`{:.value}
: The width depends on the values of other properties. See below. 

```css
/* Fixes the height of the background div to 100% of its containing block. */
div#background
{
	height : 100%;
}
```

### Computing heights and margins

If any of a box's `height`{:.prop}, `margin-top`{:.prop} or `margin-bottom`{:.prop} are set to `auto`{:.value}, then they are evaluated when the box is sized. Depending on the box type, they are set as follows:

* For an inline non-replaced box, any `auto`{:.value} margins are set to '0'. `height`{:.prop} is ignored.
* For an inline replaced box, `auto`{:.value} margins are set to '0'. A `height`{:.prop} of `auto`{:.value} is set to the element's intrinsic width.
* For a block box with a fixed height, the formula `margin-top + border-top-width + padding-top + 'content height' + padding-bottom + border-bottom-width + margin-bottom = containing block height` must hold true. The inequality in the equation is split evenly between the auto-margins.
* For a block box with an `auto`{:.value} height, any `auto`{:.value} margins are set to '0', and the height will stretch to fit the box's content exactly. 

This is different from the CSS equation in the following ways:

* The `top`{:.prop} and `bottom`{:.prop} properties cannot be set to `auto`{:.value}.
* Floating and positioned boxes are evaluated like normal boxes.
* Block boxes with a fixed height will resolve `auto`{:.value} vertical margins similarly to horizontal margins. 

### Minimum and maximum heights: 'min-height' and 'max-height'
{:#min-height}

`min-height`{:.prop}

Value: | \<length\> \| \<percentage\>
Initial: | 0px
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | relative to the height of the containing block

`max-height`{:.prop}
{:#max-height}

Value: | \<length\> \| \<percentage\>
Initial: | -1px
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | relative to the height of the containing block

Values have the following meaning:

`<length>`{:.value}
: Specifies a fixed minimum or maximum height. 

`<percentage>`{:.value}
: Specifies a minimum or maximum height relative to the height of the containing block. 

Note that there is no `auto`{:.value} value for `max-height`{:.prop}; instead, if it is a negative number there is no maximum height.

When evaluating `height`{:.prop}, if the computed width is greater than `max-height`{:.prop}, then the height is computed again, this time substituting `max-height`{:.prop} for `height`{:.prop}. If the computed value is less than `min-height`{:.prop}, the the width is computed again, this time substituting `min-height`{:.prop} for `height`{:.prop}. A block box with a `height`{:.prop} of `auto`{:.value} will never set its height below `min-height`{:.prop} or above `max-height`{:.prop}; this may result in overflow.

### Line height calculations: the 'line-height' and 'vertical-align' properties
{:#line-height}

The height of a line box is determined as follows:

1. The height of each inline element is calculated.
2. The inline boxes are aligned vertically (by their `vertical-align`{:.prop} property)
3. The line box height is given by distance between the top edge of the highest box and the bottom edge of the lowest box. 

Note that vertical padding, margins and borders of inline boxes are not taken into account when determining line box height, although they are rendered.

`line-height`{:.prop}

Value: | \<number\> \| \<length\> \| \<percentage\>
Initial: | 1.2
Applies to: | all elements
Inherited: | yes
Percentages: | relative to the the font size of the element itself

This property determines the minimal height of the element's inline boxes.

Values for this property have the following meanings:

`<number>`{:.value}
: The line height is set to the element's font height scaled by this number. 

`<length>`{:.value}
: The line height is set to this fixed value. 

`<percentage>`{:.value}
: The line height is set to the element's font height scaled by the percentage. 

```css
/* Three ways of setting the same line-height. */
div
{
	line-height: 1.3;
	line-height: 1.3em;
	line-height: 130%;
}
```

`vertical-align`{:.prop}
{:#vertical-align}

Value: | baseline \| sub \| super \| text-top \| text-bottom \| middle \| top \| bottom \| \<percentage\> \| \<length\>
Initial: | baseline
Applies to: | inline-level elements
Inherited: | no
Percentages: | relative to the element's line-height

This property affects the vertical positioning of an inline box within the line box.

The values have the following meanings:

`baseline`{:.value}
: Align the baseline of the inline box with the baseline of the line box. 

`sub`{:.value}
: Set the baseline of the inline box to an appropriate height for rendering subscript. 

`super`{:.value}
: Set the baseline of the inline box to an appropriate height for rendering superscript. 

`text-top`{:.value}
: Align the top of the inline box with the top of the parent box's font. 

`text-bottom`{:.value}
: Align the bottom of the inline box with the bottom of the parent box's font. middle: Align the midpoint of the box with the bottom of the parent box's font plus half the ex height. 

`top`{:.value}
: Align the top of the inline box with the top of the line box. 

`bottom`{:.value}
: Align the bottom of the inline box with the bottom of the line box. 

`<percentage>`{:.value}
: Raise or lower the element from the baseline by the line-height scaled by this percentage. 

`<length>`{:.value}
: Raise or lower the element from the baseline by a fixed amount. 

```css
/* Sample RCSS for defining a superscript tag. */
super
{
	vertical-align: super;
}
```

```html
/* Sample RML demonstrating rendering a superscript. */
<p>
	Better than ever before!<super>*</super>
</p>
```