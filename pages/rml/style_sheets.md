---
layout: page
title: RML Style Sheets
parent: rml
next: forms
---

Styles can be included in an RML document in three ways: included from an external style sheet, declared in the header, or declared inline inside a specific tag.

### External Style Sheets {#link}

Style sheets are included from an external source with the `<link>`{:.tag} tag. See [Link Element](documents.html#link).

### Header Style Information {#style}

RCSS can be included directly inside the header, with the `<style>`{:.tag} tag.

*No attributes*

### Inline Style Declaration

RCSS can be declared directly inside an element with the style attribute.

_Attributes_

`style`{:.attr} = style (CN)
: This attribute specifies a list of RCSS properties to be applied to the current element.
