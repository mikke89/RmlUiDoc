---
layout: page
title: Outline Effect
parent: rcss/font_effects
grandparent: rcss
next: shadow
---

The outline font effect renders a coloured outline around text.

![outline_1.jpg](outline_1.jpg)

The effect is declared as:

```css
font-effect: outline( <width> <color> );
```

Its properties are specified by the following.

`width`{:.prop}

Value: | \<length\>
Initial: | 0px
Percentages: | N/A

The width defines the maximum pixel width of the font's outline.

`color`{:.prop}

Value: | \<color\>
Initial: | white
Percentages: | N/A

The color is applied multiplicatively over the entire effect.

#### Example

```css
/* Declares an outline font effect. */
h1
{
	font-effect: outline(2px black);
}
```
