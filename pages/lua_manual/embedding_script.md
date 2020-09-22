---
layout: page
title: Embedding Lua script
parent: lua_manual
next: fonts
---

When using the Lua plugin, Lua code can be embedded into RML files. Inline responses to events are executed as Lua code. Functions, structures and variables can be declared or included with the `<script>`{:.tag} tag, then referenced from the inline code.

### Inline event responses

The Lua plugin installs an event listener instancer to execute inline event responses as Lua code. For example, in the following sample the element will run the print command when it is clicked:

```html
<button onclick="print('Hello world!')" />
```

Multiple statements can be executed as well.

```html
<button onclick="print('Hello') print('world!')" />
```
Three global variables are accessible to inline event handlers. These are:

* `event`: The event currently being processed (ie, the event that triggered the handler).
* `element`: The element currently responding to the event.
* `document`: The owner document of the current element. 

```html
<button onclick="print(element.tag_name)" />
<button onclick="print(event.parameters.mouse_x .. ', ' .. event.parameters.mouse_y)" />
```

See the [element](elements.html), [document](documents.html) and [event](events.html) documentation for their full Lua interfaces.

### Embedding Lua into RML

Lua code can be embedded into an RML document with the `<script>`{:.tag} tag. Similarly to Javascript, the script can be included from a separate file with the `src`{:.attr} attribute, or otherwise declared inline as loose content within the `<script>`{:.tag} tag. Any code embedded in this manner will be compiled with the document and will be available to inline event handlers in the RML. For example, the following document declares a Lua function in the `<script>`{:.tag} tag and calls it from an element's `click`{:.evt} handler.

```html
<rml>
	<head>
		<script>
function Test()
	print('Hello world!')
end
		</script>
	</head>
	<body>
		<button onclick="Test()">Continue</button>
	</body>
</rml>
```

The following sample imports the `test.lua`{:.path} file instead of declaring the script inline (it is assumed the Lua file declares a `Test()` function).

```html
<rml>
	<head>
		<script src="test.lua"></script>
	</head>
	<body>
		<button onclick="Test()">Continue</button>
	</body>
</rml>
```

A document can include multiple `<script>`{:.tag} tags.
