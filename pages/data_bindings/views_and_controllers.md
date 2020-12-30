---
layout: page
title: Data views and controllers
parent: data_bindings
---

{% raw %}

Data views and controllers connect the document with the data in a given data model. *Data views* are used to present a data variable in the document by different means. On the other hand, *data controllers* are used to respond to changes in the document, typically as a result of user input. When a controller is triggered, it sets a data variable in its data model.

Data views and controllers are declared in the document by the element attribute:

	data-[type]-[modifier]="[value]"

The modifier may or may not be required depending on the data view/controller. Some data bindings attach both a view and controller from the same attribute, enabling two-way bindings.

The following table lists all built-in data views and controllers in RmlUi, along with their declaration.


| Name                         | Type       | Attribute                    | Value                                           | Notes |
| ---------------------------- | ---------- | ---------------------------  | ----------------------------------------------- | ----- |
| [Attribute](#data-attr)      | View       | data-attr-[attribute_name]   | [data_expression]                               |       |
| [Attribute-if](#data-attrif) | View       | data-attrif-[attribute_name] | [data_expression]                               |       |
| [Class](#data-class)         | View       | data-class-[class_name]      | [data_expression]                               |       |
| [Style](#data-style)         | View       | data-style-[property_name]   | [data_expression]                               |       |
| [If](#data-if)               | View       | data-if                      | [data_expression]                               |       |
| [Visible](#data-visible)     | View       | data-visible                 | [data_expression]                               |       |
| [For](#data-for)             | View       | data-for                     | [iterator_name], [index_name] : [data_address]  | [1]   |
| [Rml](#data-rml)             | View       | data-rml                     | [data_expression]                               |       |
| [Text](#data-text)           | View       | N/A                          | N/A                                             | [2]   |
| [Value](#data-value)         | Two-way    | data-value                   | [data_address]                                  | [3]   |
| [Checked](#data-checked)     | Two-way    | data-checked                 | [data_address]                                  | [3]   |
| [Event](#data-event)         | Controller | data-event-[event_type]      | [assignment_expression]                         |       |

  [1] `iterator_name` and `index_name` are optional. Defaults to `it` and `it_index`, respectively.  
  [2] The text view is automatically added whenever double curly brackets {{ }} are encountered in the element's text.  
  [3] These attributes enable two-way bindings, and will attach both a view and controller to the element.  


Attribute
: `data-attr-[attribute_name]="[data_expression]"`{:.data-attr}
{:#data-attr.data-desc}

Sets the element's attribute `[attribute_name]` to the evaluated expression.

```html
<img data-attr-sprite="item.icon"/>
```

Attribute-if
: `data-attrif-[attribute_name]="[data_expression]"`{:.data-attr}
{:#data-attrif.data-desc}

Sets the element's attribute `[attribute_name]` when the expression evaluates to `true`, otherwise removes the given attribute from the element.

```html
<input type="checkbox" name="meals" value="pizza" data-attrif-disabled="rating > 70"/>
```

Useful for element behavior which depends on whether or not the attribute is present, such as `disabled`. When set, the value of the attribute is an empty string.


Class
: `data-class-[class_name]="[data_expression]"`{:.data-attr}
{:#data-class.data-desc}

Enables the class `[class_name]` on the element if the expression evaluates to `true`, otherwise it disables the class.

```html
<h1 data-class-red="score < 30">Score</h1>
```


Style
: `data-style-[property_name]="[data_expression]"`{:.data-attr}
{:#data-style.data-desc}

Sets the property `[property_name]` of the element's style to the evaluated expression.

```html
<img sprite="invader" data-style-image-color="invader.color"/>
```


If
: `data-if="[data_expression]"`{:.data-attr}
{:#data-if.data-desc}

Sets the `display` property of the element to `none` if the expression evaluates to `false`, otherwise it removes the `display` property from the element's inline style.

```html
<div data-if="rating > 50">
	Thanks for the <span data-if="rating >= 80">awesome</span> rating!
</div>
```

*Note.* The style sheet rules which applies to the element should ensure that the element's `display` property evaluates to something other than `none`. Otherwise, the element will always be hidden.


Visible
: `data-visible="[data_expression]"`{:.data-attr}
{:#data-visible.data-desc}

Sets the `visibility` property of the element to `hidden` if the expression evaluates to `false`, otherwise it removes the `visibility` property from the element's inline style.

```html
<div data-visible="collected_stars > 0">
	<img sprite="star"/>
</div>
```

As opposed to the `data-if` view, the `data-visible` view ensures that the element retains it's size regardless of visibility.

*Note.* The style sheet rules which applies to the element should ensure that the element's `visibility` property evaluates to `visible`, which is the default value. Otherwise, the element will always be hidden.


For
: `data-for="[iterator_name], [index_name] : [data_address]"`{:.data-attr}
{:#data-for.data-desc}

Repeats the element and its children *n* times for each item in the data variable designated by the `data_address`. The variable must be a data array type.

```html
<div data-for="invader : invaders">
	<h1>{{ invader.name }}</h1>
	<p>Invader {{it_index + 1}} of {{ invaders.size }}.</p>
	<img data-attr-sprite="invader.sprite" data-style-image-color="invader.color"/>
	<p>Scores: <span data-for="invader.scores"> {{it}} </span></p>
</div> 
```

An iterator can be used to retrieve values from the current item in the data array.

The `data-for` attribute can use any of the following values, enabling the user to override the default iterator and index names if desired. Note that the index is zero-based.

| Attribute value                                 | Iterator name    | Index name     |
| ----------------------------------------------- | ---------------- | -------------- |
| [data_address]                                  | `it`             | `it_index`     |
| [iterator_name] : [data_address]                | [iterator_name]  | `it_index`     |
| [iterator_name], [index_name] : [data_address]  | [iterator_name]  | [index_name]   |

The `data-for` loop is expanded by replicating the element with its attributes and its inner RML, for each entry in the array. Eg.

```html
<p data-for="subject, i : subjects" data-class-selected="i == selected_subject">{{i + ': ' + subject}}</p>
```
with three entries in `subjects` is turned into
```html
<p data-class-selected="i == selected_subject">{{i + ': ' + subject}}</p>
<p data-class-selected="i == selected_subject">{{i + ': ' + subject}}</p>
<p data-class-selected="i == selected_subject">{{i + ': ' + subject}}</p>
<p style="display: none;"/>
```
where `i` and `subject` become aliases to the array index and entry, respectively. Additionally, an element is added after all the entries so that the location of the for loop within the document tree is well defined even when there are no entries. This will become hidden by the `display: none` inline style added by the data view.

*Note.* For performance reasons the names of global data variables shadow iterator names. Thus, do not use an iterator name which is used for a data binding.  
*Implementation note.* Internally, the XML parser uses a special parsing rule whenever the `data-for` attribute is encountered, providing all the children of the current element as raw RML text to the data view, which is later used for creation of each item in the data array.


Rml
: `data-rml="[data_expression]"`{:.data-attr}
{:#data-rml.data-desc}

Sets the element's inner RML to the evaluated expression.

```html
<div data-rml="incoming_invaders ? '<em>Send help!</em>' : 'Clear skies.'">
</div>
```


Text
: `N/A`{:.data-attr}
{:#data-text.data-desc}

Evaluates any data expression inside double curly brackets {{ }} encountered in the element's text.

```html
<span class="position"> x: {{ position.x }}, y: {{ position.y }}</span>
<span data-for="i : indices"> {{ i * 2 + (i > 10 ? ' wow!' | to_upper : '') }}</span>
```

This data view is automatically added whenever double curly brackets are encountered in the text and should not be added as an attribute.


Value
: `data-value="[data_address]"`{:.data-attr}
{:#data-value.data-desc}

Synchronizes the element's `value`{:.attr} attribute to the value of the data variable located at `data_address`. This variable must be a scalar type. This is generally useful for `input`{:.tag} elements.

```html
<input type="range" min="0" max="100" step="1" data-value="rating"/>
```

A new value is assigned to the specified data variable whenever a `change`{:.evt} event occurs on the current element. The element's `value`{:.attr} attribute is updated whenever the data variable changes on the client side.
 
*Note.* Data expressions and assignment expressions are not supported for this attribute. Instead, use the `data-attr-value` view and `data-event-change` controller for more flexibility.


Checked
: `data-checked="[data_address]"`{:.data-attr}
{:#data-checked.data-desc}

Binds a checkbox or radio button's `checked` state to the variable located at `data_address`. This variable must be a scalar type. Typically combined with `<input type="checkbox"/>`{:.tag} and `<input type="radio"/>`{:.tag} elements.

```html
<input type="radio" name="animal" value="dog" data-checked="animal"/> Dog
<input type="radio" name="animal" value="cat" data-checked="animal"/> Cat
<input type="checkbox" name="meals" value="pasta" data-checked="pasta"/> Pasta
```

For checkboxes, the underlying data type should be a `bool`, where `true` means checked and `false` means unchecked. For radio buttons, the underlying type should be an `Rml::String` type where its value corresponds to the `value` attribute of the currently selected radio button.

A new value is assigned to the specified data variable whenever a `change`{:.evt} event occurs on the current element. The element's `checked`{:.attr} attribute is added or removed whenever the data variable changes on the client side.
 
*Note.* Data expressions and assignment expressions are not supported for this attribute. Instead, use the `data-attrif-checked` view and `data-event-change` controller for more flexibility.


Event
: `data-event-[event_type]="[assignment_expression]"`{:.data-attr}
{:#data-event.data-desc}

The event controller is triggered whenever the `[event_type]` event occurs on the current element. All event types in RmlUi are supported. Upon triggering, the associated *assignment expression* is evaluated.

An assignment expression is specified as one of the following two statements.

  (1) `[data_address] = [data_expression]`  
  (2) `[event_callback_name]([data_expression], [data_expression], ...)`

Furthermore, a single assignment expression can take multiple such statements by semicolon-separating them.

In (1), the data variable associated with the address on the left hand side is assigned the evaluated expression on the right hand side. Only scalar types can be assigned to.

In (2), the given event callback is called in C++, with the triggering event itself, a handle to the current data model, and the list of parameters inside the parenthesis.

The special variable `ev` can be used inside the expressions to retrieve values from the triggering event.

```html
<div class="mouse_detector"
	data-event-mousemove="mouse_detector = 'x: ' + ev.mouse_x + '<br/>y: ' + ev.mouse_y"
	data-event-click="add_mouse_pos(); hello_world = 'Hello click!'"
	data-rml="mouse_detector">
</div>
<h1>{{hello_world}}</h1>
<div data-for="positions">{{it}}</div>
```

The referenced `add_mouse_pos` event callback is triggered when the element is clicked, which can be implemented in C++ as follows.

```cpp
using namespace Rml;

std::vector<Vector2f> positions;

void AddMousePos(DataModelHandle model_handle, Event& ev, const VariantList& arguments)
{
	positions.emplace_back(ev.GetParameter("mouse_x", 0.f), ev.GetParameter("mouse_y", 0.f));
	model_handle.DirtyVariable("positions");
}
```


{% endraw %}
