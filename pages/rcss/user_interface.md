---
layout: page
title: User interface
parent: rcss
next: sprite_sheets
---

### Mouse cursor: the 'cursor' property

`cursor`{:.prop}

Value: | \<string\>
Initial: | *empty*
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property defines the cursor to display while the mouse is hovering over the element. The value is submitted directly through the [system interface](../cpp_manual/interfaces.html#the-system-interface) if the element's [context](../cpp_manual/contexts.html#mouse-cursor) is set to enable cursors.


### Pointer events: the 'pointer-events' property

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
