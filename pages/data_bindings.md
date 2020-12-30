---
layout: page
title: Data bindings
---

{% comment %} 
	The open and close brackets { { ... } } used in RmlUi's data binding syntax interferes with the Liquid templating language in Jekyll. We turn off Liquid processing by enabling raw mode for the entire document.
{% endcomment %}

{% raw %}

RmlUi features a model-view-controller (MVC) approach through data bindings. This is a powerful approach for responding to changes in the data, or in reverse, updating data based on user actions.

In the approach taken in RmlUi, the MVC terms have the following meaning.

- `Model`  The data model is the interface between the user data through data variables, and the views and controllers assigned to the model.
- `View`  Data views are used to present a data variable in the document by different means.
- `Controller` Data controllers typically respond to user input by setting a new value to a data variable.

Views are automatically updated whenever a variable becomes dirty. This ensures that the document displayed to the user is always synchronized with the application data. Using the MVC appoach, there is no need to handle individual elements, or manually modify the RML.

See the following detailed sections:

- [Examples](data_bindings/examples.html)
- [Data variables and expressions](data_bindings/expressions.html)
- [Data model](data_bindings/model.html)
- [Data views and controllers](data_bindings/views_and_controllers.html)

```html
<h1>Simple data binding example</h1>
<div data-model="my_model">
	<h2>{{title}}</h2>
	<p data-if="show_text">The quick brown fox jumps over the lazy {{animal}}.</p>
	<input type="text" data-value="animal"/>
</div>
```

---

##### Limitations

- You should not affect the document structure within a data model. This includes manually adding or removing elements. Eg. removing an element inside a `data-for` view is undefined behavior and may lead to a crash.
- Some special elements internally change the structure of the document, this includes in particular the `<select>`{:.tag} and `<option>`{:.tag} elements. For such elements, data bindings may not work as intended.
- Currently, only top-level data variables can have a dirty state. That means data addresses can not be used to dirty just an Array index or Struct member. However, sub-values that have not been changed will be ignored inside the relevant views.
- Adding `data-` attributes after the element has been attached to the document has no effect.
- Types need to be re-registered if binding variables in different dynamic libraries.

##### Authoring notes

- Element attributes starting with `data-` are reserved for databindings in RmlUi.
- It is considered illegal to use `{{` and `}}` inside RML documents outside the context of data bindings.

##### Changelog

A list of breaking changes before the initial release.

- 2020-12-21. The function `DataModelHandle::Update()` has been removed, as it is no longer needed. Data model updates are now automatically handled during `Context::Update()`.

{% endraw %}

{% comment %} End raw mode, see the comment at the beginning of the document. {% endcomment %}
