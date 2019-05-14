---
layout: page
title: Attaching To Events
parent: python_manual
---

### Statically in RML

The easiest way to attach to events with python is to write your code directly into the RML files, using the `on*`{:.attr} attributes. When the event is fired three global variables are set up, document, event and self.

self | The element thats currently being processed
[document](documents.html) | The document the element thats currently being processed belongs to
[event](events.html) | The event thats currently being processed

Example:

```html
<button onclick="print('Clicked!')"/>
```

To aid in the coding of inline Python code, {{page.lib_name}} allows multiple lines of Python code can be put on one line, separated by a semicolon. The parser will then reformat this code before passing it to the Python interpreter.

Example:

```html
<button onclick="print('Line 1');print('Line 2')"/>
```

### Dynamically from Python Code

The Python version of AddEventListener is modelled directly on Javascript. This allows you to bind any callable Python object (free function or method) or string to an event.

Method 1:

```python
element = document.GetElementById('button')
element.AddEventListener('click', "print('Line 1');print('Line 2')", True)
```

Method 2:

```python
def OnClick():
  for i in range(10):
    print('Line ' + str(i))

element = document.GetElementById('button')
element.AddEventListener('click', OnClick, True)
```
