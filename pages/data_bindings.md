---
layout: page
title: Data bindings (preview)
---

{% comment %} 
	The open and close brackets { { ... } } used in RmlUi's data binding syntax interferes with the Liquid templating language in Jekyll. We turn off Liquid processing by enabling raw mode for the entire document.
{% endcomment %}

{% raw %}

RmlUi supports a model-view-controller (MVC) approach through data bindings. This is a powerful approach for responding to changes in the data, or in reverse, updating data based on user actions.

---
***NOTE***

The data bindings feature is in-development for RmlUi 4.0 and should be considered experimental. The presented API is subject to change.

---

In the approach taken in RmlUi, the MVC terms have the following meaning.

- `Model`  The data model is the interface between the user data through data variables, and the views and controllers assigned to the model.
- `View`  Data views are used to present a data variable in the document by different means.
- `Controller` Data controllers typically respond to user input by setting a new value to a data variable.

Views are automatically updated whenever a variable becomes dirty. This ensures that the document displayed to the user is always synchronized with the application data. Using the MVC appoach, there is no need to handle individual elements, or manually modify the RML.

## Basic example

```html
<h1>Simple data binding example</h1>
<div data-model="my_model">
	<h2>{{title}}</h2>
	<p data-if="show_text">The quick brown fox jumps over the lazy {{animal}}.</p>
	<input type="text" data-value="animal"/>
</div>
```

The `data-model` attribute declares that all its children elements here belong to `my_model`.
- When `{{title}}` is encountered, it is automatically replaced by the data variable `title` bound to its model. Furthermore, whenever the variable is modified its content is automatically updated.
- The `data-if` attribute creates a data view which displays its content whenever its data variable evaluates to `true`.
- The `data-value` attribute creates both a data view and a data controller. The view updates the element's value whenever the data is changed in the application. Contrarily, the controller listens to modifications to the element's value and modifies the data variable accordingly. Thus, whenever the user changes the text field, the `animal` variable is modified which results in the text contents of the `p` tag to reflect the new text.


#### Setting up the data model

The data model is first set up in C++. Using the above example, all that is needed is the following code.
```cpp
using namespace Rml;

struct MyData {
	String title = "Hello World!";
	String animal = "dog";
	bool show_text = true;
} my_data;

bool SetupDataBinding(Context* context, DataModelHandle& my_model)
{
	DataModelConstructor constructor = context->CreateDataModel("my_model");
	if (!constructor)
		return false;

	constructor.Bind("title", &my_data.title);
	constructor.Bind("animal", &my_data.animal);
	constructor.Bind("show_text", &my_data.show_text);

	my_model = constructor.GetModelHandle();

	return true;
}

void Update(DataModelHandle my_model)
{
	my_model.Update();
}
```
The `SetupDataBinding` function should be called once before loading the document. The `Update` function should be called on every game loop iteration, after submitting input events to the context, but before the context update.

That's it! Now the basic example above will work as expected, assigning the input text to the `animal` data binding whenever changed, and updating the paragraph text.

We might want to do more though, and indeed, there is much more power available here. Let us extend the `Update()` method above with the following.
```cpp
void Update(DataModelHandle my_model)
{
	if (my_model.IsVariableDirty("animal"))
	{
		my_data.title = " Hello " + my_data.animal + "!";
		my_model.DirtyVariable("title");
	}

	my_model.Update();
}
```
Now the title is updated as well whenever the input text is changed. Note that we have to tell the model that the data has changed on the C++ side. This example is slightly contrived, as this behavior could easily be done purely with data bindings in RML. However, it is easy to envision the power here. Let us do a somewhat more involved example next to demonstrate.


## Extended example

```html
<p>
	Incoming invaders:
	<input type="range" name="rating" min="0" max="20" step="5" data-value="incoming_invaders_rate"/>
	{{ incoming_invaders_rate }} / min.
</p>
<button data-event-click="launch_weapons">Launch weapons!</button>
<div data-for="invader : invaders">
	<h1 data-class-red="invader.danger_rating > 70">{{invader.name}}</h1>
	<p>Invader {{it_index + 1}} of {{ invaders.size }}.</p>
	<img data-attr-sprite="invader.sprite" data-style-image-color="invader.color"/>
	<p>
		Shots fired (damage): <span data-for="invader.damage"> {{it}} </span>
	</p>
</div>
<h1 data-if="invaders.size == 0">It's all safe and sound, sir!</h1>
```

Notice the comparisons and additions used in some places? These are *data expressions* and can be used in several places. This is built-in to RmlUi and supports the most common operators. In addition, they are extendible by user-provided functions.

Next, let us define the data we want to use for this model.

```cpp
using namespace Rml;

struct Invader {
	String name;
	String sprite;
	Colourb color{ 255, 255, 255 };
	std::vector<int> damage;
	float danger_rating = 50;

	void GetColor(Variant& variant) {
		variant = "rgba(" + ToString(color) + ')';
	}
};

struct InvadersData {
	double time_last_invader_spawn = 0;
	double time_last_weapons_launched = 0;

	float incoming_invaders_rate = 10; // Per minute

	std::vector<Invader> invaders = {
		Invader{"Angry invader", "icon-invader", {255, 40, 30}, {3, 6, 7}, 80}
	};

	void LaunchWeapons(DataModelHandle model_handle, Event& /*ev*/, const VariantList& /*arguments*/) {
		invaders.clear();
		model_handle.DirtyVariable("invaders");
	}

} invaders_data;
```

Here we have simple plain-old-data (POD) types, but also containers, and even containers of structs. In fact, RmlUi can handle all of this no matter how deep you want to nest this. However, we need to tell RmlUi how to handle the various types. For this, we need to register types before we can bind them.

There are three main data variable types supported in RmlUi:

1. `Scalar`. A single value which can be read from and usually written to (but not necessarily).
2. `Array`. A container which we can index into. The underlying type can be any data variable type.
3. `Struct`. A collection of named members. Members can be any data variable type.

Arithmetic types (eg. `int`, `float`), as well as `Rml::String` are supported without the need to register them. Other types need to be registered first. The following C++ code demonstrates how to register the types for the above data, and bind the variables.

```cpp
bool SetupDataBinding(Context* context, DataModelHandle& invaders_model)
{
	DataModelConstructor constructor = context->CreateDataModel("invaders");
	if (!constructor)
		return false;

	// First, register types so that RmlUi knows how to process them.

	// Invader::damage uses std::vector<int>, we need to tell RmlUi that this is an array type.
	constructor.RegisterArray<std::vector<int>>();

	// Structs are registered by adding all its members through the returned handle.
	if (auto invader_handle = constructor.RegisterStruct<Invader>())
	{
		invader_handle.RegisterMember("name", &Invader::name);
		invader_handle.RegisterMember("sprite", &Invader::sprite);
		invader_handle.RegisterMember("damage", &Invader::damage);
		invader_handle.RegisterMember("danger_rating", &Invader::danger_rating);

		// Getter and setter functions can also be used.
		invader_handle.RegisterMemberFunc("color", &Invader::GetColor);
	}

	// We can even have an Array of Structs, infinitely nested if we so desire.
	// Make sure the underlying type (here Invader) is registered before the array.
	constructor.RegisterArray<std::vector<Invader>>();

	// Now we can bind the variables to the model.
	constructor.Bind("incoming_invaders_rate", &invaders_data.incoming_invaders_rate);
	constructor.Bind("invaders", &invaders_data.invaders);

	// This function will be called when the user clicks the 'Launch weapons' button.
	constructor.BindEventCallback("launch_weapons", &InvadersData::LaunchWeapons, &invaders_data);

	invaders_model = constructor.GetModelHandle();
}
```


Finally, we want to make some behaviors to make things interesting, such as spawning new invaders depending on the rate set by the user. The following should be run during the update loop of the application.

```cpp
void Update(DataModelHandle invaders_model)
{
	const double t = GetSystemInterface()->GetElapsedTime();

	// Add new invaders at regular time intervals.
	const double t_next_spawn = invaders_data.time_last_invader_spawn + 60.0 / double(invaders_data.incoming_invaders_rate);
	if (t >= t_next_spawn)
	{
		const int num_items = 4;
		static std::array<Rml::String, num_items> names = { "Angry invader", "Harmless invader", "Deceitful invader", "Cute invader" };
		static std::array<Rml::String, num_items> sprites = { "icon-invader", "icon-flag", "icon-game", "icon-waves" };
		static std::array<Rml::Colourb, num_items> colors = {{ { 255, 40, 30 }, {20, 40, 255}, {255, 255, 30}, {230, 230, 230} }};

		Invader new_invader;
		new_invader.name = names[rand() % num_items];
		new_invader.sprite = sprites[rand() % num_items];
		new_invader.color = colors[rand() % num_items];
		new_invader.danger_rating = float((rand() % 100) + 1);
		invaders_data.invaders.push_back(new_invader);

		invaders_model.DirtyVariable("invaders");
		invaders_data.time_last_invader_spawn = t;
	}

	// Launch shots from a random invader.
	if (t >= invaders_data.time_last_weapons_launched + 1.0)
	{
		if (!invaders_data.invaders.empty())
		{
			const size_t index = size_t(rand() % int(invaders_data.invaders.size()));

			Invader& invader = invaders_data.invaders[index];
			invader.damage.push_back(rand() % int(invader.danger_rating));

			invaders_model.DirtyVariable("invaders");
		}
		invaders_data.time_last_weapons_launched = t;
	}

	invaders_model.Update();
}
```

This update loop spawns new invaders at regular intervals, determined by the `range` input slider. The `data-for` loop ensures that new invaders are displayed automatically. The data bindings further ensure that the sprite and color of the invaders are set to the given values.

## Data variables

Data variables are wrappers around the user's raw data. There are three primary types.

1. `Scalar`. A single value which can be read from and usually written to (but not necessarily).
2. `Array`. A container which can be indexed into. The underlying type can be any data variable type.
3. `Struct`. A collection of named members. Members can be any data variable type.

In the data model, each variable has an associated *data address*. The address follows the normal C++ syntax, use `.x` to access a member, and `[i]` to index into an array. In addition, `.size` can be used on arrays to get their size.

The following examples are valid data addresses.
```
title
invader.health
invaders[1].name
invaders.size
a.very[5].long.data[99].address
```

Arithmetic types (eg. `int`, `float`), as well as `Rml::String` are supported without the need to register them. Other types need to be registered first. It is also possible to bind a variable using getter and setter functions, then the data variable acts as a scalar type. See details for registering types in the data model documentation. 


## Data expressions

Data expressions are small expressions which can take one or several data variables, modify them through common operations, and return the result. Several data views and controllers can use them for more flexibility in how the data should be displayed.

The syntax resembles C++, and should be familiar for most programmers. The following table lists the allowed operators, and their precedence. Operators with the same precedence are evaluated left-to-right.

| Precedence| Operator        | Description                       |
| --------- | ----------------| --------------------------------- |
|   1       |  !              | Logical NOT.                      |
|   2       |  \* \/          | Multiplication and division.      |
|   3       |  +              | Addition or string concatenation. |
|   3       |  -              | Subtraction.                      |
|   4       | == != < <= > => | Relational comparisons.           |
|   5       | && \|\|         | Logical AND, OR.                  |
|   5       | \|              | Transform.                        |
|   5       | a?b:c           | Ternary conditional.              |

Parenthesis `( )` always take precedence over operators. The addition operator will do string concatenation if either of its arguments is a string, otherwise it uses numeric addition. 

The following types can be used in the expressions.

1. Data address, pointing to a scalar data variable.
2. Literal. 
   - Numeric. Eg. `42` or `-3.2`. Integers or fractional.
   - String. Eg. `'Play!'`. Always written using single quotes.
3. Keyword. `true` or `false`.

Operators read their arguments either as a `bool`, a `double`, or a `String`. Conversions are done implicitly when needed using the type conversion facilities in RmlUi.

#### Transform functions

The transform operator `|` can call a *transform function*. A transform function can modify the evaluated value on its left-hand-side, using the following syntax.
```
| transform_name
```
or
```
| transform_name([data_expression], [data_expression], ...)
```

Any arguments in parenthesis are forwarded to the transform function. Users can provide their own transform functions. In addition, there are several built-in transform functions.

| Transform name | Arguments                                 | Return type  | Description                           |
| -------------  | ----------------------------------------- | ------------ | ------------------------------------- |
|   to_upper     |                                           | String       | Transform string to upper case.       |
|   to_lower     |                                           | String       | Transform string to lower case.       |
|   round        |                                           | Numeric      | Round a value to its nearest integer. |
|   format       |  `precision`, `remove_trailing_zeros` = `false` | String       | Format a numeric value.<br/>`precision` determines the number of fractional digits written.<br/>`remove_trailing_zeros` removes any trailing zeros and possibly the decimal character from the number. |

See the data model documentation for how to provide your own transform functions.

Note that transform functions can easily be pipelined as in the following example.
```
i * 3.14159 | round | my_pow(4) | transform(2) 
```


#### Assignment expressions

Data views never assign values to data variables, they only read from them. On the other hand, data controllers can assign values to data variables. For this purpose, there is also support for *assignment expressions*.

For now, assignment expressions can only be used in the `data-event` controller. Syntax and details are located in the documentation for this controller.



#### Expression examples


| Example                                                                 | Possible result       |
| ---------------------------------------------------------------------   | --------------------- |
| `rating < 80`                                                           | `1`                   |
| `radius + 'm'`                                                          | `8.7m`                |
| `(radius \| format(2)) + 'm'`                                           | `8.70m`               |
| `radius < 10.5 ? 'small' : 'large'`                                     | `small`               |
| `'hot' + 'dog' \| to_upper`                                             | `HOTDOG`              |
| `'x: ' + ev.mouse_x + '<br/>y: ' + ev.mouse_y`                          | `x: 128<br/>y: 958`   |
| `true \|\| false ? (true && 3==1+2 ? 'Absolutely!' : 'well..') : 'no'`  | `Absolutely!`         |





## Model

The data model is the interface between the user data, and the views and controllers assigned to the model.

Each `Context` can store several named data models. In the RML document, the given data model is applied by using the `data-model=[model_name]` attribute. Then, all its children belong to the given data model, and can reference data variables within it.

The procedure for setting up and handling a data model should be as follows.

1. Create the data model on the context with a given name.
2. Register any Struct or Array types to be used using the *data model constructor*.
3. Bind variables using the data model constructor.
4. Load the document.

Then, during the update loop, after the inputs have been submitted but before the `Context::Update` call:

1. Get dirty state of data variables if desired, and set dirty state on any data changed on the C++-side.
2. Call `Update` on the *data model handle*.

Usage of the model constructor and model handle are detailed in the following sections.

### Model constructor

The function `Context::CreateModel` returns a data model constructor which can be used to register types and functions, and bind variables.

#### Registering types

Users should first register types before binding variables, as RmlUi may need the type information to instanciate the data variables. All registered types apply to every data model in the current context.

```cpp
template<typename Container>
bool DataModelConstructor::RegisterArray();
```
Registers `Container` as an Array. The container must have the `size()` and `begin()` member functions defined, the latter which returns an iterator which can be incremented. This is satisfied by several containers such as `std::vector` and `std::array`. This register call is all that is needed to set up an Array.

```cpp
template<typename T>
StructHandle<T> DataModelConstructor::RegisterStruct();
```
Registers `T` as a Struct. The function returns an object which can be used to register its members. Member objects, and getter- and setter functions can be registered. See the following example.

```cpp
struct Vec2 {
	float x, y;
	
	void GetLength(Rml::Variant& variant) {
		variant = Variant(std::sqrt(x*x + y*y));
	}
	void SetLength(const Rml::Variant& variant) {
		float new_length = variant.Get<float>();
		float cur_length = std::sqrt(x*x + y*y);
		x *= new_length / cur_length;
		y *= new_length / cur_length;
	}
}

if (auto vec2_handle = constructor.RegisterStruct<Vec2>())
{
	vec2_handle.RegisterMember("x", &Vec2::x);
	vec2_handle.RegisterMember("y", &Vec2::y);
	vec2_handle.RegisterMemberFunc("length", &Vec2::GetLength, &Vec2::SetLength);
}
```

#### Registering transform functions

Transform functions can be used in data expression by the `|` operator. A transform function can be registered using the function

```cpp
void DataModelConstructor::RegisterTransformFunc(const String& name, DataTransformFunc transform_func);
```
where the transform function is defined as
```cpp
using DataTransformFunc = std::function<bool(Variant&, const VariantList&)>;
```
The first argument contains the value of the left hand side of the operator, and should be assigned the new, transformed value. The second argument takes a list of optional arguments passed in by the user in the data expression.

#### Binding data variables

Data variables strictly apply to the current data model. The data variable is a a wrapper around a raw pointer - or a get/set function pair. The pointed-to type must first have been *registered* unless it is an arithmetic type (such as `int`, `char`, `float`), or `Rml::String`. 

Bind the data variables using the following functions.
```cpp
// Bind a data variable.
template<typename T>
bool DataModelConstructor::Bind(const String& name, T* ptr);

// Bind a get/set function pair.
bool DataModelConstructor::BindFunc(const String& name, DataGetFunc get_func, DataSetFunc set_func = {});
```
Here, the provided `name` is used when referencing the data variable in data expressions, and for getting and setting the dirty state of variables. Next, `ptr` is a pointer to the data on the user side. The lifetime of this data must extend the current data model, which for now means until after the context has been destroyed (TODO: It is not yet possible to remove data models from the context). Finally, the get/set functions are defined as

```cpp
using DataGetFunc = std::function<void(Variant&)>;
using DataSetFunc = std::function<void(const Variant&)>;
```

#### Binding event callback functions

Event callbacks can be used in the `data-event` controller to receive and act on events.

```cpp
bool DataModelConstructor::BindEventCallback(const String& name, DataEventFunc event_func);
```

where

```cpp
using DataEventFunc = std::function<void(DataModelHandle, Event&, const VariantList&)>;
```

The `DataModelHandle` is a handle to the data model which generated the event callback. The `Event` is the event which generated the event callback, and can be used like other events in RmlUi, including reading its properties and stopping propagation. `VariantList` provides a list of arguments passed in by the user in the `data-event` assignment expression.

#### Returning the data model handle

Finally, the data model handle can be returned from the `DataModelConstructor` by calling

```cpp
DataModelHandle DataModelConstructor::GetModelHandle() const;
```



### Model handle

The data model handle is used to interact with the data model after setting it up.

```cpp
void DataModelHandle::DirtyVariable(const String& variable_name);

bool DataModelHandle::IsVariableDirty(const String& variable_name);

void DataModelHandle::Update();
```

`DirtyVariable()` should be called every time the data is changed on the C++ side.  `IsVariableDirty()` can be used to check if eg. a controller changed the value of a data variable. All dirty variables are cleared after a call to `Update()`. Thus, dirty variables should be checked after inputs have been processed but before the model update.

Finally, `Update()` calls update on all the views of the data model whose dependent data variables are dirty, updating the document to represent the new values of the data variables.


## Views

Data views are used to present a data variable in the document by different means.
A data view is declared in the document by the element attribute:
	
	data-[type]-[modifier]="[value]"

The modifier may or may not be required depending on the data view.

The following table lists all built-in data views in RmlUi, along with their declaration.


| Name     | Attribute                  | Value                                           | Notes |
| ---------| ---------------------------| ----------------------------------------------- | ----- |
| attribute| data-attr-[attribute_name] | [data_expression]                               |       |
| style    | data-style-[property_name] | [data_expression]                               |       |
| class    | data-class-[class_name]    | [data_expression]                               |       |
| if       | data-if                    | [data_expression]                               |       |
| visible  | data-visible               | [data_expression]                               |       |
| for      | data-for                   | [iterator_name], [index_name] : [data_address]  | [1]   |
| rml      | data-rml                   | [data_expression]                               |       |
| value    | data-value                 | [data_address]                                  | [2]   |
| text     | N/A                        | N/A                                             | [3]   |

  [1] `iterator_name` and `index_name` are optional. Defaults to `it` and `it_index`, respectively.  
  [2] In addition to the view, this attribute also applies the `value` controller to the element.  
  [3] The text view is automatically added whenever double curly brackets {{ }} are encountered in the element's text.

### Attribute

Sets the element's attribute `[attribute_name]` to the evaluated expression.

```html
<img data-attr-sprite="item.icon"/>
```


### Style

Sets the property `[property_name]` of the element's style to the evaluated expression.

```html
<img sprite="invader" data-style-image-color="invader.color"/>
```


### Class

Enables the class `[class_name]` on the element if the expression evaluates to `true`, otherwise it disables the class.

```html
<h1 data-class-red="score < 30">Score</h1>
```


### If

Sets the `display` property of the element to `none` if the expression evaluates to `false`, otherwise it removes the `display` property from the class.

```html
<div data-if="rating > 50">
	Thanks for the <span data-if="rating >= 80">awesome</span> rating!
</div>
```

*Note.* The style sheet rules which applies to the element should ensure that the element's `display` property evaluates to something other than `none`. Otherwise, the element will always be hidden.


### Visible

Sets the `visibility` property of the element to `hidden` if the expression evaluates to `false`, otherwise it removes the `visibility` property from the class.

```html
<div data-visible="collected_stars > 0">
	<img sprite="star"/>
</div>
```

As opposed to the `data-if` view, the `data-visible` view ensures that the element retains it's size regardless of visibility.

*Note.* The style sheet rules which applies to the element should ensure that the element's `visibility` property evaluates to `visible`, which is the default value. Otherwise, the element will always be hidden.


### For

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

*Note.* For performance reasons the names of global data variables shadow iterator names. Thus, do not use an iterator name which is used for a data binding.  
*Implementation note.* Internally, the XML parser uses a special parsing rule whenever the `data-for` attribute is encountered, providing all the children of the current element as raw RML text to the data view, which is later used for creation of each item in the data array.


### Rml

Sets the element's inner RML to the evaluated expression.

```html
<div data-rml="incoming_invaders ? '<em>Send help!</em>' : 'Clear skies.'">
</div>
```


### Value

Sets the element's `value` attribute to the value of the variable located at `data_address`. This variable must be a scalar type. This is generally useful for `input`{:.tag} elements.

```html
<input type="range" min="0" max="100" step="1" data-value="rating"/>
```

*Note.* The `data-value` attribute also applies the `value` controller to the element, enabling two-way communication.  
*Note.* Data expressions are not supported for this data view. Instead, use the attribute view for one-way communication.


### Text

Evaluates any data expression inside double curly brackets {{ }} encountered in the element's text.

```html
<span class="position"> x: {{ position.x }}, y: {{ position.y }}</span>
<span data-for="i : indices"> {{ i * 2 + (i > 10 ? ' wow!' | to_upper : '') }}</span>
```

This data view is automatically added whenever double curly brackets are encountered in the text and should not be added as an attribute.


## Controllers

Data controllers are used to respond to changes in the document, typically as a result of user input. When a controller is triggered, it sets a data variable in its owning data model.

A data controller is declared in the document by the element attribute:

    data-[type]-[modifier]="[value]"

This is similar to declaration of data views, except that controllers instead take an assignment expression to set a variable. Note that, as opposed to views, controllers only respond to certain changes in the document, not to changed data variables.

The modifier may or may not be required depending on the data controller.


| Name      | Attribute                   | Value                             | Notes |
| --------- | --------------------------- | --------------------------------- | ----- |
| value     | data-value                  | [data_address]                    | [1]   |
| event     | data-event-[event_type]     | [assignment_expression]           |       |

[1] In addition to the controller, this attribute also applies the `value` view to the element.


### Value

The value controller is triggered whenever a `change` event occurs on the current element. The new value is assigned to the specified data variable.

```html
<input type="range" min="0" max="100" step="1" data-value="rating"/>
```

*Note.* The `data-value` attribute also applies the `value` view  to the element, enabling two-way communication.  
*Note.* Assignment expressions are not supported for this data controller. Instead, use the `data-event-change` controller for more flexibility.


### Event

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


## Limitations

- Currently, only top-level data variables can have a dirty state. That means data addresses can not be used to dirty just an Array index or Struct member. However, sub-values that have not been changed will be ignored inside the relevant views.
- You should not affect the document structure within a data model. This includes manually adding or removing elements. Eg. removing an element inside a `data-for` view is undefined behavior and may lead to a crash.
- Adding `data-` attributes after the element has been attached to the document has no effect.
- Types need to be re-registered if binding variables in different dynamic libraries.

## Authoring notes

- Element attributes starting with `data-` are reserved for databindings in RmlUi.
- It is considered illegal to use `{{` and `}}` inside RML documents outside the context of data bindings.

{% endraw %}

{% comment %} End raw mode, see the comment at the beginning of the document. {% endcomment %}
