---
layout: page
title: Property index
parent: rcss
comment: Please run '_tools/generate_elements_and_properties_index.py' whenever properties or their URLs are added or changed.
---

The following table lists all properties recognised by RCSS. The **Notes** column details important changes from the CSS specification.

Name | Values | Initial value | Applies to | Inherited | Percentages | Notes
---- | ------ | ------------- | ---------- | ---------- | ----------- | -----
[`align-content`{:.prop}][align-content] |flex-start \| flex-end \| center \| space-between \| space-around \| stretch | stretch | multi-line flex containers | no | | 
[`align-items`{:.prop}][align-items] | flex-start \| flex-end \| center \| baseline \| space-around \| stretch | stretch | flex containers | no | | 
[`align-self`{:.prop}][align-self] | auto \| flex-start \| flex-end \| center \| baseline \| space-around \| stretch | auto | flex containers | no | | 
[`animation`{:.prop}][animation] | See [animations](animations_transitions_transforms.html#animation) | none | all | no | | 
[`background`{:.prop}][background] | `background-color`{:.prop} | | | | | Excludes images, use decorators instead.
[`background-color`{:.prop}][background-color] | \<colour\> | transparent | all | no | | 
[`border`{:.prop}][border] | `border-width`{:.prop} `border-color`{:.prop} | | | | | Excludes border style.
[`border-color`{:.prop}][border-color] | `border-top-color`{:.prop} `border-right-color`{:.prop} `border-bottom-color`{:.prop} `border-left-color`{:.prop} | | | | | 
[`border-top`{:.prop}][border] [`border-right`{:.prop}][border] [`border-bottom`{:.prop}][border] [`border-left`{:.prop}][border] | `border-<edge>-width`{:.prop} `border-<edge>-color`{:.prop} | | | | | Excludes border style.
[`border-top-color`{:.prop}][border-color] [`border-right-color`{:.prop}][border-color] [`border-bottom-color`{:.prop}][border-color] [`border-left-color`{:.prop}][border-color] | \<color\> | black | all | no | | 
[`border-top-width`{:.prop}][border-width] [`border-right-width`{:.prop}][border-width] [`border-bottom-width`{:.prop}][border-width] [`border-left-width`{:.prop}][border-width] | \<length\> \| \<percentage\> | 0px | all | no | width of containing block | 
[`border-width`{:.prop}][border-width] | `border-top-width`{:.prop} `border-right-width`{:.prop} `border-bottom-width`{:.prop} `border-left-width`{:.prop} | | all | | | 
[`border-top-left-radius`{:.prop}][border-radius] [`border-top-right-radius`{:.prop}][border-radius] [`border-bottom-right-radius`{:.prop}][border-radius] [`border-bottom-left-radius`{:.prop}][border-radius] | \<length\> | 0px | all | no | | Percentages and two-axis radii not supported. |
[`border-radius`{:.prop}][border-radius] | `border-top-left-radius`{:.prop} `border-top-right-radius`{:.prop} `border-bottom-right-radius`{:.prop} `border-bottom-left-radius`{:.prop} | | all | | | 
[`bottom`{:.prop}][top_right_bottom_left] | auto \| \<length\> \| \<percentage\> | auto | positioned elements | no | height of containing block | 
[`box-sizing`{:.prop}][box-sizing] | content-box \| border-box | content-box | block and replaced inline elements | no | | 
[`caret-color`{:.prop}][caret-color] | auto \| \<colour\> | auto | all elements | yes | | 
[`clear`{:.prop}][clear] | left \| right \| both \| none | none | block-level elements | no | | 
[`clip`{:.prop}][clip] | auto \| none \| always \| \<number\> | auto | all | no | | Controls interaction with ancestor element's clipping regions.
[`color`{:.prop}][color] | \<colour\> | black | all | yes | | 
[`column-gap`{:.prop}][gap] | \<length\> \| \<percentage\> | 0px | table elements | no | initial width of table | 
[`cursor`{:.prop}][cursor] | \<string\> | _empty_ | all | yes | | \<string\> refers an application specific cursor name.
[`decorator`{:.prop}][decorator] | none \| \<name\> \| \<type\>( \<properties\> ) | none | all | no | | See [decorators](decorators.html) for details.
[`display`{:.prop}][display] | inline \| block \| inline-block \| flex \| table \| table-row-group \| table-row \| table-column-group \| table-column \| table-cell \| none | inline | all | no | | 
[`drag`{:.prop}][drag] | none \| drag \| drag-drop \| block \| clone | none | all | no | | Introduced for RCSS. Controls generation of drag messages.
[`fill-image`{:.prop}][fill-image] | \<string\> | _empty_ | [progress]({{"pages/cpp_manual/element_packages/progress_bar.html"|relative_url}}) element | no | | \<string\> refers to a sprite name or an image url.
[`flex`{:.prop}][flex] | auto \| none \| \<flex-grow\> \<flex-shrink\>? \<flex-basis\>? \| \<flex-basis\> | 0 1 auto | flex items | no | | 
[`flex-basis`{:.prop}][flex-basis] | \<length\> \| \<percentage\> \| auto | auto | flex items | no | | 
[`flex-direction`{:.prop}][flex-direction] | row \| row-reverse \| column \| column-reverse | row | flex containers | no | | 
[`flex-flow`{:.prop}][flex-flow] |  \<flex-direction\> \<flex-wrap\> | | | | | 
[`flex-grow`{:.prop}][flex-grow] | \<number\> | 0 | flex items | no | | 
[`flex-shrink`{:.prop}][flex-shrink] | \<number\> | 1 | flex items | no | | 
[`flex-wrap`{:.prop}][flex-wrap] | nowrap \| wrap \| wrap-reverse | nowrap | flex containers | no | | 
[`focus`{:.prop}][focus] | none \| auto | auto | all | yes | | Introduced for RCSS.
[`font`{:.prop}][font] | `font-style`{:.prop} `font-weight`{:.prop} `font-size`{:.prop} `font-family`{:.prop} | | | | | 
[`font-effect`{:.prop}][font-effect] | none \| \<type\>( \<properties\> ) | none | all | yes | | See [font effects](font_effects.html) for details.
[`font-family`{:.prop}][font-family] | \<string\> | | all | yes | | Only single family supported.
[`font-size`{:.prop}][font-size] | \<length\> \| \<percentage\> | 12px | all | yes | size of parent font | 
[`font-style`{:.prop}][font-style] | normal \| italic | normal | all | yes | | 'oblique' not supported.
[`font-weight`{:.prop}][font-weight] | normal \| bold | normal | all | yes | | Intermediate weights not supported.
[`gap`{:.prop}][gap] | `row-gap`{:.prop} `column-gap`{:.prop} | | table elements | | | Replaces the CSS `border-spacing`{:.prop} property.
[`height`{:.prop}][height] | \<length\> \| \<percentage\> \| auto | auto | block and replaced inline elements | no | height of containing block | 
[`image-color`{:.prop}][image-color] | \<color\> | white | \<img\> elements and decorators | no | | Introduced for RCSS.
[`justify-content`{:.prop}][justify-content] | flex-start \| flex-end \| center \| space-between \| space-around | flex-start | flex containers | no | | 
[`left`{:.prop}][top_right_bottom_left] | auto \| \<length\> \| \<percentage\> | auto | positioned elements | no | width of containing block | 
[`line-height`{:.prop}][line-height] | \<number\> \| \<length\> \| \<percentage\> | 1.2 | all | yes | font size | 'normal' not supported.
[`margin`{:.prop}][margin] | `margin-top`{:.prop} `margin-right`{:.prop} `margin-bottom`{:.prop} `margin-left`{:.prop} | | | | | 
[`margin-top`{:.prop}][margin] [`margin-right`{:.prop}][margin] [`margin-bottom`{:.prop}][margin] [`margin-left`{:.prop}][margin] | \<length\> \| \<percentage\> \| auto | 0px | all | no | width of containing block | 
[`max-height`{:.prop}][max-height] | \<length\> \| \<percentage\> | -1px | block and replaced inline elements | no | height of containing block | 'none' not supported, use negative numbers instead.
[`min-height`{:.prop}][min-height] | \<length\> \| \<percentage\> | 0px | block and replaced inline elements | no | height of containing block | 
[`max-width`{:.prop}][max-width] | \<length\> \| \<percentage\> | -1px | block and replaced inline elements | no | width of containing block | 'none' not supported, use negative numbers instead.
[`min-width`{:.prop}][min-width] | \<length\> \| \<percentage\> | 0px | block and replaced inline elements | no | width of containing block | 
[`opacity`{:.prop}][opacity] | \<number\> | 1 | all | yes | | 
[`overflow`{:.prop}][overflow] | `overflow-x`{:.prop} `overflow-y`{:.prop} | | | | | 
[`overflow-x`{:.prop}][overflow] | visible \| hidden \| scroll \| auto | visible | block elements | no | | Content clipped if either axis is not 'visible'.
[`overflow-y`{:.prop}][overflow] | visible \| hidden \| scroll \| auto | visible | block elements | no | | Content clipped if either axis is not 'visible'.
[`padding`{:.prop}][padding] | `padding-top`{:.prop} `padding-right`{:.prop} `padding-bottom`{:.prop} `padding-left`{:.prop} | | | | | 
[`padding-top`{:.prop}][padding] [`padding-right`{:.prop}][padding] [`padding-bottom`{:.prop}][padding] [`padding-left`{:.prop}][padding] | \<length\> \| \<percentage\> | 0px | all | no | width of containing block | 
[`perspective`{:.prop}][perspective] | none \| \<length\> | none | all | no | | See [transforms](animations_transitions_transforms.html#transform).
[`pointer-events`{:.prop}][pointer-events] | auto \| none | auto | all | yes | | 
[`position`{:.prop}][position] | static \| relative \| absolute \| fixed | static | all | no | | 'fixed' is positioned like 'absolute' but ignores scrolling.
[`right`{:.prop}][top_right_bottom_left] | auto \| \<length\> \| \<percentage\> | auto | positioned elements | no | width of containing block | 
[`row-gap`{:.prop}][gap] | \<length\> \| \<percentage\> | 0px | table elements | no | initial height of table | 
[`scrollbar-margin`{:.prop}][scrollbar-margin] | \<length\> | 0px | scrollbar-horizontal and scrollbar-vertical elements | no | | Introduced for RCSS. Specifies a bottom / right margin (depending on orientation) that will collapse with the scrollbar on the complementary axis.
[`tab-index`{:.prop}][tab-index] | none \| auto | none | all | no | | Introduced for RCSS. Controls order of focus switching when the tab key is pressed.
[`text-align`{:.prop}][text-align] | left \| right \| center | left | block-level elements | yes | | 'justify' not supported.
[`text-decoration`{:.prop}][text-decoration] | none \| underline \| overline \| line-through | none | all | yes | | 
[`text-transform`{:.prop}][text-transform] | none \| capitalize \| uppercase \| lowercase | none | all | yes | | 
[`top`{:.prop}][top_right_bottom_left] | auto \| \<length\> \| \<percentage\> | auto | positioned elements | no | height of containing block | 
[`transition`{:.prop}][transition] | See [transitions](animations_transitions_transforms.html#transition) | none | all | no | | 
[`transform`{:.prop}][transform] | See [transforms](animations_transitions_transforms.html#transform) | none | all | no | | 
[`vertical-align`{:.prop}][vertical-align] | baseline \| sub \| super \| text-top \| text-bottom \| middle \| top \| bottom \| \<percentage\> \| \<length\> | baseline | inline-level elements | no | line-height | 
[`visibility`{:.prop}][visibility] | visible \| hidden | visible | all | no | | 
[`white-space`{:.prop}][white-space] | normal \| pre \| nowrap \| pre-wrap \| pre-line | normal | all elements | yes | | 
[`word-break`{:.prop}][word-break] | normal \| break-all \| break-word | normal | all elements | yes | | 
[`width`{:.prop}][width] | \<length\> \| \<percentage\> \| auto | auto | block and replaced inline elements | no | width of containing block | 
[`z-index`{:.prop}][z-index] | \<number\> \| auto | auto | all | no | | Applies to all elements. For documents, 'auto' allows pulling to front, otherwise remains at top or bottom. 


[align-content]:flexboxes.html#align-content
[align-items]:flexboxes.html#align-items
[align-self]:flexboxes.html#align-self
[animation]: animations_transitions_transforms.html#animation
[background-color]: colours_backgrounds.html#background-color
[background]: colours_backgrounds.html#background-color
[border-color]: box_model.html#border-color
[border-radius]: colours_backgrounds.html#border-radius
[border-width]: box_model.html#border-width
[border]: box_model.html#border
[box-sizing]: user_interface.html#box-sizing
[caret-color]: user_interface.html#caret-color
[clear]: visual_formatting_model.html#clear
[clip]: visual_effects.html#clip
[color]: colours_backgrounds.html#color
[cursor]: user_interface.html#cursor
[decorator]: decorators.html#decorator
[display]: visual_formatting_model.html#display
[drag]: user_interface.html#drag
[fill-image]: {{"pages/cpp_manual/element_packages/progress_bar.html#fill-image"|relative_url}}
[flex]:flexboxes.html#flex
[flex-basis]:flexboxes.html#flex-basis
[flex-direction]:flexboxes.html#flex-direction
[flex-flow]:flexboxes.html#flex-flow
[flex-grow]:flexboxes.html#flex-grow
[flex-shrink]:flexboxes.html#flex-shrink
[flex-wrap]:flexboxes.html#flex-wrap
[float]: visual_formatting_model.html#float
[focus]: user_interface.html#focus
[font]: fonts.html#font
[font-effect]: font_effects.html#font-effect
[font-family]: fonts.html#font-family
[font-size]: fonts.html#font-size
[font-style]: fonts.html#font-style
[font-weight]: fonts.html#font-weight
[gap]: tables.html#gap
[height]: visual_formatting_model_details.html#height
[image-color]: colours_backgrounds.html#image-color
[justify-content]:flexboxes.html#justify-content
[line-height]: visual_formatting_model_details.html#line-height
[margin]: box_model.html#margin
[max-height]: visual_formatting_model_details.html#max-height
[max-width]: visual_formatting_model_details.html#max-width
[min-height]: visual_formatting_model_details.html#min-height
[min-width]: visual_formatting_model_details.html#min-width
[opacity]: colours_backgrounds.html#opacity
[overflow]: visual_effects.html#overflow
[padding]: box_model.html#padding
[perspective]: animations_transitions_transforms.html#transform
[pointer-events]: user_interface.html#pointer-events
[position]: visual_formatting_model.html#position
[scrollbar-margin]: ../style_guide.html#scrollbar-margin
[tab-index]: user_interface.html#tab-index
[text-align]: text.html#text-align
[text-decoration]: text.html#text-decoration
[text-transform]: text.html#text-transform
[top_right_bottom_left]: visual_formatting_model.html#top_right_bottom_left
[transition]: animations_transitions_transforms.html#transition
[transform]: animations_transitions_transforms.html#transform
[vertical-align]: tables.html#vertical-align
[vertical-align]: visual_formatting_model_details.html#vertical-align
[visibility]: visual_effects.html#visibility
[white-space]: text.html#white-space
[width]: visual_formatting_model_details.html#width
[word-break]: text.html#word-break
[z-index]: visual_formatting_model.html#z-index
