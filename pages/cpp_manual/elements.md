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
const Rml::Box& GetBox(int index = 0) const;

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
Rml::Element* GetOffsetParent();
```

To retrieve the element's offset, use `GetRelativeOffset()` or `GetAbsoluteOffset()`:

```cpp
// Returns the position of the top-left corner of one of the areas of this element's primary box, relative to its
// offset parent's top-left border corner.
// @param[in] area The desired area position.
// @return The relative offset.
Rml::Vector2f GetRelativeOffset(Rml::Box::Area area = Box::CONTENT) const;

// Returns the position of the top-left corner of one of the areas of this element's primary box, relative to
// the element root.
// @param[in] area The desired area position.
// @return The absolute offset.
Rml::Vector2f GetAbsoluteOffset(Rml::Box::Area area = Box::CONTENT) const;
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
bool IsPseudoClassSet(const Rml::String& pseudo_class) const;

// Gets a list of the current active pseudo-classes.
// @return The list of active pseudo-classes.
const Rml::PseudoClassList& GetActivePseudoClasses() const;
```

`IsPseudoClassSet()` will check for the prescence of a particular pseudo-class on the element, while `GetActivePseudoClasses()` will return an STL set containing all pseudo-classes.

To set or remove a pseudo-class, call `SetPseudoClass()`.

```cpp
// Sets or removes a pseudo-class on the element.
// @param[in] pseudo_class The pseudo class to activate or deactivate.
// @param[in] activate True if the pseudo-class is to be activated, false to be deactivated.
void SetPseudoClass(const Rml::String& pseudo_class, bool activate);
```

Applications can make use of any pseudo-classes they wish for their own styling needs. However, RmlUi maintains several pseudo-classes internally and it is not recommended you set or clear them yourself. These classes are:

* `hover`{:.cls}: Set when the mouse cursor is positioned over the element.
* `active`{:.cls}: Set when the primary mouse button is depressed, and was positioned over the element when it was pressed.
* `focus`{:.cls}: Set if an element has input focus. Usually this occurs when the element is clicked on.
* `checked`{:.cls}: Set on a selected [radio button or checkbox](element_packages/form.html#radio-button-and-checkbox), or [drop-down list control item](element_packages/form.html#drop-down-select-box).
* `disabled`{:.cls}: Set on a disabled [form control](element_packages/form.html).

### DOM interface

RmlUi elements support the majority of [Gecko's HTML DOM element interface](https://developer.mozilla.org/en-US/docs/Web/API/element), so web developers should be familiar with most of an element's functionality.

| RmlUi functions | Brief description | Equivalent DOM property |
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

Supported methods have simply had their initial letter capitalised to match the rest of the RmlUi API.

| RmlUi function | Brief description | Equivalent DOM method |
|-----------------|-------------------|-----------------------|
| `AddEventListener()` | Register an event handler to a specific event type on the element. | addEventListener()
| `AppendChild()` | Insert a node as the last child node of this element. The newly parented node must first be detached from its existing parent. | appendChild()
| `Blur()` | Removes keyboard focus from the current element. | blur()
| `Click()` | Simulates a click on the current element. | click()
| `Closest()` | Retrieve the first ancestor element matching the provided RCSS selector(s). | closest()
| `DispatchEvent()` | Dispatch an event to this node in the DOM. | dispatchEvent()
| `Focus()` | Gives keyboard focus to the current element. | focus()
| `GetAttribute()` | Retrieve the value of the named attribute from the current node. | getAttribute()
| `GetElementById()` | Returns an element by its id. | getElementById()
| `GetElementsByTagName()` | Retrieve a set of all descendant elements with a particular tag name. | getElementsByTagName()
| `GetElementsByClassName()` | Retrieve a set of all descendant elements with a particular class set. | getElementsByClassName()
| `HasAttribute()` | Check if the element has the specified attribute, or not. | hasAttribute()
| `HasChildNodes()` | Check if the element has any child nodes, or not. | hasChildNodes()
| `InsertBefore()` | Inserts the first node before the second, child, node in the DOM. The newly parented node must first be detached from its existing parent. | insertBefore()
| `QuerySelector()` | Retrieve the first descendant element matching the provided RCSS selector(s). | querySelector()
| `QuerySelectorAll()` | Retrieve a set of all descendant elements matching the provided RCSS selector(s). | querySelectorAll()
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

Elements should not be created with the `new` operator; in order to be properly constructed counted and released, they need to be created either through a document (using the `CreateElement()` or `CreateTextNode()` function) or through the RmlUi factory (`Rml::Factory`) using the factory's static `InstanceElement()` function.

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
Rml::ElementPtr CreateElement(const Rml::String& name);

// Create a text element with the given text content.
// @param[in] text The text content of the text element.
Rml::ElementPtr CreateTextNode(const Rml::String& text);
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
static Rml::ElementPtr InstanceElement(Rml::Element* parent,
                                              const Rml::String& instancer,
                                              const Rml::String& tag,
                                              const Rml::XMLAttributes& attributes);
```

The function's parameters are:

* `parent`: The element you intend to parent the element to once it has been created. This is only used by custom instancers; if you're instancing a generic element you can leave this out. Note that the new element will not be automatically parented to this element, you still need to do that yourself once the element has been created.
* `instancer`: The tag name the instancer you want to create the element was registered against. For creating generic elements, this can be the same as the third parameter, `tag`. For more information, see the the documentation for [custom element instancers](custom_elements.html#creating-a-custom-element-instancer).
* `tag`: The tag the new element should have.
* `attributes`: Any attributes you want the new element to be constructed with. This is a dictionary type. The attributes will be passed into the instancer and set on the element if instancing was successful. 

For example, the following will instance a `<div>`{:.tag} element:

```cpp
Rml::ElementPtr div_element = Rml::Factory::InstanceElement(nullptr,
                                                                            "div",
                                                                            "div",
                                                                            Rml::XMLAttributes());
```

The following will instance a radio button element using the library's `input` instancer, but gives it a tag of `radio`{:.tag}:

```cpp
Rml::XMLAttributes attributes;
attributes.Set("type", "radio");
attributes.Set("name", "graphics");
attributes.Set("value", "OK");
Rml::ElementPtr radio_element = Rml::Factory::InstanceElement(div_element,
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
Rml::ElementPtr RemoveChild(Element* element);
```
The remove returns a unique pointer to the removed child. Discard the result to let it be released immediately. Otherwise, the element can now be appended to another element by moving the returned `ElementPtr`.

Note that `AppendChild` and `InsertBefore` takes `ElementPtr`s, thus, any parented elements must first be removed before they can be moved into another location in the hierarchy.
