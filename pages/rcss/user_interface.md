---
layout: page
title: User interface
parent: rcss
next: flexboxes
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


### Scroll chaining: the 'overscroll-behavior' property
{:#overscroll-behavior}

`overscroll-behavior`{:.prop}

Value: | auto \| contain
Initial: | auto
Applies to: | scroll containers
Inherited: | no
Percentages: | N/A

Controls how a scroll action is passed up the scroll chain, from one scroll container to its parent scroll container.

`auto`{:.value}
: The element will consume the scroll action if any of its scrollbars are visible. Otherwise, it will pass the scroll action up the scroll chain.

`contain`{:.value}
: The element will consume the scroll action if any of its scrollbars are visible. Otherwise, the scroll action is cancelled.

The `contain`{:.value} value can be useful to ensure that mouse wheel scrolling is not propagated outside a given element, regardless of whether its scrollbars are visible. The element will never pass a scroll action up the scroll chain.


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

Tabbing can also be enabled on the body element, so that it possible to tab back to the body such that no elements within the document has focus.


### Spatial navigation: the navigation properties
{:#nav}

The navigation properties are used to determine how the focus is moved when pressing one of the keyboard navigation buttons (arrow keys): up, right, down, and left.

`nav-up`{:.prop}, `nav-right`{:.prop}, `nav-down`{:.prop}, `nav-left`{:.prop}

Value: | none \| auto \| \<id\>
Initial: | none
Applies to: | all tabbable elements
Inherited: | no
Percentages: | N/A

Values have the following meanings:

`none`{:.value}
: The focus is not automatically moved when pressing the navigation button in the given direction.

`auto`{:.value}
: The focus is moved to the nearest tabbable element is the direction of the pressed navigation button.

`<id>`{:.value}
: The focus is moved to the element with the given id. The element is written with `#`{:.value} prefix, e.g. `#my_element`{:.value}.

Only <span class="prop-def-symbol" title="elements with 'tab-index: auto'">tabbable elements</span> are considered as navigation sources and targets. Further, automatic navigation is restricted to the same <span class="prop-def-symbol" title="elements whose 'overflow' property is set to anything other than 'visible' establish a new scroll container">scroll container</span>. Navigation can also be set on the body element, in which case `auto`{:.value} means navigating in tabbing-order when the body has focus.

> *Recommended practice*: Always set `nav: auto`{:.value} on the `body`{:.tag} element when using spatial navigation features in the same document. This ensures that users are always able to navigate within the document, even when the focus is lost from the otherwise navigable region, e.g. due to mouse focus or manual calls to blur.

When a navigation action is performed, the newly focused element has its `:focus-visible`{:.cls} [pseudo class](selectors.html#pseudo-selectors) set. This can be used to style the currently focused element.

There is also a shorthand property to set all of the above properties simultaneously.

`nav`{:.prop}

Value: | none \| auto \| horizontal \| vertical
Initial: | none
Applies to: | all tabbable elements
Inherited: | no
Percentages: | N/A

Values have the following meanings:

`none`{:.value}
: Disable navigation in all directions. Equivalent to setting `none`{:.value} to all the navigation properties.

`auto`{:.value}
: Enable automatic navigation in all directions. Equivalent to setting `auto`{:.value} to all the navigation properties.

`horizontal`{:.value}
: Enable automatic navigation in the horizontal directions. Equivalent to setting `auto`{:.value} to the horizontal navigation properties, and `none`{:.value} to the vertical navigation properties.

`vertical`{:.value}
: Enable automatic navigation in the vertical directions. Equivalent to setting `none`{:.value} to the horizontal navigation properties, and `auto`{:.value} to the vertical navigation properties.


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
