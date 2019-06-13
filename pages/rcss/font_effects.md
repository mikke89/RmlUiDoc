---
layout: page
title: Font Effects
parent: rcss
next: property_index
---

Font effects are an extension to CSS for RCSS for applying effects, such as outlining or shadowing, to text. Similarly to [decorators](decorators.html), font effects are declared and named in a style sheet like a property, and configured with font-effect-specific properties. Custom font effects can be developed to apply arbitrary effects onto text.

### Properties

Font effects are declared and configured within style sheets in exactly the same manner as decorators, except they are declared as `<name>-font-effect`{:.prop} rather that `<name>-decorator`{:.prop}, including the `z-index`{:.prop} property to resolve an ambiguous render order. The only exceptions are noted below:

#### Colour

All font effects have a `<name>-color`{:.prop} property which is applied multiplicatively over the entire effect.

#### Inheritance

Unlike decorators, font effects are inherited from parent elements. For example, the following declaration:

```css
h1
{
	header-font-effect: outline;
	header-width: 2px;
	header-color: black;
}
```

will add an outline effect on the text within all `h1`{:.tag} elements and their descendants. To prevent inheritance, override the effect with `none`{:.value}. For example, to prevent the `h1`{:.tag} outline effect from affecting `span`{:.tag} elements, you could specify the following:

```css
h1 span
{
	header-font-effect: none;
}
```

### Effects

{{page.lib_name}} comes with two built-in font effects:

1. [shadow effect](font_effects/shadow.html), for rendering shadows.
2. [outline effect](font_effects/outline.html), for outlining text. 