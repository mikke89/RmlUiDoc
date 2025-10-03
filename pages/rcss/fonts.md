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
{:#font-family}

`font-family`{:.prop}

Value: | \<string\>
Initial: | undefined
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property specifies the name of a family of fonts to be used to render sections of text descending from the element. Note that, unlike CSS, only a single font family can be specified with this property, not a comma-delimited font set.

#### Font styling: the 'font-style' and 'font-weight' properties
{:#font-style}

`font-style`{:.prop}

Value: | normal \| italic
Initial: | normal
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property can be used to request normal or italicised versions of a font from within a font-family. Note that RCSS does not yet support oblique font styles.

`font-weight`{:.prop}
{:#font-weight}

Value: | normal \| bold \| \<number \[1,1000\]\>
Initial: | normal
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

This property can be used to request normal or bolded versions of a font from within a font-family. A numeric value can be specified for more granularity on supported fonts. The range is based on the commonly used OpenType specification: 100 (Thin), 200 (Extra Light), 300 (Light), 400 (Normal), 500 (Medium), 600 (Semi Bold), 700 (Bold), 800 (Extra Bold), 900 (Black).

#### Font size: the 'font-size' property
{:#font-size}

`font-size`{:.prop}

Value: | \<length\> \| \<percentage\>
Initial: | 12px
Applies to: | all elements
Inherited: | yes
Percentages: | Font size of parent element

Values have the following meanings:

`<length>`{:.value}
: The font size is generated at the point size requested. For font-relative units (such as `em`{:.value} ), the font size is relative to the parent element's font size.

`<percentage>`{:.value}
: The font size is generated at the point size of the element's parent's font, scaled by the percentage.


#### Font shorthand
{:#font}

`font`{:.prop}

Value: | `font-style`{:.prop} `font-weight`{:.prop} `font-size`{:.prop} `font-family`{:.prop}
Initial: | See individual properties
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

A shorthand property for setting all the font properties at once.


#### Font kerning: the 'font-kerning' property
{:#font-kerning}

`font-kerning`{:.prop}

Value: | auto \| normal \| none
Initial: | auto
Applies to: | all elements
Inherited: | yes
Percentages: | N/A

Values have the following meanings:

`auto`{:.value}
: Font kerning is enabled if available by default, but is disabled for small font sizes to improve the readability of text.

`normal`{:.value}
: Font kerning is always enabled if available.

`none`{:.value}
: Font kerning is disabled.

Font kerning affects how characters are spaced next to each other. Most fonts have kerning information that improves readability by making the optical spacing between characters more uniform.
