---
layout: page
title: Troubleshooting
parent: cpp_manual
next: elements
---

Sometimes things go wrong when implementing a new interface. The most common reasons are usually related to the rendering API, but there may be other culprits. Here are some things to try if something doesn't properly render, or something else goes wrong.

- Check the log output for any warnings or errors.
- Make sure you are actually getting the log output.
  - Try calling `Rml::Log::Message(Rml::Log::LT_WARNING, "Test warning.")` just after installing the system interface to make sure.
- Carefully read the [rendering conventions](interfaces/render.html#rendering-conventions) and assumptions used in RmlUi. It describes some hints for usage with graphics APIs such as OpenGL and DirectX.
- Make sure the fonts are loaded, the log output prints some info whenever a font is loaded.
- Don't just rely on font rendering in the document being tested. Try creating a sized `div` element with a colored background in case there are any problems with the fonts, see the example document below.
- Make sure you call `Context::Update` and then `Context::Render` (in that order).
- Make sure inputs are submitted before the call to `Context::Update`.
- If you have trouble loading your own fonts, you can instead test with the font included with the debugger. To use it, `RmlDebugger` must be linked and initialized, then set the property `font-family: rmlui-debugger-font;` on a given element.
- Take a look at the included samples and shell to see how they work.

Nothing solves your problem? Try posting an issue describing your situation in the [main repository]({{page.lib_site}}), or talk to other users on [RmlUi's Gitter channel](https://gitter.im/RmlUi/community).


#### Simple document

The following very simple document can serve as a test to see that you get some render calls through the render interface.

```html
<rml>
<head>
<title>Example</title>
<style>
	body
	{
		position: absolute;
		top: 50px;
		left: 50px;
		width: 500px;
		height: 500px;
		background-color: #ccc;
	}
	div
	{
		display: block;
		height: 150px;
		width: 200px; 
		background-color: #f00;
	}
</style>
</head>
<body>
	<div/>
</body>
</rml>
```
