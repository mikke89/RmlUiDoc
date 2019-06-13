---
layout: page
title: Style sheets and Properties
parent: cpp_manual
next: decorators
---

A {{page.lib_name}} document may have a number of style sheets attached to it. Each of those style sheets has a list of RCSS properties and rules for selecting which elements those properties are applied to. Any element may also have properties set on them directly.

This document only details the C++ interface into the style sheet and property system; for detailed information on what properties are supported and what their function is, see the [RCSS documentation](../rcss.html).

### Style sheets

Style sheets are automatically loaded and attached to a document when you use the `<link type="text/rcss" />`{:.tag} tag in the header of an RML document; this is the most common way style sheets are loaded.

If you want to dynamically create or load a style sheet, the {{page.lib_name}} factory (the class `{{page.lib_ns}}::Core::Factory`) has the ability to do this:

```cpp
// Creates a style sheet from a user-generated string.
static {{page.lib_ns}}::Core::StyleSheet* InstanceStyleSheetString(const {{page.lib_ns}}::Core::String& string);
// Creates a style sheet from a file.
static {{page.lib_ns}}::Core::StyleSheet* InstanceStyleSheetFile(const {{page.lib_ns}}::Core::String& file_name);
```

`InstanceStyleSheetString()` allows you to parse a string you've built up in your application into a style sheet. This is used in the debugger to keep all of its RML and RCSS content inline. `InstanceStyleSheetFile()` will load a style sheet from an RCSS file. Both of these functions will return a style sheet pointer on success, which you can then set on a document.

Style sheets are reference counted, and a dynamically-loaded style sheet will be returned to you with a single reference count. Remember to remove the reference as appropriate, otherwise the style sheet will never be released.

There is currently no way to add rules or properties to a style sheet once it has been loaded.

### Properties

#### Querying properties

Properties can be requested from an element with the `GetProperty()` function.

```cpp
// Returns one of this element's properties.
const {{page.lib_ns}}::Core::Property* GetProperty(const {{page.lib_ns}}::Core::String& name);		
// Returns the values of one of this element's properties.		
template < typename T >
T {{page.lib_ns}}::Core::GetProperty(const {{page.lib_ns}}::Core::String& name);
```

The first, non-templated, `GetProperty()` function will return the value of request property on the element. If the element does not have the property defined itself, it will either return the default value (if the property is not inherited) or its parent's value (if it is inherited). If the property requested is invalid (ie, not defined in the specification), NULL will be returned.

The `{{page.lib_ns}}::Core::Property` structure is defined in `<{{page.lib_dir}}/Core/Property.h>`{:.incl}. Below is a list of its useful members:

```cpp
class {{page.lib_ns}}::Core::Property
{
public:
	enum Unit
	{
		UNKNOWN,
		KEYWORD,
		STRING,
		NUMBER,
		PX,
		COLOUR,
		EM,
		PERCENT,
	};

	/// Get the property as a string.
	{{page.lib_ns}}::Core::String ToString() const;

	/// Templatised accessor.
	template <typename T>
	T Get() const
	{
		return value.Get<T>();
	}

	{{page.lib_ns}}::Core::Variant value;
	Unit unit;
};
```

Each property stores the unit its value is in and the value itself as a variant type (`{{page.lib_ns}}::Core::Variant`), which is a structure capable of storing a multitude of types. To retrieve the value from the variant, use the templated `Get<>()` function on the property or the variant itself. The type you should request the value as depends on the property's unit:

* `UNKNOWN` and `STRING` values should be requested as `{{page.lib_ns}}::Core::String` types.
* `KEYWORD` values should be requested as int types. Keyword values are stored as integers for speed; to check what the value means, you can compare it to the constant values defined in `<{{page.lib_dir}}/Core/StyleSheetKeywords.h>`{:.incl}. For custom keyword properties, see below.
* `NUMBER`, `PX`, `EM` and `PERCENT` values should be requested as float types. The exact meaning of the value depends on the unit. 

If you call Get<>() with the wrong type, the variant will do the best it can to convert between the types. For example, if you request a string type on a floating-point value, you will get the stringised form of the value.

For example, the following will request the font family of an element:

```cpp
element->GetProperty("font-family")->Get< {{page.lib_ns}}::Core::String >();
```

The following will check if an element's font weight is bold:

```cpp
bool bold = element->GetProperty("font-weight")->Get< int >() == {{page.lib_ns}}::Core::FONT_WEIGHT_BOLD;
```

You can use the templated `GetProperty()` function to conveniently (and dangerously!) return you the typed value of the requested property. For example:

```cpp
bool bold = element->GetProperty< int >("font-weight") == {{page.lib_ns}}::Core::FONT_WEIGHT_BOLD;
```

#### Setting properties

Properties can be set directly on an element with the `SetProperty()` function.

```cpp
// Sets a local property override on the element.
bool SetProperty(const {{page.lib_ns}}::Core::String& name, const {{page.lib_ns}}::Core::String& value);
```

This is equivalent to setting an inline property on an element using the `style`{:.attr} attribute. For example:

```html
<div id="test" style="width: 200px;" />
```

is equivalent to:

```cpp
{{page.lib_ns}}::Core::Element* test = document->GetElementById("test");
if (test != NULL)
	test->SetProperty("width", "200px");
```

Properties changed in this manner will automatically propagate to child elements if inherited and force a layout if necessary.

#### Defining custom properties

User-defined properties can be added to the global style sheet specification, so you can attach any values you'd like to your elements. This is done through the `{{page.lib_ns}}::Core::StyleSheetSpecification` class (included through `{{page.lib_dir}}/Core.h`{:.incl} or `{{page.lib_dir}}/Core/StyleSheetSpecification.h`{:.incl}).

```cpp
// Registers a property with a new definition.
// @param[in] property_name The name to register the new property under.
// @param[in] default_value The default value to be used for an element if it has no other definition provided.
// @param[in] inherited True if this property is inherited from parent to child, false otherwise.
// @param[in] forces_layout True if a change in this property on an element will cause the element's layout to possibly change.
// @return The new property definition, ready to have parsers attached.
static {{page.lib_ns}}::Core::PropertyDefinition& RegisterProperty(const {{page.lib_ns}}::Core::String& property_name,
                                                          const {{page.lib_ns}}::Core::String& default_value,
                                                          bool inherited,
                                                          bool forces_layout = false);
```

The `RegisterProperty()` function takes the name of the new property, the default value of the property (the value of the property on an element if it has not been set on that element), and a boolean value indicating whether the property is inherited. If this is set to true, if an element does not have the property set on it then it will inherit it's parent value for the property instead of using the default value. If the last variable, forces_layout, is set to `true`, then any change in the property will force the element to be re-laid out. For custom properties this should generally be left as false, as only the built-in properties will affect layout.

So, for example, if we wanted to define a new property for storing the sound an element makes when it is clicked, we'd call this soon after the {{page.lib_name}} was initialised:

```cpp
{{page.lib_ns}}::Core::StyleSheetSpecification::RegisterProperty("click-sound", "none", false);
```

This wouldn't be much use to us though, as we haven't said what values the new property can take. For this, we need to add a property parser to the new property. A property parser attempts to parse the value of a property from a raw string into a format where it can be used by the application.

Each property can have multiple parsers attached to it. There are four default property parsers in {{page.lib_name}}, although custom parsers [can be added](#defining-custom-value-parsers). These are:

* _number_, for numerical values either with a prefix ('0px', '0.5em'), a percentage ('50%') or simply a number ('15').
* _keyword_, for keyword values (such as the `font-weight`{:.prop} property, which can be either 'normal' or 'bold').
* _string_, for values that can be set to any string (such as `font-family`{:.prop}).
* _colour_, for values that are stored as a colour. 

To attach a parser to a property, call the `AddParser()` function on the returned value from the `RegisterProperty()` function. To attach a second or third parser, call `AddParser()` again on the value returned from the previous call to `AddParser()`. If multiple parsers are added, values will be run through the parsers in the order that they are specified until one successfully parses the value. Beware of this if you are registering the 'string' parser - make sure you register it last, as it will happily parse any value you give it!

So, to add a keyword and a string parser to the previous example, we'd do:

```cpp
{{page.lib_ns}}::Core::StyleSheetSpecification::RegisterProperty("click-sound", "none", false)
	.AddParser("keyword", "none, beep, boop, bang")
	.AddParser("string");
```

Now if the property is set to 'none', 'beep', 'boop' or 'bang', the property's value will be set to the appropriate keyword, otherwise it will be set as a string. So, the following RCSS:

```
button
{
	click-sound: beep;
}

button.siren
{
	click-sound: siren.wav;
}
```

will set the `click-sound`{:.prop} property to the keyword 'beep' for all 'button' elements, except if they are of class 'siren', in which case it will be set to the string value "siren.wav".

Each of the parsers stores their values as a particular unit and type in the property's variant. These are:

* _number_ stores values as `NUMBER`, `PX`, `EM` or `PERCENTAGE`. Use `Get< float >()` to request the value.
* _keyword_ stores values as `KEYWORD`. The value is the integer index of the specified keyword in the CSV list of allowed keywords; so, in the previous example, a value of 'none' would be 0, 'beep' would be 1, and so on. Use `Get< int >()` to request the value.
* _string_ stores values as `STRING`. Use `Get< {{page.lib_ns}}::Core::String >()` to request the value.
* _colour_ stores values as `COLOUR`. Use `Get< {{page.lib_ns}}::Core::Colourb >` to request the value. 

#### Defining custom shorthands

You can define custom shorthands as well as properties. Use the `RegisterShorthand()` function to do this.

```cpp
// Registers a shorthand property definition.
// @param[in] shorthand_name The name to register the new shorthand property under.
// @param[in] properties A comma-separated list of the properties this definition is shorthand for.
// @param[in] type The type of shorthand to declare.
// @param True if all the property names exist, false otherwise.
static bool RegisterShorthand(const {{page.lib_ns}}::Core::String& shorthand_name,
                              const {{page.lib_ns}}::Core::String& property_names,
                              {{page.lib_ns}}::Core::PropertySpecification::ShorthandType type = {{page.lib_ns}}::Core::PropertySpecification::AUTO);
```

* `shorthand_name`: the name of the shorthand (the name you will use to refer to it in your RCSS).
* `property_names`: a comma-separated list of the actual properties the shorthand maps to.
* `type`: an enumeration defining how the shorthand behaves if it has fewer value given to it than it has properties to assign them to; most of the time you can leave this on `AUTO`, however you can set it to `REPLICATE` if desired (see below).

For example, the `margin`{:.prop} shorthand is defined like:

```cpp
{{page.lib_ns}}::Core::StyleSheetSpecification::RegisterShorthand("margin", "margin-top, margin-right, margin-bottom, margin-left");
```

Shorthands can operate in three modes; `FALL_THROUGH`, `REPLICATE` or `BOX`. `FALL_THROUGH` will parse each value it has against its list of properties. If any values fail to parse, they will fall-through to the next property, and so on, until they parse successfully. If there are fewer parsed values that properties, the remaining properties will be not be set. The `font`{:.prop} shorthand is the best example of this; it is a `FALL_THROUGH` shorthand property for `font-style`{:.prop}, `font-weight`{:.prop}, `font-size`{:.prop}, `font-family`{:.prop} and `font-charset`{:.prop}. The RCSS:

```css
font: italic Lacuna;
```

will parse `font-style`{:.prop} to 'italic'; 'Lacuna' will fail to parse as both a `font-weight`{:.prop} property and `font-size`{:.prop}, and fall-through to `font-family`{:.prop}. `font-charset`{:.prop} will be ignored as the shorthand is out of values.

`REPLICATE` shorthands will fail if any values fail to parse, and if there are fewer values than properties, the last value will be replicated for the other properties. For example, the `overflow`{:.prop} is a replicating shorthand for the properties `overflow-x`{:.prop} and `overflow-y`{:.prop}. The RCSS:

```css
overflow: auto;
```

will assign the 'auto' keyword to both `overflow-x`{:.prop} and `overflow-y`{:.prop}. If overflow was a `FALL_THROUGH` property, `overflow-y`{:.prop} would be left at its default.

`BOX` shorthands are for shorthands such as `margin`{:.prop}, `padding`{:.prop}, etc, that define four values for the top, right, bottom and left sides (in that order) of a box. If a `BOX` shorthand is invoked with fewer than four values, the standard CSS rules apply; that is, one value will be replicated across all four sides. Two values will be set to the vertical and horizontal sides. Three values will be set to the top, horizontal sides, and bottom.

`AUTO` shorthands will be `FALL_THROUGH` by default, unless they have exactly four properties ending in `-top`{:.prop}, `-right`{:.prop}, `-bottom`{:.prop} and `-left`{:.prop} (in that order).

#### Defining custom value parsers

If you want to define more complicated parsers for your property values, you can do so by registering a custom property parser before you register you custom properties. The base class for all property parsers is `{{page.lib_ns}}::Core::PropertyParser`; start by inheriting from this and implementing the two pure virtual functions:

```cpp
// Called to parse a RCSS declaration.
// @param[out] property The property to set the parsed value on.
// @param[in] value The raw value defined for this property.
// @param[in] parameters The list of parameters defined for this property.
// @return True if the value was parsed successfully, false otherwise.
virtual bool ParseValue({{page.lib_ns}}::Core::Property& property,
                        const {{page.lib_ns}}::Core::String& value,
                        const {{page.lib_ns}}::Core::ParameterMap& parameters) const = 0;

// Called when the parser is released. This should free all dynamic memory used by the parser.
virtual void Release() = 0;
```

`ParseValue()` is the meat of the parser. This will be called whenever the parser is required to parse a raw string value into a useful value.

* `property`: the property the parsed value and unit should be written to.
* `value`: the raw string (ie, '15px').
* `parameters`: the map of the CSV parameters given to the parser when the property was declared.

For example, if a custom parser was attached to a property in the following manner:

```cpp
{{page.lib_ns}}::Core::StyleSheetSpecification::RegisterProperty("custom-property", "parameter-1", false)
	.AddParser("custom-parser", "parameter-1, parameter-2")
```

the `parameters` map would contain the values 'parameter-1' and 'parameter-2'. The value of each of these is the index of the value in the CSV list; so, 'parameter-1' resolves to 0, 'parameter-2' resolves to 1.

If the value cannot be parsed, the unit of the property should be set to `{{page.lib_ns}}::Core::Property::UNKNOWN`. If it can be parsed, the unit should be set to something other than `UNKNOWN` and the value set on the property's variant appropriately.

The `Release()` function is called when {{page.lib_name}} is shut down; the parser should take this opportunity to delete itself if it was dynamically allocated.

Once you've got a working custom parser, call `RegisterParser()` on `StyleSheetSpecification` to register your parser against a parser name. Parser names are resolved immediately when properties are registered, so you'll need to register your parsers before you register your properties. 