---
layout: page
title: Custom elements
parent: cpp_manual
next: hidden_elements
---

If you need special functionality on an element that you can't easily manage through the event system, you have the option of creating a custom element. Custom elements derive directly from the core Element class definition and are created through a custom element instancer. Custom elements can:

* Respond to property and attribute changes.
* Manage the layout of hidden internal elements.
* Execute custom update or rendering code.
* Respond to events inline.
* Respond to descendant add / remove events. 

### Creating a custom element

All custom elements are classes derived (not necessarily directly) from `Rml::Element`. The constructor for Element takes one parameter, the tag of the element; a derived element's constructor can either pass a constant string down to the base constructor, or take a string themselves to pass down.

The virtual functions that can be overridden in a custom element are:

```cpp
// Returns the baseline of the element, in pixels offset from the bottom of the element's content area.
// @return The element's baseline. A negative baseline will be further 'up' the element, a positive on further 'down'.
virtual float GetBaseline() const;

// Gets the intrinsic dimensions of this element, if it is of a type that has an inherent size.
// @param[out] dimensions The dimensions to size, if appropriate.
// @param[out] ratio The intrinsic ratio (width/height), if appropriate.
// @return True if the element has intrinsic dimensions, false otherwise.
virtual bool GetIntrinsicDimensions(Rml::Vector2f& dimensions, float& ratio);

// Called when an emitted event propagates to this element, for event types with default actions.
// Note: See 'EventSpecification' for the events that call this function and during which phase.
// @param[in] event The event to process.
virtual void ProcessDefaultAction(Rml::Event& event);

// Called during the update loop after children are updated.
virtual void OnUpdate();
// Called during render after backgrounds, borders, decorators, but before children, are rendered.
virtual void OnRender();

// Called when attributes on the element are changed.
// @param[in] changed_attributes The attributes changed on the element.
virtual void OnAttributeChange(const Rml::AttributeNameList& changed_attributes);
// Called when properties on the element are changed.
// @param[in] changed_properties The properties changed on the element.
virtual void OnPropertyChange(const Rml::PropertyIdSet& changed_properties);

// Called when a child node has been added up to two levels below us in the hierarchy.
// @param[in] child The element that has been added. This may be this element.
virtual void OnChildAdd(Rml::Element* child);
// Called when a child node has been removed up to two levels below us in the hierarchy.
// @param[in] child The element that has been removed. This may be this element.
virtual void OnChildRemove(Rml::Element* child);

// Gets the markup and content of the element.
// @param[out] content The content of the element.
virtual void GetInnerRML(Rml::String& content) const;
// Returns the RML of this element and all children.
// @param[out] content The content of this element and those under it, in XML form.
virtual void GetRML(Rml::String& content);
```

#### Layout

A custom element can override the `GetIntrinsicDimensions()` function if it wants to be laid out as a replaced element. Replaced elements are elements with intrinsic dimensions that can be positioned like inline or block content. Examples of replaced elements are images and form controls.

```cpp
// Gets the intrinsic dimensions of this element, if it is of a type that has an inherent size.
// @param[out] dimensions The dimensions to size, if appropriate.
// @param[out] ratio The intrinsic ratio (width/height), if appropriate.
// @return True if the element has intrinsic dimensions, false otherwise.
virtual bool GetIntrinsicDimensions(Rml::Vector2f& dimensions, float& ratio);
```

If a custom element is to be a replaced element, it should override this function and return true. The actual intrinsic dimensions of the element should be put into the dimensions parameter. If the element has an intrinsic ratio, this can be set on the ratio parameter, either in addition or instead of the dimensions parameter. This function will be called every time the element is laid out, so the parameters can be dynamic values. The default element returns false.

A custom replaced element (ie, one with intrinsic dimensions) can override the `GetBaseline()` function if it wants to change its reference point for horizontal positioning on a line.

```cpp
// Returns the baseline of the element, in pixels offset from the bottom of the element's content area.
// @return The element's baseline. A negative baseline will be further 'up' the element, a positive on further 'down'.
virtual float GetBaseline() const;
```

The `GetBaseline()` function returns the pixel offset from the bottom of the element's content area that neighbouring text should, by default, line their baselines up with. This will only affect the element's positioning if it is placed inline.

#### Default actions

A custom element can override the `ProcessDefaultAction()` function to intercept all event types with a default action, sent to this element or one of its descendants. The default actions follow the normal event phases, but are only executed in the phase according to their `default_action_phase` which is defined for each event type. If an event is cancelled with `Event::StopPropagation()`, then the default action is not performed unless already executed. See the [event specifications](events.html#event-specifications) for details of each event type, and for which phases the default action is called.

Note that the element may receive events targeted at one of its children. Be sure to check the target element of the event and the event type.

**Important**: You must remember to call the base class's `ProcessDefaultAction()` function with any unprocessed events! The base element responds to many events in its `ProcessDefaultAction()` function, and all manner of strange behaviour may result if you don't do this.

```cpp
// Called when an emitted event propagates to this element, for event types with default actions.
// @param[in] event The event to process.
virtual void ProcessDefaultAction(Rml::Event& event);
```

#### Hooks into update and render loops

A custom element can override the `OnUpdate()` or `OnRender()` functions to hook functionality into the update or render loops.

The `OnUpdate()` function is called at the very beginning of the base element's update function. There is no need to call the base element's `OnUpdate()` function if you do not wish to.

```cpp
// Called during the update loop after children are updated.
virtual void OnUpdate();
```
Note that the element's property definition and computed values will be calculated after the call to `OnUpdate()`. Thus, it is safe to set new properties and expect them to be properly set during the current update loop. However, querying any of the element's computed values will return the ones calculated during the previous update loop.

The `OnRender()` function is called from the base element's render loop after the following has occurred:

* Descendant elements in the element's stacking context with a z-index of lower than 0 have been rendered.
* The clipping region has been set for the element (if appropriate).
* The elements background, border and all appropriate decorators have been rendered. 

There is no need to call the base element's `OnRender()` function if you do not wish to. Note that most custom rendering can be accomplished through the use of custom decorators; this is recommended rather than overriding `OnRender()` for reusability.

```cpp
// Called during render after backgrounds, borders, decorators, but before children, are rendered.
virtual void OnRender();
```

#### Changes to properties or attributes

A custom element can override the `OnAttributeChange()` or `OnPropertyChange()` functions to respond to changes to its attributes or properties.

`OnAttributeChange()` is called whenever an attribute is added, removed or redefined. The names of the changed attributes are passed into the function in the 'changed_attributes' variable, which is a dictionary of name and values. To check if a specific attribute has been altered, look for its presence in the list with the `find()` function.

```cpp
// Called when attributes on the element are changed.
// @param[in] changed_attributes The attributes changed on the element.
virtual void OnAttributeChange(const Rml::AttributeNameList& changed_attributes);
```

`OnPropertyChange()` is called whenever the value of a property (or group of properties) is changed. The names of the changed properties are passed into the function in the `changed_properties` variable, which is a set of `PropertyId`s.

```cpp
// Called when properties on the element are changed.
// @param[in] changed_properties The properties changed on the element.
virtual void OnPropertyChange(const Rml::PropertyIdSet& changed_properties);
```

**Important**: If you override either of these functions, you must remember to call the base class's corresponding function! As with `ProcessDefaultAction()`, the base element responds to many attribute and property changes, and all manner of strange behaviour may result if you don't do this.

#### Hierarchy changes

A custom element can override the `OnChildAdd()` or `OnChildRemove()` functions to respond to changes in the element's hierarchy. When an element is added or removed from another, the appropriate function is called on itself and its nearby ancestors immediately. Note that for performance reasons, only the nodes up to two levels up in the hierarchy are notified.

```cpp
// Called when a child node has been added up to two levels below us in the hierarchy.
// @param[in] child The element that has been added. This may be this element.
virtual void OnChildAdd(Rml::Element* child);

// Called when a child node has been removed up to two levels below us in the hierarchy.
// @param[in] child The element that has been removed. This may be this element.
virtual void OnChildRemove(Rml::Element* child);
```

#### RML generation

A custom element can override the `GetRML()` and `GetInnerRML()` function if the default RML generation functions are inadequate. This is generally not needed, unless an element rearranges its child elements internally, or makes heavy use of custom XML node handlers; in this case, the default functions may generate nonsensical RML.

`GetInnerRML()` is meant to return the internal RML of the element; ie, only the RML needed to generate the element's content, not the element itself. By default, it calls `GetRML()` on all of its DOM children and concatenates the result.

`GetRML()` is meant to return the RML required to generate the entire element. This therefore includes the element's tag and all of its attributes as well as all of its descendant's RML. By default, it generates its open tag, appends to that the the result of `GetInnerRML()`, and finally appends its closing tag.

```cpp
// Gets the markup and content of the element.
// @param[out] content The content of the element.
virtual void GetInnerRML(Rml::String& content) const;

// Returns the RML of this element and all children.
// @param[out] content The content of this element and those under it, in XML form.
virtual void GetRML(Rml::String& content);
```

### Creating a custom element instancer

In order to have a custom element created through the RmlUi factory, an instancer for the element needs to be registered with the factory against the appropriate RML tag names. An element instancer is responsible for creating and destroying its elements when required, and also destroying itself when RmlUi is shut down.

A custom element instancer needs to be derived from `Rml::ElementInstancer`, and implement the required pure virtual methods:

```cpp
// Instances an element given the tag name and attributes.
// @param[in] parent The element the new element is destined to be parented to.
// @param[in] tag The tag of the element to instance.
// @param[in] attributes Dictionary of attributes.
// @return A unique pointer to the instanced element.
virtual Rml::ElementPtr InstanceElement(Rml::Element* parent,
                                              const Rml::String& tag,
                                              const Rml::XMLAttributes& attributes) = 0;

// Releases an element instanced by this instancer.
// @param[in] element The element to release.
virtual void ReleaseElement(Rml::Element* element) = 0;
```

`InstanceElement()` will be called whenever the factory is called upon to instance an element with a tag that the instancer was registered against. The parameters to the function are:

* `parent`: The element that the new element will be parented to if it is created successfully; you do not need to actually do the parenting! This will only be non-null if the element is instanced from RML.
* `tag`: The string that whoever is creating the element wants the element's tag to be; due to the way elements are constructed through the factory, this may not be one of the tags the instancer was registered against. It is recommended you pass this through to the element to be its tag name, but this is not required.
* `attributes`: The attributes defined on the element's tag in RML or passed into the factory. You do not need to set these attributes on the element yourself; that will be done automatically if the instancing is successful. You only need to use these if element instancing is dependent on the values (for example, the instancer for `input`{:.tag} elements instances different types depending on the value of the `type`{:.attr} attribute). 

If `InstanceElement()` is successful, return the new element wrapped in an `ElementPtr` (unique element). Otherwise, return nullptr to indicate an instancing error.

`ReleaseElement()` will be called after an element has been released from its owner, that is, its `ElementPtr` is destroyed or reset. The element should be deleted appropriately.

#### Registering an instancer

To register a custom instancer with RmlUi, call the `RegisterElementInstancer()` function on the RmlUi factory (`Rml::Factory`) after RmlUi has been initialised.

```cpp
// Make sure custom_instancer is kept alive until after the call to Rml::Shutdown
auto custom_instancer = std::make_unique<ElementInstancerCustom>();
Rml::Factory::RegisterElementInstancer("custom", custom_instancer.get());
```

The first parameter to `RegisterElementInstancer()` is the tag name the instancer is bound to. In the above example, the custom instancer will be called to instance an element whenever an element with the tag 'custom' is encountered while parsing an RML stream, or as otherwise required by the factory. You can register an instancer as many times as you like with the factory against different tag names.

The library takes a non-owning pointer to the instancer. Thus, the instancer must be kept alive until after the call to `Rml::Shutdown`, and then cleaned up by the user.

#### Using a generic instancer

If a custom element does not require any special behaviour from its instancer, the easiest way to generate an instancer for it is to use the templated `ElementInstancerGeneric`. Instead of deriving your own instancer class, simply construct a new `Rml::ElementInstancerGeneric` templated to the type of the custom element you'd like to instance, and register it with the factory as you would a normal instancer.

```cpp
// Make sure custom_instancer is kept alive until after the call to Rml::Shutdown
auto custom_instancer = std::make_unique< Rml::ElementInstancerGeneric< CustomElement > >();
Rml::Factory::RegisterElementInstancer("custom", custom_instancer.get());
```

The only requirement on the element type that it is templated to is that the constructor take a string (the tag name) like the base element.

### Custom XML node handling

For some complex custom elements, the RML required to generate the element is not indicative of the actual internal hierarchy. For example, columns in a data grid element are specified by `<col>`{:.tag} tags immediately beneath the `<datagrid>`{:.tag} tag. If the standard XML parsing was being executed, an element would be instanced and parented to the data grid for each column tag - but this isn't what is wanted. So a custom XML node handler is used for data grids that processes the column tag differently.

Node handlers are registered against RML tag names. When an RML file is being parsed, the XML parser maintains a stack of node handlers. Whenever a new tag is encountered, the parser checks if a specific node handler is registered against that tag; if so, that handler is pushed onto the stack and takes over the parsing until its associated tag is closed. If no handler is associated with a particular element, the current node handler continues parsing.

#### Creating a custom XML node handler

Custom node handlers derive from the `Rml::XMLNodeHandler` class and implement the pure virtual functions:

```cpp
// Called when a new element tag is opened.
// @param parser The parser executing the parse.
// @param name The XML tag name.
// @param attributes The tag attributes.
// @return The new element, may be NULL if no element was created.
virtual Rml::Element* ElementStart(Rml::XMLParser* parser,
                                            const Rml::String& name,
                                            const Rml::XMLAttributes& attributes) = 0;

// Called when an element is closed.
// @param parser The parser executing the parse.
// @param name The XML tag name.
virtual bool ElementEnd(Rml::XMLParser* parser,
                        const Rml::String& name) = 0;

// Called for element data.
// @param parser The parser executing the parse.
// @param data The element data.
virtual bool ElementData(Rml::XMLParser* parser,
                         const Rml::String& data) = 0;
```

`ElementStart()`, `ElementEnd()` and `ElementData()` are called on the node handler for the appropriate XML parse events that occur while it is the active node handler. A self-closing tag will result in a call to `ElementEnd()` immediately after `ElementStart()`. `ElementData()` is called when loose non-whitespace data is encountered between two tags.

Each of these functions is passed a pointer to the XML parser running the parse. From the parser the current parse frame can be requested with the `GetParseFrame()` function; the parse frame object contains the current element and tag being processed, as well as the active node handler.

```cpp
struct ParseFrame
{
	// Tag being parsed.
	Rml::String tag;

	// Element representing this frame.
	Rml::Element* element;

	// Handler used for this frame.
	XMLNodeHandler* node_handler;

	// The default handler used for this frame's children.
	XMLNodeHandler* child_handler;
};
```

`ElementStart()` is called with the name and attributes of the opening tag. If the node handler creates a new element and wants it on the top parse frame, it should return the element. Otherwise, it should return NULL to keep the current element on top of the parse frame stack. This is useful if the node handler creates internal elements for the current element, but doesn't want any further parsing executed on them.

If the node handler wants to change the node handler for the new element, it can push a new handler onto the XML parser's stack using `PushHandler()` or `PushDefaultHandler()` from `ElementStart()`. The default handler will instance elements as described previously in the documentation.

```cpp
// Pushes an element handler onto the parse stack for parsing child elements.
// @param[in] tag The tag the handler was registered with.
// @return True if an appropriate handler was found and pushed onto the stack, false if not.
bool PushHandler(const Rml::String& tag);

// Pushes the default element handler onto the parse stack.
void PushDefaultHandler();
```

If it doesn't call either of these methods, it will remain the node handler for any child elements it creates.
Registering a custom node handler

Register a custom node handler with RmlUi's XML parser with the static `RegisterNodeHandler()` function on `Rml::XMLParser`. You can register the same handler multiple times with the parser against different tag names. `RegisterNodeHandler()` takes shared ownership of the handler, thus, users do not need to store their own copy when they are done.

```cpp
// Registers a custom node handler to be used to a given tag.
// @param[in] tag The tag the custom parser will handle.
// @param[in] handler The custom handler.
// @return The registered XML node handler.
static Rml::XMLNodeHandler* RegisterNodeHandler(const Rml::String& tag,
                                                         SharedPtr<Rml::XMLNodeHandler> handler);
```

#### Samples

Custom XML node handlers are used extensively by the included [element packages](element_packages.html); consult the source for the `XMLNodeHandlerDataGrid`, `XMLNodeHandlerTabSet` and `XMLNodeHandlerTextArea` classes for demonstrations of their use. 
