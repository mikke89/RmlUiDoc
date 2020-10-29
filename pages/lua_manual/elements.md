---
layout: page
title: Elements
parent: lua_manual
next: documents
status: improve
status-desc: Some examples do not work properly.
---

### Interface

- [Element Lua API reference](api_reference.html#Element)
- [Element C++ manual](../cpp_manual/elements.html)

All properties and methods that are available for elements are described in detail in the API reference. The element-specific interface is similar to the C++ interface, refer there for the full documentation.

The Lua interface for RmlUi elements closely resembles the [DOM element interface](https://developer.mozilla.org/en-US/docs/Web/API/element) of the web, similarly to the C++ element interface.

#### Proxy Properties

Under the hood, some properties return proxies which can typically be used like arrays or maps (Lua tables). In particular the properties described in the following.

`child_nodes` returns an array-like proxy for the children elements. The array only includes visible elements, the Lua plugin has no way of querying [hidden elements](../cpp_manual/hidden_elements.html). The following example iterates over all of an element's children, printing their tag names, ids and classes. The example requires the Lua `string` standard library.

```lua
for i,child in ipairs(element.child_nodes) do
	address = child.tag_name

	if child.id ~= '' then
		address = address .. '#' .. child.id
	end

	for token in string.gmatch(child.class_name, '[%w]+') do
	   address = address .. '.' .. token
	end

	print(address)
end
```

The proxy object can be accessed using indices. Note that the indices are one-based in Lua, as opposed to zero-based in the C++ API.

```lua
element.child_nodes[2].inner_rml = 'Hello world!'
```

`attributes` is accessed like a map with name and value pairs. The following example prints the element's `value`{:.attr} attribute.

```lua
print(element.attributes.value)
```

`style` is a property which operates identically to its counterpart in Javascript. Properties are accessed as members of the style property by name and can be read or written to. The value of a property is always an unparsed string in this context; ie, `200px`{:.value}, `center`{:.value}, `rgb(255,0,0)`{:.value}, etc.

The following example demonstrates uses of the style property:

```lua
element.style.width = '150px'
if element.style.float ~= 'none' then
	element.style.clear = 'left'
end
```

### Dispatching events

Events can be generated on an element from within Lua with the `DispatchEvent()` function. When calling this function, the parameters are given as a Lua table of name-value pairs.

```lua
element:DispatchEvent('open', {object = 'trapdoor', priority = 11})
```

Parameter keys must be strings, and values must be strings, booleans, or numbers.

### Creating elements

Elements can be created dynamically in Lua using the document's `CreateElement()` or `CreateTextNode()` method. The following code sample uses `CreateElement()` to dynamically create a form control.

```lua
input_element = document:CreateElement('input')
input_element:SetAttribute('type', 'radio')
input_element:SetAttribute('name', 'graphics')
input_element:SetAttribute('value', 'ok')
document:AppendChild(input_element)

text_element = document:CreateTextNode('OK')
document:AppendChild(text_element)
```
***Note/TODO:*** The first part of the example doesn't work because it returns an ElementPtr and that cannot use SetAttribute. We can improve this situation in the Lua plugin. For now you can use `Element.inner_rml = '...'` to create children, or append the child as above and then add attributes after getting the element from `Element.last_child`.
