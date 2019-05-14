---
layout: page
title: Contexts
parent: python_manual
---

### Interface

#### Properties

Python property | Brief description | Equivalent C++ functions
--------------- | ----------------- | ------------------------
`dimensions`{:.prop} | Gets/sets the dimensions of the context. | `GetDimensions()`, `SetDimensions()`
`documents`{:.prop} | Retrieves a document within the interface. | `GetDocument()`, `GetNumDocuments()`
`focus_element`{:.prop} | Retrieves the context's focus element. | `GetFocusElement()`
`hover_element`{:.prop} | Retrieves the element under the context's cursor. | `GetHoverElement()`
`root_element`{:.prop} | Retrieves the context's root element. | `GetRootElement()`
`name`{:.prop} | Retrieves the context's name. | `GetName()`

##### Retrieving documents

The documents property on the context can be referenced in several ways. For example, as an array:

```python
for document in context.documents:
	print document.title

index = 0
while index < len(context.documents):
	print str(index) + ": " + context.documents[index].title
```

Or as a dictionary, looking documents up by their ID:

```python
try:
	document = context.documents["highscores"]
except KeyError:
	print "No document found!"
```

Or accessing documents as attributes on the documents property itself:

```python
try:
	document = context.documents.highscores
except AttributeError:
	print "No document found!"
```

#### Methods

The following methods are exported from the C++ interface.

Python method | Brief description
`AddEventListener()` | Attaches an inline event listener to the root of the context.
`AddMouseCursor()` | Adds a previously-loaded mouse cursor to the document.
`CreateDocument()` | Creates a new document.
`LoadDocument()` | Loads a document from an external RML file.
`LoadMouseCursor()` | Loads a mouse cursor from an external RML file.
`Render()` | Renders the context.
`ShowMouseCursor()` | Shows or hides the mouse cursor.
`UnloadAllDocuments()` | Unloads all loaded documents within the context.
`UnloadAllMouseCursors()` | Unloads all of the context's mouse cursors.
`UnloadDocument()` | Unloads one of the context's documents.
`UnloadMouseCursor()` | Unloads one of the context's cursors.
`Update()` | Updates the context.

### Creating contexts

Contexts can be created in Python with the `CreateContext()` function in the {{page.lib_name}} module. This function takes the name of the context as a string and the dimensions as an `Vector2i` type.

```python
new_context = rocket.CreateContext("hud", rocket.Vector2i(1024, 768))
```

### Accessing contexts

Existing contexts can be accessed in Python via the contexts member on the rocket module. They can then be accessed via name or index.

```python
context = rocket.contexts["hud"]
```

List all contexts

```python
for context in rocket.contexts:
  print context.name
```