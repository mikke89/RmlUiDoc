---
layout: page
title: Documents
parent: python_manual
---

### Interface

Documents derive from elements, so inherit their [interface](elements.html#interface). The document-specific interface is similar to the C++ interface; refer [there](../cpp_manual/documents.html) for the full functional documentation.

####Properties

Python property | Brief description | Equivalent C++ methods
--------------- | ----------------- | ----------------------
`context`{:.prop} | Retrieves the document's context. | `GetContext()`
`title`{:.prop} | Gets / sets the document's title. | `GetTitle()`, `SetTitle()`

#### Methods

The following methods are exported from the C++ interface.

Python method | Brief description
------------- | -----------------
`CreateElement()` | Creates an element by tag name.
`CreateTextNode()` | Creates a text element.
`Close()` | Closes the document and destroys all child elements.
`Hide()` | Hides the document.
`PullToFront()` | Pulls to the document to the front of others with a similar z-index.
`PushToBack()` | Pushes to the document behind others with a similar z-index.
`Show(flags = FOCUS)` | Shows the document, optionally with focus flags.

The flags available for the `Show()` function are the same as the C++ function. The flags are referenced in Python as:

* `NONE`
* `FOCUS`
* `MODAL`