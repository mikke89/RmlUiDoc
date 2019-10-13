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
	
	title-bar-l: 147px 0px 82px 85px;
	title-bar-c: 229px 0px  1px 85px;
	title-bar-r: 231px 0px 15px 85px;
	
	icon-invader: 179px 152px 51px 39px;
	icon-game:    230px 152px 51px 39px;
	icon-score:   434px 152px 51px 39px;
	icon-help:    128px 152px 51px 39px;
}
```
The first property `src` provides the filename of the image for the sprite sheet. Every other property specifies a sprite as `<name>: <rectangle>`. A sprite's name applies globally to all included style sheets in a given document, and must be unique. This constraint also applies to merged style sheets.

A rectangle is declared as `x y width height`, each of which must be in `px`{:.unit} units. Here, `x` and `y` refers to the position in the image with the origin placed at the top-left corner, and `width` and `height` extends the rectangle right and down.

The sprite name can be used in decorators, such as:
```css
decorator: tiled-horizontal( title-bar-l, title-bar-c, title-bar-r );
```
This creates a tiled decorator where the `title-bar-l`{:.value} and `title-bar-r`{:.value} sprites occupy the left and right parts of the element at their native size, while `title-bar-c`{:.value} occupies the center and is stretched horizontally as the element is stretched.
