---
layout: page
title: RML Document Structure
parent: rml
---

### \<rml\>

All {{page.lib_name}} documents begin with the `<rml>`{:.tag} element. The element should contain two children, `<head>`{:.tag} and `<body>`{:.tag}.

```html
<rml>
	<head>
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
* text/rcss - [{{page.lib_name}} Style Sheet Specification](../rcss.html)
* text/template - [{{page.lib_name}} Template](templates.html)
* text/script - {{page.lib_name}} script

`href`{:.attr} = cdata (CS)
: Specifies the source URI, relative to the document being parsed.

### \<body\>

The body of a document contains the document's content. All elements within the `<body>`{:.tag} tag is laid out and rendered by {{page.lib_name}} based on the active style sheets. 