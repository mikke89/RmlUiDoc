---
layout: page
title: Decorators
parent: rcss
---

Decorators are an extension to CSS for RCSS. A decorator can be declared and named in a style sheet like a property, and then configured with decorator-specific properties. Custom decorator types can be developed to suit the needs of the user, and in this manner any kind of decoration can be applied to an element.

**Important**: Note that decorators can only be declared and defined in style sheets, not in style defined inline to an element.

### Declaring decorators

The declaration of a decorator is a property of the form:

```css
<name>-decorator: <type>;
```

where `<name>`{:.prop} is the user-specified name of the decorator to declare, and `<type>`{:.prop} is the application-specific type of decorator. {{page.lib_name}} ships with the following decorator types: 

* [`image`{:.value}](decorators/image.html)
* [`tiled-box`{:.value}](decorators/tiled_box.html)
* [`tiled-horizontal`{:.value}](decorators/tiled_horizontal.html)
* [`tiled-vertical`{:.value}](decorators/tiled_vertical.html)

The decorator type `none`{:.value} is a reserved name that represents no decorator. For example, in the following:

```css
button
{
	icon-decorator: tiled-horizontal;
}
```

the RCSS is attaching a decorator of type `tiled-horizontal`{:.value} called 'icon' to all `button`{:.tag} elements. Note that the name 'icon' could be anything; it is only used to uniquely identify the decorator for applying properties to it.

Decorator types can be overridden like any other property. So, in the example:

```css
h1
{
	icon-decorator: image;
}

h1:hover
{
	icon-decorator: none;
}
```

all `h1`{:.tag} tags will have an image decorator attached, except when they are being hovered, when the decorator will not be rendered.

### Decorator properties

Decorators have their own property specifications with properties and shorthands, and these can be defined for declared decorators just like any other property. Decorator properties are set in the form:

```css
<name>-<property>: <value>;
```

where `<name>`{:.prop} is the name the decorator was declared under, `<property>`{:.prop} is the name of the decorator's property to set, and `<value>`{:.value} is the value of the property. For example:

```css
h1
{
	icon-decorator: image;
	icon-image-src: ../images/header_arrow.png;
	icon-image-s-begin: 5px;
}
```

an `image`{:.value} decorator is declared, called 'icon'. On this decorator, the properties `<name>-image-src`{:.prop} is set to '../images/header_arrow.png' and `<name>-image-s-begin`{:.prop} is set to '5px'. The other properties in the `image`{:.prop} specification are left to their defaults.

The decorator properties behave like other properties, so are subject to precedence and the cascade. For example, if the following RCSS was loaded after the previous example:

```css
h1
{
	icon-image-s-begin: 3px;
}

h1:first-child
{
	icon-decorator: none;
}
```

all `h1`{:.tag} tags will have their 'icon' decorators defined with an `<name>-s-begin`{:.prop} property of '3px' instead of '5px', and an `h1`{:.tag} that is a first child will have no decorator.

Be careful of name conflicts! For example, in the following sample:

```css
h1
{
	icon-decorator: image;
}

.secondary
{
	icon-decorator: tiled-horizontal;
}
```

an element of type `h1`{:.tag} with a class of 'secondary' will have a single decorator, 'icon', of type `tiled-horizontal`{:.value}. If the decorators had different names then they both would be present.

### Specifying render order

If an element has more than one decorator on it, you can use the 'z-index' decorator property to control the render order in a similar fashion to elements. For example, in this sample:

```css
button
{
	background-decorator: tiled-horizontal;
	background-z-index: 0;

	icon-decorator: image;
	icon-z-index: 1;
}
```

the 'icon' decorator will appear on top of the 'background' decorator. If no z-index is specified on a decorator, it will have the default z-index of 0.

### Decorators and pseudo-classes

Because of the way {{page.lib_name}} compiles pseudo-class rules within style sheets, overriding decorator properties within dynamic pseudo-classes (:active, :hover and :focus, not any of the structural classes) might not always work the way you think it should.

In a nutshell, each decorator will only process properties from their element's base rules (ie, those not specifying dynamic pseudo-classes in their final simple selector) and one rule specifying a dynamic pseudo-class (or classes), that with the highest specificity. For example, in the following sample:

```css
button
{
	background-decorator: tiled-horizontal;
	background-image-src: ../button.png;
	background-image-s-end: 128px;
}

button:hover
{
	background-image-t-begin: 32px;
	background-image-t-end: 64px;
}

button:active
{
	background-image-s-begin: 128px;
	background-image-s-end: 256px;
}
```

if both the `:hover`{:.cls} and `:active`{:.cls} pseudo-classes are active on a `button`{:.tag} element, the `<name>-image-s-begin`{:.prop} and `<name>-image-s-end`{:.prop} properties from the `:active`{:.cls} rule will be set, but the `<name>-image-t-begin`{:.prop} and `<name>-image-t-end`{:.prop} properties from the `:hover`{:.cls} rule will be ignored. The `:active`{:.cls} rule is used as it has higher precedence that the `:hover`{:.cls} rule, appearing further down the file. If you wanted both the s and t properties set, you could create another rule:

```css
button:active:hover
{
	background-image-t-begin: 32px;
	background-image-t-end: 64px;
	background-image-s-begin: 128px;
	background-image-s-end: 256px;
}
```

### {{page.lib_name}} decorators

{{page.lib_name}} comes with several built-in decorators for displaying images and tiled images behind elements.

1. [image decorator](decorators/image.html), for displaying a single stretched image.
2. [tiled-horizontal decorator](decorators/tiled_horizontal.html), for tiling images horizontally. 
3. [tiled-vertical decorator](decorators/tiled_vertical.html), for tiling images vertically.
4. [tiled-box decorator](decorators/tiled_box.html), for tiling images across a box.