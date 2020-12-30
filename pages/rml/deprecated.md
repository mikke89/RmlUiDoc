---
layout: page
title: Deprecated RML Elements
parent: rml
status: deprecated
---

### \<datagrid\>

> ***Deprecated*** in favor of [data bindings](../data_bindings.html) possibly combined with [RCSS tables](../rcss/tables.html).

`<datagrid>`{:.tag} represents an element capable of fetching, positioning and rendering dynamic tabulated data. For a detailed description see [Data grid]({{"pages/cpp_manual/element_packages/data_grid.html"|relative_url}}) in the C++ Manual.

_Attributes_

`source`{:.attr} = datasource (CS)
: The name of the data source and table that the rows of the data grid will be fetched from.

#### \<col\>

> ***Deprecated*** in favor of [data bindings](../data_bindings.html) possibly combined with [RCSS tables](../rcss/tables.html).

The `<col>`{:.tag} element represents a column in the datagrid. Each column displays information about each row in the data source in the form of one or more fields.

_Attributes_

`fields`{:.attr}  = cdata (CS)
: A comma-separated list of fields that this column will fetch from the data source about each row and display.

`formatter`{:.attr} = cdata (CS)
: The name of the data formatter to use to turn the raw field information into RML. If not set (or the formatter can't be found) then the raw text will be displayed.

`width`{:.attr} = number (CN)
: The width (in px or %) of the column.

#### \<dataselect\>

> ***Deprecated*** in favor of [data bindings](../data_bindings.html).

_Attributes_

`source`{:.attr} = datasource (CS)
: The data source to read the options from.

`fields`{:.attr} = cdata (CS)
: A comma-separated list of fields to fetch from the data source and to display for each option (or optionally to be sent through the data formatter)

`valuefield`{:.attr} = cdata (CS)
: The field from the data source to use as the option's value. If not set, then the first field in the fields attribute is used.

`formatter`{:.attr} = cdata (CS)
: The name of the dataformatter to use to process the raw fields information into RML. If not set, then the fields are displayed in raw text.
