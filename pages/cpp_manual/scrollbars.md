---
layout: page
title: Element scrollbars
parent: cpp_manual
next: documents
---

When appropriate, RmlUi automatically generates hidden scrollbar elements for elements with content overflow. The size and positioning of the scrollbar elements can be influenced through RCSS properties. Custom elements can make use of the scrollbar functionality to generate scrollbars of their own.

### Hidden elements

Scrollbar elements are tagged `scrollbarvertical`{:.tag} or `scrollbarhorizontal`{:.tag} depending on their orientation, and are parented directly to the elements that generated them. Each scrollbar element contains four hidden child elements:

* `sliderarrowdec`{:.tag}: The button at the top (or left) of the scrollbar which can be clicked to scroll further up (or to the left) the element.
* `sliderarrowinc`{:.tag}: The button at the bottom (or right) of the scrollbar which can be clicked to scroll further down (or to the right) the element.
* `slidertrack`{:.tag}: The track that runs between the two arrow buttons.
* `sliderbar`{:.tag}: The bar that runs on the track. It represents the size and position of the visible segment of the element's content. It can be dragged to scroll the visible window around. 

![scrollbars_1.gif](scrollbars_1.gif)

When both horizontal and vertical scrollbars are present on an element, they are both shortened by the amount necessary to avoid an intersection. Another element is created and placed in this intersection point, placed and sized appropriately. This corner element is tagged scrollbarcorner and exists only for decoration purposes.

#### Applying RCSS properties

See the [style guide](../style_guide.html) for documentation on applying properties to a scroll bar.

### Generating scrollbars

Custom elements can generate scrollbars using the element's scroll interface. This is done, for example, by the [text area](element_packages/form.html#text-area) form control.

Scrollbar generation is usually done in a custom element in response to the `resize`{:.evt} event, sent during layout. To retrieve a pointer to an element's scroll interface, call `GetElementScroll()` on the element. This will return a `Rml::ElementScroll` object.

```cpp
// Returns the element's scrollbar functionality.
// @return The element's scrolling functionality.
Rml::ElementScroll* GetElementScroll() const;
```

To enable or disable one of the element's scrollbars, call `EnableScrollbar()` or `DisableScrollbar()`:

```cpp
// Enables and sizes one of the scrollbars.
// @param[in] orientation Which scrollbar (vertical or horizontal) to enable.
// @param[in] element_width The current computed width of the element, used only to resolve percentage properties.
void EnableScrollbar(Rml::ElementScroll::Orientation orientation, float element_width);

// Disables and hides one of the scrollbars.
// @param[in] orientation Which scrollbar (vertical or horizontal) to disable.
void DisableScrollbar(Rml::ElementScroll::Orientation orientation);
```

As the object will remember the state of both previous scrollbars, it is recommended you explicitly enable or disable both scrollbars.

Call `FormatScrollbars()` once you have set the state of both scrollbars and set the size (and content size) of the scrolling element.

```cpp
// Formats the enabled scrollbars based on the current size of the host element.
void FormatScrollbars();
```
