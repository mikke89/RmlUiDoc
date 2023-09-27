---
layout: page
title: Animations, transitions, and transforms
parent: rcss
next: media_queries
---

RmlUi provides comprehensive support for animations, transitions, and transforms. Together, they can be used to build very rich user experiences. These features are generally modeled after the CSS3 specifications, with some differences.

See also the [C++ documentation](../cpp_manual/animations_transforms.html) on animations and transforms.

### Animations
{:#animation}

Most RCSS properties can be animated, this includes properties representing numbers, lengths, percentages, angles, colors, transforms, and keywords. Animations can be specified entirely in RCSS, with keyframes.

`animation`{:.prop}

Value: | none \| \[\<duration\> \<delay\>? \<tweening-function\>? \[\<num-iterations\>\|infinite\]? alternate? paused? \<keyframes-name\>\]<span class="prop-def-symbol" title="one or more comma-separated occurrences">#</span>
Initial: | none
Applies to: | all elements
Inherited: | no
Percentages: | N/A

`none`{:.value}
: No animations specified.

`<duration>`{:.value}
: Duration of the animation, specified in seconds (`s`{:.value} unit). Required value.

`<delay>`{:.value}
: Time delay before starting the animation, specified in seconds. Default: `0s`{:.value}.

`<tweening-function>`{:.value}
:  Tweening functions specify how the animated value progresses during the animation cycle. See [tweening functions](#tweening-functions) below for details and possible values. Default: `linear-in-out`{:.value}.

`<num-iterations> | infinite`{:.value}
: Number of iterations to play the animation before pausing. Specify as an integer or the keyword `infinite`{:.value}. Default: 1.

`alternate`{:.value}
: If present, alternate the direction of the animation every other cycle.

`paused`{:.value}
: If present, the animation does not start on load.

`<keyframes-name>`{:.value}
: A string specifying the name of the keyframes. Keyframes are specified [as in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes), see examples below. Required value.

Values can be given in any order, with the exception that `duration`{:.value} must come before `delay`{:.value}.

Example usage:

```css
@keyframes my-progress-bar {
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
#my_element {
	width: 25px;
	animation: 2s cubic-in-out infinite alternate my-progress-bar;
}
```

Multiple animations can be specified on the same element by using a comma-separated list. 

```css
@keyframes my-progress-bar { ... }
@keyframes make-red {
	from { color: #333; }
	to   { color: #f33; }
}
#multi-animation { animation: 1s elastic-out my-progress-bar, 2s make-red; }
```

Internally, animations apply their properties on the local style of the element. Thus, mixing RML style attributes and animations should be avoided on the same element.

See the `animation` sample for more examples and details.


### Transitions
{:#transition}

Transitions apply an animation between two property values on an element when its property changes. Transitions are implemented in RCSS similar to how they operate in CSS. However, in RCSS, they only apply when a class or pseudo-class is added to or removed from an element.

`transition`{:.prop}

Value: | none \| \[ \[\<property-name\><span class="prop-def-symbol" title="one or more space-separated occurrences">+</span> \| all \| none\] \<duration\> \<delay\>? \<tweening-function\>?\]<span class="prop-def-symbol" title="one or more comma-separated occurrences">#</span>
Initial: | none
Applies to: | all elements
Inherited: | no
Percentages: | N/A

`none`{:.value}
: No transitions specified.

`<property-name>+ | all | none`{:.value}
: Specifies the list of properties to be animated when they are changed, as a space-separated list of names. Alternatively, the `all`{:.value} keyword animates all properties, while `none`{:.value} will not animate any properties.

`<duration>`{:.value}
: Duration of the animation, specified in seconds (`s`{:.value} unit). Required value.

`<delay>`{:.value}
: Time delay before starting the animation, specified in seconds. Default: `0s`{:.value}.

`<tweening-function>`{:.value}
:  Tweening functions specify how the animated value progresses during the animation cycle. See [tweening functions](#tweening-functions) below for details and possible values. Default: `linear-in-out`{:.value}.

Values can be given in any order, with the exception that `duration`{:.value} must come before `delay`{:.value}. Multiple transitions can be specified on the same element by using a comma-separated list.

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

See the `animation` sample for more examples and details. 


### Tweening functions
{:#tweening-functions}

Animations and transitions can optionally take a *tweening* function, which specifies how the animated value progresses during the animation cycle. Here, we deviate from the CSS specs where they are instead called `animation-timing-function`{:.value}s.

A tweening function in RCSS is specified as `<name>-in`{:.value}, `<name>-out`{:.value}, or `<name>-in-out`{:.value}, with one of the following names,

- `back`{:.value}
- `bounce`{:.value}
- `circular`{:.value}
- `cubic`{:.value}
- `elastic`{:.value}
- `exponential`{:.value}
- `linear`{:.value}
- `quadratic`{:.value}
- `quartic`{:.value}
- `quintic`{:.value}
- `sine`{:.value}

See the animation and transition documentation above for usage examples there. Each tweening function provides a specific mapping between normalized time *t* and used interpolation value *y*, as seen in the following plot.

<div style="text-align: center">
	<img alt="Tweening functions" src="../../assets/images/tweening_functions.svg" style="width: 100%; max-width: 700px">
</div> 

See also the `demo` sample, where users can play with different tweening functions and durations, and see the resulting animation. It is also possible to provide a custom tweening function in the [C++ animation API](../cpp_manual/animations_transforms.html).


### Transforms
{:#transform}

Transforms can be applied to elements using the `transform`{:.prop} property. The related properties `transform-origin`{:.prop}, `perspective`{:.prop}, and `perspective-origin`{:.prop} are also supported in RCSS, which controls aspects of how the transform will be applied and rendered. These are roughly equivalent to their respective [CSS properties](https://developer.mozilla.org/en-US/docs/Web/CSS/transform).

```css
transform: rotateX(10deg) skew(-10deg, 15deg) translateZ(100px);
transform-origin: left top 0;
perspective: 1000px;
perspective-origin: 20px 50%;
```

`transform`{:.prop}

Value: | none \| \<transform-function\><span class="prop-def-symbol" title="one or more space-separated occurrences">+</span>
Initial: | none
Applies to: | all elements
Inherited: | no
Percentages: | See individual transform functions

`none`{:.value}
: No transform applied.

`<transform-function>+`{:.value}
: Specifies a list of transform functions to be applied to the element, see [all available values](#transform-functions) below.


`transform-origin`{:.prop}
{:#transform-origin}

Value: | \[\<transform-origin-x\> <span class="prop-def-symbol" title="one or both must be specified">\|\|</span> \<transform-origin-y\>\] \<transform-origin-z\>?
Initial: | 50% 50% 0px
Applies to: | all elements
Inherited: | no
Percentages: | Relative to the size of the element's border-box.

Describes the origin point around which the transformation occurs, given as the distance from the top-left corner of the element's border-box. This is a shorthand property, the underlying properties are specified along each dimension as follows.

`transform-origin-x`{:.prop}: \[left \| center \| right \| \<length-percentage\>\]

`transform-origin-y`{:.prop}: \[top \| center \| right \| \<length-percentage\>\]

`transform-origin-z`{:.prop}: \<length\>


#### Transform functions
{:#transform-functions}

All transform functions and their argument types are listed in the following. 

**`<transform-function>`{:.value}**

`matrix`{:.value}( `<number>#{6}`{:.value} )            |  `rotateZ`{:.value}( `<angle>`{:.value} )       |  `skewX`{:.value}( `<angle>`{:.value} )
`matrix3d`{:.value}( `<number>#{16}`{:.value} )         |  `scale`{:.value}( `<number>#{1,2}`{:.value} )  |  `skewY`{:.value}( `<angle>`{:.value} )
`perspective`{:.value}( `<length>`{:.value} )           |  `scale3d`{:.value}( `<number>#{3}`{:.value} )  |  `translate`{:.value}( `<length-percentage>#{2}`{:.value} )
`rotate`{:.value}( `<angle>`{:.value} )                 |  `scaleX`{:.value}( `<number>`{:.value} )       |  `translate3d`{:.value}( `<length-percentage>#{2}, <length>`{:.value} )
`rotate3d`{:.value}( `<number>#{3}, <angle>`{:.value})  |  `scaleY`{:.value}( `<number>`{:.value} )       |  `translateX`{:.value}( `<length-percentage>`{:.value} )
`rotateX`{:.value}( `<angle>`{:.value} )                |  `scaleZ`{:.value}( `<number>`{:.value} )       |  `translateY`{:.value}( `<length-percentage>`{:.value} )
`rotateY`{:.value}( `<angle>`{:.value} )                |  `skew`{:.value}( `<angle>#{2}`{:.value} )      |  `translateZ`{:.value}( `<length>`{:.value} )

See a detailed description for each function in the [CSS Transforms specification](https://drafts.csswg.org/css-transforms-2/#transform-functions). Angles take units of 'deg' or 'rad'. See also the `transform` and `animation` samples for more examples.


#### Perspective
{:#perspective}

`perspective`{:.prop}

Value: | none \| \<length ≥ 0px\>
Initial: | none
Applies to: | all elements
Inherited: | no
Percentages: | N/A

Perspective can make objects that are farther away appear smaller, when combined with 3d transformations.

`none`{:.value}
: No perspective applied, equivalent to an infinite distance.

`<length ≥ 0px>`{:.value}
: Distance to the center of projection.


`perspective-origin`{:.prop}
{:#perspective-origin}

Value: | \<perspective-origin-x\> <span class="prop-def-symbol" title="one or both must be specified">\|\|</span> \<perspective-origin-y\>
Initial: | 50% 50%
Applies to: | all elements
Inherited: | no
Percentages: | Relative to the size of the element's border-box.

Describes the origin point for the `perspective`{:.prop} property. This is a shorthand property, the underlying properties are specified along each dimension as follows.

`perspective-origin-x`{:.prop}: \[left \| center \| right \| \<length-percentage\>\]

`perspective-origin-y`{:.prop}: \[top \| center \| right \| \<length-percentage\>\]


#### Interpolation

RmlUi has full interpolation support for transforms, making them very attractive to use in combination with animations and transitions.

<video src="../animations/animation_sample.webm" width="640" height="360" poster="../animations/animation_sample_poster.png" preload="metadata" controls></video>

The following video demonstrates transitions with transforms on a main menu.

<video src="../animations/game_main_menu.webm" width="640" height="360" poster="../animations/game_main_menu_poster.png" preload="metadata" controls></video>

With transforms applied to the elements, we can essentially move the camera as if in three-dimensional space by changing the perspective and origin, as shown in the following.

<video src="../animations/game_menu_transform.webm" width="640" height="360" poster="../animations/game_menu_transform_poster.png" preload="metadata" controls></video>
