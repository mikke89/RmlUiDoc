---
layout: page
title: Visual effects
parent: rcss
next: colours_backgrounds
---

### Overflow and clipping

The contents of a block box may extend beyond the content area of the box itself, for example under the following scenarios:

* The contents of an inline box wider than its containing block box cannot be broken.
* A block box has a width greater than its containing block box.
* A block box has an explicit height set, and its contents exceed that height.

When overflow occurs, the overflow-x' and 'overflow-y' properties dictate how the overflow is handled.

#### Overflow: the 'overflow' property
{:#overflow}

`overflow-x`{:.prop}, `overflow-y`{:.prop}

Value: | visible \| hidden \| auto \| scroll
Initial: | visible
Applies to: | block-level elements
Inherited: | no
Percentages: | N/A

The values have the following meanings:

`visible`{:.value}
: Overflowing content is visible along this axis.

`hidden`{:.value}
: Overflowing content is hidden along this axis.

`auto`{:.value}
: If overflow occurs along this axis, overflowing content is hidden and a scrollbar is generated and positioned along the axis so the hidden content can be scrolled into view.

`scroll`{:.value}
: A scrollbar is always visible along the axis, allowing hidden content to be scrolled into view. This will eliminate 'popping' if content suddenly overflows and a scrollbar appears.

If either `overflow-x`{:.prop} or `overflow-y`{:.prop} is set to a value other than 'visible', clipping will occur on both axes.

Note that, unlike CSS, [positioned elements](visual_formatting_model.html#position) and [transformed elements](animations_transitions_transforms.html#transform) do not affect when clipping is applied to the element. Thus, such elements may not be clipped or cause scrollbars to appear even when they overflow. Instead, one can use the [`clip: always`{:.value} property](#clip) together with hidden overflow to force clipping to occur.

`overflow`{:.prop}

Shorthand for `overflow-x overflow-y`{:.prop}. If two values are specified, the first will be used to specify `overflow-x`{:.prop} and the second `overflow-y`{:.prop}. If one value is specified, it will be used to specify both.

```css
/* Hide horizontal overflowing content and generate a scrollbar (if required) along the vertical axis. */
div#content
{
	overflow: hidden auto;
}
```

#### Clipping: the 'clip' property
{:#clip}

This property defines how the element interacts with the clipping regions of its ancestors.

The property differs completely from the CSS `clip`{:.prop} property which instead defines the clipping region of an element. In RCSS, the clipping region is always the 'client area'. The client area is normally the padding area of an element, but for certain elements it may be the content area.

`clip`{:.prop}

Value: | auto \| none \| always \| \<number\>
Initial: | auto
Applies to: | all elements
Inherited: | no
Percentages: | N/A

The values have the following meanings:

`auto`{:.value}
: The element is subjected to all the clipping regions put in place by its ancestors.

`none`{:.value}
: The element is never clipped (except by the context).

`always`{:.value}
: The element always clips, forcing all descendant elements to clip to this element's client area. This can be useful in some cases where elements are not automatically clipped even when set to e.g. `overflow: hidden`{:.prop}, such as with absolutely positioned or transformed child elements.

`<number>`{:.value}
: The element is subjected to the clipping regions of its ancestors, except it skips the closest `<number>`{:.value} ancestors that could have put in place a clipping region (ie, those ancestors with an `overflow-x`{:.prop} or `overflow-y`{:.prop} other than `visible`{:.value}). The number must be in the range `[1, 127]`{:.value}.

### Visibility: the 'visibility' property
{:#visibility}

`visibility`{:.prop}

Value: | visible \| hidden
Initial: | visible
Applies to: | all elements
Inherited: | no
Percentages: | N/A

Values have the following meanings:

`visible`{:.value}
: The generated box is visible.

`hidden`{:.value}
: The generated box, and all of its descendants, is hidden. Note that the box still has an impact on layout, it is just not rendered.

*Animation behavior*: When interpolating between `visible`{:.value} and `hidden`{:.value}, the `visible`{:.value} keyword is applied during the entire interpolation period. This is helpful in animations and transition where one wants to apply fade-in or fade-out effects when showing or hiding an element. This behavior ensures that the element is visible during the entire fading procedure.
