---
layout: page
title: HTML4 Style Sheet
parent: rml
next: deprecated
---

This sample style sheet is based on the recommended CSS 2.0 style sheet found [here](http://www.w3.org/TR/REC-CSS2/sample.html). It introduces default rules that we recommend you use as a basis for your own style sheet.

```css
body, div,
h1, h2, h3, h4,
h5, h6, p,
hr, pre, datagrid,
tabset tabs
{
	display: block;
}

h1
{
	font-size: 2em;
	margin: .67em 0;
}

h2
{
	font-size: 1.5em;
	margin: .83em 0;
}

h3
{
	font-size: 1.17em;
	margin: 1em 0;
}

h4, p
{
	margin: 1.33em 0;
}

h5
{
	font-size: .83em;
	line-height: 1.17em;
	margin: 1.67em 0;
}

h6
{
	font-size: .67em;
	margin: 2.33em 0;
}

h1, h2, h3, h4,
h5, h6, strong
{
	font-weight: bold;
}

em
{
	font-style: italic;
}

pre
{
	white-space: pre;
}

hr
{
	border-width: 1px;
}

table
{
	box-sizing: border-box;
	display: table;
}
tr
{
	box-sizing: border-box;
	display: table-row;
}
td
{
	box-sizing: border-box;
	display: table-cell;
}
col
{
	box-sizing: border-box;
	display: table-column;
}
colgroup
{
	display: table-column-group;
}
thead, tbody, tfoot
{
	display: table-row-group;
}
```
