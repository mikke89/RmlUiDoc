---
layout: page
title: RML Data Display Elements
parent: rml
next: templates
---

See also [data bindings](../data_bindings.html) for dynamically displaying and updating data from the client application.

### \<progressbar\>

The `<progressbar>`{:.tag} element can visually display progress or relative values. For a detailed description see [progress bar]({{"pages/cpp_manual/element_packages/progress_bar.html"|relative_url}}) in the C++ Manual.

_Attributes_

`value`{:.attr} = number (CN)
: A number [0, 1] representing the fraction of the progress bar that is filled and where 1 means completely filled.

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
