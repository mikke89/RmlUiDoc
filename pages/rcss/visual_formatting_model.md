---
layout: page
title: Visual formatting model
parent: rcss
next: visual_formatting_model_details
---

The visual formatting model used in RCSS is almost identical to that of [CSS](http://www.w3.org/TR/REC-CSS2/visuren.html), and it is recommended you read that for a detailed explanation of how RmlUi builds and places element boxes. A short summary can be found below.

The differences between CSS and RCSS are:

* The dimensions of the viewport are defined as the dimensions of the context the document is being rendered in.
* The document element (the root) is always positioned (as absolute), and can be positioned within its context using `top`{:.prop}, `right`{:.prop}, `bottom`{:.prop} and `left`{:.prop}.
* Compact and run-in boxes are not yet supported.
* Generated content is not yet supported. 

### Introduction to the visual formatting model

During document layout, each element generates zero or more boxes. How these boxes are sized and laid out within their document is governed by:

* The box type (either block, for boxes generally laid out top-to-bottom, or inline, for boxes laid out along a line).
* The box size; this could either be derived from intrinsic dimensions for elements such as images and form controls, or specified directly through RCSS properties, or determined by the contents of the box.
* Relationships of the box to other boxes in the document tree, such as floating boxes. 

#### Containing blocks

Every box has a 'containing block', a rectangular box with a fixed width and height. The dimensions of this box are used to evaluate such things as relative widths and margins. In general, a box will establish the containing block for its descendant elements, depending on the box's type.

A box is not necessarily constrained by the dimensions of its containing block, it may overflow along the x- or y-axes.

The containing block of the root document element is set by the dimensions of the document's context. The document element will generally establish a containing block for its descendants. However, it if does not have a fixed height, the height of the context will be used.

### Controlling box generation

#### Block level elements and block boxes

Block-level elements are those that are formatted as blocks, flowing visually down the document from top to bottom (such as paragraphs). Elements with a `display`{:.prop} of `block`{:.value} generate block boxes, as do any `absolute`{:.value} or `fixed`{:.value} positioned elements and floating elements.

Block-level elements generate exactly one block box that itself contains only block boxes. If any inline elements are inside this block box, an anonymous block box is created (one not representing any specific element) to hold and position the inline content. The anonymous block box is positioned with the original block box just like any other block box.

So, while processing the following RML fragment (assuming `div`{:.tag} and `p`{:.tag} elements are block, and `img`{:.tag} elements are inline):

```html
<div>
	<div>
	</div>
	<p>
		<img />
	</p>
</div>
```

the first `div`{:.tag} would generate a block box. This box would establish the containing block for its descendants. The second `div`{:.tag} would generate a block box using the first's containing block, as would the `p`{:.tag} element. The `img`{:.tag} element would be placed inside an anonymous block box, which would be positioned within the `p`{:.tag} tag and generated with its containing block.

#### Inline-level elements and inline boxes

Inline-level elements are those elements that do not generate blocks of content, but flow their content into lines contained by a block box. Elements with a `display`{:.prop} property of `inline`{:.value} or `inline-block`{:.value} generate inline boxes.

Loose text within elements also generates inline boxes.

#### The 'display' property
{:#display}

`display`{:.prop}

Value: | inline \| block \| inline-block \| flex \| table \| table-row-group \| table-row \| table-column-group \| table-column \| table-cell \| none
Initial: | inline
Applies to: | all elements
Inherited: | no
Percentages: | N/A

The values have the following meanings:

`block`{:.value}
: This element generates a block box. 

`inline`{:.value}
: This element generates one or more inline boxes. 

`inline-block`{:.value}
: This element generates a block box, which its descendants are positioned within, but is positioned itself as a single inline box. This is similar to the behaviour of replaced elements (those with intrinsic widths). 

`flex`{:.value}
: This element generates a flex container, and all its children are formatted as flex items, see [flexbox layout](flexboxes.html) for details.

`table, table-row-group, table-row, table-column-group, table-column, table-cell`{:.value}
: These values are used for defining and structuring [tables](tables.html).

`none`{:.value}
: This element (and all of its descendants) generate no boxes, and are not displayed. Note this will mean the element will not affect layout. The 'visibility' property can be used to make an element affect layout but not be rendered. 

The only difference between this and the CSS display property is the reduced range of allowed values.

### Positioning schemes

RCSS can position elements according to three schemes:

1. Normal flow, which includes placement of block boxes, the flowing of inline boxes and relative positioning of either.
2. Floats. Floating elements are placed as normal, then shifted as far to the left or right as possible within their containing block. Inline content is then flowed around floating boxes.
3. Absolute positioning. Elements that are positioned with `absolute`{:.value} or `fixed`{:.value} are removed from the normal flow (therefore having no impact on the layout of other elements) and placed at an explicit location relative to their containing block. 

#### Choosing a positioning scheme: 'position' property
{:#position}

`position`{:.prop}

Value: | static \| relative \| absolute \| fixed
Initial: | static
Applies to: | all elements
Inherited: | no
Percentages: | N/A

The values have the following meanings:

`static`{:.value}
: The element generates boxes that are positioned according to normal flow. 

`relative`{:.value}
: The element generates boxes that are positioned according to normal flow, but then offset according to the values of the 'top', 'right', 'bottom' and 'left' properties. Other elements are positioned as though the box was in its original location. 

`absolute`{:.value}
: The element generates a block box that is removed from normal flow. The `top`{:.prop}, `right`{:.prop}, `bottom`{:.prop} and `left`{:.prop} properties will position the box relative to the edges of its containing block. 

`fixed`{:.value}
: The element is positioned like an `absolute`{:.value} box, but will not scroll along with other content if it is within an overflowing box. 

#### Box offsets: 'top', 'right', 'bottom', 'left'
{:#top_right_bottom_left}

`top`{:.prop}, `bottom`{:.prop}

Value: | auto \| \<length\> \| \<percentage\>
Initial: | auto
Applies to: | positioned elements
Inherited: | no
Percentages: | relative to the height of the containing block

`left`{:.prop}, `right`{:.prop}

Value: | auto \| \<length\> \| \<percentage\>
Initial: | auto
Applies to: | positioned elements
Inherited: | no
Percentages: | relative to the width of the containing block

The values have the following meanings:

`auto`{:.value}
: Behavior depends on other related properties. For absolutely positioned elements, may adjust position or size to align the box with the containing block.

`<length>`{:.value}
: The edge is offset a fixed distance from the reference edge. 

`<percentage>`{:.value}
: The edge is offset from the reference edge a distance relative to the dimensions of the containing block. 

### Normal flow

#### Block formatting

When formatting block boxes, boxes are laid out vertically one after the other. The bottom edge of a block box will touch the top edge of the block box following it. The left edge of a block box will touch the left edge of its containing block. Block elements do not themselves flow around floating elements, but their inline content will.

#### Inline formatting

Inline boxes are positioned horizontally on a line, one after the other, from the top of the containing block. Horizontal padding, borders and margins are respected when positioning the boxes. Inline boxes on a single line are said to be laid out in a line box.

Each line box is generally the same width as its containing block, with its left edge touching the left edge of the containing block and its right edge touching the right edge of the containing block. However, floating elements may force a line box to be shorter along one or both of its edges. The height of a line box is governed by the height of the box's inline content. Inline boxes are positioned vertically through the line box using the `vertical-align`{:.prop} property.

If several inline boxes cannot fit horizontally onto a single line box, they are flowed into several vertically-stacked line boxes.

The `text-align`{:.prop} property governs how the excess horizontal space between the widths of the inline boxes and the width of the line box is distributed.

Inline boxes may be split across several line boxes. When this occurs, any horizontal margins, borders and padding will only be present at the beginning and end of the inline box, not on each line.

#### Relative positioning

Once a block or inline box has been positioned, it can be moved from its location if its `position`{:.prop} is set to `relative`{:.value}. It is offset from its position using the `top`{:.prop}, `right`{:.prop}, `bottom`{:.prop} and `left`{:.prop} properties. Note that it affects the positioning of further elements from its original location, not its new one.

### Floats

A float is a box that is shifted horizontally to the left or right edge of its containing block. They do not affect placement of further block boxes, however line boxes will be shortened to avoid running over them. In this way, inline content will be flowed around them. Block boxes can be forced vertically past floating boxes using the `clear`{:.prop} property.

See the [CSS2 documentation](http://www.w3.org/TR/REC-CSS2/visuren.html#floats) on floating elements for a description on the full float model, and interesting uses of floats.

#### Positioning the float: the 'float' property
{:#float}

`float`{:.prop}

Value: | left \| right \| none
Initial: | none
Applies to: | all but absolutely positioned elements
Inherited: | no
Percentages: | N/A

The values of this property have the following meanings:

`left`{:.value}
: The element generates a block box that is floated to the left. 

`right`{:.value}
: The element generates a block box that is floated to the right. 

`none`{:.value}
: The element's boxes are not floated. 

#### Controlling flow next to floats: the 'clear' property
{:#clear}

`clear`{:.prop}

Value: | left \| right \| both \| none
Initial: | none
Applies to: | block-level elements
Inherited: | no
Percentages: | N/A

The values of this property have the following meanings:

`left`{:.value}
: The box's position is pushed far enough vertically so its top edge is below the bottom edge of all previously placed left-floating elements. 

`right`{:.value}
: The box's position is pushed far enough vertically so its top edge is below the bottom edge of all previously placed right-floating elements. 

`both`{:.value}
: The box's position is pushed far enough vertically so its top edge is below the bottom edge of all previously placed floating elements. 

`none`{:.value}
: The box's position is placed irrespective of floating elements. 

Floating boxes themselves can be cleared.

Note that RCSS ignores floating elements placed within a sibling's containing block.

### Absolute positioning

An absolutely positioned box (one with a `position`{:.prop} of `absolute`{:.tag} or `fixed`{:.tag}) is explicitly offset from the edges of its containing block. Floating boxes are ignored when laying out its inline content.

Note that in RCSS, `fixed`{:.value} positioned boxes are not placed relative to the viewport, but identically to `absolute`{:.value} boxes.

### Layered presentation

Each box has a stacking level within a single stacking context. Boxes within a stacking context are rendered in stacking level order, from lowest to highest (so boxes with the highest stacking level will appear on top). All the boxes within a single stacking context are rendered at once; they will not intermingle rendering with the members of another stacking context.

The root element of a document establishes a stacking context for its descendants. Other elements within a document may establish local stacking contexts of their own. An element which does so has two stacking levels; one within the stacking context it is a member of (given by the `z-index`{:.prop} property) and another inside the stacking context it establishes (always '0').

#### Specifying the stacking level: the 'z-index' property
{:#z-index}

`z-index`{:.prop}

Value: | \<number\> \| auto
Initial: | auto
Applies to: | all elements
Inherited: | no
Percentages: | N/A

Values have the following meanings:

`<number>`{:.value}
: The number is the stack level within the current stacking context. It also establishes a local stacking context in which its own stack level is '0'. 

`auto`{:.value}
: The stack level of the box is the same as its parent's. It does not establish a local stacking context. 

Note that in RCSS any element can have the z-index property, not just positioned elements. 