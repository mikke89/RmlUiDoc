---
layout: page
title: Events
parent: python_manual
---

When an event is sent to python, three global variables are set up in the context of the called function.

* `event` - The event object
* `document` - The document in which the event fired
* `self` - The element context in which the event fired

### Event Interface

#### Properties

Python property | Brief description | Equivalent C++ method
--------------- | ----------------- | ---------------------
`current_element`{:.prop} | The current element in the event propagation. | `GetCurrentElement()`
`target_element`{:.prop} | The element the event was originally targeted at. | `GetTargetElement()`
`type`{:.prop} | The type of the event. | `GetType()`
`parameters`{:.prop} | Dictionary style container of all the parameters in the event | `GetParameters()`

#### Methods

Events have a single Python method, `StopPropagation()`, which interrupts the event propagation if allowed by the event (ie, if it is interruptible). 