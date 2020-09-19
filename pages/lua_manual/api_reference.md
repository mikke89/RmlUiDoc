---
layout: page
title: Lua API Reference
status: improve
---

All instantiable classes define a `new()` method which returns an object of that particular class. 

With the exception of this `new()` method, all members listed will be member methods.

## ElementDataGrid

Inherits: `Element`{: .type }

ElementDataGrid derives from Element. The data grid has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `ElementDataGridRow`{: .type } | rows |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | AddColumn(`string`{: .type } fields, `string`{: .type } formatter, `number`{: .type } initial_width, `string`{: .type } header_rml) |
| `nil`{: .type } | SetDataSource(`string`{: .type } data_source_name) |


### Metafunctions




### Property Descriptions

*  `ElementDataGridRow`{: .type } rows

> Returns an array containing all the rows in the data grid.



### Method Descriptions

* `nil`{: .type} AddColumn(`string`{: .type } fields, `string`{: .type } formatter, `number`{: .type } initial_width, `string`{: .type } header_rml)

> Adds a new column to the data grid. The column will read the columns fields (in CSV format) from the grid's data source, processing it through the data formatter named formatter. header_rml specifies the RML content of the column's header.

* `nil`{: .type} SetDataSource(`string`{: .type } data_source_name)

> Sets the name and table of the new data source to be used by the data grid.



## Colourb

Inherits: `nil`{: .type }

Constructs a colour with four channels, each from 0 to 255.

### Properties

| Types | Name |
| ------------ | ---- |
| `integer`{: .type } | blue |
| `integer`{: .type } | green |
| `integer`{: .type } | rgba |
| `integer`{: .type } | alpha |
| `integer`{: .type } | red |


### Methods

| Return value | Name |
| ------------ | ---- |
| `Colourb`{: .type} | new() |


### Metafunctions

| Metafunctions |
| ------------- |
| __mul |
| __eq |
| __add |


### Property Descriptions

*  `integer`{: .type } blue

> 

*  `integer`{: .type } green

> 

*  `integer`{: .type }, `integer`{: .type }, `integer`{: .type }, `integer`{: .type } rgba

> 

*  `integer`{: .type } alpha

> 

*  `integer`{: .type } red

> 



### Method Descriptions

* `nil`{: .type} new()

> 



## Colourf

Inherits: `nil`{: .type }



### Properties

| Types | Name |
| ------------ | ---- |
| `number`{: .type } | blue |
| `number`{: .type } | green |
| `number`{: .type } | rgba |
| `number`{: .type } | alpha |
| `number`{: .type } | red |


### Methods

| Return value | Name |
| ------------ | ---- |
| `Colourf`{: .type} | new() |


### Metafunctions

| Metafunctions |
| ------------- |
| __eq |


### Property Descriptions

*  `number`{: .type } blue

> 

*  `number`{: .type } green

> 

*  `number`{: .type }, `number`{: .type }, `number`{: .type }, `number`{: .type } rgba

> 

*  `number`{: .type } alpha

> 

*  `number`{: .type } red

> 



### Method Descriptions

* `nil`{: .type} new()

> 



## Vector2i

Inherits: `nil`{: .type }

Constructs a two-dimensional integral vector.

### Properties

| Types | Name |
| ------------ | ---- |
| `number`{: .type } | magnitude |
| `integer`{: .type } | y |
| `integer`{: .type } | x |


### Methods

| Return value | Name |
| ------------ | ---- |
| `Vector2i`{: .type} | new() |


### Metafunctions

| Metafunctions |
| ------------- |
| __sub |
| __eq |
| __div |
| __mul |
| __add |


### Property Descriptions

*  `number`{: .type } magnitude

> 

*  `integer`{: .type } y

> 

*  `integer`{: .type } x

> 



### Method Descriptions

* `nil`{: .type} new()

> 



## Vector2f

Inherits: `nil`{: .type }

Constructs a two-dimensional floating-point vector.

### Properties

| Types | Name |
| ------------ | ---- |
| `number`{: .type } | y |
| `number`{: .type } | magnitude |
| `number`{: .type } | x |


### Methods

| Return value | Name |
| ------------ | ---- |
| `Vector2f`{: .type }<br> | Rotate(`number`{: .type } ) |
| `Vector2f`{: .type }<br> | Normalise() |
| `number`{: .type }<br> | DotProduct(`Vector2f`{: .type } ) |
| `Vector2f`{: .type} | new() |


### Metafunctions

| Metafunctions |
| ------------- |
| __add |
| __sub |
| __div |
| __eq |
| __mul |


### Property Descriptions

*  `number`{: .type } y

> 

*  `number`{: .type } magnitude

> 

*  `number`{: .type } x

> 



### Method Descriptions

*  `Vector2f`{: .type } Rotate(`number`{: .type } )

> 

*  `Vector2f`{: .type } Normalise()

> 

*  `number`{: .type } DotProduct(`Vector2f`{: .type } )

> 

* `nil`{: .type} new()

> 



## ElementStyleProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __newindex |
| __ipairs |
| __index |
| __pairs |


### Property Descriptions



### Method Descriptions



## ContextDocumentsProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __pairs |
| __index |
| __ipairs |


### Property Descriptions



### Method Descriptions



## SelectOptionsProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __ipairs |
| __index |
| __pairs |


### Property Descriptions



### Method Descriptions



## RmlUiContextsProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __index |
| __ipairs |
| __pairs |


### Property Descriptions



### Method Descriptions



## Log

Inherits: `nil`{: .type }



### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | LogMessage() |


### Metafunctions




### Property Descriptions



### Method Descriptions

* `nil`{: .type} Message()

> 



## ElementChildNodesProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __ipairs |
| __pairs |
| __index |


### Property Descriptions



### Method Descriptions



## Document

Inherits: `Element`{: .type }

Document derives from Element. Document has no constructor; it must be instantiated through a Context object instead, either by loading an external RML file or creating an empty document. It has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `string`{: .type } | title |
| `Context`{: .type } | context |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | Hide() |
| `nil`{: .type } | Show(`integer`{: .type } [flags]) |
| `nil`{: .type } | PushToBack() |
| `nil`{: .type } | Close() |
| `ElementPtr`{: .type }<br> | CreateElement(`string`{: .type } tag_name) |
| `ElementPtr`{: .type }<br> | CreateTextNode(`string`{: .type } text) |
| `nil`{: .type } | PullToFront() |


### Metafunctions




### Property Descriptions

*  `string`{: .type } title

> The title of the document, as initially set by the \<title\> tag in the document's header.

*  `Context`{: .type } context

> The context the document belongs to. Read-only.



### Method Descriptions

* `nil`{: .type} Hide()

> Hides the document.

* `nil`{: .type} Show(`integer`{: .type } [flags])

> Shows the document. flags is either NONE, FOCUS or MODAL. flags defaults to FOCUS.

* `nil`{: .type} PushToBack()

> Pushes the document behind other documents within its context with a similar z-index.

* `nil`{: .type} Close()

> Hides and closes the document, destroying its contents.

*  `ElementPtr`{: .type } CreateElement(`string`{: .type } tag_name)

> Instances an element with a tag of tag_name.

*  `ElementPtr`{: .type } CreateTextNode(`string`{: .type } text)

> Instances a text element containing the string text.

* `nil`{: .type} PullToFront()

> Pulls the document in front of other documents within its context with a similar z-index.



## IElementText

Inherits: `nil`{: .type }

IElementText derives from Element. IElementText is an interface, and therefore cannot be instanced directly. A concrete ElementText must be instantiated through a Document object instead. It has the following property:

### Properties

| Types | Name |
| ------------ | ---- |
| `nil`{: .type } | text |


### Methods




### Metafunctions




### Property Descriptions

* `nil`{: .type } text

> The raw text content of the text element in UTF-8 encoding.



### Method Descriptions



## ElementInstancer

Inherits: `nil`{: .type }



### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `value`{: .type }<br> | InstanceElement(`ElementInstancer`{: .type } ) |
| `ElementInstancer`{: .type} | new() |


### Metafunctions




### Property Descriptions



### Method Descriptions

*  `value`{: .type } InstanceElement(`ElementInstancer`{: .type } )

> 

* `nil`{: .type} new()

> 



## DataFormatter

Inherits: `nil`{: .type }



### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `DataFormatter`{: .type} | new() |
| `value`{: .type }<br> | FormatData(`DataFormatter`{: .type } ) |


### Metafunctions




### Property Descriptions



### Method Descriptions

* `nil`{: .type} new()

> 

*  `value`{: .type } FormatData(`DataFormatter`{: .type } )

> 



## ElementAttributesProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __index |
| __ipairs |
| __pairs |


### Property Descriptions



### Method Descriptions



## ElementPtr

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions




### Property Descriptions



### Method Descriptions



## LuaDataSource

Inherits: `nil`{: .type }



### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `LuaDataSource`{: .type} | new() |


### Metafunctions




### Property Descriptions



### Method Descriptions

* `nil`{: .type} DataSourcenew()

> 



## ElementFormControlDataSelect

Inherits: `ElementFormControlSelect`{: .type }

ElementFormControlDataSelect derives from ElementFormControlSelect. It has the following additional method:

### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | SetDataSource(`string`{: .type } data_source_name) |


### Metafunctions




### Property Descriptions



### Method Descriptions

* `nil`{: .type} SetDataSource(`string`{: .type } data_source_name)

> Sets the name and table of the new data source to be used by the select box.



## ElementForm

Inherits: `Element`{: .type }

ElementForm derives from Element. The form element has the following method:

### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | Submit(`string`{: .type } submit_value) |


### Metafunctions




### Property Descriptions



### Method Descriptions

* `nil`{: .type} Submit(`string`{: .type } submit_value)

> Submits the form with a submit value of submit_value.



## ElementText

Inherits: `Element`{: .type }



### Properties

| Types | Name |
| ------------ | ---- |
| `string`{: .type } | text |


### Methods




### Metafunctions




### Property Descriptions

*  `string`{: .type } text

> 



### Method Descriptions



## Element

Inherits: `nil`{: .type }

The Element class has no constructor; it must be instantiated through a [Document](#document) object instead. It has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `nil`{: .type } | next_sibling |
| `Document`{: .type } | owner_document |
| `string`{: .type } | class_name |
| `Element`{: .type } | offset_parent |
| `number`{: .type } | scroll_height |
| `number`{: .type } | scroll_left |
| `number`{: .type } | offset_width |
| `string`{: .type } | id |
| `nil`{: .type } | first_child |
| `nil`{: .type } | last_child |
| `number`{: .type } | client_left |
| `ElementChildNodesProxy`{: .type } | child_nodes |
| `nil`{: .type } | previous_sibling |
| `number`{: .type } | client_height |
| `number`{: .type } | scroll_top |
| `number`{: .type } | offset_top |
| `ElementStyleProxy`{: .type } | style |
| `number`{: .type } | scroll_width |
| `number`{: .type } | client_top |
| `number`{: .type } | offset_left |
| `number`{: .type } | offset_height |
| `string`{: .type } | tag_name |
| `string`{: .type } | inner_rml |
| `number`{: .type } | client_width |
| `ElementAttributesProxy`{: .type } | attributes |
| `nil`{: .type } | parent_node |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | AddEventListener(`BOOL`{: .type } event, `string`{: .type } listener[, `lua_type`{: .type } in_capture_phase]) |
| `nil`{: .type } | SetAttribute(`string`{: .type } name, `string`{: .type } value) |
| `boolean`{: .type }<br> | RemoveChild(`Element`{: .type } element) |
| `Element`{: .type }<br> | GetElementById(`string`{: .type } id) |
| `boolean`{: .type }<br> | HasChildNodes() |
| `nil`{: .type }<br> | DispatchEvent(`string`{: .type } event, `lua_type`{: .type } parameters, `string`{: .type } interruptible) |
| `nil`{: .type } | AppendChild(`ElementPtr`{: .type } element) |
| `nil`{: .type } | RemoveAttribute(`string`{: .type } name) |
| `Variant`{: .type }<br> | GetAttribute(`string`{: .type } name) |
| `integer`{: .type }<br>`Element`{: .type }<br>`settable`{: .type }<br> | GetElementsByTagName(`string`{: .type } tag_name) |
| `boolean`{: .type }<br> | IsClassSet(`string`{: .type } name) |
| `nil`{: .type } | ScrollIntoView(`BOOL`{: .type } align_with_top) |
| `nil`{: .type } | SetClass(`string`{: .type } name, `BOOL`{: .type } value) |
| `nil`{: .type } | Blur() |
| `nil`{: .type } | InsertBefore(`ElementPtr`{: .type } element, `Element`{: .type } adjacent_element) |
| `Element`{: .type} | new() |
| `nil`{: .type } | Focus() |
| `boolean`{: .type }<br> | HasAttribute(`string`{: .type } name) |
| `boolean`{: .type }<br> | ReplaceChild(`ElementPtr`{: .type } inserted_element, `Element`{: .type } replaced_element) |
| `nil`{: .type } | Click() |


### Metafunctions




### Property Descriptions

*  `nil`{: .type }, `Element`{: .type } next_sibling

> The element's next sibling, or None if it is the last sibling. Read-only.

*  `Document`{: .type } owner_document

> The document this element is part of. Read-only.

*  `string`{: .type } class_name

> The space-separated list of classes on the element.

*  `Element`{: .type } offset_parent

> The element's offset parent. Read only.

*  `number`{: .type } scroll_height

> The height of this element's content. This will be at least as high as the client height. Read-only.

*  `number`{: .type } scroll_left

> The offset between the left edge of this element's client area and the left edge of the content area.

*  `number`{: .type } offset_width

> The width of the element, excluding margins. Read-only.

*  `string`{: .type } id

> The ID of the element, or the empty string if the element has no ID.

*  `nil`{: .type }, `Element`{: .type } first_child

> The first child of the element, or None if the client has no children. Read-only.

*  `nil`{: .type }, `Element`{: .type } last_child

> The last child of the element, or None if the client has no children. Read-only.

*  `number`{: .type } client_left

> The distance between the left border edge and the left client edge of the element. Read-only.

*  `ElementChildNodesProxy`{: .type } child_nodes

> The array of child nodes on the element. Read-only.

*  `nil`{: .type }, `Element`{: .type } previous_sibling

> The element's previous sibling, or None if it is the first sibling. Read-only.

*  `number`{: .type } client_height

> The height of the element's client area. Read-only.

*  `number`{: .type } scroll_top

> The offset between the top edge of this element's client area and the top edge of the content area.

*  `number`{: .type } offset_top

> The distance between the element's offset parent's top border edge and this element's top border edge. Read-only.

*  `ElementStyleProxy`{: .type } style

> An object used to access this element's style information. Individual RCSS properties can be accessed by using the name of the property as a Python property on the object itself (ie, element.style.width = "40px").

*  `number`{: .type } scroll_width

> The width of this element's content. This will be at least as wide as the client width. Read-only.

*  `number`{: .type } client_top

> The distance between the top border edge and the top client edge of the element. Read-only.

*  `number`{: .type } offset_left

> The distance between the element's offset parent's left border edge and this element's left border edge. Read-only.

*  `number`{: .type } offset_height

> The height of the element, excluding margins. Read-only.

*  `string`{: .type } tag_name

> The tag name used to instance this element. Read-only.

*  `string`{: .type } inner_rml

> The element's RML content.

*  `number`{: .type } client_width

> The width of the element's client area. Read-only.

*  `ElementAttributesProxy`{: .type } attributes

> The array of attributes on the element. Each element has the read-only properties name and value. Read-only.

*  `nil`{: .type }, `Element`{: .type } parent_node

> The element this element is directly parented to. Read-only.



### Method Descriptions

* `nil`{: .type} AddEventListener(`BOOL`{: .type } event, `string`{: .type } listener[, `lua_type`{: .type } in_capture_phase])

> NOTE: Events added from python cannot be removed.

* `nil`{: .type} SetAttribute(`string`{: .type } name, `string`{: .type } value)

> Sets the value of the attribute named name to value.

*  `boolean`{: .type } RemoveChild(`Element`{: .type } element)

> Removes the child element element from this element.

*  `Element`{: .type } GetById(`string`{: .type } id)

> Returns the descendant element with an id of id.

*  `boolean`{: .type } HasChildNodes()

> Returns True if the element has at least one child node, false if not.

*  `nil`{: .type } DispatchEvent(`string`{: .type } event, `lua_type`{: .type } parameters, `string`{: .type } interruptible)

> Dispatches an event to this element. The event is of type event. Parameters to the event are given in the dictionary parameters; the dictionary must only contain string keys and floating-point, integer or string values. interruptible determines if the event can be forced to stop propagation early.

* `nil`{: .type} AppendChild(`ElementPtr`{: .type } element)

> Appends element as a child to this element.

* `nil`{: .type} RemoveAttribute(`string`{: .type } name)

> Removes the attribute named name from the element.

*  `Variant`{: .type } GetAttribute(`string`{: .type } name)

> Returns the value of the attribute named name. If no such attribute exists, the empty string will be returned.

*  `integer`{: .type }, `Element`{: .type }, `settable`{: .type } GetsByTagName(`string`{: .type } tag_name)

> Returns a list of all descendant elements with the tag of tag_name.

*  `boolean`{: .type } IsClassSet(`string`{: .type } name)

> Returns true if the class name is set on the element, false if not.

* `nil`{: .type} ScrollIntoView(`BOOL`{: .type } align_with_top)

> Scrolls this element into view if its ancestors have hidden overflow. If align_with_top is True, the element's top edge will be aligned with the top (or as close as possible to the top) of its ancestors' viewing windows. If False, its bottom edge will be aligned to the bottom.

* `nil`{: .type} SetClass(`string`{: .type } name, `BOOL`{: .type } value)

> Sets (if value is true) or clears (if value is false) the class name on the element.

* `nil`{: .type} Blur()

> Removes input focus from this element.

* `nil`{: .type} InsertBefore(`ElementPtr`{: .type } element, `Element`{: .type } adjacent_element)

> Inserts the element element as a child of this element, directly before adjacent_element in the list of children.

* `nil`{: .type} new()

> 

* `nil`{: .type} Focus()

> Gives input focus to this element.

*  `boolean`{: .type } HasAttribute(`string`{: .type } name)

> Returns True if the element has a value for the attribute named name, False if not.

*  `boolean`{: .type } ReplaceChild(`ElementPtr`{: .type } inserted_element, `Element`{: .type } replaced_element)

> Replaces the child element replaced_element with inserted_element in this element's list of children. If replaced_element is not a child of this element, inserted_element will be appended onto the list instead.

* `nil`{: .type} Click()

> Fakes a click on this element.



## ElementFormControl

Inherits: `Element`{: .type }



### Properties

| Types | Name |
| ------------ | ---- |
| `boolean`{: .type } | disabled |
| `string`{: .type } | name |
| `string`{: .type } | value |


### Methods




### Metafunctions




### Property Descriptions

*  `boolean`{: .type } disabled

> 

*  `string`{: .type } name

> 

*  `string`{: .type } value

> 



### Method Descriptions



## Context

Inherits: `nil`{: .type }

The Context class has no constructor; it must be instantiated through the CreateContext() function. It has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `Element`{: .type } | focus_element |
| `Vector2i`{: .type } | dimensions |
| `Element`{: .type } | hover_element |
| `Element`{: .type } | root_element |
| `ContextDocumentsProxy`{: .type } | documents |
| `string`{: .type } | name |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | LoadMouseCursor() |
| `Document`{: .type }<br> | LoadDocument(`string`{: .type } document_path) |
| `boolean`{: .type }<br> | Render() |
| `nil`{: .type } | UnloadAllMouseCursors() |
| `Document`{: .type }<br> | CreateDocument(`string`{: .type } tag) |
| `nil`{: .type } | UnloadDocument(`Document`{: .type } document) |
| `boolean`{: .type }<br> | Update() |
| `nil`{: .type } | AddMouseCursor() |
| `nil`{: .type } | ShowMouseCursor() |
| `nil`{: .type } | AddEventListener(`string`{: .type } event, `Element`{: .type } script, `BOOL`{: .type } element_context, `lua_type`{: .type } in_capture_phase) |
| `nil`{: .type } | UnloadAllDocuments() |
| `nil`{: .type } | UnloadMouseCursor() |


### Metafunctions




### Property Descriptions

*  `Element`{: .type } focus_element

> Returns the leaf of the context's focus tree. Read-only.

*  `Vector2i`{: .type } dimensions

> The dimensions of the context, as a Vector2i type.

*  `Element`{: .type } hover_element

> Returns the element under the context's cursor. Read-only.

*  `Element`{: .type } root_element

> Returns the context's root element. Read-only.

*  `ContextDocumentsProxy`{: .type } documents

> Returns an array of the documents within the context. This can be looked up as an array or a dictionary. Read-only.

*  `string`{: .type } name

> The name of the context, specified at construction. Read-only.



### Method Descriptions

* `nil`{: .type} LoadMouseCursor()

> Attempts to load a document from the RML file found at cursor_document_path as a cursor. If successful, the cursor's document will be returned with a reference count of one.

*  `Document`{: .type } LoadDocument(`string`{: .type } document_path)

> Attempts to load a document from the RML file found at document_path. If successful, the document will be returned with a reference count of one.

*  `boolean`{: .type } Render()

> Renders the context.

* `nil`{: .type} UnloadAllMouseCursors()

> Unloads all cursors currently loaded with the context.

*  `Document`{: .type } CreateDocument(`string`{: .type } tag)

> Creates a new document with the tag name of tag.

* `nil`{: .type} UnloadDocument(`Document`{: .type } document)

> Unloads a specific document within the context.

*  `boolean`{: .type } Update()

> Updates the context.

* `nil`{: .type} AddMouseCursor()

> Adds a cursor document loaded by another context into this context. The cursor document will be returned.

* `nil`{: .type} ShowMouseCursor()

> If show is True, this shows the mouse cursor, otherwise hides it.

* `nil`{: .type} AddEventListener(`string`{: .type } event, `Element`{: .type } script, `BOOL`{: .type } element_context, `lua_type`{: .type } in_capture_phase)

> Adds the inline Python script, script, as an event listener to the context. element_context is an optional Element; if it is not None, then the script will be executed as if it was bound to that element.

* `nil`{: .type} UnloadAllDocuments()

> Closes all documents currently loaded with the context.

* `nil`{: .type} UnloadMouseCursor()

> Unloads a specific cursor by name.



## ElementFormControlInput

Inherits: `ElementFormControl`{: .type }

ElementFormControlInput derives from IElementFormControl. The control has the following properties, only appropriate on the relevant types:

### Properties

| Types | Name |
| ------------ | ---- |
| `boolean`{: .type } | checked |
| `integer`{: .type } | min |
| `integer`{: .type } | max |
| `integer`{: .type } | step |
| `nil`{: .type } | max_length |
| `integer`{: .type } | maxlength |
| `integer`{: .type } | size |


### Methods




### Metafunctions




### Property Descriptions

*  `boolean`{: .type } checked

> Relevant for radio and checkbox types. The checked status of the input.

*  `integer`{: .type } min

> Relevant for range types. The value of the control on the top / left of the slider.

*  `integer`{: .type } max

> Relevant for range types. The value of the control on the bottom / right of the slider.

*  `integer`{: .type } step

> Relevant for range types. The step the control's value changes in.

* `nil`{: .type } max_length

> Relevant for text types. The maximum number of characters permitted in the text field.

*  `integer`{: .type } maxlength

> 

*  `integer`{: .type } size

> Relevant for text types. The approximate number of characters the text field shows horizontally at once.



### Method Descriptions



## ElementFormControlTextArea

Inherits: `ElementFormControl`{: .type }

ElementFormControlTextArea derives from IElementFormControl. The control has the following properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `integer`{: .type } | rows |
| `integer`{: .type } | cols |
| `nil`{: .type } | max_length |
| `boolean`{: .type } | wordwrap |
| `nil`{: .type } | word_wrap |
| `integer`{: .type } | maxlength |


### Methods




### Metafunctions




### Property Descriptions

*  `integer`{: .type } rows

> The number of lines the text area shows at once.

*  `integer`{: .type } cols

> The approximate number of characters the text area shows horizontally at once.

* `nil`{: .type } max_length

> The maximum number of characters permitted in the text area.

*  `boolean`{: .type } wordwrap

> 

* `nil`{: .type } word_wrap

> True if lines are split to fit into the text area, False if not.

*  `integer`{: .type } maxlength

> 



### Method Descriptions



## ElementFormControlSelect

Inherits: `ElementFormControl`{: .type }

ElementFormControlSelect derives from IElementFormControl. The control has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `integer`{: .type } | selection |
| `SelectOptionsProxy`{: .type } | options |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | RemoveAll() |
| `integer`{: .type }<br> | Add(`string`{: .type } rml, `string`{: .type } value[, `integer`{: .type } before]) |
| `nil`{: .type } | Remove(`integer`{: .type } index) |


### Metafunctions




### Property Descriptions

*  `integer`{: .type } selection

> The index of the currently selected option.

*  `SelectOptionsProxy`{: .type } options

> The array of options available in the select box. Each entry in the array has the property value, the string value of the option, and element, the root of the element hierarchy that represents the option in the list.



### Method Descriptions

* `nil`{: .type} RemoveAll()

> 

*  `integer`{: .type } Add(`string`{: .type } rml, `string`{: .type } value[, `integer`{: .type } before])

> Adds a new option to the select box. The new option has the string value of value and is represented by the elements created by the RML string rml. The new option will be inserted by the index specified by before; if this is out of bounds (the default), then the new option will be appended onto the list. The index of the new option will be returned.

* `nil`{: .type} Remove(`integer`{: .type } index)

> Removes an existing option from the selection box.



## GlobalLuaFunctions

Inherits: `nil`{: .type }



### Properties

| Types | Name |
| ------------ | ---- |
| `nil`{: .type } | ipairsaux |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | LuaPrint() |


### Metafunctions




### Property Descriptions

* `nil`{: .type } ipairsaux

> 



### Method Descriptions

* `nil`{: .type} LuaPrint()

> 



## LuaRmlUi

Inherits: `nil`{: .type }



### Properties

| Types | Name |
| ------------ | ---- |
| `RmlUiContextsProxy`{: .type } | contexts |
| `nil`{: .type } | key_identifier |
| `nil`{: .type } | key_modifier |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type }<br>`Context`{: .type }<br> | CreateContext(`string`{: .type } ) |
| `nil`{: .type } | RegisterTag(`string`{: .type } ) |
| `boolean`{: .type }<br> | LoadFontFace(`string`{: .type } ) |


### Metafunctions




### Property Descriptions

*  `RmlUiContextsProxy`{: .type } contexts

> 

* `nil`{: .type } key_identifier

> 

* `nil`{: .type } key_modifier

> 



### Method Descriptions

*  `nil`{: .type }, `Context`{: .type } CreateContext(`string`{: .type } )

> 

* `nil`{: .type} RegisterTag(`string`{: .type } )

> 

*  `boolean`{: .type } LoadFontFace(`string`{: .type } )

> 



## EventParametersProxy

Inherits: `nil`{: .type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __index |
| __pairs |
| __ipairs |


### Property Descriptions



### Method Descriptions



## ElementTabSet

Inherits: `Element`{: .type }

ElementTabSet derives from Element. The control has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `integer`{: .type } | active_tab |
| `integer`{: .type } | num_tabs |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | SetPanel(`integer`{: .type } index, `string`{: .type } rml) |
| `nil`{: .type } | SetTab(`integer`{: .type } index, `string`{: .type } rml) |


### Metafunctions




### Property Descriptions

*  `integer`{: .type } active_tab

> Index of the active panel.

*  `integer`{: .type } num_tabs

> The number of tabs in the tab set. Read-only.



### Method Descriptions

* `nil`{: .type} SetPanel(`integer`{: .type } index, `string`{: .type } rml)

> Sets the contents of a panel to the RML content rml. If index is out-of-bounds, a new panel will be added at the end.

* `nil`{: .type} SetTab(`integer`{: .type } index, `string`{: .type } rml)

> Sets the contents of a tab to the RML content rml. If index is out-of-bounds, a new tab will be added at the end.



## IElementFormControl

Inherits: `nil`{: .type }

IElementFormControl derives from Element. The form element control has the following properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `nil`{: .type } | disabled |
| `nil`{: .type } | name |
| `nil`{: .type } | value |


### Methods




### Metafunctions




### Property Descriptions

* `nil`{: .type } disabled

> The disabled status of the control, either True or False.

* `nil`{: .type } name

> The name of the control, initial set with the "name" attribute.

* `nil`{: .type } value

> The current value of the control.



### Method Descriptions



## DataSource

Inherits: `nil`{: .type }

Abstract DataSource Interface.

### Properties




### Methods

| Return value | Name |
| ------------ | ---- |
| `value`{: .type }<br> | GetNumRows(`DataSource`{: .type } table_name) |
| `nil`{: .type } | NotifyRowAdd(`string`{: .type } table_name, `integer`{: .type } first_row_added, `integer`{: .type } num_rows_added) |
| `value`{: .type }<br> | GetRow(`DataSource`{: .type } table_name, `lua_type`{: .type } index) |
| `nil`{: .type } | NotifyRowChange(`string`{: .type } table_name) |
| `nil`{: .type } | NotifyRowRemove(`string`{: .type } table_name, `integer`{: .type } first_row_removed, `integer`{: .type } num_rows_removed) |


### Metafunctions




### Property Descriptions



### Method Descriptions

*  `value`{: .type } GetNumRows(`DataSource`{: .type } table_name)

> Return the number of rows in the given table

* `nil`{: .type} NotifyRowAdd(`string`{: .type } table_name, `integer`{: .type } first_row_added, `integer`{: .type } num_rows_added)

> Notify listeners that rows have been added to the data source.

*  `value`{: .type } GetRow(`DataSource`{: .type } table_name, `lua_type`{: .type } index)

> Return a list of the column values in string form

* `nil`{: .type} NotifyRowChange(`string`{: .type } table_name)

> Notify listeners that all rows on the data source have changed.

* `nil`{: .type} NotifyRowRemove(`string`{: .type } table_name, `integer`{: .type } first_row_removed, `integer`{: .type } num_rows_removed)

> Notify listeners that rows have been removed from the data source.



## Event

Inherits: `nil`{: .type }

The Event class has no constructor; it is generated internally. It has the following methods and properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `Element`{: .type } | target_element |
| `string`{: .type } | type |
| `EventParametersProxy`{: .type } | parameters |
| `Element`{: .type } | current_element |


### Methods

| Return value | Name |
| ------------ | ---- |
| `nil`{: .type } | StopPropagation() |


### Metafunctions




### Property Descriptions

*  `Element`{: .type } target_element

> The element the event was originally targeted at. Read-only.

*  `string`{: .type } type

> The string name of the event. Read-only.

*  `EventParametersProxy`{: .type } parameters

> A dictionary like object containing all the parameters in the event.

*  `Element`{: .type } current_element

> The element the event has propagated to. Read-only.



### Method Descriptions

* `nil`{: .type} StopPropagation()

> Stops the propagation of the event through the event cycle, if allowed.



## ElementDataGridRow

Inherits: `Element`{: .type }

ElementDataGridRow derives from Element. The data grid row has the following properties:

### Properties

| Types | Name |
| ------------ | ---- |
| `boolean`{: .type } | row_expanded |
| `ElementDataGrid`{: .type } | parent_grid |
| `integer`{: .type } | parent_relative_index |
| `ElementDataGridRow`{: .type } | parent_row |
| `integer`{: .type } | table_relative_index |


### Methods




### Metafunctions




### Property Descriptions

*  `boolean`{: .type } row_expanded

> The expanded state of the row, either True or False.

*  `ElementDataGrid`{: .type } parent_grid

> The data grid that this row belongs to.

*  `integer`{: .type } parent_relative_index

> The index of the row, relative to its parent row. So if you are the third row in your parent, then it will be 3.

*  `ElementDataGridRow`{: .type } parent_row

> The parent row of this row. None if it at the top level.

*  `integer`{: .type } table_relative_index

> The index of the row, relative to the data grid it is in. This takes into account all previous rows and their children.



### Method Descriptions


