---
layout: page
title: Planned Features
---

Have a look at the [discussions]({{page.lib_site}}/issues/) on GitHub for the main features being worked on or considered. Some long-term plans for RmlUi are listed here.

### Long-term features considered

* Make contexts thread safe, so each context can run in its own thread without affecting the other 
* Add support to render a document to texture
* Make the STL configurable (this is important for Custom Memory Allocators later too) 
* Send all allocs and frees through the SystemInterface, allowing developers to manage memory better
* Investigate switching the XML parser to RapidXML for speed
