---
layout: page
title: Shadow Effect
parent: rcss/font_effects
grandparent: rcss
next: blur
---

The shadow font effect renders a coloured copy of text with an offset, giving the effect of a shadow.

![shadow_1.jpg](shadow_1.jpg)

The effect is declared as:

```css
font-effect: shadow( <offset-x> <offset-y> <color> );
```

Its properties are specified by the following.

`offset-x`{:.prop}

Value: | \<length\>
Initial: | 0px
Percentages: | N/A

`offset-y`{:.prop}

Value: | \<length\>
Initial: | 0px
Percentages: | N/A

These properties define the offset, in pixels, between the source text and the shadow.


`color`{:.prop}

Value: | \<color\>
Initial: | white
Percentages: | N/A

The color is applied multiplicatively over the entire effect.


```css
/* Declares a shadow font effect. */
h1
{
	font-effect: shadow( 2px 2px black );
}
```
