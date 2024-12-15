---
layout: page
title: Shader decorator
grandparent: rcss
parent: rcss/decorators
next: text
---

The `shader`{:.prop} decorator serves as a customization point in RCSS style sheets for users to render their own effects. The decorator passes its specified value through to the render interface, so that it can be interpreted by users and rendered how they like.

```css
decorator: shader( <value> ) <paint-area>?;
```

Some examples where this decorator might serve useful include animated backgrounds, minimaps, glowing effects, creatively drawn borders, fluid simulations, and anything else you might be inspired to create.

In order to display shader decorators, the backend renderer must support advanced effects. In particular, this decorator requires [shader support](../../cpp_manual/interfaces/render.html#shaders), and that users themselves implement their desired effects.


### Properties

`value`{:.prop}

Value: | \<string\>
Initial: | *empty*
Percentages: | N/A

Specifies the value to pass through to the renderer. The built-in [OpenGL3 renderer](https://github.com/mikke89/RmlUi/blob/master/Backends/RmlUi_Renderer_GL3.cpp) implements a shader for demonstration purposes (`creation`{:.value}), which can be seen in the `rmlui_sample_effects` sample.

`paint-area`{:.prop}

Value: | border-box \| padding-box \| content-box
Initial: | padding-box
Percentages: | N/A

Declares the box area to render the decorator onto.


### Examples

The following RCSS declares a shader effect.

```css
.creation {
    decorator: shader("creation");
    border-radius: 20px;
    border: 3px #ddd;
}
```

Additional examples.

```css
.shader1 {
    decorator: shader("my_shader") border-box;
}
.shader2 {
    decorator: shader("snake and rabbit");
}
```
