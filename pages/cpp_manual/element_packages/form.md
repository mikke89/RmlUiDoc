---
layout: page
title: Form controls
parent: cpp_manual/element_packages
grandparent: cpp_manual
next: tab_set
---

RmlUi includes a fully-featured set of form controls. The full RML specification for these controls can be found [here]({{"pages/rml/forms.html"|relative_url}}). The available form controls are:

* [text and password fields](#text-field)
* [text area](#text-area)
* [radio button and checkbox](#radio-button-and-checkbox)
* [drop-down selection list](#drop-down-select-box)
* [range slider](#range-slider)

Below is the hierarchy for the custom form elements included in RmlUi.

![form_1.gif](form_1.gif)

### Form control interface

All form control elements are derived from the `Rml::ElementFormControl` interface. Each form control has two values associated with it; name and value. The name is used to identify the control. The value specifies the current setting of the control; the exact definition of the value depends on the control. When a group of form controls is submitted, the names and values of the controls become the parameters of the submission.

The name of a form control can be retrieved and set using the `GetName()` and `SetName()` functions on `Rml::ElementFormControl`.

```cpp
// Returns the name of the form control.
// @return The name of the form control.
Rml::String GetName() const;

// Sets the name of the form control.
// @param[in] name The new name of the form control.
void SetName(const Rml::String& name);
```

The value of a form control can be retrieved and set using the `GetValue()` and `SetValue()` functions.

```cpp
// Returns a string representation of the current value of the form control.
// @return The value of the form control.
Rml::String GetValue() const;

// Sets the current value of the form control.
// @param[in] value The new value of the form control.
void SetValue(const Rml::String& value);
```

The exact syntax of the value varies from control to control, but `GetValue()` will always return a value in a human-readable form.

Form controls can be enabled and disabled dynamically as well. All controls start enabled.

```cpp
// Returns the disabled status of the form control.
// @return True if the element is disabled, false otherwise.
bool IsDisabled() const;

// Sets the disabled status of the form control.
// @param[in] disabled True to disable the element, false to enable.
void SetDisabled(bool disable);
```

#### Generic input interface

Most of the form controls are instanced through the `<input>`{:.tag} tag, with the `type`{:.attr} attribute determining how they operate. The possible values for `type`{:.tag} are:

* _text_: A single-line text field. This is the default.
* _password_: Similar to text, but renders asterisks for all characters.
* _radio_: A radio button.
* _checkbox_: A checkbox button.
* _range_: A slider.
* _button_: A button.
* _submit_: An element with button-like behaviour for submitting its parent form. 

One interface is used to represent all such form controls regardless of their type. Their type can be changed even after they've been instanced.

However, because they do not have a unique interface, they have no helper functions for accessing their attributes like the other form controls. Their attributes have to be accessed and mutated using `GetAttribute()` and `SetAttribute()`.

### Text field

The single-line text field control is specified in RML by the `<input type="text" />`{:.tag} tag. A password-style text field can be specified by the `<input type="password" />`{:.tag} tag. The interface to both of these elements is the `Rml::ElementFormControlInput` class.

The size of a text field refers of the average number of characters visible across the field. The value can be set with the `size`{:.attr} attribute.

The maximum number of characters allowed in a text field is set with the `maxlength`{:.attr} attribute.

### Text area

The text area, or multi-line text field, is specified in RML with the `<textarea>`{:.tag} tag. Any loose text between the text area's opening and closing tag will become the initial value of the control. The interface to the text area is the `Rml::ElementFormControlTextArea` class.

The intrinsic dimensions of the text area is controlled by the `cols`{:.attr} and `rows`{:.attr} attributes, which dictate the number of characters visible horizontally and vertically. These values can also be set in C++ through the relevant methods.

```cpp
// Sets the number of characters visible across the text area.
// @param[in] size The number of visible characters.
void SetNumColumns(int num_columns);

// Returns the approximate number of characters visible at once.
// @return The number of visible characters.
int GetNumColumns() const;

// Sets the number of visible lines of text in the text area.
// @param[in] num_rows The new number of visible lines of text.
void SetNumRows(int num_rows);

// Returns the number of visible lines of text in the text area.
// @return The number of visible lines of text.
int GetNumRows() const;
```

Similarly to the single-line text field, the maximum number of characters in the text area can be limited with the `maxlength`{:.attr} attribute. It can be accessed in C++ using the `GetMaxLength()` function and changed with the `SetMaxLength()` function.

```cpp
// Sets the maximum length (in characters) of this text area.
// @param[in] max_length The new maximum length of the text area. A number lower than zero will mean infinite characters.
void SetMaxLength(int max_length);

// Returns the maximum length (in characters) of this text area.
// @return The maximum number of characters allowed in this text area.
int GetMaxLength() const;
```

The word-wrapping state of the text area is set with the `wrap`{:.attr} attribute in RML. It can be changed in C++ with the `GetWordWrap()` and `SetWordWrap()` functions.

```cpp
// Enables or disables word-wrapping in the text area.
// @param[in] word_wrap True to enable word-wrapping, false to disable.
void SetWordWrap(bool word_wrap);

// Returns the state of word-wrapping in the text area.
// @return True if the text area is word-wrapping, false otherwise.
bool GetWordWrap();
```

### Radio button and checkbox

The radio button (`<input type="radio" />`{:.tag}) and checkbox (`<input type="checkbox" />`{:.tag}) are two similar types of form control. Both only submit their value if they are checked. The radio button will, when checked, uncheck all other radio buttons with the same name. The interface for both controls is `Rml::ElementFormControlInput`.

The checked status of a checkbox or radio button defaults to false, but can be initialised to true with the `checked`{:.attr} attribute. To uncheck a checkbox, remove the `checked`{:.attr} attribute with `RemoveAttribute()`.

### Drop-down select box

The simple drop-down select control is specified in RML with the `<select>`{:.tag} tag. Individual options within the select box are specified with child `<option>`{:.tag} elements. The value of the select control is set to the value attribute of the currently selected option.
The following RML fragment declares a select box:

```html
<select name="graphics">
	<option value="bad">Bad</option>
	<option value="ok">OK</option>
	<option value="good" selected>good</option>
</select>
```

The select control's interface is the `Rml::ElementFormControlSelect` class. The total number of options in the select box can be queried with the `GetNumOptions()` method.

```cpp
// Returns the number of options in the select control.
// @return The number of options.
int GetNumOptions() const;
```

Individual options can be accessed with the `GetOption()` method.

```cpp
// Returns one of the select control's option elements.
// @param[in] The index of the desired option.
// @return The option element or nullptr if the index was out of bounds.
Rml::Element* GetOption(int index);
```

`GetOption()` returns a pointer to the `<option>`{:.tag} element of the given index. The value of the given option can be obtained by retrieving its `value`{:.attr} attribute.

The selected option can be accessed with the `GetSelection()` function and set with the `SetSelection()` function.

```cpp
// Sets the index of the selection. If the new index lies outside of the bounds, it will be clamped.
// @param[in] selection The new selection index.
void SetSelection(int selection);

// Returns the index of the currently selected item.
// @return The index of the currently selected item.
int GetSelection() const;
```

Options can be procedurally added and removed with the `Add()`, `Remove()` and `RemoveAll()` functions.

```cpp
// Adds a new option to the select control.
// @param[in] rml The RML content used to represent the option.
// @param[in] value The value of the option.
// @param[in] before The index of the element to insert the new option before. If out of bounds the new option will be added at the end of the list.
// @param[in] selectable If true this option can be selected. If false, this option is not selectable.
// @return The index of the new option.
int Add(const Rml::String& rml,
        const Rml::String& value,
        int before = -1,
        bool selectable = true);

// Removes an option from the select control.
// @param[in] index The index of the option to remove. If this is outside of the bounds of the control's option list, no option will be removed.
void Remove(int index);

// Removes all options from the select control.
void RemoveAll();
```

#### Applying properties

See the [style guide](../../style_guide.html) for documentation on applying properties to a select box.


### Range slider

The range control can be used to render a slider-based number field. It is specified in RML with the tag `<input type='range' />`{:.tag}. The range control's interface is the `Rml::ElementFormControlInput` class.

The minimum and maximum values for the range are specified with the `min`{:.attr} and `max`{:.attr} attributes. The step of the range, or increments in which the value can be increased or decreased, is specified with the `step`{:.attr} attribute.

#### Applying properties

See the [style guide](../../style_guide.html) for documentation on applying properties to a range control.


### Form container

The form element is designed as a container element for form controls. Forms can be submitted, which bundles the name and value pairs of all descendant form controls into a single event. The form element is specified in RML with the `<form>`{:.tag} tag. It will generate a `submit`{:.evt} event when it is submitted; therefore it is usual to provide an inline event handler for `onsubmit`{:.attr}.

The form element's interface is the `Rml::ElementForm` class. The form can be submitted by calling the `Submit()` function.

```cpp
// Submits the form.
// @param[in] submit_value The value to send through as the 'submit' parameter.
void Submit(const Rml::String& submit_value = "");
```

The value of the submit_value parameter will become the value of the submit parameter on the submit event. This way, objects listening for event can distinguish between different kinds of submit actions.


### Form submit button

The form submit button is specified in RML with the `<input type="submit" />`{:.tag} tag. The submit button will trigger a submit on its ancestor form when it is clicked, with a submit value equal to its `value`{:.attr} attribute. Its interface is the class `Rml::ElementFormControlInput`. 


### Data-driven drop-down select box (deprecated)

> ***Deprecated*** in favor of [data bindings](../../data_bindings.html).

The data-driven drop-down select control is specified in RML with the `<dataselect>`{:.tag} tag. No options are specified within the tag; instead, they are populated from an `Rml::DataSource` object, similarly to a data grid.

The select control's interface is the `Rml::ElementFormControlDataSelect` class. It derives from `Rml::ElementFormControlSelect`. The data select's data source is set with the `source`{:.attr} attribute, and can be changed in C++ through the `SetDataSource()` method:

```cpp
// Sets the data source the control's options are driven from.
// @param[in] data_source The name of the new data source.
void SetDataSource(const Rml::String& data_source);
```

#### Applying properties

See the [style guide](../../style_guide.html) for documentation on applying properties to a select box.
