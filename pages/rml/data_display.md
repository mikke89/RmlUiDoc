---
layout: page
title: RML Data Display Elements
parent: rml
next: templates
---

See also [data bindings](../data_bindings.html) for dynamically displaying and updating data from the client application.

### \<progress\>

The `<progress>`{:.tag} element can display progress bars and gauges. For a detailed description and styling information see the [progress element]({{"pages/cpp_manual/element_packages/progress_bar.html"|relative_url}}) in the C++ Manual.

_Attributes_

`value`{:.attr} = number (CN)
: A number between `0` and `max`, representing the fraction of the progress element that is filled and where `max` means completely filled.

`max`{:.attr} = number (CN)
: A positive number representing the maximum value, defaults to `1`.

`direction`{:.attr} = cdata (CI)
: The direction the progress bar expands with increasing values. Must be one of:
* `top`{:.value}
* `right`{:.value} (default)
* `bottom`{:.value}
* `left`{:.value}
* `clockwise`{:.value}
* `counter-clockwise`{:.value}

`start-edge`{:.attr} = cdata (CI)
: Only applies to `clockwise`{:.value} or `counter-clockwise`{:.value} directions. Defines which edge the
circle should start expanding from. Must be one of:
* `top`{:.value} (default)
* `right`{:.value}
* `bottom`{:.value}
* `left`{:.value}
