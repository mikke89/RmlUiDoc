---
layout: page
title: Elements
parent: python_manual
---

### Interface

The Python interface for {{page.lib_name}} elements closely resembles [Gecko's HTML DOM element interface](http://developer.mozilla.org/en/docs/DOM:element), similarly to the C++ element interface.

### Properties

{{page.lib_name}} property | Brief description | Equivalent DOM property
--------------- | ----------------- | -----------------------
`absolute_left`{:.prop} | The distance from the context's left edge and the element's left border. 
`absolute_top`{:.prop} | The distance from the context's top edge and the element's top border. 
`attributes`{:.prop} | All attributes associated with an element. | attributes
`child_nodes`{:.prop} | All child nodes of an element. | childNodes
`class_name`{:.prop} | Gets/sets the class of the element. | className
`client_height`{:.prop} | The inner height of an element. | clientHeight
`client_left`{:.prop} | The width of the left border of an element. | clientLeft
`client_top`{:.prop} | The width of the top border of an element. | clientTop
`client_width`{:.prop} | The inner width of an element. | clientWidth
`first_child`{:.prop} | The first direct child node of an element. | firstChild
`id`{:.prop} | Gets/sets the id of the element. | id
`inner_rml`{:.prop} | Gets/sets the markup and content of the element. | innerHTML
`last_child`{:.prop} | The last direct child node of an element. | lastChild
`next_sibling`{:.prop} | The node immediately following the given one in the tree. | nextSibling
`offset_height`{:.prop} | The height of an element, relative to the layout. | offsetHeight
`offset_left`{:.prop} | The distance from this element's left border to its offset parent's left border. | offsetLeft
`offset_parent`{:.prop} | The element from which all offset calculations are currently computed. | offsetParent
`offset_top`{:.prop} | The distance from this element's top border to its offset parent's top border. | offsetTop
`offset_width`{:.prop} | The width of an element, relative to the layout. | offsetWidth
`owner_document`{:.prop} | The document that this node is in. | ownerDocument
`parent_node`{:.prop} | The parent element of this node. | parentNode
`previous_sibling`{:.prop} | The node immediately preceding the given one in the tree. | previousSibling
`scroll_height`{:.prop} | The scroll view height of an element. | scrollHeight
`scroll_left`{:.prop} | Gets/sets the left scroll offset of an element. | scrollLeft
`scroll_top`{:.prop} | Gets/sets the top scroll offset of an element. | scrollTop
`scroll_width`{:.prop} | The scroll view width of an element. | scrollWidth
`style`{:.prop} | An object representing the declarations of an element's style attributes. | style
`tag_name`{:.prop} | The name of the tag for the given element. | tagName

#### Array properties

The child_nodes and attributes properties are accessed as arrays; they are indexed numerically, from the front or back, and their length can be queried with the `len()` function.

`child_nodes` is an array of element types. The array only includes visible elements; Python has no way of querying [hidden elements](../cpp_manual/hidden_elements.html). The following example iterates over all of an element's children, printing their tag names, ids and classes:

```python
for child in element.child_nodes:
	address = child.tag_name

	if child.id != "":
		address += "#" + child.id

	classes = child.class_name.split()
		for class in classes:
			address += "." + class

	print address
```

attributes is an array of attribute types, each of which has a name and value property. The following example iterates over an element's attributes, printing their names and values:

```python
for attribute in element.attributes:
	print attribute.name + ": " + attribute.value
```

#### The style property

The style property operates identically to its counterpart in Javascript. Properties are accessed as members of the style property by name and can be read or written to. The value of a property is always an unparsed string in this context; ie, `200px`{:.value}, `center`{:.value}, `rgb(255,0,0)`{:.value}, etc.

The following example demonstrates uses of the style property:

```python
element.style.width = "150px";
if element.style.float != "none":
	element.style.clear = "left";
```

### Methods

{{page.lib_name}} methods | Brief description | Equivalent DOM method
-------------- | ----------------- | ---------------------
`AddEventListener()` | Register an event handler to a specific event type on the element. | addEventListener()
`AppendChild()` | Insert a node as the last child node of this element. | appendChild()
`Blur()` | Removes keyboard focus from the current element. | blur()
`Click()` | Simulates a click on the current element. | click()
`DispatchEvent()` | Dispatch an event to this node in the DOM. | dispatchEvent()
`Focus()` | Gives keyboard focus to the current element. | focus()
`GetAttribute()` | Retrieve the value of the named attribute from the current node. | getAttribute()
`GetElementById()` | Returns an object reference to the identified element. | getElementById()
`GetElementsByTagName()` | Retrieve a set of all descendant elements, of a particular tag name, from the current element. | getElementsByTagName()
`HasAttribute()` | Check if the element has the specified attribute, or not. | hasAttribute()
`HasChildNodes()` | Check if the element has any child nodes, or not. | hasChildNodes()
`InsertBefore()` | Inserts the first node before the second, child, node in the DOM. | insertBefore()
`RemoveAttribute()` | Remove the named attribute from the current node. | removeAttribute()
`RemoveChild()` | Removes a child node from the current element. | removeChild()
`ReplaceChild()` | Replaces one child node in the current element with another. | replaceChild()
`ScrollIntoView()` | Scrolls the page until the element gets into the view. | scrollIntoView()
`SetAttribute()` | Set the value of the named attribute from the current node. | setAttribute()

### Dispatching events

Events can be generated on an element from within Python with the `DispatchEvent()` function. When calling this function, the parameters are given as a Python dictionary.

```python
element.DispatchEvent("open", {"object": "trapdoor", "priority": 11}, False)
```

Parameter keys must be strings, and values must be strings, integers or floating-point. Others will generate a `KeyError` or `ValueError` exception as appropriate.

### Creating elements

Elements can be created dynamically in Python using the document's `CreateElement()` or `CreateTextNode()` method. The following code sample uses `CreateElement()` to dynamically create a form control.

```python
input_element = document.CreateElement("input")
input_element.SetAttribute("type", "radio")
input_element.SetAttribute("name", "graphics")
input_element.SetAttribute("value", "ok")
document.AppendChild(input_element)

text_element = document.CreateTextNode("OK")
document.AppendChild(text_element)
```
