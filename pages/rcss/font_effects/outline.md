---
layout: page
title: Outline Effect
parent: rcss/font_effects
grandparent: rcss
---

The outline font effect renders a coloured outline around text.

![outline_1.jpg](outline_1.jpg)

The effect has the following properties:

`<name>-width`{:.prop}

Value: | \<number\>
Initial: | 0
Percentages: | N/A

The width defines the maximum pixel width of the font's outline.

```css
/* Declares a font effect outline. */
h1
{
	header-font-effect: outline;
	header-width: 2px;
	header-colour: black;
}
```
