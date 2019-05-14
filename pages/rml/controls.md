---
layout: page
title: RML Controls
parent: rml
---

### \<handle\>

The `<handle>`{:.tag} element can be used to move or change the size of elements.

_Attributes_

`move_target`{:.attr} = idref (CI)
: If specified, the handle will move the element specified by the ID when dragged. Can be `#document`{:.value} to reference the parent document.

`size_target`{:.attr} = idref (CI)
: If specified, the handle will size the element specified by the ID when dragged. Can be `#document`{:.value} to reference the parent document.

```html
<handle move_target="#document">
	<div id="title">My document</div>
</handle>
```

### \<tabset\>

A `<tabset>`{:.tag} element contains `<tab>`{:.tag} elements and `<panel>`{:.tag} elements.

Tabset elements are supported only when the [Controls plugin]({{"pages/cpp_manual/controls.html"|relative_url}}) is used.

#### \<tab\>

Each `<tab>`{:.tag} element acts as a button, that when clicked will hide the currently visible panel and show its corresponding panel.

#### \<panel\>

A `<panel>`{:.tag} element is the body of the tabset. The visibility of the panel is controlled by the tab elements in the parent tabset. 