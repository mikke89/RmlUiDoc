---
layout: page
title: RML Controls
parent: rml
next: data_display
---

### \<handle\>

The `<handle>`{:.tag} element can be used to move or change the size of elements.

_Attributes_

`move_target`{:.attr} = idref (CI)
: If specified, the handle will move the element specified by the ID when dragged. Can be `#document`{:.value} to reference the current document, or `#parent`{:.value} to reference the parent element.

`size_target`{:.attr} = idref (CI)
: If specified, the handle will size the element specified by the ID when dragged. Can be `#document`{:.value} to reference the current document, or `#parent`{:.value} to reference the parent element.

`edge_margin`{:.attr} = \<length-percentage\>{1-4} | none
: Constrains the target placement to the edges of its containing block. This attribute can take any length or percentage, which specifies the minimum distance between the target and the edges of its containing block. These constraints will be satisfied while dragging the handle, for both position and size targets.\
By default, this value is set to `0px`, which means that handle targets will be constrained exactly to the edges of their containing block. The value can also be specified by up to four space-separated values in box order (top/right/bottom/left), determining the minimum distance to each side. Negative values are allowed, which enables movement outside the edges of the containing block. Percentages are resolved against the size of the target element. The value `none`{:.value} can be used to remove all constraints.

During drag operations, the handle element will first consider the target element's combination of inset properties (`top`{:.prop}, `right`{:.prop}, `bottom`{:.prop}, `left`{:.prop}) and size properties (`width`{:.prop}, `height`{:.prop}). It will then adjust the necessary aforementioned properties to move or size the target element according to the drag delta, in a way that retains the sides that the element anchors to. This way, the target element can still automatically be resized when its container is resized, even after the handle has changed its placement.

```html
<div id="bucket">Bucket</div>
<handle move_target="bucket">Drag to move the bucket.</handle>
```

```html
<handle move_target="#document">
	<div id="title">My document</div>
</handle>
```

```html
<div class="help_box">
	<handle size_target="#parent" edge_margin="20px 30px"/>
</div>
```

```html
<handle class="drag_icon" move_target="#self" edge_margin="-50%"/>
```


### \<tabset\>

A `<tabset>`{:.tag} element contains `<tab>`{:.tag} elements and `<panel>`{:.tag} elements.

See also the [tab set documentation]({{"pages/cpp_manual/element_packages/tab_set.html"|relative_url}}) in the C++ manual.

#### \<tab\>

Each `<tab>`{:.tag} element acts as a button, that when clicked will hide the currently visible panel and show its corresponding panel.

#### \<panel\>

A `<panel>`{:.tag} element is the body of the tabset. The visibility of the panel is controlled by the tab elements in the parent tabset.
