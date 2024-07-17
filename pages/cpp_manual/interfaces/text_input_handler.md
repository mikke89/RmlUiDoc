---
layout: page
title: Text input handler interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
---

The text input handler interface, unlike other interfaces, does not hinder the application's functionality without implementation. It listens to events of all editable text areas, such as text field activation, and provides a proxy object to manipulate the text input in question. It is the best entry point for a custom implementation of the [input method editor (IME)](../ime.html).

To handle these events, create a class derived from `Rml::TextInputHandler` (defined in `<RmlUi/Core/TextInputHandler.h>`{:.incl}) and override the abstract methods you are interested in:

```cpp
// Called when a text input area is activated (e.g., focused).
virtual void OnActivate(TextInputContext* input_context) {}

// Called when a text input area is deactivated (e.g., by losing focus).
virtual void OnDeactivate(TextInputContext* input_context) {}

// Invoked when the context of a text input area is destroyed (e.g., when the element is being removed).
virtual void OnDestroy(TextInputContext* input_context) {}
```

Once you complete your implementation, install it globally with `Rml::SetTextInputHandler()` or pass it during context construction to have an instance specific to the created context. Remember that overriding the global handler will not affect already existing contexts.

The class implementing the input handler can then communicate with the input context handed to it. Typically, the implementation of the input context is provided by the library, allowing the user to focus on the IME or other input-related functionality.

### Text input context

A text input context is a proxy class for managing an editable text area. {{ page.lib_name }} implements the `Rml::TextInputContext` interface (defined in `<RmlUi/Core/TextInputContext.h>`{:.incl}) for text field elements, but users of the library may decide to provide a custom implementation with definitions for the pure virtual methods:

```cpp
/// Retrieve the screen-space bounds of the text area (in px).
/// @param[out] out_rectangle The resulting rectangle covering the projected element's box (in px).
/// @return True if the bounds can be successfully retrieved, false otherwise.
virtual bool GetBoundingBox(Rectanglef& out_rectangle) const = 0;

/// Retrieve the selection range.
/// @param[out] start The first character selected.
/// @param[out] end The first character *after* the selection.
virtual void GetSelectionRange(int& start, int& end) const = 0;

/// Select the text in the given character range.
/// @param[in] start The first character to be selected.
/// @param[in] end The first character *after* the selection.
virtual void SetSelectionRange(int start, int end) = 0;

/// Move the cursor caret to after a specific character.
/// @param[in] position The character position after which the cursor should be moved.
virtual void SetCursorPosition(int position) = 0;

/// Replace a text in the given character range.
/// @param[in] text The string to replace the character range with.
/// @param[in] start The first character to be replaced.
/// @param[in] end The first character *after* the range.
/// @note This method does not respect internal restrictions, such as the maximum length.
virtual void SetText(StringView text, int start, int end) = 0;

/// Update the range of the text being composed (for IME).
/// @param[in] start The first character in the range.
/// @param[in] end The first character *after* the range.
virtual void SetCompositionRange(int start, int end) = 0;

/// Commit an composition string (from IME), and respect internal restrictions (e.g., the maximum length).
/// @param[in] composition The string to replace the composition range with.
/// @note If the composition range equals to [0, 0], it takes no action.
virtual void CommitComposition(String composition) = 0;
```

This interface provides means to connect {{ page.lib_name }} with existing game engines for the IME or any other user input-related functionality. The lifetime of an input context instance is ended with the call to `OnDestroy()` in `Rml::TextInputHandler`, the text input handler must ensure not to interact with the same instance after this point.

#### IME Composition

Commonly, while the IME composition is active, the text may ignore internal restrictions, such as the maximum text length, to improve the user experience. `SetText()` is a method that takes the passed text and replaces the character range with it. Once the composition ends, however, the resulting string should be inserted while following the input configuration; this is when `CommitComposition()` should be used. Note that it takes effect only when the composition range is set from `SetCompositionRange()`, which must be executed before modifying the text; text modifications cancel the composition range.

This is an example implementation of a text input method editor using the text input context:

```cpp
class TextInputMethodEditor {
public:
    void SetComposition(Rml::StringView composition);
    void ConfirmComposition(Rml::StringView composition);

private:
    // An actively used text input method context.
    Rml::TextInputContext* input_context;

    // Composition range (character position) relative to the text input value.
    int composition_range_start;
    int composition_range_end;
};

void TextInputMethodEditor::SetComposition(Rml::StringView composition)
{
    // Retrieve the composition range if it is missing.
    if (composition_range_start == 0 && composition_range_end == 0)
        input_context->GetSelectionRange(composition_range_start, composition_range_end);

    // First, modify the text value of the text area to insert the current composition string.
    input_context->SetText(composition, composition_range_start, composition_range_end);

    // Calculate the new end of the composition range, as the string has changed.
    size_t length = Rml::StringUtilities::LengthUTF8(composition);
    composition_range_end = composition_range_start + (int)length;

    // Once we are finished with text modifications, apply the composition range for visual feedback.
    input_context->SetCompositionRange(composition_range_start, composition_range_end);
}

void TextInputMethodEditor::ConfirmComposition(Rml::StringView composition)
{
    // First, set the composition range, which will be used for inserting the composition string.
    input_context->SetCompositionRange(composition_range_start, composition_range_end);
    // Once the range is set, insert the composition string into the text field.
    input_context->CommitComposition(Rml::String(composition));

    // Move the cursor to the end of the string.
    input_context->SetCursorPosition(composition_range_end);

    // End the composition, clean up the state, ...

    // ...
}
```

In a real application, you want to connect the editor to your backend and handle the composition state. See the [platform implementations](https://github.com/mikke89/RmlUi/tree/master/Backends) for detailed examples with ready-to-use text input handlers.
