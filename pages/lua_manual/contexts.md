---
layout: page
title: Contexts
parent: lua_manual
next: events
---

### Interface

- [Context Lua API reference](api_reference.html#Context)
- [Context C++ manual](../cpp_manual/contexts.html)

All properties and methods that are available for contexts are described in detail in the API reference. The context-specific interface contains a subset of the C++ interface, refer there for the full documentation.

#### Retrieving documents

The `documents` property on the context is a proxy element (Lua table) that can be iterated.

```lua
for i,document in ipairs(context.documents) do
	print('Document ' .. i .. ': ' .. document.title)
end
```

Or it can be used as a dictionary, looking documents up by their ID:

```lua
document = context.documents['highscores']
```

Or accessing documents as attributes on the documents property itself:

```lua
document = context.documents.highscores
```

#### Creating contexts

Contexts can be created in Lua with the `CreateContext()` function on the `rmlui` global. This function takes the name of the context as a string and the dimensions as a `Vector2i` type.

```lua
new_context = rmlui:CreateContext('hud', Vector2i.new(1024, 768))
```

#### Accessing contexts

Existing contexts can be accessed in Lua via the contexts member on the `rmlui` global. They can then be accessed via name or index.

```lua
context = rmlui.contexts['hud']
```

List all contexts:

```lua
for i,context in ipairs(rmlui.contexts) do
	print('Context ' .. i .. ': ' .. context.name)
end
```
