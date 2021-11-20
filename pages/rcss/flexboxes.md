---
layout: page
title: Flexible boxes (preview)
parent: rcss
next: user_interface
---

Flexible box (flexbox) layout is made for laying out items along a single direction. It allows flexible sizing of items, both shrinking to avoid overflow as well as growing to fill the container. Both horizontal and vertical alignment can be controlled. Together, these properties make this layout scheme powerful for many types of user interfaces.

RmlUi generally follows the [CSS Flexible Box specification](https://drafts.csswg.org/css-flexbox/), although there are some smaller differences. There are many resources on how to write flexbox layout in CSS on the web, see eg. a [flexbox introduction at MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout) and an illustrated overview of the [flexbox properties at CSS-Tricks](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

Flexbox layout is initialized by setting an element's [`display`{:.prop} property](visual_formatting_model.html#display) to `display: flex`{:.value}. This generates a flex container for the element, and all its children are formatted as flex items within this container.

(Documentation is a work-in-progress).

### Basic example

```css
.flex {
	display: flex;
	background: #666;
	padding: 3px;
}
.flex > div {
	padding: 10px;
	margin: 3px;
	background-color: #edd3c0;
	flex: 1;
}
h2 {
	text-align: center;
	font-size: 1.3em;
}
```

```html
<div class="flex">
	<div>
		<h2>First column</h2>
		<p>Etiam libero lorem.</p>
	</div>
	<div>
		<h2>Second column</h2>
		<p>Ut volutpat, odio et facilisis molestie.</p>
	</div>
	<div>
		<h2>Third column</h2>
		<p>Lorem ipsum dolor sit amet.</p>
	</div>
</div>
```

### Differences from CSS

- Will not create anonymous flex items from text.
- No 'content' flex-basis property value.
- No 'order' property.
- No automatic minimum-sizing of flex items (or any elements for that matter).
- No aspect ratio.
- No visibility: collapse.
- Stretched items are not reformatted (§9.4.11).
- Baseline alignment is only approximate.
- 'gap' property not (yet) supported for flexbox.

### Performance

Avoid content based sizing to prevent formatting the same flex items multiple times:

- Use the `flex: <number ≥ 1> `{:.value} shorthand.
- Set a definite height (length or percentage) on the flex items – or width in column layout.
  
This is especially important when each flex items is complicated to format, such as when using flexbox for larger layout structures.

### Orientation


`flex-direction`{:.prop}
{:#flex-direction}

Value: | row \| row-reverse \| column \| column-reverse
Initial: | row
Applies to: | flex containers
Inherited: | no
Percentages: | N/A



`flex-wrap`{:.prop}
{:#flex-wrap}

Value: | nowrap \| wrap \| wrap-reverse
Initial: | nowrap
Applies to: | flex containers
Inherited: | no
Percentages: | N/A



`flex-flow`{:.prop}
{:#flex-flow}

A shorthand for setting the `flex-direction`{:.prop} and `flex-wrap`{:.prop} properties in that order.




### Flexibility


#### The 'flex' shorthand
{:#flex}

`flex`{:.prop}

Value: | auto \| none \| \<flex-grow\> \<flex-shrink\>? \<flex-basis\>? \| \<flex-basis\>
Initial: | 0 1 auto
Applies to: | flex items
Inherited: | no
Percentages: | N/A

A shorthand property for setting the flexible sizing behavior of flex items. Generally, the following short forms should cover most use cases:

`flex: *default*`{:.value}
: Equivalent to `flex: 0 1 auto`{:.value}. Items will be sized according to their content size, but allow shrinking proportionally if the container is too small in order to avoid overflow.

`flex: auto`{:.value}
: Equivalent to `flex: 1 1 auto`{:.value}. Items will initially be sized according to their content size and then proportionally shrink or grow to fill the container. 

`flex: none`{:.value}
: Equivalent to `flex: 0 0 auto`{:.value}. Items will be sized according to their content size, and neither shrink nor grow.

`flex: <number ≥ 1> `{:.value}
: Equivalent to `flex: <number> 1 0`{:.value}. Items will be sized proportionally to their given `<number>`{:.value}, and then proportionally shrink or grow to match the container size. This gives the best performance.

The flexbox sizing algorithm will also respect min- and max-sizing constraints given on the items.


#### Individual flexible properties

The flexible size properties can also be controlled individually.

`flex-grow`{:.prop}
{:#flex-grow}

Value: | \<number\>
Initial: | 0
Applies to: | flex items
Inherited: | no
Percentages: | N/A

`flex-shrink`{:.prop}
{:#flex-shrink}

Value: | \<number\>
Initial: | 1
Applies to: | flex items
Inherited: | no
Percentages: | N/A

`flex-basis`{:.prop}
{:#flex-basis}

Value: | \<length\> \| \<percentage\> \| auto
Initial: | auto
Applies to: | flex items
Inherited: | no
Percentages: | relative to the flex container’s inner main size

Units have the same meaning as for the [`width`{:.prop} property](visual_formatting_model_details.html#width).



### Alignment


#### Axis alignment

`justify-content`{:.prop}
{:#justify-content}

Value: | flex-start \| flex-end \| center \| space-between \| space-around
Initial: | flex-start
Applies to: | flex containers
Inherited: | no
Percentages: | N/A


#### Cross-axis alignment

`align-items`{:.prop}
{:#align-items}

Value: | flex-start \| flex-end \| center \| baseline \| space-around \| stretch
Initial: | stretch
Applies to: | flex containers
Inherited: | no
Percentages: | N/A

`align-self`{:.prop}
{:#align-self}

Value: | auto \| flex-start \| flex-end \| center \| baseline \| space-around \| stretch
Initial: | auto
Applies to: | flex items
Inherited: | no
Percentages: | N/A


#### Packing flex lines

`align-content`{:.prop}
{:#align-content}

Value: | flex-start \| flex-end \| center \| space-between \| space-around \| stretch
Initial: | stretch
Applies to: | multi-line flex containers
Inherited: | no
Percentages: | N/A

