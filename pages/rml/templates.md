---
layout: page
title: RML Templates
parent: rml
next: events
---

### \<template\>

The `<template>`{:.tag} element has two uses, to define a template and inject a template inline into an existing RML documents.

When defining a template, `<template>`{:.tag} should be used in place of `<rml>`{:.tag}.

_Attributes_

`name`{:.attr} = cdata (CI)
: The name of the template. Must be unique. Is used by other RML documents to reference the template.

`content`{:.attr} = idref (CI)
: The id of the element that the content will be put into.

When injecting a template, all elements inside the `<template>`{:.tag} tag will be placed inside the template's content element.

`src`{:.attr} = cdata (CS)
: The name of the template to inject

### \<body\>

The `<body>`{:.tag} element has a `template`{:.attr} attribute that is a shorthand for injecting a template around the body tag.

_Attributes_

`template`{:.attr} = cdata (CS)
: The name of the template to use. All child elements under the `<body>`{:.tag} element will be loaded into the template.

