---
layout: page
title: Property index
parent: rcss
---

Following is a full index of properties recognised by RCSS. The **Notes** column details important changes from the CSS specification.

Name | Values | Initial value | Applies to | Inherited? | Percentages | Notes
---- | ------ | ------------- | ---------- | ---------- | ----------- | -----
`animation`{:.prop} | See [animations](animations_transitions_transforms.html#animations) | none | all | no | | 
`background`{:.prop} | `background-color`{:.prop} | | | | | Excludes images, use decorators instead.
`background-color`{:.prop} | \<colour\> | transparent | all | no | | 
`border`{:.prop} | `border-width`{:.prop} `border-color`{:.prop} | | | | | Excludes border style.
`border-color`{:.prop} | `border-top-color`{:.prop} `border-right-color`{:.prop} `border-bottom-color`{:.prop} `border-left-color`{:.prop} | | | | | 
`border-top`{:.prop} `border-right`{:.prop} `border-bottom`{:.prop} `border-left`{:.prop} | `border-<edge>-width`{:.prop} `border-<edge>-color`{:.prop} | | | | | Excludes border style.
`border-top-color`{:.prop} `border-right-color`{:.prop} `border-bottom-color`{:.prop} `border-left-color`{:.prop} | \<color\> | black | all | no | | 
`border-top-width`{:.prop} `border-right-width`{:.prop} `border-bottom-width`{:.prop} `border-left-width`{:.prop} | \<length\> \| \<percentage\> | 0px | all | no | width of containing block | 
`border-width`{:.prop} | `border-top-width`{:.prop} `border-right-width`{:.prop} `border-bottom-width`{:.prop} `border-left-width`{:.prop} | | all | | | 
`bottom`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | height of containing block | No 'auto'.
`clear`{:.prop} | left \| right \| both \| none | none | block-level elements | no | | 
`clip`{:.prop} | \<number\> \| auto \| none | auto | all | yes | | Controls interaction with ancestor element's clipping regions.
`color`{:.prop} | \<colour\> | black | all | yes | | 
`cursor`{:.prop} | \<string\> | _empty_ | all | yes | | \<string\> refers an application specific cursor name.
`decorator`{:.prop} | none \| \<name\> \| \<type\>( \<properties\> ) | none | all | no | | See [decorators](decorators.html) for details.
`display`{:.prop} | inline \| block \| inline-block \| none | inline | all | no | | 
`drag`{:.prop} | none \| drag \| drag-drop \| block \| clone | none | all | no | | Introduced for RCSS. Controls generation of drag messages.
`focus`{:.prop} | none \| auto | auto | all | yes | | 
`font`{:.prop} | `font-style`{:.prop} `font-weight`{:.prop} `font-size`{:.prop} `font-family`{:.prop} | | | | | 
`font-effect`{:.prop} | none \| \<type\>( \<properties\> ) | none | all | yes | | See [font effects](font_effects.html) for details.
`font-family`{:.prop} | \<string\> | | all | yes | | Only single family supported.
`font-size`{:.prop} | \<length\> \| \<percentage\> | 12px | all | yes | size of parent font | 
`font-style`{:.prop} | normal \| italic | normal | all | yes | | 'oblique' not supported.
`font-weight`{:.prop} | normal \| bold | normal | all | yes | | Intermediate weights not supported.
`height`{:.prop} | \<length\> \| \<percentage\> \| auto | auto | block and replaced inline elements | no | height of containing block | 
`image-color`{:.prop} | \<color\> | white | \<img\> elements and decorators | no | | 
`left`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | width of containing block | No 'auto'.
`line-height`{:.prop} | \<number\> \| \<length\> \| \<percentage\> | 1.2 | all | yes | font size | 'normal' not supported.
`margin`{:.prop} | `margin-top`{:.prop} `margin-right`{:.prop} `margin-bottom`{:.prop} `margin-left`{:.prop} | | | | | 
`margin-top`{:.prop} `margin-right`{:.prop} `margin-bottom`{:.prop} `margin-left`{:.prop} | \<length\> \| \<percentage\> \| auto | 0px | all | no | width of containing block | 
`max-height`{:.prop} | \<length\> \| \<percentage\> | -1px | block and replaced inline elements | no | height of containing block | 'none' not supported, use negative numbers instead.
`min-height`{:.prop} | \<length\> \| \<percentage\> | 0px | block and replaced inline elements | no | height of containing block | 
`max-width`{:.prop} | \<length\> \| \<percentage\> | -1px | block and replaced inline elements | no | width of containing block | 'none' not supported, use negative numbers instead.
`min-width`{:.prop} | \<length\> \| \<percentage\> | 0px | block and replaced inline elements | no | width of containing block | 
`opacity`{:.prop} | \<number\> | 1 | all | yes | | 
`overflow`{:.prop} | `overflow-x`{:.prop} `overflow-y`{:.prop} | | | | | 
`overflow-x`{:.prop} | visible \| hidden \| scroll \| auto | visible | block elements | no | | Content clipped if either axis is not 'visible'.
`overflow-y`{:.prop} | visible \| hidden \| scroll \| auto | visible | block elements | no | | Content clipped if either axis is not 'visible'.
`padding`{:.prop} | `padding-top`{:.prop} `padding-right`{:.prop} `padding-bottom`{:.prop} `padding-left`{:.prop} | | | | | 
`padding-top`{:.prop} `padding-right`{:.prop} `padding-bottom`{:.prop} `padding-left`{:.prop} | \<length\> \| \<percentage\> | 0px | all | no | width of containing block | 
`perspective`{:.prop} | none \| \<length\> | none | all | no | | See [transforms](animations_transitions_transforms.html#transform-property).
`pointer-events`{:.prop} | auto \| none | auto | all | yes | | 
`position`{:.prop} | static \| relative \| absolute \| fixed | static | all | no | | 'fixed' is positioned like 'absolute' but ignores scrolling.
`right`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | width of containing block | No 'auto'.
`scrollbar-margin`{:.prop} | \<length\> | 0px | scrollbar-horizontal and scrollbar-vertical elements | no | | Introduced for RCSS. Specifies a bottom / right margin (depending on orientation) that will collapse with the scrollbar on the complementary axis.
`tab-index`{:.prop} | none \| auto | none | all | no | | Introduced for RCSS. Controls order of focus switching when the tab key is pressed.
`text-align`{:.prop} | left \| right \| center | left | block-level elements | yes | | 'justify' not supported.
`text-decoration`{:.prop} | none \| underline \| overline \| line-through | none | all | yes | | 
`text-transform`{:.prop} | none \| capitalize \| uppercase \| lowercase | none | all | yes | | 
`top`{:.prop} | \<length\> \| \<percentage\> | 0px | positioned elements | no | height of containing block | No 'auto'.
`transition`{:.prop} | See [transitions](animations_transitions_transforms.html#transitions) | none | all | no | | 
`transform`{:.prop} | See [transforms](animations_transitions_transforms.html#transform-property) | none | all | no | | 
`vertical-align`{:.prop} | baseline \| sub \| super \| text-top \| text-bottom \| middle \| top \| bottom \| \<percentage\> \| \<length\> | baseline | inline-level elements | no | line-height | 
`visibility`{:.prop} | visible \| hidden | visible | all | no | | 
`white-space`{:.prop} | normal \| pre \| nowrap \| pre-wrap \| pre-line | normal | block-level elements | yes | | 
`width`{:.prop} | \<length\> \| \<percentage\> \| auto | auto | block and replaced inline elements | no | width of containing block | 
`z-index`{:.prop} | \<number\> \| auto | auto | all | no | | Applies to all elements. For documents, 'auto' allows pulling to front, otherwise remains at top or bottom. 