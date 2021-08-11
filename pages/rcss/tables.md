---
layout: page
title: Tables
parent: rcss
next: user_interface
---

Table support in RCSS is similar to that of the [CSS tables specifiation](https://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html). There are some enhancements and differences, the main ones being as follows.

##### Enhancements

- The width of columns and height of rows support flexible sizing (like using the CSS `fr` unit for grid layout).
- Minimum and maximum size constraints are respected for column widths and row heights.
- Spacing between rows and between columns can be controlled individually using margin, border and padding.

##### Differences

- The width of columns are computed as if setting the CSS property `table-layout: fixed`{:.prop}, with the above enhancements.
- RmlUi does not generate anonymous elements or attempt to clean up invalid tables.
  - Table row elements must be present for borders to be generated as specified for the row.
  - Table cells will not inherit any properties from the column elements they belong to, except for adjusting the width.
- Percentage-relative values are calculated based on the initial block-size of the table element, and are not re-adjusted if the table size is changed during formatting.

### The RCSS table model

The RCSS table model follows the structure of CSS tables. This means that the table is made up of table rows, optionally wrapped in row groups, which contain individual cells. Table columns and column groups can optionally be specified for visual effects (mainly backgrounds, borders, and decorators) and for defining widths of columns. Columns never contain cells directly. Table columns and column groups must precede any rows or row groups. Table cells can be placed as direct children of the table, then consecutive cells will form a new row.

The `display`{:.prop} property is used to define the formatting of tables, with the following relevant values.

`display`{:.prop} value       | Description | Attributes | Valid children
----------------------------- | ----------- | ---------- | --------------
`table`{:.value}              | Specifies a block-level table.         | | `table-row`{:.value}, `table-row-group`{:.value},<br>`table-column`{:.value}, `table-column-group`{:.value},<br>`table-cell`{:.value}
`table-row`{:.value}          | Specifies a table row.                 | | `table-cell`{:.value}
`table-row-group`{:.value}    | Specifies a grouping of table rows.    | | `table-row`{:.value}
`table-column`{:.value}       | Specifies a table column.              | `span`{:.value} | 
`table-column-group`{:.value} | Specifies a grouping of table columns. | `span`{:.value} (when no children present) | `table-column`{:.value}
`table-cell`{:.value}         | Specifies a table cell.                | `colspan`{:.value}, `rowspan`{:.value} |

In particular, the following CSS `display`{:.prop} modes are *not* supported: `inline-table`{:.value}, `table-header-group`{:.value}, `table-footer-group`{:.value}, `table-caption`{:.value}.


#### Example

The following example demonstrates a table with grouped rows and columns, using all the table display modes.

```html
<table>
	<col/>
	<colgroup>
		<col span="2"/>
		<col/>
	</colgroup>
	<thead>
		<tr>
			<td>Name</td>
			<td colspan="2">Items</td>
			<td>Age</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Gimli</td>
			<td>Helmet</td>
			<td>Axe</td>
			<td>139 years</td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<td colspan="4">Footnote</td>
		</tr>
	</tfoot>
</table>
```

This example assumes that the recommended stylesheet below is applied.


#### Recommended stylesheet

Unlike in HTML, the `table`{:.tag} element or any of the other table tags do not have any special meaning in RmlUi. Instead, they will be derived entirely from their RCSS properties. Furthermore, RmlUi does not contain a default stylesheet, thus, the RCSS properties for tables must first be declared. The following RCSS properties are recommended for declaring tables with the tags known from HTML.


```css
table {
	box-sizing: border-box;
	display: table;
}
tr {
	box-sizing: border-box;
	display: table-row;
}
td {
	box-sizing: border-box;
	display: table-cell;
}
col {
	box-sizing: border-box;
	display: table-column;
}
colgroup {
	display: table-column-group;
}
thead, tbody, tfoot {
	display: table-row-group;
}
```

### Visual layout of tables

Table elements are rendered in the following order, from bottom to top:

1. Table
2. Column groups
3. Columns
4. Row groups
5. Rows
6. Cells

Column groups and column elements are sized to cover the table columns they are spanning. Row groups are sized to cover the rows they are spanning. This way, backgrounds, borders, and decorators can be used on these elements, and will be visible if cells and rows have transparent backgrounds.


#### Table width algorithm

The table width is the sum of all table columns and the horizontal table spacing, such as `column-gap`{:.prop}, column margins, and table padding.

The width of table columns are defined entirely by the width specified on column elements and/or the cells of the first row. In the following, *columns* mean any of the aforementioned elements.

- Columns with `width: auto`{:.prop} are distributed equally to fill the table width.
- Columns with `width: <length> | <percentage < 100%>`{:.prop} will use the specified value.
- Columns with `width: <percentage ≥ 100%>`{:.prop} adjusts the flexible width of the column relative to other flexible columns (like the CSS `fr` unit for grid layout).
- Columns can specify `min-width`{:.prop} and `max-width`{:.prop} to constraint their sizing.

Unlike in CSS, column groups and columns can use horizontal `padding`{:.prop}, `border`{:.prop} and `margin`{:.prop}. This will be added to the horizontal spacing of the table. Column groups and columns can also use vertical `border`{:.prop} and `margin`{:.prop} to add borders and offset them from the table edges, but will not affect the position of the cells.


#### Table height algorithm

The table height is determined by the sum of the height of all its rows, in addition to vertical spacing such as `row-gap`{:.prop}, row margins, and table padding.

Each row has their height determined as follows:

- Rows with `height: auto`{:.prop} determine their height by the tallest formatted cell in the row.
- Rows with `height: <length> | <percentage < 100%>`{:.prop} will use the specified value.
- Rows with `height: <percentage ≥ 100%>`{:.prop} adjusts the flexible height of the row relative to other flexible rows (like the CSS `fr` unit for grid layout).
- Rows can specify `min-height`{:.prop} and `max-height`{:.prop} to constraint their sizing.

If the rows do not fill the height specified on the table, all rows will be scaled up proportionally while respecting any `max-height`{:.prop} constraints. If there is still space available, empty space will be left at the bottom of the table.

All percentage values are resolved using the initial block height of the table. Thus, if the table height is specified as `auto`{:.value}, they will resolve to zero. Instead, the table height should be set to a specific length. Percentage heights can also be used if the parent element's height is specified.

Unlike in CSS, row groups and rows can use vertical `padding`{:.prop}, `border`{:.prop} and `margin`{:.prop}. This will be added to the vertical spacing of the table. Row groups and rows can also use horizontal `border`{:.prop} and `margin`{:.prop} to add borders and offset them from the table edges, but will not affect the position of the cells.

`vertical-align`{:.prop}

When used on a table cell, this property has the following meaning.

`top`{:.value} (*default*)
: Aligns the table cell with the top of the first row it spans.

`bottom`{:.value}
: Aligns the table cell with the bottom of the last row it spans.

`middle`{:.value}
: Aligns the table cell with the middle of the rows it spans.

*other*{:.value}
:  Other values have no meaning in this context and defaults to `top`{:.value}.

The alignment is done by adding top or bottom padding to the cell element. Unlike in CSS, `baseline`{:.value} is currently not supported.


### Borders

The model for setting borders on tables in RCSS is similar to the separated borders model in CSS (`border-collapse: separate`{:.value}).

That is, each cell element control their own borders separately.

However, unlike CSS, borders can still be added to rows, row groups, columns, and column groups. They will be separated from the cell borders, as if extending the borders of their inner elements.


#### Cell spacing
{:#gap}

`row-gap`{:.prop}, `column-gap`{:.prop}

Value: | \<length\> \| \<percentage\>
Initial: | 0px
Applies to: | `table`{:.value} elements
Inherited: | no
Percentages: | relative to the height and width, respectively, of the initial table block size

Specifies the gap *between* table cells. Like the CSS property `border-spacing`{:.prop}, except that spacing is not applied before and after the first and last cell, respectively. Instead, use `padding`{:.prop} on the table element to add spacing between the table border and its cells.

`gap`{:.prop}

A shorthand property for setting both `row-gap`{:.prop} and `column-gap`{:.prop} properties, in that order. If only a single value is specified, it sets both gap properties to the given value.
