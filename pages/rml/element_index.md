---
layout: page
title: Element Index
parent: rml
next: html4_style_sheet
comment: Please run '_tools/generate_elements_and_properties_index.py' whenever elements or their URLs are added or changed.
---

The following is a list of elements supported by RML:

- [`<rml>`{:.tag}](documents.html#rml)
- [`<head>`{:.tag}](documents.html#head)
- [`<title>`{:.tag}](documents.html#title)
- [`<link>`{:.tag}](documents.html#link)
- [`<style>`{:.tag}](style_sheets.html#style)
- [`<body>`{:.tag}](documents.html#body)
- [`<handle>`{:.tag}](controls.html#handle)
- [`<img>`{:.tag}](images.html#img)
- [`<form>`{:.tag}](forms.html#form)
- [`<input>`{:.tag}](forms.html#input)
- [`<textarea>`{:.tag}](forms.html#textarea)
- [`<select>`{:.tag}](forms.html#select)
- [`<option>`{:.tag}](forms.html#option)
- [`<label>`{:.tag}](forms.html#label)
- [`<tabset>`{:.tag}](controls.html#tabset)
- [`<tab>`{:.tag}](controls.html#tab)
- [`<panel>`{:.tag}](controls.html#panel)
- [`<progress>`{:.tag}](data_display.html#progress)

See also [element packages]({{"pages/cpp_manual/element_packages.html"|relative_url}}) in the C++ manual for controlling the behavior of several of these elements.

RmlUi does not provide a default style sheet, thus, tags which only represent a specific style rule in HTML have no special in RmlUi, such as `<div>`{:.tag} and `<span>`{:.tag}. Users can include the [recommended style sheet](html4_style_sheet.html) to enable common rules for these tags.

The following elements are additionally enabled when including their respective plugins:

- [`<lottie>`{:.tag}](../cpp_manual/lottie.html)
- [`<svg>`{:.tag}](../cpp_manual/svg.html)

---

Deprecated elements:

- [`<datagrid>`{:.tag}](deprecated.html#datagrid)
- [`<col>`{:.tag}](deprecated.html#col)
- [`<dataselect>`{:.tag}](deprecated.html#dataselect)

Users are encouraged to replace these elements with [data bindings](../data_bindings.html) possibly combined with [RCSS tables](../rcss/tables.html).
