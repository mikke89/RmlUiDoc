---
layout: page
title: Troubleshooting
parent: cpp_manual
next: elements
---

Sometimes challenges arise when integrating a new library. The most common integration issues in RmlUi are related to initialization, lifetimes, and the rendering API, but there may be other culprits. Here are some things to try if something goes wrong or it doesn't render properly.

***The first thing you should do:***

- Check the log output for any warnings or errors.
- Make sure you are actually getting the log output.
  - Try calling `Rml::Log::Message(Rml::Log::LT_WARNING, "Test warning.")` just after installing the system interface to make sure.

#### Application crash

- Make sure everything is initialized in the correct order, see [initialization and main loop](main_loop.html) for details.
- Make sure your [custom interfaces](interfaces.html) are kept alive until after the call to `Rml::Shutdown()`.
- When you call `ElementDocument::Close()`, make sure event listeners attached to any element of the document are kept alive until the next call to `Context::Update()` or `Rml::Shutdown()`.

#### Rendering issues

- Carefully read the [rendering conventions](interfaces/render.html#rendering-conventions) and assumptions used in RmlUi. It describes some hints for usage with graphics APIs such as OpenGL and DirectX.
- Make sure the fonts are loaded, the log output prints some info whenever a font is loaded.
- Don't just rely on font rendering in the document being tested. Try creating a sized `div` element with a colored background in case there are any problems with the fonts, see the example document below.
- Make sure inputs are submitted before the call to `Context::Update`.
- Make sure you call `Context::Update` and then `Context::Render` (in that order).
- If you have trouble loading your own fonts, you can instead test with the font included with the debugger. To use it, `RmlDebugger` must be linked and initialized, then set the property `font-family: rmlui-debugger-font;` on a given element.

#### Animation issues

Experiencing slow, fast, or non-smooth animations?

- Make sure `SystemInterface::GetElapsedTime()` is properly implemented. It should return a high-resolution time value in seconds, always increasing as the application runs.

Nothing solves your problem? Take a look at the included samples and shell to see how they work. You can also write a post describing your situation in the [main repository]({{page.lib_site}}), or talk to other users on [RmlUi's Gitter channel](https://gitter.im/RmlUi/community).


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
