---
layout: page
title: Fonts
parent: rcss
next: text
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
