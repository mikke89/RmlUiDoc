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

The target element is sized by adjusting its `width`{:.prop} and `height`{:.prop} properties, while it is moved by adjusting its `top`{:.prop} and `left`{:.prop} properties.

```html
<handle move_target="#document">
	<div id="title">My document</div>
</handle>
```

```html
<div class="help_box">
	<handle size_target="#parent"/>
</div>
```

```html
<div id="bucket">Bucket</div>
<handle move_target="bucket">Drag to move the bucket.</handle>
```

### \<tabset\>

A `<tabset>`{:.tag} element contains `<tab>`{:.tag} elements and `<panel>`{:.tag} elements.

See also the [tab set documentation]({{"pages/cpp_manual/element_packages/tab_set.html"|relative_url}}) in the C++ manual.

#### \<tab\>

Each `<tab>`{:.tag} element acts as a button, that when clicked will hide the currently visible panel and show its corresponding panel.

#### \<panel\>

A `<panel>`{:.tag} element is the body of the tabset. The visibility of the panel is controlled by the tab elements in the parent tabset.
