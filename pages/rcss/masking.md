---
layout: page
title: Masking
parent: rcss
next: filters
---

Masking is a way to hide parts of an element by using another graphical object to define which parts to occlude. In RmlUi, mask images can be generated using decorators, and the alpha channel of the resulting mask image will be used to fully or partially occlude the element, including its children.

To use masking, the backend renderer must support advanced rendering features, see the [render interface feature table](../cpp_manual/interfaces/render.html#feature-table) for details.

![Filters from the `effects` sample](../../assets/images/mask-image.png)

### Mask image
{:#mask-image}

The mask image provides a way to define a mask using decorators, including images and gradients. It is specified just like the [`decorator`{:.prop} property](decorators.html#decorator), and can be used with the same decorators. The alpha channel of the resulting mask image defines the mask, and will be used to determine the occlusion across the element.

`mask-image`{:.prop}

Value: | none \| \[ \<type\>( \<properties\> ) \<paint-area\>? \| \<name\> \<paint-area\>? \]<span class="prop-def-symbol" title="One or more comma-separated occurrences">#+</span>
Initial: | none
Inherited: | no
Percentages: | N/A

\<type\>
: Declares the decorator type, see the list of [built-in decorators](decorators.html#decorators).

\<properties\>
: Declares the properties specific to the given decorator type.

\<name\>
: Declares a decorator name defined by an [@decorator rule](decorators.html#decorator-at-rule).

\<paint-area\>
: Optionally, specifies the area of the element the decorator should be applied to, i.e. one of `border-box`{:.value}, `padding-box`{:.value}, or `content-box`{:.value}. For mask images, this value defaults to `border-box`{:.value}, as opposed to `padding-box`{:.value} for the `decorator`{:.prop} property.

For illustration, a single decorator can be used as in the following.

```css
mask-image: <type>( <properties> );
```

While multiple decorators can be used as follows. They will be rendered in the declared order from top to bottom.

```css
mask-image: <type>( <properties> ), <type>( <properties> ), ... ;
```

#### Examples

```css
/* declares a mask with an image repeating across the element */
mask-image: image("star.png" repeat);

/* declares a mask with a linear gradient, fading in towards the right */
mask-image: horizontal-gradient(transparent black);

/* declares a mask with a conic gradient rendered on top of an image */
mask-image: conic-gradient(from 45deg, black, transparent, black), image("star.png" cover);
```
