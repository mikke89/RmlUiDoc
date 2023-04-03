---
layout: page
title: Initialization and main loop
parent: cpp_manual
next: fonts
---


The following code snippet is a rough template on how you would initialize and run RmlUi within your application or game. Its main purpose is to show the order of API calls to get a basic user interface up and running. More complex topics such as multithreading and separating the update and rendering logic is out of scope for this example.


```cpp
// To ensure fast compilation times, you may want to replace the below "include-all" headers with specific files.
#include <RmlUi/Core.h>
#include <RmlUi/Debugger.h>

class MyRenderInterface : public Rml::RenderInterface
{
	/* ... */
}

class MySystemInterface : public Rml::SystemInterface
{
	/* ... */
}


int main(int argc, char** argv)
{
	// Initialize the window and graphics API being used, along with your game or application.
	
	/* ... */

	// Instantiate the interfaces to RmlUi.
	MyRenderInterface render_interface;
	MySystemInterface system_interface;

	// Begin by installing the custom interfaces.
	Rml::SetRenderInterface(&render_interface);
	Rml::SetSystemInterface(&system_interface);

	// Now we can initialize RmlUi.
	Rml::Initialise();
	
	// Create a context next.
	Rml::Context* context = Rml::CreateContext("main", Rml::Vector2i(window_width, window_height));
	if (!context)
	{
		Rml::Shutdown();
		return -1;
	}

	// If you want to use the debugger, initialize it now.
	Rml::Debugger::Initialise(context);

	// Fonts should be loaded before any documents are loaded.
	Rml::LoadFontFace("my_font_file.otf");

	// Now we are ready to load our document.
	Rml::ElementDocument* document = context->LoadDocument("my_document.rml");
	if (!document)
	{
		Rml::Shutdown();
		return -1;
	}

	document->Show();

	bool exit_application = false;
	while (!exit_application)
	{
		// We assume here that we have some way of updating and retrieving inputs internally.
		my_input->Update();

		if (my_input->KeyPressed(KEY_ESC))
			exit_application = true;

		// Submit input events before the call to Context::Update().
		if (my_input->MouseMoved())
			context->ProcessMouseMove(mouse_pos.x, mouse_pos.y, 0);

		// Toggle the debugger with a key binding.
		if (my_input->KeyPressed(KEY_F8))
			Rml::Debugger::SetVisible(!Rml::Debugger::IsVisible());

		// This is a good place to update your game or application.
		my_application->Update();

		// Update any elements to reflect changed data.
		if (Rml::Element* el = document->GetElementById("score"))
			el->SetInnerRML("Current score: " + my_application->GetScoreAsString());

		// Update the context to reflect any changes resulting from input events, animations, modified and
		// added elements, or changed data in data bindings.
		context->Update();

		// After the context update, the properties and layout of all elements are properly resolved.
		// At this point, we should no longer change any elements, or submit input or other events until
		// after the call to Context::Render().

		// Render your game or application.
		my_application->Render();

		// Set up any rendering states necessary before the render.
		my_renderer->PrepareRenderBuffer();

		// Render the user interface on top of the application.
		context->Render();

		// Present the rendered frame.
		my_renderer->PresentRenderBuffer();
	}

	// Shutting down RmlUi releases all its resources, including elements, documents, and contexts.
	Rml::Shutdown();

	// It is now safe to destroy the custom interfaces previously passed to RmlUi.

	return 0;
}

```

In a real application, you typically want to separate the render and update loops. Regardless, you may consider updating the RmlUi context at the rendering updates, as this provides the lowest input lag which is important to make the user interface feel good.

### On demand rendering
In the graphics world you can roughly divide applications into two groups. On the one hand there are games that aim to spit out as much frames in as little time as possible. On the other extrem are desktop applications that will only redraw parts of the screen if there has been an update to the content.

RmlUi provides a way to allow the application to sleep waiting for events unless there have been changes to the onscreen content. In order to keep breaking changes to a minimum, this feature is not enabled by default and requires explicit support by the code that drives the rendering loop. The feature consists of two functions on the `Context` class, which can be used to manipulate a time value.

`RequestNextUpdate` is used by RmlUi and custom elements to set the delay until the ui should be rendered again, unless user input is received in between. This is not a direct setter, it takes the minimum value of the already stored and the passed in value. The rendering loop can then use `GetNextUpdateDelay` to retrieve the value in the range between 0 and positive infinity. Zero means the rendering loop should not block for events and render the next frame as soon as possible. This usually means some kind of animation is playing. Infinity means there is no reason to redraw the content at all unless a user event is received. This is the usual case if there are no custom elements or running animations. Everything else is a delay in seconds until the update and render loop should be invoked again.

You can see this in action by tweaking the `power_save` flag passed to `Backend::Process` function in the provided samples. With the exception of SFML, it is implemented for all supported backends.