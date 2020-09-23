---
layout: page
title: Attaching To Events
parent: lua_manual
next: elements
---

### Statically in RML

The easiest way to attach to events with Lua is to write your code directly into the RML files, using the `on*`{:.attr} attributes. When the event is fired three global variables are set up, `document`, `event` and `element`.

[element](elements.html)  | The element that is currently being processed.
[document](documents.html) | The document the element that is currently being processed belongs to.
[event](events.html) | The event that is currently being processed.

Example:

```html
<button onclick="print('Clicked!')"/>
```

Multiple statements can be called as in normal Lua.

Example:

```html
<button onclick="print('Line 1') print('Line 2')"/>
```

### Dynamically from Lua Code

The Lua version of `AddEventListener` is modeled directly on Javascript. This allows you to bind any callable Lua function or string to an event.

Method 1:

```lua
function Init(document)			
	element = document:GetElementById('button')
	element:AddEventListener('click', "print('Line 1') print('Line 2')", true)
end
```

Method 2:

```lua
function OnClick()
	for i=1,10 do print('Line ' .. i) end
end

function Init(document)			
	element = document:GetElementById('button')
	element:AddEventListener('click', OnClick, true)
end
```
