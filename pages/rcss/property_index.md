---
layout: page
title: Property index
parent: rcss
---

Following is a full index of properties recognised by RCSS. The **Notes** column details important changes from the CSS specification.

For decorators' properties see [Decorators](decorators.html).

Name | Values | Initial value | Applies to | Inherited? | Percentages | Notes
---- | ------ | ------------- | ---------- | ---------- | ----------- | -----
`background`{:.prop} | `background-color`{:.prop} | | | | | Excludes images.
`background-color`{:.prop} | \<colour\> | transparent | all | no | | 
`border-color`{:.prop} | `border-top-color`{:.prop} `border-right-color`{:.prop} `border-bottom-color`{:.prop} `border-left-color`{:.prop} | | | | | 
`border-top`{:.prop} `border-right`{:.prop} `border-bottom`{:.prop} `border-left`{:.prop} | `border-<edge>-width`{:.prop} `border-<edge>-color`{:.prop} | | | | | Excludes border style.
`border-top-color`{:.prop} `border-right-color`{:.prop} `border-bottom-color`{:.prop} `border-left-color`{:.prop} | \<color\> | black | all | no | N/A | 
`border-top-width`{:.prop} `border-right-width`{:.prop} `border-bottom-width`{:.prop} `border-left-width`{:.prop} | \<length\> \| \<percentage\> | 0px | all | no | width of containing block | 
`border-width`{:.prop} | `border-top-width`{:.prop} `border-right-width`{:.prop} `border-bottom-width`{:.prop} `border-left-width`{:.prop} | | all | | | 
`bottom`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | height of containing block | No 'auto'.
`clear`{:.prop} | left \| right \| both \| none | none | block-level elements | no | N/A | 
`clip`{:.prop} | \<number\> \| auto \| none | auto | all | yes | N/A | Controls interaction with ancestor element's clipping regions.
`color`{:.prop} | \<colour\> | black | all | yes | N/A | 
`cursor`{:.prop} | \<string\> | _empty_ | all | yes | N/A | \<string\> refers an application specific cursor name.
`display`{:.prop} | inline \| block \| inline-block \| none | inline | all | no | N/A | 
`drag`{:.prop} | none \| drag \| drag-drop \| block | none | all | no | N/A | Introduced for RCSS. Controls generation of drag messages.
`font`{:.prop} | `font-style`{:.prop} `font-weight`{:.prop} `font-size`{:.prop} `font-family`{:.prop} `font-charset`{:.prop} | | | | | 
`font-charset`{:.prop} | \<urange\> | U+0020-007E | all | yes | N/A | Introduced for RCSS. Specifies required range of characters.
`font-family`{:.prop} | \<string\> | | all | yes | N/A | Only single family supported.
`font-size`{:.prop} | \<length\> \| \<percentage\> | 12 | all | yes | size of parent font | 
`font-style`{:.prop} | normal \| italic | normal | all | yes | N/A | 'oblique' not supported.
`font-weight`{:.prop} | normal \| bold | normal | all | yes | N/A | Intermediate weights not supported.
`height`{:.prop} | \<length\> \| \<percentage\> \| auto | auto | block and replaced inline elements | no | height of containing block | 
`left`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | width of containing block | No 'auto'.
`line-height`{:.prop} | \<number\> \| \<length\> \| \<percentage\> | 1.2 | all | yes | font size | 'normal' not supported.
`margin`{:.prop} | `margin-top`{:.prop} `margin-right`{:.prop} `margin-bottom`{:.prop} `margin-left`{:.prop} | | | | | 
`margin-top`{:.prop} `margin-right`{:.prop} `margin-bottom`{:.prop} `margin-left`{:.prop} | \<length\> \| \<percentage\> \| auto | 0px | all | no | width of containing block | 
`max-height`{:.prop} | \<length\> \| \<percentage\> | -1 | block and replaced inline elements | no | height of containing block | 'none' not supported, use negative numbers instead.
`min-height`{:.prop} | \<length\> \| \<percentage\> | 0px | block and replaced inline elements | no | height of containing block | 
`max-width`{:.prop} | \<length\> \| \<percentage\> | -1 | block and replaced inline elements | no | width of containing block | 'none' not supported, use negative numbers instead.
`min-width`{:.prop} | \<length\> \| \<percentage\> | 0px | block and replaced inline elements | no | width of containing block | 
`overflow`{:.prop} | `overflow-x`{:.prop} `overflow-y`{:.prop} | | | | | 
`overflow-x`{:.prop} | visible \| hidden \| scroll \| auto | visible | block elements | no | N/A | Content clipped if either axis is not 'visible'.
`overflow-y`{:.prop} | visible \| hidden \| scroll \| auto | visible | block elements | no | N/A | Content clipped if either axis is not 'visible'.
`padding`{:.prop} | `padding-top`{:.prop} `padding-right`{:.prop} `padding-bottom`{:.prop} `padding-left`{:.prop} | | | | | 
`padding-top`{:.prop} `padding-right`{:.prop} `padding-bottom`{:.prop} `padding-left`{:.prop} | \<length\> \| \<percentage\> | 0px | all | no | width of containing block | 
`position`{:.prop} | static \| relative \| absolute \| fixed | static | all | no | N/A | 'fixed' is positioned like 'absolute' but ignores scrolling.
`right`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | width of containing block | No 'auto'.
`scrollbar-margin`{:.prop} | \<length\> | 0px | scrollbar-horizontal and scrollbar-vertical elements | no | N/A | Introduced for RCSS. Specifies a bottom / right margin (depending on orientation) that will collapse with the scrollbar on the complementary axis.
`tab-index`{:.prop} | none \| auto | none | all | yes | N/A | Introduced for RCSS. Controls order of focus switching when the tab key is pressed.
`text-align`{:.prop} | left \| right \| center | left | block-level elements | yes | N/A | 'justify' not supported.
`text-decoration`{:.prop} | underline \| none | none | all | yes | N/A | 'overline', 'line-through' not supported.
`top`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | height of containing block | No 'auto'.
`vertical-align`{:.prop} | baseline \| sub \| super \| text-top \| text-bottom \| middle \| top \| bottom \| \<percentage\> \| \<length\> | baseline | inline-level elements | no | line-height | 
`visibility`{:.prop} | visible \| hidden | visible | all | no | N/A | 
`white-space`{:.prop} | normal \| pre \| nowrap \| pre-wrap \| pre-line | normal | block-level elements | yes | N/A | 'pre-wrap' and 'pre-line' from CSS3.
`width`{:.prop} | \<length\> \| \<percentage\> \| auto | auto | block and replaced inline elements | no | width of containing block | 
`z-index`{:.prop} | \<number\> \| auto \| top \| bottom | auto | all | no | N/A | Applies to all elements. 'top' and 'bottom' introduced. For documents, 'auto' allows pulling to front, otherwise remains at top or bottom. 