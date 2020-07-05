---
layout: page
title: System interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
next: render
---

The system interface is needed for RmlUi to tell the time, and allows the application to perform common tasks such as logging messages from RmlUi, translating strings, and setting the mouse cursor. A system interface is necessary, however the only function you need to define is `GetElapsedTime()`.

The system interface is given in `<RmlUi/Core/SystemInterface.h>`{:.incl}. To develop a custom system interface, create a class derived from `Rml::SystemInterface` and provide function definitions for the one pure virtual function:

```cpp
// Get the number of seconds elapsed since the start of the application.
virtual double GetElapsedTime() = 0;
```

Provide function definitions for the other virtual functions if required, the most common ones being:

```cpp
// Translate the input string into the translated string.
virtual int TranslateString(Rml::String& translated, const Rml::String& input);

// Log the specified message.
virtual bool LogMessage(Rml::Log::Type type, const Rml::String& message);

// Set the mouse cursor.
virtual void SetMouseCursor(const Rml::String& cursor_name);
```

The `GetElapsedTime()` function should simply return the number of seconds that have elapsed since the start of the application.

`TranslateString()` is called when a text element is constructed from an RML stream. This allows the application to send all text read from file through its string tables. The parameter `input` is the raw text read from the RML, while `translated` should be set to the final text to be given to the text element to render. The total number of changes made to the raw text should be returned. If the number is greater than 0, RmlUi will recursively call your translate function to process any new text that was added to the stream (watch out for infinite recursion). If your translation function does all the recursion itself, you can safely return 0 on every call.

Note that the translated text can include RML tags and they will be processed as if they were in the original stream; this can be used, for example, to substitute images for certain tokens.

The `LogMessage()` function is called when RmlUi generates a message. Here, `type` is one of `Rml::Log::ERROR` for error messages, `Rml::Log::ASSERT` for failed internal assertions (debug library only), `Rml::Log::WARNING` for non-fatal warnings, or `Rml::Log::INFO` for generic information messages. The `message` parameter is the actual message itself. The function should return true if program execution should continue, or false to generate an interrupt to break execution. This can be useful if you are running inside a debugger to see exactly what an application is doing to trigger a certain message.

The `SetMouseCursor()` function is called when RmlUi wants to change the mouse cursor. This behavior is controlled by the [`cursor`{:.prop} property](../../rcss/user_interface.html#mouse-cursor-the-cursor-property), the value of which is directly sent through the interface as the `cursor_name`. The user is responsible for setting the system cursor or otherwise rendering the cursor as desired. The default value for the `cursor`{:.prop} property is an empty string, thus, this can be used to set a default cursor. It is possible to choose for each context whether it should call this function, see [context cursor](../contexts.html#mouse-cursor) for additional details.
