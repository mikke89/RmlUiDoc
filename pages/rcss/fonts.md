---
layout: page
title: Fonts
parent: rcss
---

RCSS implements a simpler version of the [CSS2 font model](http://www.w3.org/TR/REC-CSS2/fonts.html) when dealing with text rendering. This is for two reasons:

* The document renderer is fully under the control of the author, so (for example) a specific font can be assumed to exist.
* Improved performance. 

Fonts are specified in a similar fashion.
NOTE: You will need to load all ttf files via the C++ interfaces before they can be used in RCSS.

### Font specification properties

#### Font family: the 'font-family' property

`font-family`{:.prop}

Value: | \<string\>
Initial: | undefined
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property specifies the name of a family of fonts to be used to render sections of text descending from the element. Note that, unlike CSS, only a single font family can be specified with this property, not a comma-delimited font set.

#### Font styling: the 'font-style' and 'font-weight' properties

`font-style`{:.prop}

Value: | normal \| italic
Initial: | normal
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property can be used to request normal or italicised versions of a font from within a font-family. Note that RCSS does not yet support oblique font styles.

`font-weight`{:.prop} 

Value: | normal \| bold
Initial: | normal
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property can be used to request normal or bolded versions of a font from within a font-family. Note that RCSS only supports bold and non-bold fonts, and not different strengths of boldness.

#### Font size: the 'font-size' property

`font-size`{:.prop} 

Value: | \<length\> \| \<percentage\>
Initial: | 12px
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

Values have the following meanings:

`<length>`{:.value} 
: The font size is generated at the point size requested. For font-relative units (such as `em`{:.value} ), the font size is relative to the parent element's font size.

`<percentage>`{:.value} 
: The font size is generated at the point size of the element's parent's font, scaled by the percentage. 

#### Font charset: the 'font-charset' property

`font-charset`{:.prop} 

Value: | \<urange\>
Initial: | U+0020-007E
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property allows elements to request a font that is capable of rendering characters within a range (or ranges). Because fonts are rasterised and rendered to texture before they can be used, this can be quite useful in limiting the size of textures used by the font engine. For example, a large font used for titles could be restricted to only capital letters.

The value of `font-charset`{:.prop}  is a comma-separated list of Unicode ranges, each of which is in one of the forms:

* U+xxxx, to specify a single character (where x is any hexadecimal digit).
* U+xxxx-yyyy, to specify the range of xxxx through yyyy.
* U+xx??, to specify the range of xx00 through xxFF. The wildcard '?' can be used to substitute any digits, but must appear in an uninterrupted range at the end of the specifier. 

For more information, see the CSS specification of [unicode-range](http://www.w3.org/TR/REC-CSS2/fonts.html#descdef-unicode-range). 