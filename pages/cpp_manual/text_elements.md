---
layout: page
title: Text Elements
parent: cpp_manual
next: scrollbars
---

{{page.lib_name}} uses text elements (elements derived from `{{page.lib_ns}}::Core::ElementText`) to store and render loose text. Text elements are generated automatically for text in RML documents, and can be created dynamically by using the '#text' element instancer through the {{page.lib_name}} factory, or through the `CreateTextNode()` function on a document.

### Text encoding

The string type used through the majority of {{page.lib_name}}'s interfaces, `{{page.lib_ns}}::Core::String`, stores 8-bit wide characters. In order to store wider characters efficiently, text elements store their contents as a `{{page.lib_ns}}::Core::String` type. The {{page.lib_name}} string stores 16-bit wide characters in UCS-2 format; while not sufficient to store every possible UTF-8 character, it can store every useful one, so is a good compromise between size and usefulness.

### HTML characters

{{page.lib_name}} text nodes support a subset of the full HTML-encoding for special characters to allow XML characters to be present in loose text. The characters supported are:

* `&lt;`{:.value} The less-than symbol, '<'.
* `&gt;`{:.value} The greater-than symbol, '>'.
* `&amp;`{:.value} The ampersand symbol, '&'.
* `&nbsp;`{:.value} A non-breaking space. 

You should use these symbols instead of their literal equivalents when putting them into RML. For example, the following RML fragment will most likely generate a parse error:

```html
<p>You shouldn't use < or > characters in loose text.</p>
```

The following fragment puts the characters in correctly:

```html
<p>You shouldn't use &lt; or &gt; characters in loose text.</p>
```

### Setting an element's text

The `SetText()` function on a `{{page.lib_ns}}::Core::ElementText` will change the text on the text element to a new string.

```cpp
// Sets the raw string this text element contains.
// @param[in] text The new string to set on this element.
void SetText(const {{page.lib_ns}}::Core::String& text);
```

If you pass in a constant string or an `{{page.lib_ns}}::Core::String`, it will be converted to a {{page.lib_name}} string as described above (interpreted as UTF-8 encoding). This means it will interpret standard ASCII characters OK.

Note that this sets the raw text on the element; the actual rendered text may differ due to whitespace processing.

### Retrieving an element's text

The `GetText()` function will return the element's raw text.

```cpp
// Returns the raw string this text element contains.
// @return This element's raw text.
const {{page.lib_ns}}::Core::String& GetText() const;
```

This will return the raw text as a UCS-2 encoded {{page.lib_name}} string. To convert the string to a UTF-8 encoded string, call `ToUTF8()` on the string.

```cpp
{{page.lib_ns}}::Core::String utf8_string;
element_text->GetText().ToUTF8(utf8_string);
```

### String generation

Text elements are capable of generating formatted sub-sections of their content. This is generally only required by custom elements placing text internally; see the section on hidden elements for more information. 