---
layout: page
title: Frequently Asked Questions
---

### How do I bind to events from C++/script?

Use the AddEventListener function, passing in the `Rml::EventId` or the name of the event you want to bind to (without the "on" prefix), the function to call, and whether you want to bind in the capture phase or not.

From C++:

```cpp
class MyListener : public Rml::EventListener
{
public:
	void ProcessEvent(Rml::Event& event)
	{
		printf("Processing event %s", event.GetType().c_str());
	}
}
```

```cpp
   auto my_listener = std::make_unique<MyListener>();
   element = document->GetElementById("my_button");
   element->AddEventListener(Rml::EventId::Click, my_listener.get(), false);
```

### Can I change decorators from script?

It is possible to set decorators by inline style. However, for performance reasons, it is recommended to instead change the element's class to affect which decorators are applied to it.

### How do I set up custom cursors?

You display custom cursors using OS cursor facilities. See [here](cpp_manual/contexts.html#mouse-cursor) for details.
