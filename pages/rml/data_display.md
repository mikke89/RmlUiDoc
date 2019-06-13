---
layout: page
title: RML Data Display Elements
parent: rml
next: templates
---

### \<datagrid\>

`<datagrid>`{:.tag} represents an element capable of fetching, positioning and rendering dynamic tabulated data. For a detailed description see [Data grid]({{"pages/cpp_manual/controls/data_grid.html"|relative_url}}) in the C++ Manual.

Supported when the [Controls plugin]({{"pages/cpp_manual/controls.html"|relative_url}}) is used.

_Attributes_

`source`{:.attr} = datasource (CS)
: The name of the data source and table that the rows of the data grid will be fetched from.

#### \<col\>

The `<col>`{:.tag} element represents a column in the datagrid. Each column displays information about each row in the data source in the form of one or more fields.

_Attributes_

`fields`{:.attr}  = cdata (CS)
: A comma-separated list of fields that this column will fetch from the data source about each row and display.

`formatter`{:.attr} = cdata (CS)
: The name of the data formatter to use to turn the raw field information into RML. If not set (or the formatter can't be found) then the raw text will be displayed.

`width`{:.attr} = number (CN)
: The width (in px or %) of the column.

### \<dataselect\>

The `<dataselect>`{:.tag} element is described in the [Forms](forms.html#dataselect) section.
