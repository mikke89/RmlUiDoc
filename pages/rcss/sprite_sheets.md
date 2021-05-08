---
layout: page
title: Sprite sheets
parent: rcss
next: decorators
---

The RCSS at-rule `@spritesheet` can be used to declare a sprite sheet. A sprite sheet consists of a single image and multiple sprites each specifying a region of the image. Sprites can in turn be used in decorators and `<img>`{:.tag} elements.

A sprite sheet can be declared in RCSS as in the following example.

```css
@spritesheet theme 
{
	src: invader.tga;
	resolution: 1x;
	
	title-bar-l: 147px 0px 82px 85px;
	title-bar-c: 229px 0px  1px 85px;
	title-bar-r: 231px 0px 15px 85px;
	
	icon-invader: 179px 152px 51px 39px;
	icon-game:    230px 152px 51px 39px;
	icon-score:   434px 152px 51px 39px;
	icon-help:    128px 152px 51px 39px;
}
```

The sprite sheet name (here `theme`) is optional. All sprite names (eg. `icon-invader`) are global, and can be overrided by later defined sprite sheets.

### Properties


`src`{:.prop#src}

Value: | \<string\>
Initial: | undefined
Applies to: | `@spritesheet`{:.prop} blocks
Inherited: | N/A
Percentages: | N/A

Provides the filename of the source image for the sprite sheet.

 
`resolution`{:.prop#resolution}

Value: | \<resolution\>
Initial: | 1x
Applies to: | `@spritesheet`{:.prop} blocks
Inherited: | N/A
Percentages: | N/A

Determines the resolution scaling the source image is designed to be displayed at. Eg. if it was made to be displayed at 200% DPI, set this to `2x`{:.value}. This property is optional and defaults to `1x`{:.value}.

This value, together with the current context's [dp-ratio](syntax.html#dp-unit), will determine the natural size of the sprites in this sprite sheet.

For example, if we set the `resolution`{:.prop} property to `2x`{:.value} and the dp-ratio to `2.0`{:.value} on the context, the size of an `<img>` element using this sprite will be displayed at 1:1 texel to pixel ratio. If for the same sprite, the current dp-ratio is `1.0`{:.value}, the image element will be scaled to half. Of course, RCSS styles can be used to override this natural size of the image element.

#### Sprites

`[sprite-name]`{:.prop}  
(any name other than `src`{:.prop} and `resolution`{:.prop})

Value: | \<rectangle\>
Initial: | undefined
Applies to: | `@spritesheet`{:.prop} blocks
Inherited: | N/A
Percentages: | N/A

Every other property specifies a sprite as `<sprite-name>: <rectangle>`{:.prop}. A sprite's name applies globally to all included style sheets in a given document. If multiple sprites are defined with the same name, the last one will be used.

A \<rectangle\> is declared as `x y width height`, each of which must be in `px`{:.unit} units. Here, `x` and `y` refers to the position in the image with the origin placed at the top-left corner, and `width` and `height` extends the rectangle right and down.


### Usage

The sprite name can be used in decorators, such as:
```css
decorator: tiled-horizontal( title-bar-l, title-bar-c, title-bar-r );
```
This creates a tiled decorator where the `title-bar-l`{:.value} and `title-bar-r`{:.value} sprites occupy the left and right parts of the element at their native size, while `title-bar-c`{:.value} occupies the center and is stretched horizontally as the element is stretched.

Sprites can also be used in `<img>` elements using the `sprite`{:.attr} attribute.

```css
<img sprite="icon-invader"/>
```

### High DPI

Using sprite sheets together with media queries, it is easy to swap between low- and high-resolution images automatically, determined by the context's current dp-ratio.

To override the above `theme` sprite sheet, define one for high resolution just below it and place it within a media query.

```css
@media (min-resolution: 2x)
{
	@spritesheet theme2x
	{
		src: invader2x.tga;
		resolution: 2x;
		
		title-bar-l: 147px 0px 164px 170px;
		title-bar-c: 429px 0px   1px 170px;
		title-bar-r: 631px 0px  30px 170px;
		
		icon-invader: 179px 152px 102px 78px;
		icon-game:    330px 152px 102px 78px;
		icon-score:   534px 152px 102px 78px;
		icon-help:    728px 152px 102px 78px;
	}
}
```

Since sprite names are global, when this media rule is activated, the high resolution sprites will override and replace those of the low resolution, providing crisply rendered icons for your users.
