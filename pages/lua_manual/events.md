---
layout: page
title: Events
parent: lua_manual
---

### Interface

- [Event Lua API reference](api_reference.html#Event)
- [Event C++ manual](../cpp_manual/events.html)

All properties and methods that are available for events are described in detail in the API reference. The event-specific interface is similar to the C++ interface, refer there for the full documentation.


### Global variables

When an event is fired and captured by a Lua script, three global variables are set up in the context of the called function.

- `element` The element context in which the event fired.
- `document` The document in which the event fired.
- `event` The event object.

See usage details in [attaching to events](attaching_to_events.html) Lua documentation.
