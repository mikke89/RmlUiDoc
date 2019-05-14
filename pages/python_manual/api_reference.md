---
layout: page
title: API Reference
parent: python_manual
---

### Module

`CreateContext(name, dimensions)`
: Creates and returns a new context called name, with initial dimensions of dimensions. The dimensions are a Vector2i type. The name of the context must be unique; if it is not, None will be returned 

`LoadFontFace(font_path)`
: Loads the font face at font_path. The function will return True if the font face was loaded, False if not. 

`RegisterTag(tag_name, class_definition)`
: Registers an Python class to instance when a specific XML tag is encountered in an RML file. 

`Log(type, message)`
: Sends a log message to {{page.lib_name}} (and the attached debugger if present).
`type` should be one of:
* `rocket.logtype.always`{:.value}
* `rocket.logtype.error`{:.value}
* `rocket.logtype.warning`{:.value}
* `rocket.logtype.info`{:.value}
* `rocket.logtype.debug`{:.value}

`contexts`
: A dictionary of the active {{page.lib_name}} contexts. It can be indexed by string (in which case the context with the matching name is returned), or number (in which case the nth context is returned). The number of contexts can be queried with the len operator. 

### Basic Types

`class Vector2i(x, y)`
: Constructs a two-dimensional integral vector. 

`class Vector2f(x, y)`
: Constructs a two-dimensional floating-point vector. 

`class Colourb(red, green, blue, alpha)`
: Constructs a colour with four channels, each from 0 to 255. 

### DataSource

`class DataSource(name)`

Abstract DataSource Interface.

`GetNumRows(table_name)`
: Return the number of rows in the given table 

`GetRow(table_name, index, columns)`
: Return a list of the column values in string form 

`NotifyRowAdd(table_name, first_row_added, num_rows_added)`
: Notify listeners that rows have been added to the data source. 

`NotifyRowRemove(table_name, first_row_removed, num_rows_removed)`
: Notify listeners that rows have been removed from the data source. 

`NotifyRowChange(table_name, first_row_changed, num_rows_changed)`
: Notify listeners that rows have been changed on the data source. 

`NotifyRowChange(table_name)`
: Notify listeners that all rows on the data source have changed. 

### Element

`class Element`

The Element class has no constructor; it must be instantiated through a [Document](#document) object instead. It has the following methods and properties:

`AddEventListener(event, listener[, in_capture_phase])`
: Attaches listener to this element, listening for occurrences of event in either the bubble or capture phase. If not specified, in_capture_phase will default to False.
NOTE: Events added from python cannot be removed. 

`AppendChild(element)`
: Appends element as a child to this element. 

`Blur()`
: Removes input focus from this element. 

`Click()`
: Fakes a click on this element. 

`DispatchEvent(event, parameters, interruptible)`
: Dispatches an event to this element. The event is of type event. Parameters to the event are given in the dictionary parameters; the dictionary must only contain string keys and floating-point, integer or string values. interruptible determines if the event can be forced to stop propagation early. 

`Focus()`
: Gives input focus to this element. 

`GetAttribute(name)`
: Returns the value of the attribute named name. If no such attribute exists, the empty string will be returned. 

`GetElementById(id)`
: Returns the descendant element with an id of id. 

`GetElementsByTagName(tag_name)`
: Returns a list of all descendant elements with the tag of tag_name. 

`HasAttribute(name)`
: Returns True if the element has a value for the attribute named name, False if not. 

`HasChildNodes()`
: Returns True if the element has at least one child node, false if not. 

`InsertBefore(element, adjacent_element)`
: Inserts the element element as a child of this element, directly before adjacent_element in the list of children. 

`IsClassSet(name)`
: Returns true if the class name is set on the element, false if not. 

`RemoveAttribute(name)`
: Removes the attribute named name from the element. 

`RemoveChild(element)`
: Removes the child element element from this element. 

`ReplaceChild(inserted_element, replaced_element)`
: Replaces the child element replaced_element with inserted_element in this element's list of children. If replaced_element is not a child of this element, inserted_element will be appended onto the list instead. 

`ScrollIntoView(align_with_top)`
: Scrolls this element into view if its ancestors have hidden overflow. If align_with_top is True, the element's top edge will be aligned with the top (or as close as possible to the top) of its ancestors' viewing windows. If False, its bottom edge will be aligned to the bottom. 

`SetAttribute(name, value)`
: Sets the value of the attribute named name to value. 

`SetClass(name, value)`
: Sets (if value is true) or clears (if value is false) the class name on the element. 

`attributes`
: The array of attributes on the element. Each element has the read-only properties name and value. Read-only. 

`child_nodes`
: The array of child nodes on the element. Read-only. 

`class_name`
: The space-separated list of classes on the element. 

`client_left`
: The distance between the left border edge and the left client edge of the element. Read-only. 

`client_height`
: The height of the element's client area. Read-only. 

`client_top`
: The distance between the top border edge and the top client edge of the element. Read-only. 

`client_width`
: The width of the element's client area. Read-only. 

`first_child`
: The first child of the element, or None if the client has no children. Read-only. 

`id`
: The ID of the element, or the empty string if the element has no ID. 

`inner_rml`
: The element's RML content. 

`last_child`
: The last child of the element, or None if the client has no children. Read-only. 

`next_sibling`
: The element's next sibling, or None if it is the last sibling. Read-only. 

`offset_height`
: The height of the element, excluding margins. Read-only. 

`offset_left`
: The distance between the element's offset parent's left border edge and this element's left border edge. Read-only. 

`offset_parent`
: The element's offset parent. Read only. 

`offset_top`
: The distance between the element's offset parent's top border edge and this element's top border edge. Read-only. 

`offset_width`
: The width of the element, excluding margins. Read-only. 

`owner_document`
: The document this element is part of. Read-only. 

`parent_node`
: The element this element is directly parented to. Read-only. 

`previous_sibling`
: The element's previous sibling, or None if it is the first sibling. Read-only. 

`scroll_height`
: The height of this element's content. This will be at least as high as the client height. Read-only. 

`scroll_left`
: The offset between the left edge of this element's client area and the left edge of the content area. 

`scroll_top`
: The offset between the top edge of this element's client area and the top edge of the content area. 

`scroll_width`
: The width of this element's content. This will be at least as wide as the client width. Read-only. 

`style`
: An object used to access this element's style information. Individual RCSS properties can be accessed by using the name of the property as a Python property on the object itself (ie, element.style.width = "40px"). 

`tag_name`
: The tag name used to instance this element. Read-only. 

### ElementText

`class IElementText`

IElementText derives from Element. IElementText is an interface, and therefore cannot be instanced directly. A concrete ElementText must be instantiated through a Document object instead. It has the following property:

`text`
: The raw text content of the text element in UTF-8 encoding. 

### Document

`class Document`

Document derives from Element. Document has no constructor; it must be instantiated through a Context object instead, either by loading an external RML file or creating an empty document. It has the following methods and properties:

`PullToFront()`
: Pulls the document in front of other documents within its context with a similar z-index. 

`PushToBack()`
: Pushes the document behind other documents within its context with a similar z-index. 

`Show([flags])`
: Shows the document. flags is either NONE, FOCUS or MODAL. flags defaults to FOCUS. 

`Hide()`
: Hides the document. 

`Close()`
: Hides and closes the document, destroying its contents. 

`CreateElement(tag_name)`
: Instances an element with a tag of tag_name. 

`CreateTextNode(text)`
: Instances a text element containing the string text. 

`title`
: The title of the document, as initially set by the \<title\> tag in the document's header. 

`context`
: The context the document belongs to. Read-only. 

### Event

`class Event`

The Event class has no constructor; it is generated internally. It has the following methods and properties:

`StopPropagation()`
: Stops the propagation of the event through the event cycle, if allowed. 

`current_element`
: The element the event has propagated to. Read-only. 

`type`
: The string name of the event. Read-only. 

`target_element`
: The element the event was originally targeted at. Read-only. 

`parameters`
: A dictionary like object containing all the parameters in the event. 

### Context

`class Context`

The Context class has no constructor; it must be instantiated through the CreateContext() function. It has the following methods and properties:

`AddEventListener(event, script, element_context, in_capture_phase)`
: Adds the inline Python script, script, as an event listener to the context. element_context is an optional Element; if it is not None, then the script will be executed as if it was bound to that element. 

`AddMouseCursor(cursor_document)`
: Adds a cursor document loaded by another context into this context. The cursor document will be returned. 

`CreateDocument(tag)`
: Creates a new document with the tag name of tag. 

`LoadDocument(document_path)`
: Attempts to load a document from the RML file found at document_path. If successful, the document will be returned with a reference count of one. 

`LoadMouseCursor(cursor_document_path)`
: Attempts to load a document from the RML file found at cursor_document_path as a cursor. If successful, the cursor's document will be returned with a reference count of one. 

`Render()`
: Renders the context. 

`ShowMouseCursor(show)`
: If show is True, this shows the mouse cursor, otherwise hides it. 

`UnloadAllDocuments()`
: Closes all documents currently loaded with the context. 

`UnloadAllMouseCursors()`
: Unloads all cursors currently loaded with the context. 

`UnloadDocument(document)`
: Unloads a specific document within the context. 

`UnloadMouseCursor(cursor_name)`
: Unloads a specific cursor by name. 

`Update()`
: Updates the context. 

`dimensions`
: The dimensions of the context, as a Vector2i type. 

`documents`
: Returns an array of the documents within the context. This can be looked up as an array or a dictionary. Read-only. 

`focus_element`
: Returns the leaf of the context's focus tree. Read-only. 

`hover_element`
: Returns the element under the context's cursor. Read-only. 

`name`
: The name of the context, specified at construction. Read-only. 

`root_element`
: Returns the context's root element. Read-only. 

## Controls API Reference

### ElementForm

`class ElementForm`

ElementForm derives from Element. The form element has the following method:

`Submit(submit_value)`
: Submits the form with a submit value of submit_value. 

### ElementFormControl

`class IElementFormControl`

IElementFormControl derives from Element. The form element control has the following properties:

`disabled`
: The disabled status of the control, either True or False. 

`name`
: The name of the control, initial set with the "name" attribute. 

`value`
: The current value of the control. 

### ElementFormControlSelect

`class ElementFormControlSelect`

ElementFormControlSelect derives from IElementFormControl. The control has the following methods and properties:

`Add(rml, value[, before])`
: Adds a new option to the select box. The new option has the string value of value and is represented by the elements created by the RML string rml. The new option will be inserted by the index specified by before; if this is out of bounds (the default), then the new option will be appended onto the list. The index of the new option will be returned. 

`Remove(index)`
: Removes an existing option from the selection box. 

`options`
: The array of options available in the select box. Each entry in the array has the property value, the string value of the option, and element, the root of the element hierarchy that represents the option in the list. 

`selection`
: The index of the currently selected option. 

### ElementFormControlDataSelect

`class ElementFormControlDataSelect`

ElementFormControlDataSelect derives from ElementFormControlSelect. It has the following additional method:

`SetDataSource(data_source_name)`
: Sets the name and table of the new data source to be used by the select box. 

### ElementFormControlInput

`class ElementFormControlInput`

ElementFormControlInput derives from IElementFormControl. The control has the following properties, only appropriate on the relevant types:

`checked`
: Relevant for radio and checkbox types. The checked status of the input. 

`max_length`
: Relevant for text types. The maximum number of characters permitted in the text field. 

`size`
: Relevant for text types. The approximate number of characters the text field shows horizontally at once. 

`max`
: Relevant for range types. The value of the control on the bottom / right of the slider. 

`min`
: Relevant for range types. The value of the control on the top / left of the slider. 

`step`
: Relevant for range types. The step the control's value changes in. 

### ElementFormControlTextArea

`class ElementFormControlTextArea`

ElementFormControlTextArea derives from IElementFormControl. The control has the following properties:

`cols`
: The approximate number of characters the text area shows horizontally at once. 

`max_length`
: The maximum number of characters permitted in the text area. 

`rows`
: The number of lines the text area shows at once. 

`word_wrap`
: True if lines are split to fit into the text area, False if not. 

### ElementTabSet

`class ElementTabSet`

ElementTabSet derives from Element. The control has the following methods and properties:

`SetPanel(index, rml)`
: Sets the contents of a panel to the RML content rml. If index is out-of-bounds, a new panel will be added at the end. 

`SetTab(index, rml)`
: Sets the contents of a tab to the RML content rml. If index is out-of-bounds, a new tab will be added at the end. 

`active_tab`
: Index of the active panel. 

`num_tabs`
: The number of tabs in the tab set. Read-only.

### ElementDataGrid

`class ElementDataGrid`

ElementDataGrid derives from Element. The data grid has the following methods and properties:

`AddColumn(fields, formatter, initial_width, header_rml)`
: Adds a new column to the data grid. The column will read the columns fields (in CSV format) from the grid's data source, processing it through the data formatter named formatter. header_rml specifies the RML content of the column's header. 

`SetDataSource(data_source_name)`
: Sets the name and table of the new data source to be used by the data grid. 

`rows`
: Returns an array containing all the rows in the data grid. 

### ElementDataGridRow

`class ElementDataGridRow`

ElementDataGridRow derives from Element. The data grid row has the following properties:

`row_expanded`
: The expanded state of the row, either True or False. 

`parent_relative_index`
: The index of the row, relative to its parent row. So if you are the third row in your parent, then it will be 3. 

`table_relative_index`
: The index of the row, relative to the data grid it is in. This takes into account all previous rows and their children. 

`parent_row`
: The parent row of this row. None if it at the top level. 

`parent_grid`
: The data grid that this row belongs to. 