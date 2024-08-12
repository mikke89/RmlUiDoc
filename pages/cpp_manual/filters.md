---
layout: page
title: Filters
parent: cpp_manual
next: debugger
---

Filters are generic, configurable, reusable objects designed to be attached to elements to add custom visual effects during rendering. The same filters can either be applied to the background of an element (the `backdrop-filter`{:.prop} property), or to the otherwise fully rendered element (the `filter`{:.prop} property). They can also be invoked to create special effects during other rendering operations, for example to apply blur onto a `box-shadow`{:.prop}.

For a full description on how filters are attached to elements and configured through RML, see the [relevant section in the RCSS documentation](../rcss/filters.html).

### Filter overview

RmlUi ships with several built-in filters, including blur, drop-shadow, and color adjustments. Depending on the visual effects you want to achieve, you may need to develop custom filters. Custom filters are defined and instanced in a similar way to custom decorators. A custom filter class is created, which needs to derive from `Rml::Filter`, and an instancer is registered for it with the RmlUi factory.

When a filter is applied to an element, all rendering for that element and its children is done one a separate render layer. When the element has completed rendering, the filter is applied to that layer, and composited onto the below layer in the layer stack. On the other hand, backdrop filters render directly onto the background of the element, before the rest of the element is rendered, without layering the element and its children.

Filters represent effects that require a specific behavior on the renderer side. Thus, a custom filter is typically accompanied by some new code, such as a new graphics shader, on the renderer side. The user will need to implement this behavior in their renderer. However, by declaring new filter types in RmlUi, users will be able to declare their custom filters directly in RCSS, just like any other built-in filters. Additionally, RmlUi will automatically handle the necessary layering so that elements are rendered correctly with the filter effect applied.

Like for decorators, filters are instanced once for each declaration in an RCSS document. Then, for each element that uses the filter, a compiled filter is created. This compiled filter is used to render the filter effect for that element.

### Custom filters

If you need custom filter effects beyond what the built-in filters can provide, you can easily create a custom filter to suit your needs.

#### Creating a custom filter

All custom filters are classes derived from `Rml::Filter`. There are two virtual functions that need to be overridden in a custom filter:

```cpp
/// Called to compile the filter for a given element.
/// @param[in] element The element the filter will be applied to.
/// @return A compiled filter constructed through the render manager, or a default-constructed one to indicate an error.
virtual Rml::CompiledFilter CompileFilter(Rml::Element* element) const = 0;

/// Called to allow extending the area being affected by this filter beyond the border box of the element.
/// @param[in] element The element the filter is being rendered on.
/// @param[in,out] overflow The ink overflow rectangle determining the clipping region to be applied when filtering the current element.
virtual void ExtendInkOverflow(Rml::Element* element, Rml::Rectanglef& overflow) const;
```

`CompileFilter()` will be called by an element that uses the filter before it is rendered. This function should return a `Rml::CompiledFilter` object containing any data needed for rendering the filter on this specific element.

`ExtendInkOverflow()` is an optional function that allows you to extend the area affected by the filter beyond the element's border box. This is useful for filters that take effect outside the border area, or that need to consider neighboring pixels, such as the blur and drop-shadow filters. If your filter doesn't need to extend beyond the element's bounds, you don't need to override this function.

For a full example, please take a look at the library's source code for the `Rml::FilterDropShadow` filter.

#### Generating a compiled filter

The compiled filter holds the data needed to render the filter for a given element. It should be constructed during the call to `CompileFilter()` function of the filter class.

```cpp
Rml::Colourb color(255, 0, 0);
Rml::Vector2f offset = {10, 20};
float sigma = 5.0f;
Rml::CompiledFilter filter = element->GetRenderManager()->CompileFilter("drop-shadow",
    Rml::Dictionary{
        {"color", Variant(color)},
        {"offset", Variant(offset)},
        {"sigma", Variant(sigma)},
    });
return filter;
```

The values provided in this dictionary will be submitted to the `CompileFilter()` function in the render interface. The user can then use these values to configure the filter effect for their renderer. The render interface will be able to return a compiled filter handle to later refer back to these values. See the [render interface filters section](interfaces/render.html#filters) for details.

Once the compiled filter is returned from `CompileFilter()`, the library will be able to use it when calling into the render interface to composite layers. It will use it to render any filters or backdrop filters declared for the element.

#### Creating a custom filter instancer

The instancer for a filter is responsible for defining and processing the properties that can be used to configure the filter. While you can create custom filters with no properties, we recommend that you expose all variables to RCSS. It's quick and easy, and you'll have much more flexible filters.

A filter instancer needs to derive from `Rml::FilterInstancer`. The following pure virtual function needs to be overridden:

```cpp
/// Instances a filter given the name and attributes from the RCSS file.
/// @param[in] name The type of filter desired. For example, "filter: simple(...)" is declared as type "simple".
/// @param[in] properties All RCSS properties associated with the filter.
/// @return A shared_ptr to the filter if it was instanced successfully.
virtual Rml::SharedPtr<Rml::Filter> InstanceFilter(const Rml::String& name,
                                                   const Rml::PropertyDictionary& properties) = 0;
```

`InstanceFilter()` will be called whenever a filter needs to be created using this instancer. It is passed `name` which provides the name that the filter was created with, and `properties` which contains the parsed property values used to specify the filter in RCSS (see below).

Once the filter has been constructed, return it as a shared pointer. If the filter was not created successfully, return a `nullptr` to indicate an error.

#### Defining the filter's properties

Each filter instancer holds a complete property specification for the filters it creates. In its constructor, the custom instancer has the opportunity to add properties and shorthands to its specification by using the protected functions `RegisterProperty()` and `RegisterShorthand()`. For detailed documentation on defining properties, see the documentation on [registering custom properties](rcss.html#defining-custom-properties).

The following is an example filter defining a simple property specification:

```cpp
CustomFilterInstancer::CustomFilterInstancer() : Rml::FilterInstancer()
{
	property_id1 = RegisterProperty("custom-property-1", "1").AddParser("number").GetId();
	property_id2 = RegisterProperty("custom-property-2", "normal").AddParser("keyword", "normal, colorful")
	                                                              .GetId();
	RegisterShorthand("filter", "custom-property-1, custom-property-2", Rml::ShorthandType::FallThrough);
}
```

The custom filter now has two properties. The property dictionary passed into the instancer's `InstanceFilter()` function will contain values for the two properties, defaulting to their specified default values if they weren't set in the RCSS.

Note that the shorthand `filter` is special. This shorthand will be used to parse the text inside the parenthesis of the property value. This allows specifying the filter with inline properties as in the following example.

```css
filter: custom-filter( 15 colorful );
```

Now this will be parsed by the above rules such that 'custom-property-1' contains 15, and 'custom-property-2' contains the keyword 'colorful'.

The property IDs are stored on the instancer object, so they can easily retrieve the parsed value during the call to `InstanceFilter()`,

```cpp
int value1 = properties.GetProperty(property_id1)->Get<int>();
```

The `value1` variable will now contain the value specified in the style sheet, e.g. '15' in the above example.

#### Registering an instancer

To register a custom filter instancer with RmlUi, call the `RegisterFilterInstancer()` function on the RmlUi factory (`Rml::Factory`) after RmlUi has been initialized.

```cpp
// Registers a non-owning pointer to an instancer that will be used to instance filters.
// @param[in] name The name of the filter the instancer will be called for.
// @param[in] instancer The instancer to call when the filter name is encountered.
// @lifetime The instancer must be kept alive until after the call to Rml::Shutdown.
// @return The added instancer if the registration was successful, nullptr otherwise.
static Rml::FilterInstancer* RegisterFilterInstancer(const Rml::String& name,
                                                     Rml::FilterInstancer* instancer);
```

For example:

```cpp
// Keep instancer alive until after the call to Rml::Shutdown().
auto instancer = std::make_unique<CustomFilterInstancer>();
Rml::Factory::RegisterFilterInstancer("custom-filter", instancer.get());
```

This will allow you to use the custom filter in RML as follows:

```html
<rml>
<head>
	<style>
		div
		{
			filter: custom-filter( 1.5 colorful );
		}
	</style>
</head>
<body>
...
```

Like for other instancers, it is the user's responsibility to manage the lifetime of the instancer. Thus, it must be kept alive until after the call to `Rml::Shutdown()`, and then cleaned up by the user.

### Updating filters

After being instanced, filters are not updated from inside the library. Instead, animation of filters in RmlUi involves destroying an existing filter and instancing a new one each time a parameter needs to be updated. Normally, a compiled filter is considered a light-weight construction.

If you have a filter that requires updating independently of the library's animation feature, you would need to implement your own update mechanism. This could involve separately maintaining values through an index or pointer passed through the compiled filter dictionary, and updating these values during your application's update loop.
