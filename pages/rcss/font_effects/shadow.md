---
layout: page
title: Shadow Effect
parent: rcss/font_effects
---

The shadow font effect renders a coloured copy of text with an offset, giving the effect of a shadow.

![shadow_1.jpg](shadow_1.jpg)

The effect has the following properties:

`<name>-offset-x`{:.prop}

Value: | \<number\>
Initial: | 0
Percentages: | N/A

`<name>-offset-y`{:.prop}

Value: | \<number\>
Initial: | 0
Percentages: | N/A

These properties define the offset, in pixels, between the source text and the shadow.

`<name>-offset`{:.prop}

A shorthand property for setting offset-x and offset-y.

```css
/* Declares a font effect shadow. */
h1
{
	header-font-effect: shadow;
	header-offset: 2px 2px;
	header-colour: black;
}
```
