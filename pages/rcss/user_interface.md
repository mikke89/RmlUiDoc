---
layout: page
title: User interface
parent: rcss
next: animations_transitions_transforms
---

### Mouse cursor: the 'cursor' property
{:#cursor}

`cursor`{:.prop}

Value: | \<string\>
Initial: | *empty*
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property defines the cursor to display while the mouse is hovering over the element. The value is submitted directly through the [system interface](../cpp_manual/interfaces/system.html) if the element's [context](../cpp_manual/contexts.html#mouse-cursor) is set to enable cursors.

### Caret color
{:#caret-color}

`caret-color`{:.prop}

Value: | auto \| \<colour\>
Initial: | auto
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property sets the color of the text input cursor, the marker which tells where the next character will be inserted. Can be used on text fields such as in `<input>`{:.tag} and `<textarea>`{:.tag} elements. A value of `auto`{:.value} means that the caret color will use the element's `color`{:.prop} property.

### Box sizing
{:#box-sizing}

`box-sizing`{:.prop}

Value: | content-box \| border-box
Initial: | content-box
Applies to: | block and replaced inline elements
Inherited: | no
Percentages: | N/A

Determines how widths and heights are calculated.

`content-box`{:.value}
: This is the normal behavior. The `width`{:.prop} and `height`{:.prop} properties set the size of the *content box*.

`border-box`{:.value}
: The `width`{:.prop} and `height`{:.prop} properties set the size of the *border box*. This includes the content, padding and border, but not the margins. The sizes of the content box is calculated by subtracting the padding and border size, and is then floored at zero. 

Setting the value to `border-box`{:.value} can be valuable for laying out elements to fit on a line, especially when combining percentages and lengths for widths or heights, paddings, and borders. For example, if you have two elements of `width: 50%`{:.value} and some positive length for the border, they will not normally fit on a line. However, by applying `box-sizing: border-box`{:.value} to the elements they will be able to fit next to each other.

This property takes no effect for `auto`{:.value} values of `width`{:.prop} or `height`{:.prop}. 

### Pointer events: the 'pointer-events' property
{:#pointer-events}

`pointer-events`{:.prop}

Value: | auto \| none
Initial: | auto
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

Set the element property to disregard mouse input events on this and descending elements.


`auto`{:.value}
: The element behaves as it would if the pointer-events property were not specified.

`none`{:.value}
: The element is never the target of pointer events.


### Drag & drop: the 'drag' property
{:#drag}

The `drag`{:.prop} property is a new property, not shared by CSS. It controls the generation of events as the mouse cursor begins a drag over an element (ie, clicks the left mouse button and moves the mouse), drags over elements (moves the mouse with the button depressed) and finishes a drag, or 'drops', an element over another.

`drag`{:.prop}

Value: | none \| drag \| drag-drop \| block \| clone
Initial: | none
Applies to: | all elements
Inherited: | no
Percentages: | N/A

Values have the following meanings:

`none`{:.value}
: If the mouse begins a drag over this element, the element is not dragged and does not generate any drag messages. However, it does not prevent an ancestor element from being dragged. 

`drag`{:.value}
: If the mouse begins a drag over this element, the element will begin spawning drag messages. However, no messages will be directed to other elements relating to the drag or the eventual drop. 

`drag-drop`{:.value}
: If the mouse begins a drag over this element, the element will begin spawning drag messages. Messages will also be directed to over elements if the dragged element is dragged over them. 

`block`{:.value}
: If the mouse begins a drag over this element, the element is not dragged and neither is any ancestor element. 

`clone`{:.value}
:  Like `drag-drop`{:.value}, but a clone of the element is attached to the mouse cursor during dragging. The clone has the pseudo-class `:drag`{:.cls} set on it to allow it to be differentiated from the original element.

### Tab index: the 'tab-index' property
{:#tab-index}

The 'tab-index' property is introduced for RCSS. It controls the generation of a tab order, which is an ordered list of elements within a document that gain input focus in turn as the 'tab' key is pressed.

`tab-index`{:.prop}

Value: | none \| auto
Initial: | none
Applies to: | all elements
Inherited: | no
Percentages: | N/A

Values have the following meanings:

`none`{:.value}
: The element is not part of the tabbing order. 

`auto`{:.value}
: The element inserts itself into the tabbing order in a location relative to its order in the element hierarchy.


### Focus: the 'focus' property
{:#focus}

`focus`{:.prop}

Value: | none \| auto
Initial: | auto
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

The 'focus' property is introduced for RCSS. It controls whether or not an element can receive focus. Typically set to `none`{:.value} for disabled input elements,

Values have the following meanings:

`none`{:.value}
: The element can not receive focus. This will also prevent click events (when originating from user input) to reach the element.

`auto`{:.value}
: The element can receive focus.
