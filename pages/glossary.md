---
layout: page
title: Glossary
---

### Basic Types

* **CDATA** is a sequence of characters from the document character set and may include character entities.
* **ID** tokens must begin with a letter ([A-Za-z]) and may be followed by any number of letters, digits ([0-9]), hyphens ("-"), underscores ("_"), colons (":"), and periods (".").
* **IDREF** and IDREFS are references to ID tokens defined by other attributes. **IDREF** is a single token and **IDREFS** is a space-separated list of tokens.
* **NUMBER** tokens must contain at least one digit ([0-9]).
* **DATASOURCE** is the address of a data source and table. Is in the format "source.table". 

### URI

RmlUi uses URIs as specified by [RFC1630](http://www.w3.org/TR/1999/REC-html401-19991224/references.html#ref-RFC1630).

### Style information

Style sheet data can be the content of the STYLE element and the value of the style attribute. If declared in the STYLE element it is resolved just as if it was an external style sheet. If it is the value of the style attribute then it can only include properties (ie, no rules) and these properties are applied directly to the element in which the attribute is defined.

### Case Information

* **CS** The value is case-sensitive (i.e., user agents interpret "a" and "A" differently).
* **CI** The value is case-insensitive (i.e., user agents interpret "a" and "A" as the same).
* **CN** The value is not subject to case changes, e.g., because it is a number or a character from the document character set.
* **CA** The element or attribute definition itself gives case information.
* **CT** Consult the type definition for details about case-sensitivity.
