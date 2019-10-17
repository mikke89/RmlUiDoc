---
layout: page
title: Elements
parent: cpp_manual
next: text_elements
---

An element is the smallest subdivision of functionality within a [document](documents.html).

### Size

Elements are made up of zero or more boxes, each of which has a rectangular content area surrounded by three areas of varying thicknesses; padding, borders and margin (see the [box model documentation](../rcss/box_model.html) for more details).

You can query the current size of an element with the `GetBox()` and `GetNumBoxes()` functions:

```cpp
// Returns one of the boxes describing the size of the element.
// @param[in] index The index of the desired box.
// @return The requested box.
const {{page.lib_ns}}::Core::Box& GetBox(int index = 0) const;

// Returns the number of boxes making up this element's geometry.
// @return the number of boxes making up this element's geometry.
int GetNumBoxes() const;
```

Most elements will have one box, except if they represent inline content split over multiple lines.

### Position

Elements measure their position as a pixel offset from a containing ancestor element. The containing element, referred to as the offset parent, is generally the element's closest ancestor with a `position`{:.prop} value other than `static`{:.value}. To get an element's offset parent, call the `GetOffsetParent()` function.

```cpp
// Returns the element from which all offset calculations are currently computed.
// @return This element's offset parent.
{{page.lib_ns}}::Core::Element* GetOffsetParent();
```

To retrieve the element's offset, use `GetRelativeOffset()` or `GetAbsoluteOffset()`:

```cpp
// Returns the position of the top-left corner of one of the areas of this element's primary box, relative to its
// offset parent's top-left border corner.
// @param[in] area The desired area position.
// @return The relative offset.
{{page.lib_ns}}::Core::Vector2f GetRelativeOffset({{page.lib_ns}}::Core::Box::Area area = Box::CONTENT) const;

// Returns the position of the top-left corner of one of the areas of this element's primary box, relative to
// the element root.
// @param[in] area The desired area position.
// @return The absolute offset.
{{page.lib_ns}}::Core::Vector2f GetAbsoluteOffset({{page.lib_ns}}::Core::Box::Area area = Box::CONTENT) const;
```

`GetRelativeOffset()` will return the offset from the element's offset parent's top-left border to one of the areas of the element's primary box. `GetAbsoluteOffset()` will return the offset from the top-left corner of the context the element is part of.

You can also use the [DOM functions](#dom-interface) `GetClientLeft()` and `GetClientTop()`.

### Pseudo-classes

Elements may have one or more pseudo-classes active on them at any one time. Pseudo-classes represent minor, temporary changes of state (such as input focus or mouse hovering) that can be used to change the value of RCSS properties.

To check if a pseudo-class is set on a particular element, you can use either the `IsPseudoClassSet()` or `GetActivePseudoClasses()` function.

```cpp
// Checks if a specific pseudo-class has been set on the element.
// @param[in] pseudo_class The name of the pseudo-class to check for.
// @return True if the pseudo-class is set on the element, false if not.
bool IsPseudoClassSet(const {{page.lib_ns}}::Core::String& pseudo_class) const;

// Gets a list of the current active pseudo-classes.
// @return The list of active pseudo-classes.
const {{page.lib_ns}}::Core::PseudoClassList& GetActivePseudoClasses() const;
```

`IsPseudoClassSet()` will check for the prescence of a particular pseudo-class on the element, while `GetActivePseudoClasses()` will return an STL set containing all pseudo-classes.

To set or remove a pseudo-class, call `SetPseudoClass()`.

```cpp
// Sets or removes a pseudo-class on the element.
// @param[in] pseudo_class The pseudo class to activate or deactivate.
// @param[in] activate True if the pseudo-class is to be activated, false to be deactivated.
void SetPseudoClass(const {{page.lib_ns}}::Core::String& pseudo_class, bool activate);
```

Applications can make use of any pseudo-classes they wish for their own styling needs. However, {{page.lib_name}} maintains several pseudo-classes internally and it is not recommended you set or clear them yourself. These classes are:

* `hover`{:.cls}: Set when the mouse cursor is positioned over the element.
* `active`{:.cls}: Set when the primary mouse button is depressed, and was positioned over the element when it was pressed.
* `focus`{:.cls}: Set if an element has input focus. Usually this occurs when the element is clicked on.
* `checked`{:.cls}: Set on a selected [radio button or checkbox](controls/form.html#radio-button-and-checkbox), or [drop-down list control item](controls/form.html#drop-down-select-box).
* `disabled`{:.cls}: Set on a disabled [form control](controls/form.html).

### DOM interface

{{page.lib_name}} elements support the majority of [Gecko's HTML DOM element interface](https://developer.mozilla.org/en-US/docs/Web/API/element), so web developers should be familiar with most of an element's functionality.

| {{page.lib_name}} functions | Brief description | Equivalent DOM property |
|------------------|-------------------|-------------------------|
| `GetAbsoluteLeft()` | The distance from the context's left edge and the element's left border.
| `GetAbsoluteTop()` | The distance from the context's top edge and the element's top border.
| `SetAttribute()`, `GetAttribute()` | All attributes associated with an element. | attributes
| `GetChild()`, `GetNumChildren()` | All child nodes of an element. | childNodes
| `IsClassSet()`, `SetClass()` | Gets/sets the class of the element. | className
| `GetClientHeight()` | The inner height of an element. | clientHeight
| `GetClientLeft()` | The width of the left border of an element. | clientLeft
| `GetClientTop()` | The width of the top border of an element. | clientTop
| `GetClientWidth()` | The inner width of an element. | clientWidth
| `GetFirstChild()` | The first direct child node of an element. | firstChild
| `GetId()`, `SetId()` | Gets/sets the id of the element. | id
| `GetInnerRML()`, `SetInnerRML()` | Gets/sets the markup and content of the element. | innerHTML
| `GetLastChild()` | The last direct child node of an element. | lastChild
| `GetNextSibling()` | The node immediately following the given one in the tree. | nextSibling
| `GetOffsetHeight()` | The height of an element, relative to the layout. | offsetHeight
| `GetOffsetLeft()` | The distance from this element's left border to its offset parent's left border. | offsetLeft
| `GetOffsetParent()` | The element from which all offset calculations are currently computed. | offsetParent
| `GetOffsetTop()` | The distance from this element's top border to its offset parent's top border. | offsetTop
| `GetOffsetWidth()` | The width of an element, relative to the layout. | offsetWidth
| `GetOwnerDocument()` | The document that this node is in. | ownerDocument
| `GetParentNode()` | The parent element of this node. | parentNode
| `GetPreviousSibling()` | The node immediately preceding the given one in the tree. | previousSibling
| `GetScrollHeight()` | The scroll view height of an element. | scrollHeight
| `GetScrollLeft()` | Gets/sets the left scroll offset of an element. | scrollLeft
| `GetScrollTop()` | Gets/sets the top scroll offset of an element. | scrollTop
| `GetScrollWidth()` | The scroll view width of an element. | scrollWidth
| `GetProperty()`, `SetProperty()` | An object representing the declarations of an element's style attributes. | style
| `GetTagName()` | The name of the tag for the given element. | tagName

Supported methods have simply had their initial letter capitalised to match the rest of the {{page.lib_name}} API.

| {{page.lib_name}} function | Brief description | Equivalent DOM method |
|-----------------|-------------------|-----------------------|
| `AddEventListener()` | Register an event handler to a specific event type on the element. | addEventListener()
| `AppendChild()` | Insert a node as the last child node of this element. The newly parented node must first be detached from its existing parent. | appendChild()
| `Blur()` | Removes keyboard focus from the current element. | blur()
| `Click()` | Simulates a click on the current element. | click()
| `DispatchEvent()` | Dispatch an event to this node in the DOM. | dispatchEvent()
| `Focus()` | Gives keyboard focus to the current element. | focus()
| `GetAttribute()` | Retrieve the value of the named attribute from the current node. | getAttribute()
| `GetElementById()` | Returns an element by its id. | getElementById()
| `GetElementsByTagName()` | Retrieve a set of all descendant elements, of a particular tag name, from the current element. | getElementsByTagName()
| `HasAttribute()` | Check if the element has the specified attribute, or not. | hasAttribute()
| `HasChildNodes()` | Check if the element has any child nodes, or not. | hasChildNodes()
| `InsertBefore()` | Inserts the first node before the second, child, node in the DOM. The newly parented node must first be detached from its existing parent. | insertBefore()
| `RemoveAttribute()` | Remove the named attribute from the current node. | removeAttribute()
| `RemoveChild()` | Removes a child node from the current element, returning it as a unique pointer. | removeChild()
| `RemoveEventListener()` | Removes an event listener from the element. | removeEventListener()
| `ReplaceChild()` | Replaces one child node in the current element with another. | replaceChild()
| `ScrollIntoView()` | Scrolls the page until the element gets into the view. | scrollIntoView()
| `SetAttribute()` | Set the value of the named attribute from the current node. | setAttribute()

### Validity of retrieved values

Whenever an element is modified, added, or removed from the DOM hierarchy, the values retrieved from the [DOM interface](#dom-interface) may become dirty. Instead of immediately updating properties on any affected elements, most of this work is done during the `Context::Update` call in a carefully chosen order for performance reasons. 

Thus, values related to the layout (sizes and offsets) and computed values may return default values or values calculated during the previous update loop. If such values need to be retrieved after a modification to the DOM, the element's document can be manually updated by calling

```cpp
// Updates the document, including its layout. Users must call this manually before requesting information such as 
// size or position of an element if any element in the document was recently changed, unless Context::Update has
// already been called after the change. This has a perfomance penalty, only call when necessary.
void ElementDocument::UpdateDocument();
```
before retrieving such values with the performance penalties this entails. This ensures all retrieved values are correct.

Due to the complexity of the HTML/CSS model, it is a highly challenging task to infer exactly which values of which elements become dirty after a modification to the DOM or style. Simultaneously, for performance reasons, the library can not always do a full update of the whole document when retrieving some element value. Until a good solution can be made for dirtying such values, this workaround is necessary.

### Dynamically creating elements

Elements should not be created with the `new` operator; in order to be properly constructed counted and released, they need to be created either through a document (using the `CreateElement()` or `CreateTextNode()` function) or through the {{page.lib_name}} factory (`{{page.lib_ns}}::Core::Factory`) using the factory's static `InstanceElement()` function.

#### Ownership of elements

Generally, elements are uniquely owned by their parents. For newly created elements or removed elements, the element is returned with a unique ownership, e.g.
```cpp
ElementPtr ElementDocument::CreateElement(const String& name);
```
where `ElementPtr` is a unique pointer and an alias as follows.
```cpp
using ElementPtr = std::unique_ptr<Element, Releaser<Element>>;
```
Note that, the custom deleter `Releaser` is there to ensure the element is released from the `ElementInstancer` in which it was created.

When storing around non-owning raw pointer to an element, it may be useful to know when an element has been destroyed. An `ObserverPtr` can be used for this purpose, see [core ownership and lifetimes](core_overview.html#ownership-and-lifetimes) for details.

#### Using a document

To create an element through a document use one of the following functions:

```cpp
// Creates the named element.
// @param[in] name The tag name of the element.
{{page.lib_ns}}::Core::ElementPtr CreateElement(const {{page.lib_ns}}::Core::String& name);

// Create a text element with the given text content.
// @param[in] text The text content of the text element.
{{page.lib_ns}}::Core::ElementPtr CreateTextNode(const {{page.lib_ns}}::Core::String& text);
```

`CreateElement()` takes a single parameter, name, the tag name of the new element. This will be used to both look up the instancer and tag the element. Like instancing the element through the factory, the new element will be returned if it was created successfully, or `nullptr` if not.

`CreateTextNode()` creates a single text element containing the text given in the parameter text.

Note that elements returned by these functions are not affiliated with the document itself. Instead, they are returned unparented by a unique pointer, and must be moved into other elements if desired.

After having called `ElementDocument::CreateElement`, the element can be moved into the list of children of another element.
```cpp
ElementPtr new_child = document->CreateElement("div");
element->AppendChild( std::move(new_child) );
```
Since we moved `new_child`, we cannot use the pointer anymore. Instead, `Element::AppendChild` returns a non-owning raw pointer to the appended child which can be used. Furthermore, the new element can be constructed in-place, e.g.
```cpp
Element* new_child = element->AppendChild( document->CreateElement("div") );
```
and now `new_child` can safely be used until the element is destroyed.


#### Using the factory

Creating an element through the factory allows more control. The `InstanceElement()` function is detailed below:

```cpp
// Instances a single element.
// @param[in] parent The parent of the new element, or nullptr for a root tag.
// @param[in] instancer The name of the instancer to create the element with.
// @param[in] tag The tag of the element to be instanced.
// @param[in] attributes The attributes to instance the element with.
// @return The instanced element, or nullptr if the instancing failed.
static {{page.lib_ns}}::Core::ElementPtr InstanceElement({{page.lib_ns}}::Core::Element* parent,
                                              const {{page.lib_ns}}::Core::String& instancer,
                                              const {{page.lib_ns}}::Core::String& tag,
                                              const {{page.lib_ns}}::Core::XMLAttributes& attributes);
```

The function's parameters are:

* `parent`: The element you intend to parent the element to once it has been created. This is only used by custom instancers; if you're instancing a generic element you can leave this out. Note that the new element will not be automatically parented to this element, you still need to do that yourself once the element has been created.
* `instancer`: The tag name the instancer you want to create the element was registered against. For creating generic elements, this can be the same as the third parameter, `tag`. For more information, see the section on [custom element instancers](#creating-a-custom-element-instancer).
* `tag`: The tag the new element should have.
* `attributes`: Any attributes you want the new element to be constructed with. This is a dictionary type. The attributes will be passed into the instancer and set on the element if instancing was successful. 

For example, the following will instance a `<div>`{:.tag} element:

```cpp
{{page.lib_ns}}::Core::ElementPtr div_element = {{page.lib_ns}}::Core::Factory::InstanceElement(nullptr,
                                                                            "div",
                                                                            "div",
                                                                            {{page.lib_ns}}::Core::XMLAttributes());
```

The following will instance a radio button element using the Controls plugin input instancer, but gives it a tag of `radio`{:.tag}:

```cpp
{{page.lib_ns}}::Core::XMLAttributes attributes;
attributes.Set("type", "radio");
attributes.Set("name", "graphics");
attributes.Set("value", "OK");
{{page.lib_ns}}::Core::ElementPtr radio_element = {{page.lib_ns}}::Core::Factory::InstanceElement(div_element,
                                                                              "input",
                                                                              "radio",
                                                                              attributes);
```

If the element is instanced successfully, it will be returned. If not, `nullptr` will be returned. As `ElementPtr` is a unique pointer, it must be moved into the element hierarchy, such as by using `std::move`. If the unique pointer goes out of scope, it will automatically be released.

### Destroying and moving elements

Raw element pointers are non-owning, so are not meant to be deleted directly. If it is an unparented unique pointer, `ElementPtr`, simply let the object go out of scope or call `element.reset()`. If an element is part of a hierarchy, simply remove it from its parent to destroy it with the `RemoveChild()` function.
```cpp
/// Remove a child element from this element.
/// @param[in] The element to remove.
/// @returns A unique pointer to the element if found, discard the result to immediately destroy.
{{page.lib_ns}}::Core::ElementPtr RemoveChild(Element* element);
```
The remove returns a unique pointer to the removed child. Discard the result to let it be released immediately. Otherwise, the element can now be appended to another element by moving the returned `ElementPtr`.

Note that `AppendChild` and `InsertBefore` takes `ElementPtr`s, thus, any parented elements must first be removed before they can be moved into another location in the hierarchy.

### Custom elements

If you need special functionality on an element that you can't easily manage through the event system, you have the option of creating a custom element. Custom elements derive directly from the core Element class definition and are created through a custom element instancer. Custom elements can:

* Respond to property and attribute changes.
* Manage the layout of hidden internal elements.
* Execute custom update or rendering code.
* Respond to events inline.
* Respond to descendant add / remove events. 

#### Creating a custom element

All custom elements are classes derived (not necessarily directly) from `{{page.lib_ns}}::Core::Element`. The constructor for Element takes one parameter, the tag of the element; a derived element's constructor can either pass a constant string down to the base constructor, or take a string themselves to pass down.

The virtual functions that can be overridden in a custom element are:

```cpp
// Returns the baseline of the element, in pixels offset from the bottom of the element's content area.
// @return The element's baseline. A negative baseline will be further 'up' the element, a positive on further 'down'.
virtual float GetBaseline() const;

// Gets the intrinsic dimensions of this element, if it is of a type that has an inherent size.
// @param[in] dimensions The dimensions to size, if appropriate.
// @return True if the element has intrinsic dimensions, false otherwise.
virtual bool GetIntrinsicDimensions({{page.lib_ns}}::Core::Vector2f& dimensions);

// Called when an emitted event propagates to this element, for event types with default actions.
// Note: See 'EventSpecification' for the events that call this function and during which phase.
// @param[in] event The event to process.
virtual void ProcessDefaultAction({{page.lib_ns}}::Core::Event& event);

// Called during the update loop after children are updated.
virtual void OnUpdate();
// Called during render after backgrounds, borders, decorators, but before children, are rendered.
virtual void OnRender();

// Called when attributes on the element are changed.
// @param[in] changed_attributes The attributes changed on the element.
virtual void OnAttributeChange(const {{page.lib_ns}}::Core::AttributeNameList& changed_attributes);
// Called when properties on the element are changed.
// @param[in] changed_properties The properties changed on the element.
virtual void OnPropertyChange(const {{page.lib_ns}}::Core::PropertyIdSet& changed_properties);

// Called when a child node has been added up to two levels below us in the hierarchy.
// @param[in] child The element that has been added. This may be this element.
virtual void OnChildAdd({{page.lib_ns}}::Core::Element* child);
// Called when a child node has been removed up to two levels below us in the hierarchy.
// @param[in] child The element that has been removed. This may be this element.
virtual void OnChildRemove({{page.lib_ns}}::Core::Element* child);

// Gets the markup and content of the element.
// @param[out] content The content of the element.
virtual void GetInnerRML({{page.lib_ns}}::Core::String& content) const;
// Returns the RML of this element and all children.
// @param[out] content The content of this element and those under it, in XML form.
virtual void GetRML({{page.lib_ns}}::Core::String& content);
```

#### Layout

A custom element can override the `GetIntrinsicDimensions()` function if it wants to be laid out as a replaced element. Replaced elements are elements with intrinsic dimensions that can be positioned like inline or block content. Examples of replaced elements are images and form controls.

```cpp
// Gets the intrinsic dimensions of this element, if it is of a type that has an inherent size.
// @param[in] dimensions The dimensions to size, if appropriate.
// @return True if the element has intrinsic dimensions, false otherwise.
virtual bool GetIntrinsicDimensions({{page.lib_ns}}::Core::Vector2f& dimensions);
```

If a custom element is to be a replaced element, it should override this function and return true. The actual intrinsic dimensions of the element should be put into the dimensions parameter. This function will be called every time the element is laid out, so the dimension can be a dynamic value. The default element returns false.

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
virtual void ProcessDefaultAction({{page.lib_ns}}::Core::Event& event);
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
virtual void OnAttributeChange(const {{page.lib_ns}}::Core::AttributeNameList& changed_attributes);
```

`OnPropertyChange()` is called whenever the value of a property (or group of properties) is changed. The names of the changed properties are passed into the function in the `changed_properties` variable, which is a set of `PropertyId`s.

```cpp
// Called when properties on the element are changed.
// @param[in] changed_properties The properties changed on the element.
virtual void OnPropertyChange(const {{page.lib_ns}}::Core::PropertyIdSet& changed_properties);
```

**Important**: If you override either of these functions, you must remember to call the base class's corresponding function! As with `ProcessDefaultAction()`, the base element responds to many attribute and property changes, and all manner of strange behaviour may result if you don't do this.

#### Hierarchy changes

A custom element can override the `OnChildAdd()` or `OnChildRemove()` functions to respond to changes in the element's hierarchy. When an element is added or removed from another, the appropriate function is called on itself and its nearby ancestors immediately. Note that for performance reasons, only the nodes up to two levels up in the hierarchy are notified.

```cpp
// Called when a child node has been added up to two levels below us in the hierarchy.
// @param[in] child The element that has been added. This may be this element.
virtual void OnChildAdd({{page.lib_ns}}::Core::Element* child);

// Called when a child node has been removed up to two levels below us in the hierarchy.
// @param[in] child The element that has been removed. This may be this element.
virtual void OnChildRemove({{page.lib_ns}}::Core::Element* child);
```

#### RML generation

A custom element can override the `GetRML()` and `GetInnerRML()` function if the default RML generation functions are inadequate. This is generally not needed, unless an element rearranges its child elements internally, or makes heavy use of custom XML node handlers; in this case, the default functions may generate nonsensical RML.

`GetInnerRML()` is meant to return the internal RML of the element; ie, only the RML needed to generate the element's content, not the element itself. By default, it calls `GetRML()` on all of its DOM children and concatenates the result.

`GetRML()` is meant to return the RML required to generate the entire element. This therefore includes the element's tag and all of its attributes as well as all of its descendant's RML. By default, it generates its open tag, appends to that the the result of `GetInnerRML()`, and finally appends its closing tag.

```cpp
// Gets the markup and content of the element.
// @param[out] content The content of the element.
virtual void GetInnerRML({{page.lib_ns}}::Core::String& content) const;

// Returns the RML of this element and all children.
// @param[out] content The content of this element and those under it, in XML form.
virtual void GetRML({{page.lib_ns}}::Core::String& content);
```

### Creating a custom element instancer

In order to have a custom element created through the {{page.lib_name}} factory, an instancer for the element needs to be registered with the factory against the appropriate RML tag names. An element instancer is responsible for creating and destroying its elements when required, and also destroying itself when {{page.lib_name}} is shut down.

A custom element instancer needs to be derived from `{{page.lib_ns}}::Core::ElementInstancer`, and implement the required pure virtual methods:

```cpp
// Instances an element given the tag name and attributes.
// @param[in] parent The element the new element is destined to be parented to.
// @param[in] tag The tag of the element to instance.
// @param[in] attributes Dictionary of attributes.
// @return A unique pointer to the instanced element.
virtual {{page.lib_ns}}::Core::ElementPtr InstanceElement({{page.lib_ns}}::Core::Element* parent,
                                              const {{page.lib_ns}}::Core::String& tag,
                                              const {{page.lib_ns}}::Core::XMLAttributes& attributes) = 0;

// Releases an element instanced by this instancer.
// @param[in] element The element to release.
virtual void ReleaseElement({{page.lib_ns}}::Core::Element* element) = 0;
```

`InstanceElement()` will be called whenever the factory is called upon to instance an element with a tag that the instancer was registered against. The parameters to the function are:

* `parent`: The element that the new element will be parented to if it is created successfully; you do not need to actually do the parenting! This will only be non-null if the element is instanced from RML.
* `tag`: The string that whoever is creating the element wants the element's tag to be; due to the way elements are constructed through the factory, this may not be one of the tags the instancer was registered against. It is recommended you pass this through to the element to be its tag name, but this is not required.
* `attributes`: The attributes defined on the element's tag in RML or passed into the factory. You do not need to set these attributes on the element yourself; that will be done automatically if the instancing is successful. You only need to use these if element instancing is dependent on the values (for example, the instancer for `input`{:.tag} elements instances different types depending on the value of the `type`{:.attr} attribute). 

If `InstanceElement()` is successful, return the new element wrapped in an `ElementPtr` (unique element). Otherwise, return nullptr to indicate an instancing error.

`ReleaseElement()` will be called after an element has been released from its owner, that is, its `ElementPtr` is destroyed or reset. The element should be deleted appropriately.

#### Registering an instancer

To register a custom instancer with {{page.lib_name}}, call the `RegisterElementInstancer()` function on the {{page.lib_name}} factory (`{{page.lib_ns}}::Core::Factory`) after {{page.lib_name}} has been initialised.

```cpp
// Make sure custom_instancer is kept alive until after the call to {{page.lib_ns}}::Core::Shutdown
auto custom_instancer = std::make_unique<ElementInstancerCustom>();
{{page.lib_ns}}::Core::Factory::RegisterElementInstancer("custom", custom_instancer.get());
```

The first parameter to `RegisterElementInstancer()` is the tag name the instancer is bound to. In the above example, the custom instancer will be called to instance an element whenever an element with the tag 'custom' is encountered while parsing an RML stream, or as otherwise required by the factory. You can register an instancer as many times as you like with the factory against different tag names.

The library takes a non-owning pointer to the instancer. Thus, the instancer must be kept alive until after the call to `Rml::Core::Shutdown`, and then cleaned up by the user.

#### Using a generic instancer

If a custom element does not require any special behaviour from its instancer, the easiest way to generate an instancer for it is to use the templated `ElementInstancerGeneric`. Instead of deriving your own instancer class, simply construct a new `{{page.lib_ns}}::Core::ElementInstancerGeneric` templated to the type of the custom element you'd like to instance, and register it with the factory as you would a normal instancer.

```cpp
// Make sure custom_instancer is kept alive until after the call to {{page.lib_ns}}::Core::Shutdown
auto custom_instancer = std::make_unique< {{page.lib_ns}}::Core::ElementInstancerGeneric< CustomElement > >();
{{page.lib_ns}}::Core::Factory::RegisterElementInstancer("custom", custom_instancer.get());
```

The only requirement on the element type that it is templated to is that the constructor take a string (the tag name) like the base element.

### Custom XML node handling

For some complex custom elements, the RML required to generate the element is not indicative of the actual internal hierarchy. For example, in the Controls plugin, columns in a data grid element are specified by `<col>`{:.tag} tags immediately beneath the `<datagrid>`{:.tag} tag. If the standard XML parsing was being executed, an element would be instanced and parented to the data grid for each column tag - but this isn't what is wanted. So a custom XML node handler is used for data grids that processes the column tag differently.

Node handlers are registered against RML tag names. When an RML file is being parsed, the XML parser maintains a stack of node handlers. Whenever a new tag is encountered, the parser checks if a specific node handler is registered against that tag; if so, that handler is pushed onto the stack and takes over the parsing until its associated tag is closed. If no handler is associated with a particular element, the current node handler continues parsing.

#### Creating a custom XML node handler

Custom node handlers derive from the `{{page.lib_ns}}::Core::XMLNodeHandler` class and implement the pure virtual functions:

```cpp
// Called when a new element tag is opened.
// @param parser The parser executing the parse.
// @param name The XML tag name.
// @param attributes The tag attributes.
// @return The new element, may be NULL if no element was created.
virtual {{page.lib_ns}}::Core::Element* ElementStart({{page.lib_ns}}::Core::XMLParser* parser,
                                            const {{page.lib_ns}}::Core::String& name,
                                            const {{page.lib_ns}}::Core::XMLAttributes& attributes) = 0;

// Called when an element is closed.
// @param parser The parser executing the parse.
// @param name The XML tag name.
virtual bool ElementEnd({{page.lib_ns}}::Core::XMLParser* parser,
                        const {{page.lib_ns}}::Core::String& name) = 0;

// Called for element data.
// @param parser The parser executing the parse.
// @param data The element data.
virtual bool ElementData({{page.lib_ns}}::Core::XMLParser* parser,
                         const {{page.lib_ns}}::Core::String& data) = 0;
```

`ElementStart()`, `ElementEnd()` and `ElementData()` are called on the node handler for the appropriate XML parse events that occur while it is the active node handler. A self-closing tag will result in a call to `ElementEnd()` immediately after `ElementStart()`. `ElementData()` is called when loose non-whitespace data is encountered between two tags.

Each of these functions is passed a pointer to the XML parser running the parse. From the parser the current parse frame can be requested with the `GetParseFrame()` function; the parse frame object contains the current element and tag being processed, as well as the active node handler.

```cpp
struct ParseFrame
{
	// Tag being parsed.
	{{page.lib_ns}}::Core::String tag;

	// Element representing this frame.
	{{page.lib_ns}}::Core::Element* element;

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
bool PushHandler(const {{page.lib_ns}}::Core::String& tag);

// Pushes the default element handler onto the parse stack.
void PushDefaultHandler();
```

If it doesn't call either of these methods, it will remain the node handler for any child elements it creates.
Registering a custom node handler

Register a custom node handler with {{page.lib_name}}'s XML parser with the static `RegisterNodeHandler()` function on `{{page.lib_ns}}::Core::XMLParser`. You can register the same handler multiple times with the parser against different tag names. `RegisterNodeHandler()` takes shared ownership of the handler, thus, users do not need to store their own copy when they are done.

```cpp
// Registers a custom node handler to be used to a given tag.
// @param[in] tag The tag the custom parser will handle.
// @param[in] handler The custom handler.
// @return The registered XML node handler.
static {{page.lib_ns}}::Core::XMLNodeHandler* RegisterNodeHandler(const {{page.lib_ns}}::Core::String& tag,
                                                         SharedPtr<{{page.lib_ns}}::Core::XMLNodeHandler> handler);
```

### Samples

Custom XML node handlers are used extensively in the Controls plugin; consult the source for the `XMLNodeHandlerDataGrid`, `XMLNodeHandlerTabSet` and `XMLNodeHandlerTextArea` classes for demonstrations of their use. 