---
layout: page
title: Frequently Asked Questions
---

### How do I bind to events from C++/script?

Use the AddEventListener function, passing in the name of the event you want to bind to (without the "on" prefix), the function to call and whether you want to bind in the capture phase or not.

From C++:

```cpp
class MyListener : public {{page.lib_ns}}::Core::EventListener
{
public:
	void ProcessEvent({{page.lib_ns}}::Core::Event& event)
	{
		printf("Processing event %s", event.GetType().CString());
	}
}
```

```cpp
   my_listener = new MyListener();
   element = document->GetElementById("element5");
   element->AddEventListener("click", my_listener, false);
```

From Python:

```
	element = document.GetElementById('element5')
	element.AddEventListener('click', 'MyFunction(self, document)', False)
```

### Can I change decorators from script?

Not directly, however you can change the element's class which will affect which decorators are applied to it.

### How do I set up custom cursors?

You can load documents as cursor objects into your context with the `LoadMouseCursor()` function. The first cursor to be loaded into a context is the default cursor; if an element does not specify a cursor override, then that is the cursor that will be visible. To override the default cursor, set the cursor property of your element. See [Cursors](rcss/user_interface.html#cursors-the-cursor-property) for full details.
