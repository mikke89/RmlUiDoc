---
layout: page
title: Embedding Python script
parent: python_manual
---

When using the Python plugin, Python code can be embedded into RML files. Inline responses to events are executed as Python code. Functions, structures and variables can be declared or included with the `<script>`{:.tag} tag, then referenced from the inline code.

### Inline event responses

The Python plugin installs an event listener instancer to execute inline event responses as Python code. For example, in the following sample the element will run the print command when it is clicked:

```html
<button onclick="print 'Hello world!'" />
```

Separate lines can be separated by semi-colons like Javascript.

```html
<button onclick="print 'Hello'; print 'world!'" />
```
Three global variables are accessible to inline event handlers. These are:

* `event`: The event currently being processed (ie, the event that triggered the handler).
* `self`: The element currently responding to the event.
* `document`: The owner document of the current element. 

```html
<button onclick="print self.tag_name" />
<button onclick="print event.mouse_x + ', ' + event.mouse_y" />
```

See the [element](elements.html), [document](documents.html) and [event](events.html) documentation for their full Python interfaces.

### Embedding Python into RML

Python code can be embedded into an RML document with the `<script>`{:.tag} tag. Similarly to Javascript, the script can be included from a separate file with the src attribute, or otherwise declared inline as loose content within the `<script>`{:.tag} tag. Any code embedded in this manner will be compiled with the document and will be available to inline event handlers in the RML. For example, the following document declares a Python function in the `<script>`{:.tag} tag and calls it from an element's onclick hander.

```html
<rml>
	<head>
		<script>
def Test():
	print 'Hello world!'
		</script>
	</head>
	<body>
		<button onclick="Test()">Continue</button>
	</body>
</rml>
```

Python code declared inline in an RML file like this must begin at the beginning of the line like a normal Python file.

The following sample imports the `test.py`{:.path} file instead of declaring the script inline (it is assumed the Python file declares a `Test()` function).

```html
<rml>
	<head>
		<script src="test.py"></script>
	</head>
	<body>
		<button onclick="Test()">Continue</button>
	</body>
</rml>
```

A document can include multiple `<script>`{:.tag} tags. 