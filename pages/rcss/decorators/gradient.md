---
layout: page
title: Gradient decorator
grandparent: rcss
parent: rcss/decorators
---

The `gradient`{:.prop} decorator renders a linear color gradient across the padded area of its element, in a horizontal or vertical direction.

```css
decorator: gradient( <direction> <start-color> <stop-color> );
```

### Properties


`direction`{:.prop}

Value: | horizontal \| vertical
Initial: | horizontal
Percentages: | N/A

Declares the direction of the color gradient.

`start-color`{:.prop}

Value: | \<color\>
Initial: | white
Percentages: | N/A

Declares the start color, either at the left edge or top edge.

`stop-color`{:.prop}

Value: | \<color\>
Initial: | white
Percentages: | N/A

Declares the stop color, either at the right edge or bottom edge.

### Example

The following declares a button with a horizontal color gradient from a red-like color to a yellow-like color, and adds a border.

```css
button
{
	decorator: gradient( horizontal #DB6565 #F1B58A );
	border: 2px #DB6565;
}
```
