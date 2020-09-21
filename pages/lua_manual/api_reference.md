---
layout: page
title: Lua API Reference
status: improve
---

All instantiable classes define a `new()` method which returns an object of that particular class. 

With the exception of this `new()` method, all members listed will be member methods.

| Contents |
| -------- |
| [Colourb](#Colourb) |
| [Colourf](#Colourf) |
| [Context](#Context) |
| [ContextDocumentsProxy](#ContextDocumentsProxy) |
| [DataFormatter](#DataFormatter) |
| [DataSource](#DataSource) |
| [Document](#Document) |
| [Element](#Element) |
| [ElementAttributesProxy](#ElementAttributesProxy) |
| [ElementChildNodesProxy](#ElementChildNodesProxy) |
| [ElementDataGrid](#ElementDataGrid) |
| [ElementDataGridRow](#ElementDataGridRow) |
| [ElementForm](#ElementForm) |
| [ElementFormControl](#ElementFormControl) |
| [ElementFormControlDataSelect](#ElementFormControlDataSelect) |
| [ElementFormControlInput](#ElementFormControlInput) |
| [ElementFormControlSelect](#ElementFormControlSelect) |
| [ElementFormControlTextArea](#ElementFormControlTextArea) |
| [ElementInstancer](#ElementInstancer) |
| [ElementPtr](#ElementPtr) |
| [ElementStyleProxy](#ElementStyleProxy) |
| [ElementTabSet](#ElementTabSet) |
| [ElementText](#ElementText) |
| [Event](#Event) |
| [EventParametersProxy](#EventParametersProxy) |
| [GlobalLuaFunctions](#GlobalLuaFunctions) |
| [IElementFormControl](#IElementFormControl) |
| [IElementText](#IElementText) |
| [Log](#Log) |
| [LuaDataSource](#LuaDataSource) |
| [LuaRmlUi](#LuaRmlUi) |
| [RmlUiContextsProxy](#RmlUiContextsProxy) |
| [SelectOptionsProxy](#SelectOptionsProxy) |
| [Vector2f](#Vector2f) |
| [Vector2i](#Vector2i) |


---


## <a href='#Colourb' name='Colourb'>Colourb</a>

Inherits: `nil`{: .lua-type }

Constructs a colour with four channels, each from 0 to 255.

### Properties

| Name | Type |
| ------------ | ---- |
| [alpha](#Colourb-alpha){: .lua-method } | `integer`{: .lua-type } |
| [blue](#Colourb-blue){: .lua-method } | `integer`{: .lua-type } |
| [green](#Colourb-green){: .lua-method } | `integer`{: .lua-type } |
| [red](#Colourb-red){: .lua-method } | `integer`{: .lua-type } |
| [rgba](#Colourb-rgba){: .lua-method } | `integer`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `Colourb`{: .lua-type} | [new](#Colourb-new){: .lua-method }() |


### Metafunctions

| Metafunctions |
| ------------- |
| __add |
| __eq |
| __mul |


### Property Descriptions

####  `integer`{: .lua-type } <a name='Colourb-alpha'>alpha</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='Colourb-blue'>blue</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='Colourb-green'>green</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='Colourb-red'>red</a>{: .lua-method }



####  `integer`{: .lua-type }, `integer`{: .lua-type }, `integer`{: .lua-type }, `integer`{: .lua-type } <a name='Colourb-rgba'>rgba</a>{: .lua-method }





### Method Descriptions

#### `nil`{: .lua-type} <a name='Colourb-new'>new</a>{: .lua-method }()





---

## <a href='#Colourf' name='Colourf'>Colourf</a>

Inherits: `nil`{: .lua-type }



### Properties

| Name | Type |
| ------------ | ---- |
| [alpha](#Colourf-alpha){: .lua-method } | `number`{: .lua-type } |
| [blue](#Colourf-blue){: .lua-method } | `number`{: .lua-type } |
| [green](#Colourf-green){: .lua-method } | `number`{: .lua-type } |
| [red](#Colourf-red){: .lua-method } | `number`{: .lua-type } |
| [rgba](#Colourf-rgba){: .lua-method } | `number`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `Colourf`{: .lua-type} | [new](#Colourf-new){: .lua-method }() |


### Metafunctions

| Metafunctions |
| ------------- |
| __eq |


### Property Descriptions

####  `number`{: .lua-type } <a name='Colourf-alpha'>alpha</a>{: .lua-method }



####  `number`{: .lua-type } <a name='Colourf-blue'>blue</a>{: .lua-method }



####  `number`{: .lua-type } <a name='Colourf-green'>green</a>{: .lua-method }



####  `number`{: .lua-type } <a name='Colourf-red'>red</a>{: .lua-method }



####  `number`{: .lua-type }, `number`{: .lua-type }, `number`{: .lua-type }, `number`{: .lua-type } <a name='Colourf-rgba'>rgba</a>{: .lua-method }





### Method Descriptions

#### `nil`{: .lua-type} <a name='Colourf-new'>new</a>{: .lua-method }()





---

## <a href='#Context' name='Context'>Context</a>

Inherits: `nil`{: .lua-type }

The Context class has no constructor; it must be instantiated through the CreateContext() function. It has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [dimensions](#Context-dimensions){: .lua-method } | `Vector2i`{: .lua-type } |
| [documents](#Context-documents){: .lua-method } | `ContextDocumentsProxy`{: .lua-type } |
| [focus_element](#Context-focus_element){: .lua-method } | `Element`{: .lua-type } |
| [hover_element](#Context-hover_element){: .lua-method } | `Element`{: .lua-type } |
| [name](#Context-name){: .lua-method } | `string`{: .lua-type } |
| [root_element](#Context-root_element){: .lua-method } | `Element`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [AddEventListener](#Context-AddEventListener){: .lua-method }(`string`{: .lua-type } event, `Element`{: .lua-type } script, `boolean`{: .lua-type } element_context, `lua_type`{: .lua-type } in_capture_phase) |
| `Document`{: .lua-type }<br> | [CreateDocument](#Context-CreateDocument){: .lua-method }(`string`{: .lua-type } tag) |
| `Document`{: .lua-type }<br> | [LoadDocument](#Context-LoadDocument){: .lua-method }(`string`{: .lua-type } document_path) |
| `boolean`{: .lua-type }<br> | [Render](#Context-Render){: .lua-method }() |
| `nil`{: .lua-type } | [UnloadAllDocuments](#Context-UnloadAllDocuments){: .lua-method }() |
| `nil`{: .lua-type } | [UnloadDocument](#Context-UnloadDocument){: .lua-method }(`Document`{: .lua-type } document) |
| `boolean`{: .lua-type }<br> | [Update](#Context-Update){: .lua-method }() |


### Metafunctions




### Property Descriptions

####  `Vector2i`{: .lua-type } <a name='Context-dimensions'>dimensions</a>{: .lua-method }

The dimensions of the context, as a Vector2i type.

####  `ContextDocumentsProxy`{: .lua-type } <a name='Context-documents'>documents</a>{: .lua-method }

Returns an array of the documents within the context. This can be looked up as an array or a dictionary. Read-only.

####  `Element`{: .lua-type } <a name='Context-focus_element'>focus_element</a>{: .lua-method }

Returns the leaf of the context's focus tree. Read-only.

####  `Element`{: .lua-type } <a name='Context-hover_element'>hover_element</a>{: .lua-method }

Returns the element under the context's cursor. Read-only.

####  `string`{: .lua-type } <a name='Context-name'>name</a>{: .lua-method }

The name of the context, specified at construction. Read-only.

####  `Element`{: .lua-type } <a name='Context-root_element'>root_element</a>{: .lua-method }

Returns the context's root element. Read-only.



### Method Descriptions

#### `nil`{: .lua-type} <a name='Context-AddEventListener'>AddEventListener</a>{: .lua-method }(`string`{: .lua-type } event, `Element`{: .lua-type } script, `boolean`{: .lua-type } element_context, `lua_type`{: .lua-type } in_capture_phase)

Adds the inline Python script, script, as an event listener to the context. element_context is an optional Element; if it is not None, then the script will be executed as if it was bound to that element.

####  `Document`{: .lua-type } <a name='Context-CreateDocument'>CreateDocument</a>{: .lua-method }(`string`{: .lua-type } tag)

Creates a new document with the tag name of tag.

####  `Document`{: .lua-type } <a name='Context-LoadDocument'>LoadDocument</a>{: .lua-method }(`string`{: .lua-type } document_path)

Attempts to load a document from the RML file found at document_path. If successful, the document will be returned with a reference count of one.

####  `boolean`{: .lua-type } <a name='Context-Render'>Render</a>{: .lua-method }()

Renders the context.

#### `nil`{: .lua-type} <a name='Context-UnloadAllDocuments'>UnloadAllDocuments</a>{: .lua-method }()

Closes all documents currently loaded with the context.

#### `nil`{: .lua-type} <a name='Context-UnloadDocument'>UnloadDocument</a>{: .lua-method }(`Document`{: .lua-type } document)

Unloads a specific document within the context.

####  `boolean`{: .lua-type } <a name='Context-Update'>Update</a>{: .lua-method }()

Updates the context.



---

## <a href='#ContextDocumentsProxy' name='ContextDocumentsProxy'>ContextDocumentsProxy</a>

Inherits: `nil`{: .lua-type }



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



---

## <a href='#DataFormatter' name='DataFormatter'>DataFormatter</a>

Inherits: `nil`{: .lua-type }



### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `DataFormatter`{: .lua-type} | [new](#DataFormatter-new){: .lua-method }() |
| `value`{: .lua-type }<br> | [FormatData](#DataFormatter-FormatData){: .lua-method }(`DataFormatter`{: .lua-type } ) |


### Metafunctions




### Property Descriptions



### Method Descriptions

#### `nil`{: .lua-type} <a name='DataFormatter-new'>new</a>{: .lua-method }()



####  `value`{: .lua-type } <a name='DataFormatter-FormatData'>FormatData</a>{: .lua-method }(`DataFormatter`{: .lua-type } )





---

## <a href='#DataSource' name='DataSource'>DataSource</a>

Inherits: `nil`{: .lua-type }

Abstract DataSource Interface.

### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `value`{: .lua-type }<br> | [GetNumRows](#DataSource-GetNumRows){: .lua-method }(`DataSource`{: .lua-type } table_name) |
| `value`{: .lua-type }<br> | [GetRow](#DataSource-GetRow){: .lua-method }(`DataSource`{: .lua-type } table_name, `lua_type`{: .lua-type } index) |
| `nil`{: .lua-type } | [NotifyRowAdd](#DataSource-NotifyRowAdd){: .lua-method }(`string`{: .lua-type } table_name, `integer`{: .lua-type } first_row_added, `integer`{: .lua-type } num_rows_added) |
| `nil`{: .lua-type } | [NotifyRowChange](#DataSource-NotifyRowChange){: .lua-method }(`string`{: .lua-type } table_name) |
| `nil`{: .lua-type } | [NotifyRowRemove](#DataSource-NotifyRowRemove){: .lua-method }(`string`{: .lua-type } table_name, `integer`{: .lua-type } first_row_removed, `integer`{: .lua-type } num_rows_removed) |


### Metafunctions




### Property Descriptions



### Method Descriptions

####  `value`{: .lua-type } <a name='DataSource-GetNumRows'>GetNumRows</a>{: .lua-method }(`DataSource`{: .lua-type } table_name)

Return the number of rows in the given table

####  `value`{: .lua-type } <a name='DataSource-GetRow'>GetRow</a>{: .lua-method }(`DataSource`{: .lua-type } table_name, `lua_type`{: .lua-type } index)

Return a list of the column values in string form

#### `nil`{: .lua-type} <a name='DataSource-NotifyRowAdd'>NotifyRowAdd</a>{: .lua-method }(`string`{: .lua-type } table_name, `integer`{: .lua-type } first_row_added, `integer`{: .lua-type } num_rows_added)

Notify listeners that rows have been added to the data source.

#### `nil`{: .lua-type} <a name='DataSource-NotifyRowChange'>NotifyRowChange</a>{: .lua-method }(`string`{: .lua-type } table_name)

Notify listeners that all rows on the data source have changed.

#### `nil`{: .lua-type} <a name='DataSource-NotifyRowRemove'>NotifyRowRemove</a>{: .lua-method }(`string`{: .lua-type } table_name, `integer`{: .lua-type } first_row_removed, `integer`{: .lua-type } num_rows_removed)

Notify listeners that rows have been removed from the data source.



---

## <a href='#Document' name='Document'>Document</a>

Inherits: `Element`{: .lua-type }

Document derives from Element. Document has no constructor; it must be instantiated through a Context object instead, either by loading an external RML file or creating an empty document. It has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [context](#Document-context){: .lua-method } | `Context`{: .lua-type } |
| [title](#Document-title){: .lua-method } | `string`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [Close](#Document-Close){: .lua-method }() |
| `ElementPtr`{: .lua-type }<br> | [CreateElement](#Document-CreateElement){: .lua-method }(`string`{: .lua-type } tag_name) |
| `ElementPtr`{: .lua-type }<br> | [CreateTextNode](#Document-CreateTextNode){: .lua-method }(`string`{: .lua-type } text) |
| `nil`{: .lua-type } | [Hide](#Document-Hide){: .lua-method }() |
| `nil`{: .lua-type } | [PullToFront](#Document-PullToFront){: .lua-method }() |
| `nil`{: .lua-type } | [PushToBack](#Document-PushToBack){: .lua-method }() |
| `nil`{: .lua-type } | [Show](#Document-Show){: .lua-method }(`integer`{: .lua-type } [flags]) |


### Metafunctions




### Property Descriptions

####  `Context`{: .lua-type } <a name='Document-context'>context</a>{: .lua-method }

The context the document belongs to. Read-only.

####  `string`{: .lua-type } <a name='Document-title'>title</a>{: .lua-method }

The title of the document, as initially set by the \<title\> tag in the document's header.



### Method Descriptions

#### `nil`{: .lua-type} <a name='Document-Close'>Close</a>{: .lua-method }()

Hides and closes the document, destroying its contents.

####  `ElementPtr`{: .lua-type } <a name='Document-CreateElement'>CreateElement</a>{: .lua-method }(`string`{: .lua-type } tag_name)

Instances an element with a tag of tag_name.

####  `ElementPtr`{: .lua-type } <a name='Document-CreateTextNode'>CreateTextNode</a>{: .lua-method }(`string`{: .lua-type } text)

Instances a text element containing the string text.

#### `nil`{: .lua-type} <a name='Document-Hide'>Hide</a>{: .lua-method }()

Hides the document.

#### `nil`{: .lua-type} <a name='Document-PullToFront'>PullToFront</a>{: .lua-method }()

Pulls the document in front of other documents within its context with a similar z-index.

#### `nil`{: .lua-type} <a name='Document-PushToBack'>PushToBack</a>{: .lua-method }()

Pushes the document behind other documents within its context with a similar z-index.

#### `nil`{: .lua-type} <a name='Document-Show'>Show</a>{: .lua-method }(`integer`{: .lua-type } [flags])

Shows the document. flags is either NONE, FOCUS or MODAL. flags defaults to FOCUS.



---

## <a href='#Element' name='Element'>Element</a>

Inherits: `nil`{: .lua-type }

The Element class has no constructor; it must be instantiated through a [Document](#document) object instead. It has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [attributes](#Element-attributes){: .lua-method } | `ElementAttributesProxy`{: .lua-type } |
| [child_nodes](#Element-child_nodes){: .lua-method } | `ElementChildNodesProxy`{: .lua-type } |
| [class_name](#Element-class_name){: .lua-method } | `string`{: .lua-type } |
| [client_height](#Element-client_height){: .lua-method } | `number`{: .lua-type } |
| [client_left](#Element-client_left){: .lua-method } | `number`{: .lua-type } |
| [client_top](#Element-client_top){: .lua-method } | `number`{: .lua-type } |
| [client_width](#Element-client_width){: .lua-method } | `number`{: .lua-type } |
| [first_child](#Element-first_child){: .lua-method } | `nil`{: .lua-type } |
| [id](#Element-id){: .lua-method } | `string`{: .lua-type } |
| [inner_rml](#Element-inner_rml){: .lua-method } | `string`{: .lua-type } |
| [last_child](#Element-last_child){: .lua-method } | `nil`{: .lua-type } |
| [next_sibling](#Element-next_sibling){: .lua-method } | `nil`{: .lua-type } |
| [offset_height](#Element-offset_height){: .lua-method } | `number`{: .lua-type } |
| [offset_left](#Element-offset_left){: .lua-method } | `number`{: .lua-type } |
| [offset_parent](#Element-offset_parent){: .lua-method } | `Element`{: .lua-type } |
| [offset_top](#Element-offset_top){: .lua-method } | `number`{: .lua-type } |
| [offset_width](#Element-offset_width){: .lua-method } | `number`{: .lua-type } |
| [owner_document](#Element-owner_document){: .lua-method } | `Document`{: .lua-type } |
| [parent_node](#Element-parent_node){: .lua-method } | `nil`{: .lua-type } |
| [previous_sibling](#Element-previous_sibling){: .lua-method } | `nil`{: .lua-type } |
| [scroll_height](#Element-scroll_height){: .lua-method } | `number`{: .lua-type } |
| [scroll_left](#Element-scroll_left){: .lua-method } | `number`{: .lua-type } |
| [scroll_top](#Element-scroll_top){: .lua-method } | `number`{: .lua-type } |
| [scroll_width](#Element-scroll_width){: .lua-method } | `number`{: .lua-type } |
| [style](#Element-style){: .lua-method } | `ElementStyleProxy`{: .lua-type } |
| [tag_name](#Element-tag_name){: .lua-method } | `string`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [AddEventListener](#Element-AddEventListener){: .lua-method }(`boolean`{: .lua-type } event, `string`{: .lua-type } listener[, `lua_type`{: .lua-type } in_capture_phase]) |
| `nil`{: .lua-type } | [AppendChild](#Element-AppendChild){: .lua-method }(`ElementPtr`{: .lua-type } element) |
| `nil`{: .lua-type } | [Blur](#Element-Blur){: .lua-method }() |
| `nil`{: .lua-type } | [Click](#Element-Click){: .lua-method }() |
| `nil`{: .lua-type }<br> | [DispatchEvent](#Element-DispatchEvent){: .lua-method }(`string`{: .lua-type } event, `lua_type`{: .lua-type } parameters, `string`{: .lua-type } interruptible) |
| `Element`{: .lua-type} | [new](#Element-new){: .lua-method }() |
| `nil`{: .lua-type } | [Focus](#Element-Focus){: .lua-method }() |
| `Variant`{: .lua-type }<br> | [GetAttribute](#Element-GetAttribute){: .lua-method }(`string`{: .lua-type } name) |
| `Element`{: .lua-type }<br> | [GetElementById](#Element-GetElementById){: .lua-method }(`string`{: .lua-type } id) |
| `integer`{: .lua-type }<br>`Element`{: .lua-type }<br>`settable`{: .lua-type }<br> | [GetElementsByTagName](#Element-GetElementsByTagName){: .lua-method }(`string`{: .lua-type } tag_name) |
| `boolean`{: .lua-type }<br> | [HasAttribute](#Element-HasAttribute){: .lua-method }(`string`{: .lua-type } name) |
| `boolean`{: .lua-type }<br> | [HasChildNodes](#Element-HasChildNodes){: .lua-method }() |
| `nil`{: .lua-type } | [InsertBefore](#Element-InsertBefore){: .lua-method }(`ElementPtr`{: .lua-type } element, `Element`{: .lua-type } adjacent_element) |
| `boolean`{: .lua-type }<br> | [IsClassSet](#Element-IsClassSet){: .lua-method }(`string`{: .lua-type } name) |
| `nil`{: .lua-type } | [RemoveAttribute](#Element-RemoveAttribute){: .lua-method }(`string`{: .lua-type } name) |
| `boolean`{: .lua-type }<br> | [RemoveChild](#Element-RemoveChild){: .lua-method }(`Element`{: .lua-type } element) |
| `boolean`{: .lua-type }<br> | [ReplaceChild](#Element-ReplaceChild){: .lua-method }(`ElementPtr`{: .lua-type } inserted_element, `Element`{: .lua-type } replaced_element) |
| `nil`{: .lua-type } | [ScrollIntoView](#Element-ScrollIntoView){: .lua-method }(`boolean`{: .lua-type } align_with_top) |
| `nil`{: .lua-type } | [SetAttribute](#Element-SetAttribute){: .lua-method }(`string`{: .lua-type } name, `string`{: .lua-type } value) |
| `nil`{: .lua-type } | [SetClass](#Element-SetClass){: .lua-method }(`string`{: .lua-type } name, `boolean`{: .lua-type } value) |


### Metafunctions




### Property Descriptions

####  `ElementAttributesProxy`{: .lua-type } <a name='Element-attributes'>attributes</a>{: .lua-method }

The array of attributes on the element. Each element has the read-only properties name and value. Read-only.

####  `ElementChildNodesProxy`{: .lua-type } <a name='Element-child_nodes'>child_nodes</a>{: .lua-method }

The array of child nodes on the element. Read-only.

####  `string`{: .lua-type } <a name='Element-class_name'>class_name</a>{: .lua-method }

The space-separated list of classes on the element.

####  `number`{: .lua-type } <a name='Element-client_height'>client_height</a>{: .lua-method }

The height of the element's client area. Read-only.

####  `number`{: .lua-type } <a name='Element-client_left'>client_left</a>{: .lua-method }

The distance between the left border edge and the left client edge of the element. Read-only.

####  `number`{: .lua-type } <a name='Element-client_top'>client_top</a>{: .lua-method }

The distance between the top border edge and the top client edge of the element. Read-only.

####  `number`{: .lua-type } <a name='Element-client_width'>client_width</a>{: .lua-method }

The width of the element's client area. Read-only.

####  `nil`{: .lua-type }, `Element`{: .lua-type } <a name='Element-first_child'>first_child</a>{: .lua-method }

The first child of the element, or None if the client has no children. Read-only.

####  `string`{: .lua-type } <a name='Element-id'>id</a>{: .lua-method }

The ID of the element, or the empty string if the element has no ID.

####  `string`{: .lua-type } <a name='Element-inner_rml'>inner_rml</a>{: .lua-method }

The element's RML content.

####  `nil`{: .lua-type }, `Element`{: .lua-type } <a name='Element-last_child'>last_child</a>{: .lua-method }

The last child of the element, or None if the client has no children. Read-only.

####  `nil`{: .lua-type }, `Element`{: .lua-type } <a name='Element-next_sibling'>next_sibling</a>{: .lua-method }

The element's next sibling, or None if it is the last sibling. Read-only.

####  `number`{: .lua-type } <a name='Element-offset_height'>offset_height</a>{: .lua-method }

The height of the element, excluding margins. Read-only.

####  `number`{: .lua-type } <a name='Element-offset_left'>offset_left</a>{: .lua-method }

The distance between the element's offset parent's left border edge and this element's left border edge. Read-only.

####  `Element`{: .lua-type } <a name='Element-offset_parent'>offset_parent</a>{: .lua-method }

The element's offset parent. Read only.

####  `number`{: .lua-type } <a name='Element-offset_top'>offset_top</a>{: .lua-method }

The distance between the element's offset parent's top border edge and this element's top border edge. Read-only.

####  `number`{: .lua-type } <a name='Element-offset_width'>offset_width</a>{: .lua-method }

The width of the element, excluding margins. Read-only.

####  `Document`{: .lua-type } <a name='Element-owner_document'>owner_document</a>{: .lua-method }

The document this element is part of. Read-only.

####  `nil`{: .lua-type }, `Element`{: .lua-type } <a name='Element-parent_node'>parent_node</a>{: .lua-method }

The element this element is directly parented to. Read-only.

####  `nil`{: .lua-type }, `Element`{: .lua-type } <a name='Element-previous_sibling'>previous_sibling</a>{: .lua-method }

The element's previous sibling, or None if it is the first sibling. Read-only.

####  `number`{: .lua-type } <a name='Element-scroll_height'>scroll_height</a>{: .lua-method }

The height of this element's content. This will be at least as high as the client height. Read-only.

####  `number`{: .lua-type } <a name='Element-scroll_left'>scroll_left</a>{: .lua-method }

The offset between the left edge of this element's client area and the left edge of the content area.

####  `number`{: .lua-type } <a name='Element-scroll_top'>scroll_top</a>{: .lua-method }

The offset between the top edge of this element's client area and the top edge of the content area.

####  `number`{: .lua-type } <a name='Element-scroll_width'>scroll_width</a>{: .lua-method }

The width of this element's content. This will be at least as wide as the client width. Read-only.

####  `ElementStyleProxy`{: .lua-type } <a name='Element-style'>style</a>{: .lua-method }

An object used to access this element's style information. Individual RCSS properties can be accessed by using the name of the property as a Python property on the object itself (ie, element.style.width = "40px").

####  `string`{: .lua-type } <a name='Element-tag_name'>tag_name</a>{: .lua-method }

The tag name used to instance this element. Read-only.



### Method Descriptions

#### `nil`{: .lua-type} <a name='Element-AddEventListener'>AddEventListener</a>{: .lua-method }(`boolean`{: .lua-type } event, `string`{: .lua-type } listener[, `lua_type`{: .lua-type } in_capture_phase])

NOTE: Events added from python cannot be removed.

#### `nil`{: .lua-type} <a name='Element-AppendChild'>AppendChild</a>{: .lua-method }(`ElementPtr`{: .lua-type } element)

Appends element as a child to this element.

#### `nil`{: .lua-type} <a name='Element-Blur'>Blur</a>{: .lua-method }()

Removes input focus from this element.

#### `nil`{: .lua-type} <a name='Element-Click'>Click</a>{: .lua-method }()

Fakes a click on this element.

####  `nil`{: .lua-type } <a name='Element-DispatchEvent'>DispatchEvent</a>{: .lua-method }(`string`{: .lua-type } event, `lua_type`{: .lua-type } parameters, `string`{: .lua-type } interruptible)

Dispatches an event to this element. The event is of type event. Parameters to the event are given in the dictionary parameters; the dictionary must only contain string keys and floating-point, integer or string values. interruptible determines if the event can be forced to stop propagation early.

#### `nil`{: .lua-type} <a name='Element-new'>new</a>{: .lua-method }()



#### `nil`{: .lua-type} <a name='Element-Focus'>Focus</a>{: .lua-method }()

Gives input focus to this element.

####  `Variant`{: .lua-type } <a name='Element-GetAttribute'>GetAttribute</a>{: .lua-method }(`string`{: .lua-type } name)

Returns the value of the attribute named name. If no such attribute exists, the empty string will be returned.

####  `Element`{: .lua-type } <a name='Element-GetById'>GetById</a>{: .lua-method }(`string`{: .lua-type } id)

Returns the descendant element with an id of id.

####  `integer`{: .lua-type }, `Element`{: .lua-type }, `settable`{: .lua-type } <a name='Element-GetsByTagName'>GetsByTagName</a>{: .lua-method }(`string`{: .lua-type } tag_name)

Returns a list of all descendant elements with the tag of tag_name.

####  `boolean`{: .lua-type } <a name='Element-HasAttribute'>HasAttribute</a>{: .lua-method }(`string`{: .lua-type } name)

Returns True if the element has a value for the attribute named name, False if not.

####  `boolean`{: .lua-type } <a name='Element-HasChildNodes'>HasChildNodes</a>{: .lua-method }()

Returns True if the element has at least one child node, false if not.

#### `nil`{: .lua-type} <a name='Element-InsertBefore'>InsertBefore</a>{: .lua-method }(`ElementPtr`{: .lua-type } element, `Element`{: .lua-type } adjacent_element)

Inserts the element element as a child of this element, directly before adjacent_element in the list of children.

####  `boolean`{: .lua-type } <a name='Element-IsClassSet'>IsClassSet</a>{: .lua-method }(`string`{: .lua-type } name)

Returns true if the class name is set on the element, false if not.

#### `nil`{: .lua-type} <a name='Element-RemoveAttribute'>RemoveAttribute</a>{: .lua-method }(`string`{: .lua-type } name)

Removes the attribute named name from the element.

####  `boolean`{: .lua-type } <a name='Element-RemoveChild'>RemoveChild</a>{: .lua-method }(`Element`{: .lua-type } element)

Removes the child element element from this element.

####  `boolean`{: .lua-type } <a name='Element-ReplaceChild'>ReplaceChild</a>{: .lua-method }(`ElementPtr`{: .lua-type } inserted_element, `Element`{: .lua-type } replaced_element)

Replaces the child element replaced_element with inserted_element in this element's list of children. If replaced_element is not a child of this element, inserted_element will be appended onto the list instead.

#### `nil`{: .lua-type} <a name='Element-ScrollIntoView'>ScrollIntoView</a>{: .lua-method }(`boolean`{: .lua-type } align_with_top)

Scrolls this element into view if its ancestors have hidden overflow. If align_with_top is True, the element's top edge will be aligned with the top (or as close as possible to the top) of its ancestors' viewing windows. If False, its bottom edge will be aligned to the bottom.

#### `nil`{: .lua-type} <a name='Element-SetAttribute'>SetAttribute</a>{: .lua-method }(`string`{: .lua-type } name, `string`{: .lua-type } value)

Sets the value of the attribute named name to value.

#### `nil`{: .lua-type} <a name='Element-SetClass'>SetClass</a>{: .lua-method }(`string`{: .lua-type } name, `boolean`{: .lua-type } value)

Sets (if value is true) or clears (if value is false) the class name on the element.



---

## <a href='#ElementAttributesProxy' name='ElementAttributesProxy'>ElementAttributesProxy</a>

Inherits: `nil`{: .lua-type }



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



---

## <a href='#ElementChildNodesProxy' name='ElementChildNodesProxy'>ElementChildNodesProxy</a>

Inherits: `nil`{: .lua-type }



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



---

## <a href='#ElementDataGrid' name='ElementDataGrid'>ElementDataGrid</a>

Inherits: `Element`{: .lua-type }

ElementDataGrid derives from Element. The data grid has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [rows](#ElementDataGrid-rows){: .lua-method } | `ElementDataGridRow`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [AddColumn](#ElementDataGrid-AddColumn){: .lua-method }(`string`{: .lua-type } fields, `string`{: .lua-type } formatter, `number`{: .lua-type } initial_width, `string`{: .lua-type } header_rml) |
| `nil`{: .lua-type } | [SetDataSource](#ElementDataGrid-SetDataSource){: .lua-method }(`string`{: .lua-type } data_source_name) |


### Metafunctions




### Property Descriptions

####  `ElementDataGridRow`{: .lua-type } <a name='ElementDataGrid-rows'>rows</a>{: .lua-method }

Returns an array containing all the rows in the data grid.



### Method Descriptions

#### `nil`{: .lua-type} <a name='ElementDataGrid-AddColumn'>AddColumn</a>{: .lua-method }(`string`{: .lua-type } fields, `string`{: .lua-type } formatter, `number`{: .lua-type } initial_width, `string`{: .lua-type } header_rml)

Adds a new column to the data grid. The column will read the columns fields (in CSV format) from the grid's data source, processing it through the data formatter named formatter. header_rml specifies the RML content of the column's header.

#### `nil`{: .lua-type} <a name='ElementDataGrid-SetDataSource'>SetDataSource</a>{: .lua-method }(`string`{: .lua-type } data_source_name)

Sets the name and table of the new data source to be used by the data grid.



---

## <a href='#ElementDataGridRow' name='ElementDataGridRow'>ElementDataGridRow</a>

Inherits: `Element`{: .lua-type }

ElementDataGridRow derives from Element. The data grid row has the following properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [parent_grid](#ElementDataGridRow-parent_grid){: .lua-method } | `ElementDataGrid`{: .lua-type } |
| [parent_relative_index](#ElementDataGridRow-parent_relative_index){: .lua-method } | `integer`{: .lua-type } |
| [parent_row](#ElementDataGridRow-parent_row){: .lua-method } | `ElementDataGridRow`{: .lua-type } |
| [row_expanded](#ElementDataGridRow-row_expanded){: .lua-method } | `boolean`{: .lua-type } |
| [table_relative_index](#ElementDataGridRow-table_relative_index){: .lua-method } | `integer`{: .lua-type } |


### Methods




### Metafunctions




### Property Descriptions

####  `ElementDataGrid`{: .lua-type } <a name='ElementDataGridRow-parent_grid'>parent_grid</a>{: .lua-method }

The data grid that this row belongs to.

####  `integer`{: .lua-type } <a name='ElementDataGridRow-parent_relative_index'>parent_relative_index</a>{: .lua-method }

The index of the row, relative to its parent row. So if you are the third row in your parent, then it will be 3.

####  `ElementDataGridRow`{: .lua-type } <a name='ElementDataGridRow-parent_row'>parent_row</a>{: .lua-method }

The parent row of this row. None if it at the top level.

####  `boolean`{: .lua-type } <a name='ElementDataGridRow-row_expanded'>row_expanded</a>{: .lua-method }

The expanded state of the row, either True or False.

####  `integer`{: .lua-type } <a name='ElementDataGridRow-table_relative_index'>table_relative_index</a>{: .lua-method }

The index of the row, relative to the data grid it is in. This takes into account all previous rows and their children.



### Method Descriptions



---

## <a href='#ElementForm' name='ElementForm'>ElementForm</a>

Inherits: `Element`{: .lua-type }

ElementForm derives from Element. The form element has the following method:

### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [Submit](#ElementForm-Submit){: .lua-method }(`string`{: .lua-type } submit_value) |


### Metafunctions




### Property Descriptions



### Method Descriptions

#### `nil`{: .lua-type} <a name='ElementForm-Submit'>Submit</a>{: .lua-method }(`string`{: .lua-type } submit_value)

Submits the form with a submit value of submit_value.



---

## <a href='#ElementFormControl' name='ElementFormControl'>ElementFormControl</a>

Inherits: `Element`{: .lua-type }



### Properties

| Name | Type |
| ------------ | ---- |
| [disabled](#ElementFormControl-disabled){: .lua-method } | `boolean`{: .lua-type } |
| [name](#ElementFormControl-name){: .lua-method } | `string`{: .lua-type } |
| [value](#ElementFormControl-value){: .lua-method } | `string`{: .lua-type } |


### Methods




### Metafunctions




### Property Descriptions

####  `boolean`{: .lua-type } <a name='ElementFormControl-disabled'>disabled</a>{: .lua-method }



####  `string`{: .lua-type } <a name='ElementFormControl-name'>name</a>{: .lua-method }



####  `string`{: .lua-type } <a name='ElementFormControl-value'>value</a>{: .lua-method }





### Method Descriptions



---

## <a href='#ElementFormControlDataSelect' name='ElementFormControlDataSelect'>ElementFormControlDataSelect</a>

Inherits: `ElementFormControlSelect`{: .lua-type }

ElementFormControlDataSelect derives from ElementFormControlSelect. It has the following additional method:

### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [SetDataSource](#ElementFormControlDataSelect-SetDataSource){: .lua-method }(`string`{: .lua-type } data_source_name) |


### Metafunctions




### Property Descriptions



### Method Descriptions

#### `nil`{: .lua-type} <a name='ElementFormControlDataSelect-SetDataSource'>SetDataSource</a>{: .lua-method }(`string`{: .lua-type } data_source_name)

Sets the name and table of the new data source to be used by the select box.



---

## <a href='#ElementFormControlInput' name='ElementFormControlInput'>ElementFormControlInput</a>

Inherits: `ElementFormControl`{: .lua-type }

ElementFormControlInput derives from IElementFormControl. The control has the following properties, only appropriate on the relevant types:

### Properties

| Name | Type |
| ------------ | ---- |
| [checked](#ElementFormControlInput-checked){: .lua-method } | `boolean`{: .lua-type } |
| [max](#ElementFormControlInput-max){: .lua-method } | `integer`{: .lua-type } |
| [maxlength](#ElementFormControlInput-maxlength){: .lua-method } | `integer`{: .lua-type } |
| [min](#ElementFormControlInput-min){: .lua-method } | `integer`{: .lua-type } |
| [size](#ElementFormControlInput-size){: .lua-method } | `integer`{: .lua-type } |
| [step](#ElementFormControlInput-step){: .lua-method } | `integer`{: .lua-type } |


### Methods




### Metafunctions




### Property Descriptions

####  `boolean`{: .lua-type } <a name='ElementFormControlInput-checked'>checked</a>{: .lua-method }

Relevant for radio and checkbox types. The checked status of the input.

####  `integer`{: .lua-type } <a name='ElementFormControlInput-max'>max</a>{: .lua-method }

Relevant for range types. The value of the control on the bottom / right of the slider.

####  `integer`{: .lua-type } <a name='ElementFormControlInput-maxlength'>maxlength</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='ElementFormControlInput-min'>min</a>{: .lua-method }

Relevant for range types. The value of the control on the top / left of the slider.

####  `integer`{: .lua-type } <a name='ElementFormControlInput-size'>size</a>{: .lua-method }

Relevant for text types. The approximate number of characters the text field shows horizontally at once.

####  `integer`{: .lua-type } <a name='ElementFormControlInput-step'>step</a>{: .lua-method }

Relevant for range types. The step the control's value changes in.



### Method Descriptions



---

## <a href='#ElementFormControlSelect' name='ElementFormControlSelect'>ElementFormControlSelect</a>

Inherits: `ElementFormControl`{: .lua-type }

ElementFormControlSelect derives from IElementFormControl. The control has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [options](#ElementFormControlSelect-options){: .lua-method } | `SelectOptionsProxy`{: .lua-type } |
| [selection](#ElementFormControlSelect-selection){: .lua-method } | `integer`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `integer`{: .lua-type }<br> | [Add](#ElementFormControlSelect-Add){: .lua-method }(`string`{: .lua-type } rml, `string`{: .lua-type } value[, `integer`{: .lua-type } before]) |
| `nil`{: .lua-type } | [Remove](#ElementFormControlSelect-Remove){: .lua-method }(`integer`{: .lua-type } index) |
| `nil`{: .lua-type } | [RemoveAll](#ElementFormControlSelect-RemoveAll){: .lua-method }() |


### Metafunctions




### Property Descriptions

####  `SelectOptionsProxy`{: .lua-type } <a name='ElementFormControlSelect-options'>options</a>{: .lua-method }

The array of options available in the select box. Each entry in the array has the property value, the string value of the option, and element, the root of the element hierarchy that represents the option in the list.

####  `integer`{: .lua-type } <a name='ElementFormControlSelect-selection'>selection</a>{: .lua-method }

The index of the currently selected option.



### Method Descriptions

####  `integer`{: .lua-type } <a name='ElementFormControlSelect-Add'>Add</a>{: .lua-method }(`string`{: .lua-type } rml, `string`{: .lua-type } value[, `integer`{: .lua-type } before])

Adds a new option to the select box. The new option has the string value of value and is represented by the elements created by the RML string rml. The new option will be inserted by the index specified by before; if this is out of bounds (the default), then the new option will be appended onto the list. The index of the new option will be returned.

#### `nil`{: .lua-type} <a name='ElementFormControlSelect-Remove'>Remove</a>{: .lua-method }(`integer`{: .lua-type } index)

Removes an existing option from the selection box.

#### `nil`{: .lua-type} <a name='ElementFormControlSelect-RemoveAll'>RemoveAll</a>{: .lua-method }()





---

## <a href='#ElementFormControlTextArea' name='ElementFormControlTextArea'>ElementFormControlTextArea</a>

Inherits: `ElementFormControl`{: .lua-type }

ElementFormControlTextArea derives from IElementFormControl. The control has the following properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [cols](#ElementFormControlTextArea-cols){: .lua-method } | `integer`{: .lua-type } |
| [maxlength](#ElementFormControlTextArea-maxlength){: .lua-method } | `integer`{: .lua-type } |
| [rows](#ElementFormControlTextArea-rows){: .lua-method } | `integer`{: .lua-type } |
| [wordwrap](#ElementFormControlTextArea-wordwrap){: .lua-method } | `boolean`{: .lua-type } |


### Methods




### Metafunctions




### Property Descriptions

####  `integer`{: .lua-type } <a name='ElementFormControlTextArea-cols'>cols</a>{: .lua-method }

The approximate number of characters the text area shows horizontally at once.

####  `integer`{: .lua-type } <a name='ElementFormControlTextArea-maxlength'>maxlength</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='ElementFormControlTextArea-rows'>rows</a>{: .lua-method }

The number of lines the text area shows at once.

####  `boolean`{: .lua-type } <a name='ElementFormControlTextArea-wordwrap'>wordwrap</a>{: .lua-method }





### Method Descriptions



---

## <a href='#ElementInstancer' name='ElementInstancer'>ElementInstancer</a>

Inherits: `nil`{: .lua-type }



### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `ElementInstancer`{: .lua-type} | [new](#ElementInstancer-new){: .lua-method }() |
| `value`{: .lua-type }<br> | [InstanceElement](#ElementInstancer-InstanceElement){: .lua-method }(`ElementInstancer`{: .lua-type } ) |


### Metafunctions




### Property Descriptions



### Method Descriptions

#### `nil`{: .lua-type} <a name='ElementInstancer-new'>new</a>{: .lua-method }()



####  `value`{: .lua-type } <a name='ElementInstancer-InstanceElement'>InstanceElement</a>{: .lua-method }(`ElementInstancer`{: .lua-type } )





---

## <a href='#ElementPtr' name='ElementPtr'>ElementPtr</a>

Inherits: `nil`{: .lua-type }



### Properties




### Methods




### Metafunctions




### Property Descriptions



### Method Descriptions



---

## <a href='#ElementStyleProxy' name='ElementStyleProxy'>ElementStyleProxy</a>

Inherits: `nil`{: .lua-type }



### Properties




### Methods




### Metafunctions

| Metafunctions |
| ------------- |
| __index |
| __ipairs |
| __newindex |
| __pairs |


### Property Descriptions



### Method Descriptions



---

## <a href='#ElementTabSet' name='ElementTabSet'>ElementTabSet</a>

Inherits: `Element`{: .lua-type }

ElementTabSet derives from Element. The control has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [active_tab](#ElementTabSet-active_tab){: .lua-method } | `integer`{: .lua-type } |
| [num_tabs](#ElementTabSet-num_tabs){: .lua-method } | `integer`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [SetPanel](#ElementTabSet-SetPanel){: .lua-method }(`integer`{: .lua-type } index, `string`{: .lua-type } rml) |
| `nil`{: .lua-type } | [SetTab](#ElementTabSet-SetTab){: .lua-method }(`integer`{: .lua-type } index, `string`{: .lua-type } rml) |


### Metafunctions




### Property Descriptions

####  `integer`{: .lua-type } <a name='ElementTabSet-active_tab'>active_tab</a>{: .lua-method }

Index of the active panel.

####  `integer`{: .lua-type } <a name='ElementTabSet-num_tabs'>num_tabs</a>{: .lua-method }

The number of tabs in the tab set. Read-only.



### Method Descriptions

#### `nil`{: .lua-type} <a name='ElementTabSet-SetPanel'>SetPanel</a>{: .lua-method }(`integer`{: .lua-type } index, `string`{: .lua-type } rml)

Sets the contents of a panel to the RML content rml. If index is out-of-bounds, a new panel will be added at the end.

#### `nil`{: .lua-type} <a name='ElementTabSet-SetTab'>SetTab</a>{: .lua-method }(`integer`{: .lua-type } index, `string`{: .lua-type } rml)

Sets the contents of a tab to the RML content rml. If index is out-of-bounds, a new tab will be added at the end.



---

## <a href='#ElementText' name='ElementText'>ElementText</a>

Inherits: `Element`{: .lua-type }



### Properties

| Name | Type |
| ------------ | ---- |
| [text](#ElementText-text){: .lua-method } | `string`{: .lua-type } |


### Methods




### Metafunctions




### Property Descriptions

####  `string`{: .lua-type } <a name='ElementText-text'>text</a>{: .lua-method }





### Method Descriptions



---

## <a href='#Event' name='Event'>Event</a>

Inherits: `nil`{: .lua-type }

The Event class has no constructor; it is generated internally. It has the following methods and properties:

### Properties

| Name | Type |
| ------------ | ---- |
| [current_element](#Event-current_element){: .lua-method } | `Element`{: .lua-type } |
| [parameters](#Event-parameters){: .lua-method } | `EventParametersProxy`{: .lua-type } |
| [target_element](#Event-target_element){: .lua-method } | `Element`{: .lua-type } |
| [type](#Event-type){: .lua-method } | `string`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [StopPropagation](#Event-StopPropagation){: .lua-method }() |


### Metafunctions




### Property Descriptions

####  `Element`{: .lua-type } <a name='Event-current_element'>current_element</a>{: .lua-method }

The element the event has propagated to. Read-only.

####  `EventParametersProxy`{: .lua-type } <a name='Event-parameters'>parameters</a>{: .lua-method }

A dictionary like object containing all the parameters in the event.

####  `Element`{: .lua-type } <a name='Event-target_element'>target_element</a>{: .lua-method }

The element the event was originally targeted at. Read-only.

####  `string`{: .lua-type } <a name='Event-type'>type</a>{: .lua-method }

The string name of the event. Read-only.



### Method Descriptions

#### `nil`{: .lua-type} <a name='Event-StopPropagation'>StopPropagation</a>{: .lua-method }()

Stops the propagation of the event through the event cycle, if allowed.



---

## <a href='#EventParametersProxy' name='EventParametersProxy'>EventParametersProxy</a>

Inherits: `nil`{: .lua-type }



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



---

## <a href='#GlobalLuaFunctions' name='GlobalLuaFunctions'>GlobalLuaFunctions</a>

Inherits: `nil`{: .lua-type }



### Properties

| Name | Type |
| ------------ | ---- |
| [ipairsaux](#GlobalLuaFunctions-ipairsaux){: .lua-method } | `nil`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [LuaPrint](#GlobalLuaFunctions-LuaPrint){: .lua-method }() |


### Metafunctions




### Property Descriptions

#### `nil`{: .lua-type } <a name='GlobalLuaFunctions-ipairsaux'>ipairsaux</a>{: .lua-method }





### Method Descriptions

#### `nil`{: .lua-type} <a name='GlobalLuaFunctions-LuaPrint'>LuaPrint</a>{: .lua-method }()





---

## <a href='#IElementFormControl' name='IElementFormControl'>IElementFormControl</a>

Inherits: `nil`{: .lua-type }

IElementFormControl derives from Element. The form element control has the following properties:

### Properties




### Methods




### Metafunctions




### Property Descriptions



### Method Descriptions



---

## <a href='#IElementText' name='IElementText'>IElementText</a>

Inherits: `nil`{: .lua-type }

IElementText derives from Element. IElementText is an interface, and therefore cannot be instanced directly. A concrete ElementText must be instantiated through a Document object instead. It has the following property:

### Properties




### Methods




### Metafunctions




### Property Descriptions



### Method Descriptions



---

## <a href='#Log' name='Log'>Log</a>

Inherits: `nil`{: .lua-type }



### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type } | [LogMessage](#Log-LogMessage){: .lua-method }() |


### Metafunctions




### Property Descriptions



### Method Descriptions

#### `nil`{: .lua-type} <a name='Log-Message'>Message</a>{: .lua-method }()





---

## <a href='#LuaDataSource' name='LuaDataSource'>LuaDataSource</a>

Inherits: `nil`{: .lua-type }



### Properties




### Methods

| Return Type | Name |
| ------------ | ---- |
| `LuaDataSource`{: .lua-type} | [new](#LuaDataSource-new){: .lua-method }() |


### Metafunctions




### Property Descriptions



### Method Descriptions

#### `nil`{: .lua-type} <a name='LuaDataSource-DataSourcenew'>DataSourcenew</a>{: .lua-method }()





---

## <a href='#LuaRmlUi' name='LuaRmlUi'>LuaRmlUi</a>

Inherits: `nil`{: .lua-type }



### Properties

| Name | Type |
| ------------ | ---- |
| [contexts](#LuaRmlUi-contexts){: .lua-method } | `RmlUiContextsProxy`{: .lua-type } |
| [key_identifier](#LuaRmlUi-key_identifier){: .lua-method } | `nil`{: .lua-type } |
| [key_modifier](#LuaRmlUi-key_modifier){: .lua-method } | `nil`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `nil`{: .lua-type }<br>`Context`{: .lua-type }<br> | [CreateContext](#LuaRmlUi-CreateContext){: .lua-method }(`string`{: .lua-type } ) |
| `boolean`{: .lua-type }<br> | [LoadFontFace](#LuaRmlUi-LoadFontFace){: .lua-method }(`string`{: .lua-type } ) |
| `nil`{: .lua-type } | [RegisterTag](#LuaRmlUi-RegisterTag){: .lua-method }(`string`{: .lua-type } ) |


### Metafunctions




### Property Descriptions

####  `RmlUiContextsProxy`{: .lua-type } <a name='LuaRmlUi-contexts'>contexts</a>{: .lua-method }



#### `nil`{: .lua-type } <a name='LuaRmlUi-key_identifier'>key_identifier</a>{: .lua-method }



#### `nil`{: .lua-type } <a name='LuaRmlUi-key_modifier'>key_modifier</a>{: .lua-method }





### Method Descriptions

####  `nil`{: .lua-type }, `Context`{: .lua-type } <a name='LuaRmlUi-CreateContext'>CreateContext</a>{: .lua-method }(`string`{: .lua-type } )



####  `boolean`{: .lua-type } <a name='LuaRmlUi-LoadFontFace'>LoadFontFace</a>{: .lua-method }(`string`{: .lua-type } )



#### `nil`{: .lua-type} <a name='LuaRmlUi-RegisterTag'>RegisterTag</a>{: .lua-method }(`string`{: .lua-type } )





---

## <a href='#RmlUiContextsProxy' name='RmlUiContextsProxy'>RmlUiContextsProxy</a>

Inherits: `nil`{: .lua-type }



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



---

## <a href='#SelectOptionsProxy' name='SelectOptionsProxy'>SelectOptionsProxy</a>

Inherits: `nil`{: .lua-type }



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



---

## <a href='#Vector2f' name='Vector2f'>Vector2f</a>

Inherits: `nil`{: .lua-type }

Constructs a two-dimensional floating-point vector.

### Properties

| Name | Type |
| ------------ | ---- |
| [magnitude](#Vector2f-magnitude){: .lua-method } | `number`{: .lua-type } |
| [x](#Vector2f-x){: .lua-method } | `number`{: .lua-type } |
| [y](#Vector2f-y){: .lua-method } | `number`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `number`{: .lua-type }<br> | [DotProduct](#Vector2f-DotProduct){: .lua-method }(`Vector2f`{: .lua-type } ) |
| `Vector2f`{: .lua-type }<br> | [Normalise](#Vector2f-Normalise){: .lua-method }() |
| `Vector2f`{: .lua-type }<br> | [Rotate](#Vector2f-Rotate){: .lua-method }(`number`{: .lua-type } ) |
| `Vector2f`{: .lua-type} | [new](#Vector2f-new){: .lua-method }() |


### Metafunctions

| Metafunctions |
| ------------- |
| __add |
| __div |
| __eq |
| __mul |
| __sub |


### Property Descriptions

####  `number`{: .lua-type } <a name='Vector2f-magnitude'>magnitude</a>{: .lua-method }



####  `number`{: .lua-type } <a name='Vector2f-x'>x</a>{: .lua-method }



####  `number`{: .lua-type } <a name='Vector2f-y'>y</a>{: .lua-method }





### Method Descriptions

####  `number`{: .lua-type } <a name='Vector2f-DotProduct'>DotProduct</a>{: .lua-method }(`Vector2f`{: .lua-type } )



####  `Vector2f`{: .lua-type } <a name='Vector2f-Normalise'>Normalise</a>{: .lua-method }()



####  `Vector2f`{: .lua-type } <a name='Vector2f-Rotate'>Rotate</a>{: .lua-method }(`number`{: .lua-type } )



#### `nil`{: .lua-type} <a name='Vector2f-new'>new</a>{: .lua-method }()





---

## <a href='#Vector2i' name='Vector2i'>Vector2i</a>

Inherits: `nil`{: .lua-type }

Constructs a two-dimensional integral vector.

### Properties

| Name | Type |
| ------------ | ---- |
| [magnitude](#Vector2i-magnitude){: .lua-method } | `number`{: .lua-type } |
| [x](#Vector2i-x){: .lua-method } | `integer`{: .lua-type } |
| [y](#Vector2i-y){: .lua-method } | `integer`{: .lua-type } |


### Methods

| Return Type | Name |
| ------------ | ---- |
| `Vector2i`{: .lua-type} | [new](#Vector2i-new){: .lua-method }() |


### Metafunctions

| Metafunctions |
| ------------- |
| __add |
| __div |
| __eq |
| __mul |
| __sub |


### Property Descriptions

####  `number`{: .lua-type } <a name='Vector2i-magnitude'>magnitude</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='Vector2i-x'>x</a>{: .lua-method }



####  `integer`{: .lua-type } <a name='Vector2i-y'>y</a>{: .lua-method }





### Method Descriptions

#### `nil`{: .lua-type} <a name='Vector2i-new'>new</a>{: .lua-method }()





---
