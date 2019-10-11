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

### Can I change decorators from script?

It is possible to set decorators by inline style. However, for performance reasons, it is recommended to instead change the element's class to affect which decorators are applied to it.

### How do I set up custom cursors?

You display custom cursors using OS cursor facilities. See [here](cpp_manual/contexts.html#mouse-cursor) for details.
