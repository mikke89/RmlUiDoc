---
layout: page
title: Localisation
---

While RmlUi fully supports localisation, there are a number of issues you will need to be aware of.

### String encoding

RmlUi assumes all data it is given, whether read in from RML or provided procedurally, is in UTF-8 encoding. This means if you're using 8-bit ASCII you don't need to change anything, but allows you to specify multi-byte Unicode characters if required.

### Translation

All raw text that RmlUi reads while parsing RML (i.e., everything other than XML tags) is sent through the `TranslateString()` function on the [system interface](cpp_manual/interfaces.html#the-system-interface). The function is given the raw string as read, and the application can make any modifications necessary before returning the translated string (and the number of substitutions made) back to RmlUi.

A pass-through translator would do the following:

```cpp
#include <RmlUi/Core/SystemInterface.h>

class SampleSystemInterface : public Rml::SystemInterface
{
	int TranslateString(Rml::String& translated, const Rml::String& input)
	{
		translated = input;
		return 0;
	}
```

#### String tables

The `TranslateString()` method can be used in conjunction with an application's string table to make text substitutions on a document's text. For example, take the pause.rml file in the _Rocket Invaders_ sample:

```html
<rml>
	<head>
		<title>Quit?</title>
	</head>
	<body>
		<p>Are you sure you want to end this game?</p>
		<button>Yes</button>
		<button>No!</button>
	</body>
</rml>
```

If we were to localise _Rocket Invaders_, we'd want to move all of the English strings out from the RML and into a string table. The raw text in the RML would then be replaced with the string table tokens:

```html
<rml>
	<head>
		<title>[QUIT_TITLE]</title>
	</head>
	<body>
		<p>[QUIT_CONFIRM]</p>
		<button>[CONFIRM]</button>
		<button>[DENY]</button>
	</body>
</rml>
```

Assuming the appliation has a `StringTable` class that has loaded the appropriate string table for the language, our sample translator would then become:

```cpp
	int TranslateString(Rml::String& translated, const Rml::String& input)
	{
		// Attempt to find the translation in the string table.
		if (StringTable::GetString(translated, input))
			return 1;

		// No translation; return the raw input string.
		translated = input;
		return 0;
	}
```

Now the strings will be valid for whatever language we specify a string table for. In practice, you might need a more sophisticated translator that could replace multiple tokens within a string.

Note that you can place RML into the translated string, and it will be parsed appropriately. For example, you could replace a token with an `<img>`{:.tag} tag to render an icon for a controller button.
