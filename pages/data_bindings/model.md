---
layout: page
title: Data model
parent: data_bindings
next: views_and_controllers
---

{% raw %}

The data model is the interface between the user data, and the views and controllers assigned to the model.

Each `Context` can store several named data models. In the RML document, the given data model is applied by using the `data-model=[model_name]` attribute. Then, all its children belong to the given data model, and can reference data variables within it.

The procedure for setting up and handling a data model should be as follows.

1. Create the data model on the context with a given name.
2. Register any Struct or Array types to be used using the *data model constructor*.
3. Bind variables using the data model constructor.
4. Load the document.

Then, during the update loop:

1. Submit inputs to the context as normal. Data controllers will update data variables on the client side as necessary, and consequently set the dirty flag on the same variables.
2. It is now safe to query the data model for dirty data variables if desired, and set dirty state on any data changed on the client side.
3. Finally, during the call to `Context::Update`, all data views will be updated with any dirtied data variables.

Usage of the model constructor and model handle are detailed in the following sections.

### Model constructor

The function `Context::CreateModel` returns a data model constructor which can be used to register types and functions, and bind variables.

```cpp
/// Creates a data model.
/// @param[in] name The name of the data model.
/// @return A constructor for the data model, or empty if it could not be created.
DataModelConstructor Context::CreateDataModel(const String& name);
```

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
Here, the provided `name` is used when referencing the data variable in data expressions, and for getting and setting the dirty state of variables. Next, `ptr` is a pointer to the data on the user side. The lifetime of this data must extend the current data model. That means either until the context is destroyed, or until the data model has been manually removed from the context. Finally, the get/set functions are defined as

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
```

`DirtyVariable()` should be called every time the data is changed on the client side. `IsVariableDirty()` can be used to check if eg. a controller changed the value of a data variable. All dirty variables are cleared after a call to `Context::Update()`. Thus, dirty variables should be checked after inputs have been processed but before the context update.


### Removing the data model

The data model can be manually closed by calling the following on the owning context.

```cpp
/// Removes the given data model.
/// This also removes all data views, controllers and bindings contained by the data model.
/// @warning Invalidates all handles and constructors pointing to the data model.
/// @param[in] name The name of the data model.
/// @return True if succesfully removed, false if no data model was found.
bool Context::RemoveDataModel(const String& name);
```

Otherwise the data model is removed automatically when the context is destroyed.

{% endraw %}
