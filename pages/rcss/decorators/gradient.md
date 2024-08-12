---
layout: page
title: Straight gradient decorator
grandparent: rcss
parent: rcss/decorators
next: linear_gradient
---

Straight gradients are supported with the `horizontal-gradient`{:.prop} and `vertical-gradient`{:.prop} decorators. They render a linear color gradient across the area of the element they are being applied to, in either a horizontal or a vertical direction.

```css
decorator: horizontal-gradient( <start-color> <stop-color> ) <paint-area>?;
decorator: vertical-gradient( <start-color> <stop-color> ) <paint-area>?;
```

Straight gradients can be described as a subset of [linear gradients](linear_gradient.html). The main motivation for straight gradients is that they can be rendered even without shader support from the renderer. Straight gradients only use vertex colors, which makes them simpler and lighter to render. For this reason, they should be preferred when possible.

### Properties

`start-color`{:.prop}

Value: | \<color\>
Initial: | white
Percentages: | N/A

Declares the start color, that is, at the left or top edge.

`stop-color`{:.prop}

Value: | \<color\>
Initial: | white
Percentages: | N/A

Declares the stop color, that is, at the right or bottom edge.

`paint-area`{:.prop}

Value: | border-box \| padding-box \| content-box
Initial: | padding-box
Percentages: | N/A

Declares the box area to render the decorator onto.

### Examples

The following RCSS declares two buttons, one with a vertical gradient and another with a horizontal gradient.

```css
button.vertical {
	decorator: vertical-gradient( #415857 #5990a3 );
	border: 3px #415857;
	border-radius: 8px;
}

button.horizontal {
	decorator: horizontal-gradient( #db6565 #f1b58a );
	border: 3px #db6565;
	border-radius: 8px;
}
```

The rendered result:

![Vertical and horizontal gradients](../../../assets/images/decorators/vertical-horizontal-gradient.png)
