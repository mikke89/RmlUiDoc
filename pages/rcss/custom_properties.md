---
layout: page
title: Custom properties and variables
parent: rcss
next: media_queries
---

RCSS supports custom properties and the `var()` function for referencing them, commonly known as CSS variables (see [CSS custom properties specification](https://www.w3.org/TR/css-variables-1/)). They let you store a value once and reuse it across many declarations.

```css
body {
	--main-color: #b73a2a;
	--gap: 16px;
}
h1 {
	color: var(--main-color);
	margin-bottom: var(--gap);
}
```

### Differences from CSS

For the most part, the behavior matches that of CSS. The following lists some smaller deviations:

- Custom properties cannot themselves be animated. However, regular properties and shorthands that use `var()` can.
- Fallback values are only used when a referenced variable is missing. They are *not* used when a dependency cycle is detected.

### Declaring custom properties

A custom property is any property whose name begins with two dashes (`--`). The value is stored as written, and is only interpreted when substituted into another property with `var()`.

```css
body {
	--brand: #b73a2a;
	--rgb-accent: 211, 84, 0;
	--gap: 16px;
	--title-size: 24px;
}
```

### Using variables: the `var()` function

Reference a custom property with the `var()` function. It can be used in any regular property, in another custom property, or in a shorthand. The function may form part of a larger value, and a declaration can contain any number of references.

```css
h1 {
	color: var(--brand);
	font-size: var(--title-size);
}
#panel {
	/* Variables substituted into a function. */
	background-color: rgba(var(--rgb-accent), 200);
}
.swatch {
	/* A custom property built from another. */
	--brand-faded: var(--brand);
}
```

Variables are substituted at compute time and parsed for the property they are used in. Any syntax errors during parsing are therefore logged at compute time.

### Fallback values

`var()` accepts an optional fallback value, used when the referenced custom property is not defined.

```css
color: var(--brand, black);
```

The fallback itself may contain a `var()` or other function, and may consist of multiple values.

```css
color:   var(--accent, var(--brand, black));
padding: var(--inset, 10px 5px);
```

### Cascading and inheritance

Custom properties participate in the [cascade](cascade.html) like regular properties, and they are inherited. A custom property defined on an element is visible to that element and all of its descendants, and may be overridden further down the tree.

```css
body     { --color-bg: #ffffff; }
#sidebar { --color-bg: #eeeeee; }
.panel   { background-color: var(--color-bg); }
```

Whenever a variable changes, every property that references it is recomputed automatically.

Together with [media queries](media_queries.html), variables provide a compact way to implement themes. Declare the tokens once, override them inside a `@media` block, and reference them throughout the style sheet:

```css
body {
	--bg: #f0ebd8;
	--fg: #1d1d1d;
}
@media (theme: dark) {
	body {
		--bg: #18181b;
		--fg: #f4f4f5;
	}
}
body {
	background-color: var(--bg);
	color: var(--fg);
}
```

The theme can then be toggled from C++ with [`Context::ActivateTheme()`](../cpp_manual/contexts.html#themes), and all variable-based declarations update accordingly.

### Variables in shorthands

`var()` works in shorthand properties, and each component is resolved independently. A single variable may also expand to several values.

```css
body { --inset: 20px 5px; }

div {
	padding: var(--inset);
	margin: 0 var(--gap);
}
```

When a shorthand and one of its longhand components are both declared, normal cascade rules apply. The declaration that comes last wins. For example, `padding: var(--inset)`{:.value} followed by `padding-top: 0px`{:.value} keeps the explicit top padding while the remaining edges come from the variable.

### Animations and transitions

Regular properties and shorthands that reference variables can be [animated and transitioned](animations_transitions_transforms.html) as usual. The variable is resolved to a concrete value when the animation is built. This includes variables used inside `@keyframes` blocks.

Custom properties themselves cannot be animated or transitioned.

### Reading and writing variables from C++

Custom properties are accessed through the regular property functions on `Element`{:.cls}, by passing the full name including the `--` prefix.

```cpp
// Set or change a custom property.
element->SetProperty("--brand", "#b73a2a");

// The context should be updated before retrieving resolved properties,
context->Update();

// Read the value with all variables fully resolved.
if (const Rml::Property* property = element->GetProperty("--brand"))
	Rml::String value = property->ToString();

// Remove the local override.
element->RemoveProperty("--brand");
```

`Element::GetProperty()` returns the value after cascading and inheritance, and with `var()` references fully resolved. On the other hand, `Element::GetLocalProperty()` retrieves the *specified value* with any variables left unresolved, and only when set directly on the current element. As with other computed values, resolved variables are only guaranteed to be up-to-date after a [context update](../cpp_manual/elements.html#validity-of-retrieved-values). The returned pointer is only valid until the next call into RmlUi, so copy the property by value if you need to keep it.

### Sample

See the `variables` sample (`Samples/basic/variables`{:.path}) for a complete example using design tokens and switchable themes.
