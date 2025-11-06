---
layout: page
title: Syntax
parent: rcss
next: selectors
---

A style sheet is made up of a number of rules. Each rule has a number of selectors, which define which elements the rule applies to, and properties, which are applied to those elements.

The basic syntax of a rule is as follows:

```css
selector1,
selector2,
selector3
{
	property1: value1;
	property2: value2;
	property3: value3;
}
```

Selectors are comma-separated, followed by the rule block which is defined by curly braces. Inside the rule block is a list of semi-colon separated property declarations; each property declaration is made up of the property to set, a colon, and a space-separated list of the values to assign to that property. The values accepted by each value, and how many they require, is specific to each value.

### Comments

Comments can be included in a style sheet using the C-style /* and */ characters.

### Values

Which values each property accepts is given in their definition. Values may be keywords, which are set as specific strings such as auto, left, etc, or generic strings (such as font names or file paths), or one of the types described below.

#### Numbers

Specified as <number> in a property's Values list. A number can be an integer or real number.

```css
z-index: 16;
```

#### Lengths

Specified as <length> in a property's Values list. A length is a horizontal or vertical measurement consisting of a number and a unit. RCSS recognises the following units:

- `px`{:.value}: One px is equivalent to one pixel on the output medium.
- `em`{:.value}: When specified in the `font-size`{:.prop} property, one em is equivalent to the font size of the parent element. For other properties, it is the font size of the element itself.
- `rem`{:.value}: One rem is equivalent to the font size of the root (body) element.
- `ex`{:.value}: One ex is equivalent to the height of the current font's lower-case x.
- `dp`{:.value}: One dp is equivalent to one pixel scaled by a globally defined ratio, [see below](#dp-unit).
- `vw`{:.value}: One vw is equivalent to 1% of the width of the context.
- `vh`{:.value}: One vh is equivalent to 1% of the height of the context.

In addition, units based on pixels-per-inch (PPI) are supported. The PPI units are defined as follows:

- `in`{:.value}: One inch is `96px`{:.value}.
- `cm`{:.value}: One centimeter is `1/2.54 inch`{:.value}.
- `mm`{:.value}: One millimeter is `1/25.4 inch`{:.value}.
- `pt`{:.value}: One point is `1/72 inch`{:.value}.
- `pc`{:.value}: One pica is `1/6 inch`{:.value}.

```css
width: 125px;
```

##### Density-independent pixel (dp)
{:#dp-unit}

The `dp`{:.value} unit behaves like `px`{:.value} except that its size can be set globally to scale relative to pixels. This makes it easy to achieve a scalable user interface. Set the ratio globally on the context by calling:

```c++
float dp_ratio = 1.5f;
context->SetDensityIndependentPixelRatio(dp_ratio);
```

Usage example in RCSS:
```css
div#header
{
	width: 800dp;
	height: 50dp;
	font-size: 20dp;
}
```

#### Percentages

Specified as `<percentage>`{:.value} in the property's Values list. A percentage value is evaluated relative to some other value, which is specified in each property that supports a percentage. For example, width can be expressed as a percentage, which is evaluated against the width of the element's containing block.

```css
min-height: 50%;
```

#### Colours

Specified as `<colour>`{:.value} in the property's Values list. Colours can be declared in numerous ways, as follows.

\<colour name\> --- Named colours
: One of the 16 colours defined in the HTML 4.0 specification: aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, purple, red, silver, teal, white, and yellow. Plus grey (alias for gray), orange, and transparent.

`#RGB`{:.value}, `#RGBA`{:.value}, `#RRGGBB`{:.value}, `#RRGGBBAA`{:.value} --- Hexadecimal
: Prefixed with `#` followed by 3, 4, 6, or 8 hexadecimal digits. 3- and 6-digit forms are RGB and opaque. 4- and 8-digit forms include an alpha channel for translucency. The 3- and 4- digit forms expand each component, e.g. `#FE0` → `#FFEE00`.

`rgb(r, g, b)`{:.value}, `rgba(r, g, b, a)`{:.value} --- [sRGB](https://en.wikipedia.org/wiki/SRGB)
: - `r`, `g`, `b`: Red, green, and blue channel respectively. 0 to 255 (0% to 100%).
  - `a`: Alpha channel. 0 to 255 (0% to 100%).\
  **Important**: Note that the declaration of the alpha channel when using the `rgba` keyword differs from the HTML5 specification.

`hsl(h, s, l)`{:.value}, `hsla(h, s, l, a)`{:.value} --- Cylindrical [sRGB](https://en.wikipedia.org/wiki/SRGB)
: - `h`: Hue in degrees (typed without units).
  - `s`: Saturation. Percentage value from 0% to 100%.
  - `l`: Lightness. Percentage value from 0% to 100%.
  - `a`: Alpha value. 0 to 1.

`lab(L a b)`{:.value}, `lab(L a b / A)`{:.value} --- [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)
: - `L`: Overall lightness. 0 to 100 (0% to 100%).
  - `a`: Distance along green-to-red axis. Typically -125 to +125 (-100% to +100%), but can be exceeded.
  - `b`: Distance along blue-to-yellow axis. Typically -125 to +125 (-100% to +100%), but can be exceeded.
  - `A`: Optional alpha value. 0 to 1 (0% to 100%).

  All parameters can take the value `none`, which is equivalent to 0.

`lch(L C H)`{:.value}, `lch(L C H / A)`{:.value} --- Cylindrical [CIELAB](https://en.wikipedia.org/wiki/CIELAB_color_space)
: - `L`: Overall lightness. 0 to 100 (0% to 100%).
  - `C`: Chroma (amount of colour). Typically 0 to 150 (0% to 100%), but can be exceeded.
  - `H`: Hue angle in degrees (typed without units).
  - `A`: Optional alpha value. 0 to 1 (0% to 100%).

  All parameters can take the value `none`, which is equivalent to 0.

`oklab(L a b)`{:.value}, `oklab(L a b / A)`{:.value} --- [Oklab](https://en.wikipedia.org/wiki/Oklab_color_space)
: - `L`: Overall lightness. 0 to 1 (0% to 100%).
  - `a`: Distance along green-to-red axis. Typically -0.4 to +0.4 (-100% to +100%), but can be exceeded.
  - `b`: Distance along blue-to-yellow axis. Typically -0.4 to +0.4 (-100% to +100%), but can be exceeded.
  - `A`: Optional alpha value. 0 to 1 (0% to 100%).

  All parameters can take the value `none`, which is equivalent to 0.

`oklch(L C H)`{:.value}, `oklch(L C H / A)`{:.value} --- Cylindrical [Oklab](https://en.wikipedia.org/wiki/Oklab_color_space)
: - `L`: Overall lightness. 0 to 1 (0% to 100%).
  - `C`: Chroma (amount of colour). Typically 0 to 0.4 (0% to 100%), but can be exceeded.
  - `H`: Hue angle in degrees (typed without units).
  - `A`: Optional alpha value. 0 to 1 (0% to 100%).

  All parameters can take the value `none`, which is equivalent to 0.

So, for example, the following colour declarations are identical:

```css
color: red;

color: #F00;
color: #FF0000FF;

color: rgb(100%, 0%, 0%);
color: rgba(100%, 0%, 0%, 100%);
color: rgba(255, 0, 0, 255);

color: hsl(0, 100%, 50%);
color: hsla(0, 100%, 50%, 1.0);

color: lab(53% 80 67);
color: lab(53% 80 67 / 1.0);
color: lch(53% 105 40);
color: lch(53% 105 40 / 1.0);

color: oklab(63% 0.25 0.125);
color: oklab(63% 0.25 0.125 / 1.0);
color: oklch(63% 0.25 30);
color: oklch(63% 0.25 30 / 1.0);
```

#### Resolution

Specified as `<resolution>`{:.value} in the property's Values list. Resolution describes the scaling for high DPI displays, and can be used in media queries and sprite sheets.

In RCSS, resolution is always specificied using a number (the scaling factor) followed by the `x`{:.value} unit.

```css
@media (min-resolution: 1.2x) { /* ... */ }
```

In this case, the specified number will be compared against the context's [dp-ratio](#dp-unit).

#### Ratio

Specified as `<ratio>`{:.value} in the property's Values list. A ratio is specified using the syntax `<integer> / <integer>`{:.value}.

```css
@media (min-aspect-ratio: 16 / 9) { /* ... */ }
```

### Referencing RCSS from RML

A style sheet can be either stored in an external file (usually with the extension .rcss) and referenced from an RML file, or declared inline inside an RML file. Referencing an external RCSS file is done using the `<link>`{:.tag} tag in the following manner:

```html
<rml>
	<head>
		<link type="text/css" href="sample.rcss" />

	...
```

File paths are relative to the referencing document.

Declaring an inline style sheet is done using the `<style>`{:.tag} tag, also within the <head> tag:

```html
<rml>
	<head>
		<style>
			body
			{
				margin: 0px;
			}
		</style>

	...
```

Multiple style sheets can be included in a single document and combined with inline style declarations. The ordering of style declarations is important, as they may be used to resolve the precedence conflicting style sheet rules.

Also, style sheet properties can be declared directly on an element. This is done by inserting semi-colon separated style sheet property declarations into the `style`{:.attr} attribute of an element. For example, the following RML fragment:

```html
<div style="width: 25%; min-width: 55px;">
</div>
```

sets the `width`{:.prop} property to '25%' and the `min-width`{:.prop} property to '55px' on the `div`{:.tag} element.
