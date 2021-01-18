---
layout: page
title: Animations and Transforms
parent: cpp_manual
next: decorators
---

RmlUi has rich support for transforms and animations. This guide describes how to control these features from C++ side.

See also the [RCSS documentation](../rcss/animations_transitions_transforms.html) on animations, transitions and transforms for more details and usage of these features from RCSS.


### Transforms
{:#transform}

Transforms are set on elements using the `transform`{:.prop} property.

```cpp
element->SetProperty("transform", "rotate(30deg)");
```

This will parse the provided string, and activate the provided transform(s) on the element. See also the related properties `perspective`{:.prop}, `perspective-origin`{:.prop}, and `transform-origin`{:.prop}, which controls aspects of how the transform will be applied and rendered.

Transforms can also be provided directly without the parsing step. This increases performance, and can be easier if transform values are provided programmatically. Using the helper function `Transform::MakeProperty`, we can set transforms like this:

```cpp
auto p = Transform::MakeProperty({ Transforms::Rotate2D{10.f}, Transforms::TranslateX{100.f} });
element->SetProperty(PropertyId::Transform, p);
```

A custom transformation matrix can be provided using the `Transforms::Matrix3D` transform primitive. See all transform primitives that can be applied in the `TransformPrimitive.h`{:.path} header. You can also have a look at the included `transform` sample and the `animation` sample for more examples.


### Animations
{:#animation}

Support for animations are mainly described in the [RCSS documentation](../rcss/animations_transitions_transforms.html). From C++, an animation can be started on an element by calling the following function.

```c++
// Start an animation of the given property on this element.
// @return True if a new animation was added.
bool Element::Animate(
	const String& property_name,
	const Property& target_value,
	float duration,
	Tween tween = Tween{},
	int num_iterations = 1,
	bool alternate_direction = true,
	float delay = 0.0f,
	const Property* start_value = nullptr
);
```

This will start an animation of the property specified by `property_name`. The animation will start by using the current value of the given property on the element, or from `start_value` if provided. And then it will smoothly interpolate towards the `target_value`. The `duration` is given in seconds. A tweening function `tween` can be provided to control the interpolation time progression, see the RCSS documentation for details. The animation will repeat for `num_iterations` times, or infinite time when specified as -1. The `delay` argument, given in seconds, sets a delay before the property starts to animate.

The value of an animated property is updated during `Context::Update`.

Additional animation keys can be added, extending the duration of the animation, by calling

```c++
// Add a key to an animation, extending its duration.
// @return True if a new animation key was added.
bool Element::AddAnimationKey(
	const String& property_name,
	const Property& target_value,
	float duration,
	Tween tween = Tween{}
);
```

The animation key will be added to an existing animation on the same property. The arguments correspond to those in `Element::Animate`.

Example usage:

```c++
auto p1 = Transform::MakeProperty({ Transforms::Rotate2D{10.f}, Transforms::TranslateX{100.f} });
auto p2 = Transform::MakeProperty({ Transforms::Scale2D{3.f} });
el->Animate("transform", p1, 1.8f, Tween( Tween::Elastic, Tween::InOut ), -1, true);
el->AddAnimationKey("transform", p2, 1.3f, Tween( Tween::Elastic, Tween::InOut ));
```

Instead of using any of the built-in tweening functions, a custom tweening function can be provided by constructing it as follows:

```c++
Tween tween(
	[](float t) { return t * t; },
	Tween::Out
);
```
The function should provide a mapping from normalized time `float t` in the range [0, 1] to an interpolation factor `float` output. It is a light-weight function pointer, and thus cannot take any lambda bindings.

See the `animation` sample for more examples and details.
