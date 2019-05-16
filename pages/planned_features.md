---
layout: page
title: Planned Features
---

Based on current [discussions]({{page.lib_site}}/issues/), the following are planned features for {{page.lib_name}}.

### Sooner

* Increase performance ([#8]({{page.lib_site}}/issues/8))
* Revamp the font provider interface to make it more flexbile ([#10]({{page.lib_site}}/issues/10))

### Later

* Make contexts thread safe, so each context can run in its own thread without affecting the other 
* Make the STL configurable (this is important for Custom Memory Allocators later too) 
* Add support to render a document to texture
* Send all allocs and frees through the SystemInterface, allowing developers to manage memory better
* Investigate switching the XML parser to RapidXML for speed

### Some Day

* Address the global element transparency issues. Some elements don't currently support transparency, due to HTML spec, but I think its worth coming up with a way to allow this.

