---
layout: page
title: Decorators
parent: rcss
next: font_effects
---

Decorators are an extension to CSS for RCSS. A decorator can be declared and named in a style sheet like a property, and then configured with decorator-specific properties. Custom decorator types can be developed to suit the needs of the user, and in this manner any kind of decoration can be applied to an element.

### Declaring decorators
{:#decorator}

The decorator property is specified as follows.

`decorator`{:.prop}

Value: | none \| \<name\> \| \<type\>( \<properties\> )
Initial: | none
Inherited: | no
Percentages: | N/A

where `<name>`{:.prop} is a decorator name declared by an [@decorator rule](#decorator-at-rule), `<type>`{:.prop} is a decorator type, and `<properties>`{:.prop} specify the properties of the given decorator type.

Multiple decorators can also be specified, eg.
```css
decorator: <type>( <properties> ), <type>( <properties> ), ... ;
```
**Note**: For performance reasons, it is recommended to declare decorators in style sheets, not in the style defined inline to an element.

RmlUi ships with the following decorator types:

* [`image`{:.value}](decorators/image.html)
* [`tiled-horizontal`{:.value}](decorators/tiled_horizontal.html)
* [`tiled-vertical`{:.value}](decorators/tiled_vertical.html)
* [`tiled-box`{:.value}](decorators/tiled_box.html)
* [`ninepatch`{:.value}](decorators/ninepatch.html)
* [`gradient`{:.value}](decorators/gradient.html)

A decorator is typically declared by the decorator type and its properties in parenthesis. Some examples follow.

```css
/* declares an image decorater by a sprite name */
decorator: image( icon-invader );

/* declares a tiled-box decorater by several sprites */
decorator: tiled-box(
	window-tl, window-t, window-tr, 
	window-l, window-c, window-r,
	window-bl, window-b, window-br
);

 /* declares an image decorator by the url of an image */
decorator: image( invader.tga );
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

When creating a [custom decorator](../cpp_manual/decorators.html#custom-decorators), you can provide a shorthand property named `decorator` which will be used to parse the text inside the parenthesis of the property declaration. This allows specifying the decorator with inline properties as in the above examples.

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


### Specifying render order

Multiple decorators can be specified on any element by a comma-separated list of decorators as in the following example.
```css
/* declares two decorators on the same element, the first will be rendered on top of the latter */
decorator: image( icon-invader ), tiled-horizontal( title-bar-l, title-bar-c, title-bar-r );
```
Multiple decorators will be rendered such that the first declared decorator appears on top, and the subsequent decorators appear below the previous one.


### RmlUi decorators

RmlUi comes with several built-in decorators for displaying images and tiled images behind elements.

1. [image decorator](decorators/image.html), for displaying a single stretched image.
2. [tiled-horizontal decorator](decorators/tiled_horizontal.html), for tiling images horizontally. 
3. [tiled-vertical decorator](decorators/tiled_vertical.html), for tiling images vertically.
4. [tiled-box decorator](decorators/tiled_box.html), for tiling images across a box.
5. [ninepatch decorator](decorators/ninepatch.html), for efficiently tiling images across a box.
6. [gradient decorator](decorators/gradient.html), for adding a color gradient.