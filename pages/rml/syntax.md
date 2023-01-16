---
layout: page
title: RML Syntax
parent: rml
next: events
---

RML generally follows the [XML syntax](https://html.spec.whatwg.org/multipage/xhtml.html) for HTML. In particular this means that *all tags* must be closed. Further, it is assumed that documents are encoded in UTF-8. XML namespaces are not supported.

RML documents consist of a tree of nodes, see the [documents](documents.html) page for their general structure. The following describes some features beyond the common tree parsing behavior. For the most part, the syntax is equivalent to a subset of XML and HTML, with some additions.


### Character references

RML supports character references in attributes and in data (text) encountered inside tags. When encountered, they will be translated into the specified Unicode code point.

#### Named character references

| Escape string |  Character           |
|---------------|--------------------  |
| `&lt;`        | `<`                  |
| `&gt;`        | `>`                  |
| `&quot;`      | `"`                  |
| `&amp;`       | `&`                  |
| `&nbsp;`      | *Non-breaking space* |

#### Numerical character references

Characters can be specified numerically based on their Unicode code points, just like in HTML.

| Escape format |  Description |
| ------------- |  ----------- |
| `&#nnnn;`     | Unicode code point specified in decimal form `nnnn`. |
| `&#xhhhh;`    | Unicode code point specified in hexadecimal form `hhhh`. |

For example, the euro sign € can be written using decimal form `&#8364;` or equivalently in hexadecimal form `&#x20ac;`.


### Comments

Comments are supported using the familiar format.

```html
<!-- My comment -->
```

Comments can also include tags, which will be ignored.


### CData sections

CData sections can be used to include text that should not be parsed as RML. The section is started by `<![CDATA[`, followed by some data, and finally ended by `]]>`.

**Example**
```html
<p>A strange face appeared:
<![CDATA[
	'</"O"--"O"\>' 
]]></p>
```


### CData tags

When a CData tag is encountered in a document, all subsequent text is considered raw data until its end tag is encountered.

|   CData tags  |
| ------------- |
| `<style>`{:.tag}     |
| `<script>`{:.tag}    |


### Structural data attributes

When a node with a structural data attribute is encountered, then all descendant RML nodes and data will be treated as a single data child of the structural node.

| Structural data attributes  |
| --------------------------  |
| `data-for`{:.attr}          |

Note that a valid subtree is still required, and that the subtree will be considered when finding the node's end tag.

##### Example

{% raw %}

In the following, [data bindings](../data_bindings.html) are used to dynamically display a list of elements. During RML parsing, only a single node is created, for the `div`{:.tag} tag. All its inner contents, including the `h1`{:.tag} and `p`{:.tag} tags, are submitted as a single data child.

```html
<div data-for="invader : invaders">
	<h1>{{ invader.name }}</h1>
	<p>Invader {{it_index + 1}} of {{ invaders.size }}.</p>
</div> 
```

This allows the `data-for` view to store its inner contents without generating them immediately, so that it can later dynamically create a list of the provided elements as needed.

{% endraw %}
