---
layout: page
title: Animations, Transitions, and Transforms
parent: rcss
next: visual_effects
---

### Transform property

Use `perspective`{:.prop}, `perspective-origin`{:.prop}, `transform`{:.prop} and `transform-origin`{:.prop} in RCSS, roughly equivalent to their respective CSS properties.

```css
perspective: 1000px;
perspective-origin: 20px 50%;
transform: rotateX(10deg) skew(-10, 15) translateZ(100px);
transform-origin: left top 0;
```

All transform properties and their argument types are as follows:
```
perspective,  length1
matrix,       abs_numbers6
matrix3d,     abs_numbers16
translateX,   length1
translateY,   length1
translateZ,   length1
translate,    length2
translate3d,  length3
scaleX,       number1
scaleY,       number1
scaleZ,       number1
scale,        number2
scale,        number1
scale3d,      number3
rotateX,      angle1
rotateY,      angle1
rotateZ,      angle1
rotate,       angle1
rotate3d,     length3angle1
skewX,        angle1
skewY,        angle1
skew,         angle2
```

Angles are in degrees by default.


### Animations


Most RCSS properties can be animated, this includes properties representing lengths, colors, or transforms. From C++, an animation can be started on an Element by calling

```c++
bool Element::Animate(const String& property_name, const Property& target_value, float duration, Tween tween = Tween{}, int num_iterations = 1, bool alternate_direction = true, float delay = 0.0f, const Property* start_value = nullptr);
```

Additional animation keys can be added, extending the duration of the animation, by calling

```c++
bool Element::AddAnimationKey(const String& property_name, const Property& target_value, float duration, Tween tween = Tween{});
```

C++ example usage:

```c++
auto p1 = Transform::MakeProperty({ Transforms::Rotate2D{10.f}, Transforms::TranslateX{100.f} });
auto p2 = Transform::MakeProperty({ Transforms::Scale2D{3.f} });
el->Animate("transform", p1, 1.8f, Tween{ Tween::Elastic, Tween::InOut }, -1, true);
el->AddAnimationKey("transform", p2, 1.3f, Tween{ Tween::Elastic, Tween::InOut });
```


Animations can also be specified entirely in RCSS, with keyframes.
```css
animation: <duration> <delay> <tweening-function> <num_iterations|infinite> <alternate> <paused> <keyframes-name>;
```
All values, except `<duration>`{:.value} and `<keyframes-name>`{:.value}, are optional. `delay`{:.value} must be specified after `<duration>`{:.value}, otherwise values can be given in any order. Keyframes are specified as in CSS, see example below. Multiple animations can be specified on the same element by using a comma-separated list.

Tweening functions (or in CSS lingo, `animation-timing-function`{:.prop}s) specify how the animated value progresses during the animation cycle. A tweening function in RCSS is specified as `<name>-in`{:.prop}, `<name>-out`{:.prop}, or `<name>-in-out`{:.prop}, with one of the following names,

* `back`{:.value}
* `bounce`{:.value}
* `circular`{:.value}
* `cubic`{:.value}
* `elastic`{:.value}
* `exponential`{:.value}
* `linear`{:.value}
* `quadratic`{:.value}
* `quartic`{:.value}
* `quintic`{:.value}
* `sine`{:.value}


RCSS example usage:

```css
@keyframes my-progress-bar
{
	0%, 30% {
		background-color: #d99;
	}
	50% {
		background-color: #9d9;
	}
	to { 
		background-color: #f9f;
		width: 100%;
	}
}
#my_element
{
	width: 25px;
	animation: 2s cubic-in-out infinite alternate my-progress-bar;
}
```

Internally, animations apply their properties on the local style of the element. Thus, mixing RML style attributes and animations should be avoided on the same element.

Animations are very powerful coupled with transforms. See the animation sample project for more examples and details.

<video src="../animations/animation_sample.webm" width="640" height="360" poster="../animations/animation_sample_poster.png" preload="metadata" controls></video>


### Transitions

Transitions apply an animation between two property values on an element when its property changes. Transitions are implemented in RCSS similar to how they operate in CSS. However, in RCSS, they only apply when a class or pseudo-class is added to or removed from an element.

```css
transition: <space-separated-list-of-properties|all|none> <duration> <delay> <tweening-function>;
```
The property list specifies the properties to be animated. `delay`{:.value} and `tweening-function`{:.value} are optional. `delay`{:.value} must be specified after `duration`{:.value}, otherwise values can be given in any order. Multiple transitions can be specified on the same element by using a comma-separated list. The tweening function is specified as in the `animation`{:.prop} RCSS property.


Example usage:

```css
#transition_test {
	transition: padding-left background-color transform 1.6s elastic-out;
	transform: scale(1.0);
	background-color: #c66;
}
#transition_test:hover {
	padding-left: 60px;
	transform: scale(1.5);
	background-color: #ddb700;
} 
```

See the animation sample project for more examples and details. 

The following video demonstrates transitions with transforms on a main menu.

<video src="../animations/game_main_menu.webm" width="640" height="360" poster="../animations/game_main_menu_poster.png" preload="metadata" controls></video>

With transforms applied to the elements, we can essentially move the camera as if in three-dimensional space by changing the perspective and origin, as shown in the following.

<video src="../animations/game_menu_transform.webm" width="640" height="360" poster="../animations/game_menu_transform_poster.png" preload="metadata" controls></video>