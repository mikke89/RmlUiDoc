---
layout: page
title: Progress bar
parent: cpp_manual/controls
---

The `<progressbar>`{:.tag} element can visually display progress or relative values.

You can find the RML documentation for the progressbar element [here]({{"pages/rml/data_display.html#progressbar"|relative_url}}). The element is only available with the `RmlControls` library.


### C++ Interface

The `{{page.lib_ns}}::Controls::ElementProgressBar` class (found in `<{{page.lib_dir}}/Controls/ElementProgressBar.h>`{:.incl}) defines the interface to the progress bar element.

The progress bar's value can be set through the C++ interface.

```cpp
// Return the value of the progress bar [0, 1]
float GetValue() const;

// Set the value of the progress bar
void SetValue(float value);
```

Otherwise, the value and the other attributes can be set using the `Element::SetAttribute` function.


### Styling

The `progressbar`{:.tag} element generates a non-dom `fill`{:.tag} child element which can be used to style the filled part of the bar. The `fill`{:.tag} element can use normal properties such as `background-color`{:.prop}, `border`{:.prop}, and `decorator`{:.prop} to style it, or use the `fill-image`{:.prop} property to set an image which will be clipped according to the progress bar's `value`. The `fill`{:.tag} element will automatically be positioned and scaled to cover the content region of the parent `progressbar`{:.tag} element, then scaled down according to its `value` and `direction` attributes.

The `fill-image`{:.prop} property is the only way to style circular progress bars (`clockwise` and `counter-clockwise` directions). The `fill`{:.tag} element is still available but it will always be fixed in size independent of the `value` attribute.


**RCSS property**

`fill-image`{:.prop}

The `fill-image`{:.prop} property sets an image to fill the progress bar, and must be applied to the `fill`{:.tag} child element. It will be clipped according to the progress bar's `value`. This property is the only way to style circular progress bars (`clockwise` and `counter-clockwise` directions). The `fill`{:.tag} element is still available but it will always be fixed in size independent of the `value` attribute.

Value: | \<string\>
Initial: | undefined
Applies to: | `fill`{:.tag} element
Inherited: | no
Percentages: | N/A


### Examples

The following RCSS styles three different progress bars.
```css
@spritesheet progress_bars
{
	src: my_progress_bars.tga;
	progress:        103px 267px 80px 34px;
	progress-fill-l: 110px 302px  6px 34px;
	progress-fill-c: 140px 302px  6px 34px;
	progress-fill-r: 170px 302px  6px 34px;
	gauge:      0px 271px 100px 86px;
	gauge-fill: 0px 356px 100px 86px;
}
.progress_horizontal { 
	decorator: image( progress );
	width: 80px;
	height: 34px;
}
.progress_horizontal fill {
	decorator: tiled-horizontal( progress-fill-l, progress-fill-c, progress-fill-r );
	margin: 0 7px;
	/* padding ensures that the decorator has a minimum width when the value is zero */
	padding-left: 14px;
}
.progress_vertical {
	width: 30px;
	height: 80px;
	background-color: #E3E4E1;
	border: 4px #A90909;
}
.progress_vertical fill {
	border: 3px #4D9137;
	background-color: #7AE857;
}
.gauge { 
	decorator: image( gauge );
	width: 100px;
	height: 86px;
}
.gauge fill { 
	fill-image: gauge-fill;
}
```
Now, they can be used in RML as follows.
```html
<progressbar class="progress_horizontal" value="0.75"/>
<progressbar class="progress_vertical" direction="top" value="0.6"/>
<progressbar class="gauge" direction="clockwise" start-edge="bottom" value="0.3"/>
```
