---
layout: page
title: RML Document Structure
parent: rml
next: style_sheets
---

### \<rml\>

All RmlUi documents begin with the `<rml>`{:.tag} element. The element should contain two children, `<head>`{:.tag} and `<body>`{:.tag}, as shown in the following basic structure of a document.

```html
<rml>
	<head>
		<title>...</title>
		<link type="text/rcss" href="style.rcss"/>
		...
	</head>
	<body>
		...
	</body>
</rml>
```

### \<head\>

The `<head>`{:.tag} element contains information about the current document, such as its title, style and template information is references. No information in the header is rendered.

### \<title\>

The `<title>`{:.tag} element contains the title of the document. This is often used for the specifying the contents of the title bar of a game window.

### \<link\>

The `<link>`{:.tag} element is used to specify additional resources the document requires.

_Attributes_

`type`{:.attr} = cdata (CI)
: Type of link, which should be one of:
* text/rcss - [RmlUi Style Sheet Specification](../rcss.html)
* text/template - [RmlUi Template](templates.html)

`href`{:.attr} = cdata (CS)
: Specifies the source URI, relative to the document being parsed.

### \<script\>

The `<script>`{:.tag} element can be used to integrate scripting capabilities. A plugin is required to handle the script, such as the [Lua plugin](../lua_manual.html).

_Attributes_

`src`{:.attr} = cdata (CS)
: Specifies the source URI, relative to the document being parsed.

If the `src`{:.attr} attribute is not present, the element is an inline script whose content represents the script to run.

### \<body\>

The `<body>`{:.tag} element contains the document's content. All elements within the `<body>`{:.tag} tag become part of the document tree and are processed during layout, as determined by the active style sheets.
