---
layout: page
title: User input
parent: cpp_manual
next: interfaces
---

RmlUi does not read user input directly, instead, it requires the application to feed its contexts with input events. Each context will process the input it is provided with and dispatch events as appropriate.

### Key modifiers

Most of the input functions take the parameter `key_modifier_state`. This is a bitmask of active key modifiers; keys such as Control, Alt, etc, as well as the lock keys. This is used to generate the key modifier parameters on any events that are spawned, so is entirely optional. If you don't want or need the key modifier parameters on your input events, feel free to pass `0`{:.value} for the `key_modifier_state` into all the input functions you call.

The bitmask should be configured using the enumeration `Rml::Input::KeyModifier`, detailed below:

```cpp
enum KeyModifier
{
	KM_CTRL = 1 << 0,	// Set if at least one Ctrl key is depressed.
	KM_SHIFT = 1 << 1,	// Set if at least one Shift key is depressed.
	KM_ALT = 1 << 2,	// Set if at least one Alt key is depressed.
	KM_META = 1 << 3,	// Set if at least one Meta key (the command key) is depressed.
	KM_CAPSLOCK = 1 << 4,	// Set if caps lock is enabled.
	KM_NUMLOCK = 1 << 5,	// Set if num lock is enabled.
	KM_SCROLLLOCK = 1 << 6	// Set if scroll lock is enabled.
};
```

See the documentation on [RML events](../rml/events.html#events) for a specification of the key modifier events parameters.

### Mouse input

Different aspects of mouse input are given to a context through a variety of functions, detailed below.

#### Mouse movement

Call the `ProcessMouseMove()` function on a context to inform the context that the position of the mouse cursor within the context has changed.

```cpp
// Sends a mouse movement event into this context.
// @param[in] x The x-coordinate of the mouse cursor.
// @param[in] y The y-coordinate of the mouse cursor.
// @param[in] key_modifier_state The state of key modifiers.
// @return True if the mouse is not interacting with any elements in the context, otherwise false.
bool ProcessMouseMove(int x, int y, int key_modifier_state);
```

Note that the x and y coordinates are in pixel offsets from the top-left of the context. If the mouse cursor has moved since the previous call to `ProcessMouseMove()` then the `mousemove`{:.evt} will be submitted to the element being hovered over. Regardless of mouse movement, the hover chain will always be updated to account for any elements that may have changed under the mouse cursor. Then any of the following events may be generated, targeted at the appropriate elements:

* `mousemove`{:.evt}
* `mouseover`{:.evt}
* `mouseout`{:.evt}
* `dragstart`{:.evt}
* `drag`{:.evt}
* `dragover`{:.evt}
* `dragout`{:.evt}

After the call to `ProcessMouseMove()` the mouse cursor is considered active. When the cursor is active every call to the context's `Update()` function will update the hover states of the elements, regardless of mouse movement. This ensures that any elements that have been moved, removed, or added, have their hover states changed appropriately. See `ProcessMouseLeave()` to [deactivate the mouse cursor](#mouse-cursor-leave) and prevent `Update()` from updating the hover state of elements.

#### Mouse buttons

Call `ProcessMouseButtonDown()` and `ProcessMouseButtonUp()` on a context to to inform the context when a mouse button is pressed or released.

```cpp
// Sends a mouse-button down event into this context.
// @param[in] button_index The index of the button that was pressed; 0 for the left button, 1 for right, and 2 for middle button.
// @param[in] key_modifier_state The state of key modifiers.
// @return True if the mouse is not interacting with any elements in the context, otherwise false.
bool ProcessMouseButtonDown(int button_index, int key_modifier_state);

// Sends a mouse-button up event into this context.
// @param[in] button_index The index of the button that was pressed; 0 for the left button, 1 for right, and 2 for middle button.
// @param[in] key_modifier_state The state of key modifiers.
// @return True if the mouse is not interacting with any elements in the context, otherwise false.
bool ProcessMouseButtonUp(int button_index, int key_modifier_state);
```

`ProcessMouseButtonDown()` may generate any of the following events:

* `focus`{:.evt}
* `blur`{:.evt}
* `mousedown`{:.evt}
* `dblclick`{:.evt}
* `mousescroll`{:.evt}

Middle mouse button may initiate [autoscroll mode](contexts.html#autoscroll). In this case, it will first submit a `mousescroll`{:.evt} event targeted at the hover element. If this event is not stopped from propagation, autoscroll will be initiated on the closest scrollable ancestor. However, if the event is stopped, the autoscroll mode will not be initiated.

`ProcessMouseButtonUp()` may generate:

* `mouseup`{:.evt}
* `click`{:.evt}
* `dragdrop`{:.evt}
* `dragend`{:.evt}

#### Mouse wheel

If you want to send mouse-wheel events to your documents, call the `ProcessMouseWheel()` function on your contexts as appropriate.

```cpp
// Sends a mousescroll event into this context, and scrolls the document unless the event was stopped from propagating.
// @param[in] wheel_delta The mouse-wheel movement this frame, with positive values being directed right and down.
// @param[in] key_modifier_state The state of key modifiers (shift, control, caps-lock, etc) keys; this should be generated by ORing together members of the Input::KeyModifier enumeration.
// @return True if the event was not consumed (ie, was prevented from propagating by an element), false if it was.
bool ProcessMouseWheel(Vector2f wheel_delta, int key_modifier_state);
```

`ProcessMouseWheel()` will generate a `mousescroll`{:.evt} event targeted at the hover element. If this event is not stopped from propagation, the nearest scrollable element will be scrolled according to the delta value. However, if the event is stopped, the actual scroll will be cancelled. Normally, scrolling with the mouse wheel initiates smooth scrolling, however, this can be [configured on the context](contexts.html#smooth-scrolling).

The nearest scrollable element can be controlled using the `overscroll-behavior`{:.prop} property.


### Mouse cursor leave

In some situations the mouse cursor may leave the active window, or should otherwise be disabled such as when changing the input device to a controller. Then `ProcessMouseLeave()` can be called to remove the hovered state from all elements. In addition, this also stops the call to the context's `Update()` function from automatically hovering elements, which is particularly useful when using a controller input.

```cpp
// Tells the context the mouse has left the window. This removes any hover state from all elements and prevents 'Update()' from setting the hover state for elements under the mouse.
// @return True if the mouse is not interacting with any elements in the context (see 'IsMouseInteracting'), otherwise false.
bool ProcessMouseLeave();
```

The [mouse is considered active](#mouse-movement) again after the next call to `ProcessMouseMove()`.


#### Mouse cursor interaction

The following can provide a hint on whether or not the mouse cursor is currently interacting with any documents in the context, as a result of previously submitted `ProcessMouse...()` commands.

```cpp
// Returns a hint on whether the mouse is currently interacting with any elements in this context.
// @return True if the mouse hovers over or has activated an element in this context, otherwise false.
bool IsMouseInteracting() const;
```

Note that interaction is determined irrespective of background and opacity. See the [`pointer-events`{:.prop}](../rcss/user_interface.html#pointer-events) property to disable interaction for specific elements.

### Key input

The key input functions use the `KeyIdentifier` enumeration found in `<RmlUi/Core/Input.h>`{:.incl}; refer to that file for the possible values. They are modeled after the Windows virtual key codes (the VK_* enumeration), so should be familiar to Windows developers. Any confusing enumeration names are explained in the comments.

RmlUi makes a distinction between key input and text input; key input (specified by the `ProcessKeyDown()` and `ProcessKeyUp()` functions) refers to actual physical key presses, while text input refers to characters being generated from user input. Depending on user locale, it may take more than one physical key stroke to generate a single character of text input. At present, RmlUi offers no translation between key input and text input; that is left to the application.

Call the following functions on a context to inform the context of key presses or releases:

```cpp
// Sends a key down event into this context.
// @param[in] key_identifier The key pressed.
// @param[in] key_modifier_state The state of key modifiers.
// @return True if the event was not consumed, false if it was.
bool ProcessKeyDown(Rml::Input::KeyIdentifier key_identifier, int key_modifier_state);

// Sends a key up event into this context.
// @param[in] key_identifier The key released.
// @param[in] key_modifier_state The state of key modifiers.
// @return True if the event was not consumed, false if it was.
bool ProcessKeyUp(Rml::Input::KeyIdentifier key_identifier, int key_modifier_state);
```

`ProcessKeyDown()` will generate a `keydown`{:.evt} event targeted at the current focus element (if an element is in focus). `ProcessKeyUp()` will likewise generate the `keyup`{:.evt} event.

### Text input

RmlUi takes text input as `Rml::Character` (32-bit Unicode code points), `char` (ASCII), or UTF-8 strings. To notify RmlUi of a text input occurrence, use the following functions:

```cpp
// Sends a single unicode character as text input into this context.
// @param[in] character The unicode code point to send into this context.
// @return True if the event was not consumed (ie, was prevented from propagating by an element), false if it was.
bool ProcessTextInput(Character character);
// Sends a single ascii character as text input into this context.
bool ProcessTextInput(char character);
// Sends a string of text as text input into this context.
// @param[in] string The UTF-8 string to send into this context.
// @return True if the event was not consumed (ie, was prevented from propagating by an element), false if it was.
bool ProcessTextInput(const String& string);
```

These functions will generate a `textinput`{:.evt} event targeted at the context's current focus element (if there is one).

### Touch input

Touch input is submitted to a context similarly to mouse input. Each call processes a provided list of touch points.

```cpp
/// Process touch movements for this context.
/// @param[in] touches List of touches.
/// @param[in] key_modifier_state The state of key modifiers (shift, control, caps-lock, etc.) keys;
/// this should be generated by ORing together members of the Input::KeyModifier enumeration.
/// @return True if no touch points are interacting with any elements in the context, otherwise false.
bool ProcessTouchMove(const TouchList& touches, int key_modifier_state);
/// Process touch start (press) for this context.
bool ProcessTouchStart(const TouchList& touches, int key_modifier_state);
/// Process touch end (release) for this context.
bool ProcessTouchEnd(const TouchList& touches, int key_modifier_state);
/// Process touch cancel for this context.
bool ProcessTouchCancel(const TouchList& touches);
```

A list of `Rml::Touch` specifies each touch point to be processed, defined as follows.

```cpp
using TouchId = uintptr_t;
struct Touch {
	TouchId identifier;
	Vector2f position;
};
using TouchList = Vector<Touch>;
```

Here, `identifier` is a user-specified identifier for the given touch. Multiple touch points should use different identifiers to be able to track them separately. The touch `position` should be given in the RmlUi pixel coordinate system, whose origin is at the top-left of the window.

While a finger is down, scroll containers are scrolled immediately. On release, the motion may continue with inertial scrolling. Inertia is currently only applied to a single scroll target at a time.

Currently, RML events for touch are not yet implemented, and so are not dispatched to elements.

Some of the built-in backends support touch input. For some backends, touch events can be simulated from mouse events, see the [CMake build options](building_with_cmake.html#backend-options) for details.

### Sample input processing

The included backends (found under your RmlUi installation at `/Backends/`{:.path}) contain sample implementations of input processing for multiple supported platforms, including key conversion to RmlUi (see `/Backends/RmlUi_Platform_<...>.cpp`{:.path}).
