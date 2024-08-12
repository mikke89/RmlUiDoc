---
layout: page
title: Decorators
parent: rcss
next: masking
---

Decorators are an extension to CSS for RCSS. A decorator can be declared in a style sheet and configured with decorator-specific properties. Custom decorator types can be developed to suit the needs of the user, and in this manner any kind of decoration can be applied to an element.

See also the [C++ documentation](../cpp_manual/decorators.html) on decorators for more details and how to define your own decorators.

### RmlUi decorators
{:#decorators}

RmlUi comes with several built-in decorators for displaying images and tiled images behind elements.

| Decorator                                            | Types                                                          | Description                              | Requires shader support |
|------------------------------------------------------|----------------------------------------------------------------|------------------------------------------|:-----------------------:|
| [Image](decorators/image.html)                       | `image`{:.prop}                                                | A single image.                          |                         |
| [Tiled horizontal](decorators/tiled_horizontal.html) | `tiled-horizontal`{:.prop}                                     | Tiled images horizontally.               |                         |
| [Tiled vertical](decorators/tiled_vertical.html)     | `tiled-vertical`{:.prop}                                       | Tiled images vertically.                 |                         |
| [Tiled box](decorators/tiled_box.html)               | `tiled-box`{:.prop}                                            | Tiled images across a box.               |                         |
| [Ninepatch](decorators/ninepatch.html)               | `ninepatch`{:.prop}                                            | Efficiently tiled images across a box.   |                         |
| [Straight gradients](decorators/gradient.html)       | `horizontal-gradient`{:.prop}, `vertical-gradient`{:.prop}     | Horizontal and vertical color gradients. |                         |
| [Linear gradients](decorators/linear_gradient.html)  | `linear-gradient`{:.prop}, `repeating-linear-gradient`{:.prop} | Linear color gradients.                  |           ✔️            |
| [Radial gradients](decorators/radial_gradient.html)  | `radial-gradient`{:.prop}, `repeating-radial-gradient`{:.prop} | Radial color gradients.                  |           ✔️            |
| [Conic gradients](decorators/conic_gradient.html)    | `conic-gradient`{:.prop}, `repeating-conic-gradient`{:.prop}   | Conic color gradients.                   |           ✔️            |
| [Shader](decorators/shader.html)                     | `shader`{:.prop}                                               | Custom shaders.                          |           ✔️            |

Some decorators require the backend renderer to support advanced rendering features, see the [render interface feature table](../cpp_manual/interfaces/render.html#feature-table) for details.

### Decoration: The 'decorator' property
{:#decorator}

The decorator property is specified as follows.

`decorator`{:.prop}

Value: | none \| \[ \<type\>( \<properties\> ) \<paint-area\>? \| \<name\> \<paint-area\>? \]<span class="prop-def-symbol" title="One or more comma-separated occurrences">#+</span>
Initial: | none
Inherited: | no
Percentages: | N/A

\<type\>
: Declares the decorator type, see the list of [built-in decorators](#decorators) above.

\<properties\>
: Declares the properties specific to the given decorator type.

\<name\>
: Declares a decorator name defined by an [@decorator rule](#decorator-at-rule).

\<paint-area\>
: Optionally, specifies the area of the element the decorator should be applied to, i.e. one of `border-box`{:.value}, `padding-box`{:.value}, or `content-box`{:.value}. This value defaults to `padding-box`{:.value} when omitted.

For illustration, a single decorator can be used as in the following.

```css
decorator: <type>( <properties> );
```

While multiple decorators can be used as follows. They will be rendered in the declared order from top to bottom.

```css
decorator: <type>( <properties> ), <type>( <properties> ), ... ;
```

For performance reasons, it is recommended to declare decorators in style sheets, not in the style defined inline to an element.

When creating a [custom decorator](../cpp_manual/decorators.html#custom-decorators), you can provide a shorthand property named `decorator` which will be used to parse the text inside the parenthesis of the property declaration. This allows specifying the decorator with inline properties as in the provided examples.

#### Examples

```css
/* declares an image decorater by a sprite name */
decorator: image( icon-invader );

/* declares a tiled-box decorater by several sprites */
decorator: tiled-box(
	window-tl, window-t, window-tr,
	window-l, window-c, window-r,
	window-bl, window-b, window-br
);

/* declares an image decorator by the url of an image,
   displayed across the content box of the element */
decorator: image( invader.tga ) content-box;
```

For the built-in decorators with support for images and sprites, the specified 'src' looks for a [sprite](sprite_sheets.html) with the same name first. If none exists, then it treats it as a file name for an image.

Decorators can be overridden like any other property. So, in the example:

```css
h1 {
	decorator: image( cat.png );
}

h1:hover {
	decorator: none;
}
```
all `h1`{:.tag} tags will have an image decorator attached, except when they are being hovered, then they will not be rendered.


### Decorator at-rule

The `@decorator` at-rule in RCSS can be used to declare a decorator when the shorthand syntax given above is not sufficient. It is best served with an example, we use the custom `starfield` decorator type from the invaders sample. In the style sheet, we can populate it with properties as follows.

```css
@decorator stars : starfield {
	num-layers: 5;
	top-colour: #fffc;
	bottom-colour: #fff3;
	top-speed: 80.0;
	bottom-speed: 20.0;
	top-density: 8;
	bottom-density: 20;
}
```
And then use it in a decorator.
```css
decorator: stars;
```
Note the lack of parenthesis which means it is a decorator name and not a type with shorthand properties declared.
