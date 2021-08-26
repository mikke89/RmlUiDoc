---
layout: page
title: Events
parent: cpp_manual
next: rcss
---

Events are sent to elements to indicate actions that have occurred to that element. RmlUi generates many events internally. The application can also send arbitrary events to elements.

When an event is dispatched to an element, it goes through three distinct phases in the following order.
* Capture phase. Propagating from the root element to the target element's parent.
* Target phase. Target element.
* Bubble phase. Propagating from the target element's parent to the root element. Only executed for certain event types.

An event listener is able to subscribe to specific events on an element and will be notified whenever those events occur. Each event listener is either attached to the bubble phase (default) or the capture phase. If the event listener is reached during the target phase, it is executed regardless of the listener's attached phase. Listeners are executed in the order they were attached to the element. Event listeners can stop further propagation of the event at any stage, however, the event type must be interruptible to stop the propagation.

After all event listeners are executed, the event's default actions can be processed. Default actions are primarily for actions performed internally in the library, and can be prevented by stopping propagation. Any object that derives from `Element` can override the default behavior and add new behavior. The default actions are only processed in specific phases which is defined for each event type.

Events are specified by
* An identifier, `Rml::EventId` such as `EventId::Keydown`.
* A descriptive string name, such as `keydown`{:.evt} or `blur`{:.evt}.
* Whether or not it is interruptible.
* Whether or not it executes the bubble phase.
* During which phases it executes `Element::ProcessDefaultAction()`.
* A dictionary of parameters that further describe the event. For example, the `keydown`{:.evt} event has parameters for identifying the actual key that was pressed and the state of the key modifiers.

See the [event specifications](#event-specifications) below for details of each type, and the [RML event documentation](../rml/events.html) for a description of and a list of parameters for each event.


### Event interface

An event is represented by the `Rml::Event` structure, defined in `RmlUi/Core/Event.h`{:.incl}. A subset of the public interface to the event object is given in the following.

```cpp
enum class EventPhase { None, Capture = 1, Target = 2, Bubble = 4 };

class Event
{
public:
	// Get the current propagation phase.
	Rml::EventPhase GetPhase() const;
	// Get the current element in the propagation.
	Rml::Element* GetCurrentElement() const;
	// Get the target element.
	Rml::Element* GetTargetElement() const;

	// Get the event type.
	const Rml::String& GetType() const;
	// Get the event id.
	EventId GetId() const;
	
	// Stops propagation of the event if it is interruptible, but finish all listeners on the current element.
	void StopPropagation();
	// Stops propagation of the event if it is interruptible, including to any other listeners on the current element.
	void StopImmediatePropagation();

	// Returns the value of one of the event's parameters.
	// @param key[in] The name of the desired parameter.
	// @return The value of the requested parameter.
	template < typename T >
	T GetParameter(const Rml::String& key, const T& default_value);
};
```

The phase of the event, returned by `GetPhase()`, will be one of `EventPhase::Capture`, `EventPhase::Target` and `EventPhase::Bubble`.

The target element, returned by `GetTargetElement()`, is the element the event was originally sent to. The current element, returned by `GetCurrentElement()`, is the element the event is currently being sent to. This may be the target element or one of the target element's ancestors.

The id of the event, such as `EventId::Keydown` and `EventId::Focus`, is returned from `GetId()`. You can also use the equality operator to compare the event with an `EventId`. The event can also be compared to strings, such as `keydown`{:.evt} and `focus`{:.evt} in a similar manner.

You can fetch the parameters of the event with the templated `GetParameter()` function. The exact parameters of each event are detailed in the [event documentation](../rml/events.html).

For event types that can be interrupted, a listener can call the `StopPropagation()` and `StopImmediatePropagation()` functions to stop the event from propagating. The immediate variant will also stop the rest of the listeners on the current element to be executed. If propagation is interrupted, then default actions are not processed.

### Event listeners

Any object that wants to listen for events derives from `Rml::EventListener`, and implements the one required pure virtual function:

```cpp
// Process the incoming event.
virtual void ProcessEvent(Rml::Event& event) = 0;
```

The `ProcessEvent()` function will be called every time a relevant event is sent to an element the listener is subscribed to.

#### Attaching to an element

To subscribe an event listener to an element, call the `AddEventListener()` function on the element to attach to.

```cpp
// Adds an event listener to this element.
// @param[in] event Event to attach to.
// @param[in] listener The listener object to be attached.
// @param[in] in_capture_phase True to attach in the capture phase, false in bubble phase.
void AddEventListener(const Rml::String& event,
                      Rml::EventListener* listener,
                      bool in_capture_phase = false);
```

The function takes the following parameters:

* `event`: The string name of the event the listener wants to attach to, for example "keydown", "focus", etc.
* `listener`: The event listener object to attach.
* `in_capture_phase`: If true, the event listener will receive the event in the capture phase, otherwise, in the bubbling phase. See the RML event documentation for more information. 

Note that the event listener must be kept alive until the listener is removed or the element is destroyed.
Be aware that documents closed with `ElementDocument::Close()` are not actually destroyed until the next call to `Context::Update()` or `Rml::Shutdown()`.

#### Detaching from an element

To unsubscribe an event listener from an element, call the `RemoveEventListener()` function on the element:

```cpp
// Removes an event listener from this element.
// @param[in] event Event to detach from.
// @param[in] listener The listener object to be detached.
// @param[in] in_capture_phase True to detach from the capture phase, false from the bubble phase.
void RemoveEventListener(const Rml::String& event,
                         Rml::EventListener* listener,
                         bool in_capture_phase = false);
```

### Sending events

The application can send an arbitrary event to an element through the `DispatchEvent()` function on `Rml::Element`.

```cpp
// Sends an event to this element.
// @param[in] event Name of the event in string form.
// @param[in] parameters The event parameters.
// @param[in] interruptible True if the propagation of the event be stopped.
void DispatchEvent(const Rml::String& event,
                   const Rml::Dictionary& parameters);
```

The event will be created and sent through the standard event loop. The following example sends a "close" event to an element:

```cpp
Rml::Dictionary parameters;
parameters["source"] = "user";

element->DispatchEvent("close", parameters);
```

### Custom events

Events are instanced through an event instancer similarly to contexts. The instancer can be overridden with a custom instancer if a custom event is required; this is generally only needed to integrate a scripting language into RmlUi.

A custom event inherits from `Rml::Event`. There are no virtual functions to be overridden.

#### Creating a custom event instancer

A custom event instancer needs to be created and registered with the RmlUi factory in order to have custom events instanced. A custom event instancer derives from `Rml::EventInstancer` and implements the required pure virtual functions:

```cpp
// Instance an event object.
// @param[in] target Target element of this event.
// @param[in] id EventId of this event.
// @param[in] name Name of this event.
// @param[in] parameters Additional parameters for this event.
// @param[in] interruptible If the event propagation can be stopped.
virtual Rml::EventPtr InstanceEvent(Rml::Element* target,
										   Rml::EventId id,
                                           const Rml::String& name,
                                           const Rml::Dictionary& parameters,
                                           bool interruptible) = 0;

// Releases an event instanced by this instancer.
// @param[in] event The event to release.
virtual void ReleaseEvent(Event* event) = 0;
```

`InstanceEvent()` will be called whenever the factory is called upon to instance an event. The parameters to the function are:

* `target`: The element the event is begin targeted at.
* `id`: The EventId of the event (EventId::Keydown, EventId::Focus, etc).
* `name`: The name of the event ("keydown", "focus", etc).
* `parameters`: The parameters to the event as a dictionary.
* `interruptible`: True if the event can be interrupted (ie, prevented from propagating throughout the entire event cycle), false if not. 

If `InstanceEvent()` is successful, return the new event wrapped in an `EventPtr` which is a unique pointer with a custom deleter. Otherwise, return nullptr to indicate an instancing error.

`ReleaseEvent()` will be called when an event instanced through the instancer is no longer required by the system. It should be deleted appropriately.

#### Registering an instancer

To register a custom instancer with RmlUi, call the `RegisterEventInstancer()` function on the RmlUi factory (`Rml::Factory`) after RmlUi has been initialised.

```cpp
// Registers an instancer for all events.
// @param[in] instancer The instancer to be called.
// @return The registered instanced on success, NULL on failure.
static Rml::EventInstancer* RegisterEventInstancer(Rml::EventInstancer* instancer);
```

Like for other instancers, it is the user's responsibility to manage the lifetime of the instancer. Thus, it must be kept alive until after the call to `Rml::Shutdown()`, and then cleaned up by the user.

### Inline events

Event responses can be specified as element attributes inside RML, similarly to HTML. For example, in the following RML fragment a response is given to the `click`{:.evt} event.

```html
<rml>
	<head>
	</head>
	<body>
		<button onclick="game.start()">Start Game</button>
...
```

Notice the `on`{:.attr} prefix before the event name of `click`{:.evt}. All event bindings from RML are prefixed this way.

RmlUi sends inline events to event listener proxy objects that are created by the application. An application must therefore register a custom event listener instancer to have an opportunity to interpret the events.

#### Creating a custom event listener instancer

A custom event listener instancer derives from `Rml::EventListenerInstancer`. The following pure virtual functions must be implemented:

```cpp
// Instance an event listener object.
// @param value Value of the inline event.
// @param element Element that triggers this call to the instancer.
// @return An event listener which will be attached to the element.
// @lifetime The returned event listener must be kept alive until the call to `EventListener::OnDetach` on the
//           returned listener, and then cleaned up by the user. The detach function is called when the listener
//           is detached manually, or automatically when the element is destroyed.
virtual Rml::EventListener* InstanceEventListener(const Rml::String& value, Rml::Element* element) = 0;
```

`InstanceEventListener()` will be called during RML parsing whenever the factory needs to find an event listener for an inline event. The parameter value will be the raw event response string as specified in the RML, eg. `game.start()`.

Once the event listener instancer is created, it can be passed to the factory.

```cpp
// Register the instancer to be used for all event listeners, or nullptr to clear an existing instancer.
// @lifetime The instancer must be kept alive until after the call to Rml::Shutdown, or until a new instancer is set.
void Rml::Factory::RegisterEventListenerInstancer(Rml::EventListenerInstancer* instancer);
```

Then all encountered inline event declarations will be passed to the instancer. Only a single instancer can be active at any one time.

### Custom event types

Custom events can be dispatched without any particular setup. They will then automatically be assigned a unique `EventId` and given the default specification: `interruptible: true, bubbles: true, default_action_phase: None`. 

To provide a custom specification for a new event, first call the method:
```cpp
EventId Rml::RegisterEventType(const String& type, bool interruptible, bool bubbles, DefaultActionPhase default_action_phase);
```
After this call, any usage of this type will use the provided specification by default. The returned `EventId` can be used to dispatch events instead of the type string.


### Event specifications

The following lists the specifications of all built-in events. Also see the parameters available for each event type in the [RML event documentation](../rml/events.html).

|  `EventId` id  |  `String` type  | `bool` interruptible  | `bool` bubbles |   `DefaultActionPhase` default_action  |
|------------------------|-----------------|-------|-------|---------------------------------------|
| Mousedown    | mousedown     | true  | true  | TargetAndBubble |
| Mousescroll  | mousescroll   | true  | true  | TargetAndBubble |
| Mouseover    | mouseover     | true  | true  | Target          |
| Mouseout     | mouseout      | true  | true  | Target          |
| Focus        | focus         | false | false | Target          |
| Blur         | blur          | false | false | Target          |
| Keydown      | keydown       | true  | true  | TargetAndBubble |
| Keyup        | keyup         | true  | true  | TargetAndBubble |
| Textinput    | textinput     | true  | true  | TargetAndBubble |
| Mouseup      | mouseup       | true  | true  | TargetAndBubble |
| Click        | click         | true  | true  | TargetAndBubble |
| Dblclick     | dblclick      | true  | true  | TargetAndBubble |
| Load         | load          | false | false | None            |
| Unload       | unload        | false | false | None            |
| Show         | show          | false | false | None            |
| Hide         | hide          | false | false | None            |
| Mousemove    | mousemove     | true  | true  | None            |
| Dragmove     | dragmove      | true  | true  | None            |
| Drag         | drag          | false | true  | Target          |
| Dragstart    | dragstart     | false | true  | Target          |
| Dragover     | dragover      | true  | true  | None            |
| Dragdrop     | dragdrop      | true  | true  | None            |
| Dragout      | dragout       | true  | true  | None            |
| Dragend      | dragend       | true  | true  | None            |
| Handledrag   | handledrag    | false | true  | None            |
| Resize       | resize        | false | false | None            |
| Scroll       | scroll        | false | true  | None            |
| Animationend | animationend  | false | true  | None            |
| Transitionend| transitionend | false | true  | None            |
|              |		       |       |                           |
| Change       | change        | false | true  | None            |
| Submit       | submit        | true  | true  | None            |
| Tabchange    | tabchange     | false | true  | None            |
| Columnadd    | columnadd     | false | true  | None            |
| Rowadd       | rowadd        | false | true  | None            |
| Rowchange    | rowchange     | false | true  | None            |
| Rowremove    | rowremove     | false | true  | None            |
| Rowupdate    | rowupdate     | false | true  | None            |


