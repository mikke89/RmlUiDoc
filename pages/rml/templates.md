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
: For inline templates, the name of the template to inject.

### \<body\>

The `<body>`{:.tag} element has a `template`{:.attr} attribute that is a shorthand for injecting a template around the body tag.

_Attributes_

`template`{:.attr} = cdata (CS)
: The name of the template to use. All child elements under the `<body>`{:.tag} element will be loaded into the template.


### Example

Start by defining a template file `basic.rml`:

```html
<template name="basic" content="content">
<head>
	<link type="text/rcss" href="style.rcss"/>
</head>
<body class="window">
	<h1>Header</h1>
	<p id="content"></p>
</body>
</template>
```

#### Body template

The template can then be can be used as a body template in a document as follows.


```html
<rml>
	<head>
		<title>Basic document</title>
		<link type="text/template" href="basic.rml" />
	</head>
	<body template="basic">
		A paragraph.
	</body>
</rml>
```

The template is then injected with the document body contents inserted into the `#content` element defined in the template. The resulting document structure is as follows:

```
body.window
  h1         "Header"
  p#content  "A paragraph."
```

#### Inline template

The template can also be inserted inline into the document using the `<template src="[name]">` element.

```html
<rml>
	<head>
		<title>Basic document</title>
		<link type="text/template" href="basic.rml" />
	</head>
	<body>
		<img src="header.png"/>
		<div id="template_parent">
			<template src="basic">
				Another paragraph.
			</template>
		</div>
	</body>
</rml>
```

Which results in the following document structure:

```
body
  img
  div#template_parent
    h1         "Header"
    p#content  "Another paragraph."
```

Note that the body class from the template is not inserted in this case. However, headers, including styles, are inserted as normal.
