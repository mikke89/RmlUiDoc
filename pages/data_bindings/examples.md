---
layout: page
title: Data binding examples
parent: data_bindings
next: expressions
---

{% raw %}

### Basic example

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
- The `data-value` attribute creates both a data view and a data controller, enabling a two-way binding. The view updates the element's value whenever the data is changed in the application. Contrarily, the controller listens to modifications to the element's value and modifies the data variable accordingly. Thus, whenever the user changes the text field, the `animal` variable is modified which results in the text contents of the `p` tag to reflect the new text.


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
```
The `SetupDataBinding` function should be called once before loading the document.

That's it! Now the basic example above will work as expected, assigning the input text to the `animal` data binding whenever changed, and updating the paragraph text.

We might want to do more though, and indeed, there is much more power available here. Let us add an `Update()` method which is called on every game loop iteration. This should be called after submitting input events to the context, but before the context update.
```cpp
void Update(DataModelHandle my_model)
{
	if (my_model.IsVariableDirty("animal"))
	{
		my_data.title = " Hello " + my_data.animal + "!";
		my_model.DirtyVariable("title");
	}
}
```
Now the title is updated as well whenever the input text is changed. Note that we have to tell the model that the data has changed on the C++ side. This example is slightly contrived, as this behavior could easily be done purely with data bindings in RML. However, it is easy to envision the power here. Let us do a somewhat more involved example next to demonstrate.


### Extended example

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
}
```

This update loop spawns new invaders at regular intervals, determined by the `range` input slider. The `data-for` loop ensures that new invaders are displayed automatically. The data bindings further ensure that the sprite and color of the invaders are set to the given values.

{% endraw %}
