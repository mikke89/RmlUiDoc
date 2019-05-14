---
layout: page
title: Python Event Tutorial
---

The Python interface to {{page.lib_name}} exposes a DOM API in a very similar way to Javascript. Python code can be attached to any event in the RML definition which in turn can dynamically update any part of the document, including opening new documents. Full source code to the final PyInvaders application can be found in the samples folder once the Python plugin has been installed.

### Step 1: Setting up the Python environment

Make sure you've got the required Python support packages installed. For more information, see [this page](../python_manual/overview.html).

The first thing we need to do is initialise Python in our application. Once we have done this we can start executing scripts. We're going to make a PythonInterface class that will hide all the Python intricacies.

```cpp
/**
	Creates and maintains the Python interface to Invaders.
 */

class PythonInterface
{
public:
    static bool Initialise();
    static void Shutdown();

private:
    PythonInterface();
    ~PythonInterface();
};
```

We then implement these methods.

*NOTE: Its a good idea to forcibly import the {{page.lib_name}} Python module. This ensures all Boost bindings have been done and that you can proceed to expose your own classes that rely on these bindings having taken place.*

*NOTE: For more information Python initialisation and shutdown please see the Python documentation at http://docs.python.org*

```cpp
bool PythonInterface::Initialise()
{
    Py_Initialize();

    // Pull in the Rocket Python module.
    Py_XDECREF(PyImport_ImportModule("rocket"));
    return true;
}

void PythonInterface::Shutdown()
{
    Py_Finalize();
}
```

PythonInterface::Initialise should be called before {{page.lib_name}} is initialised. This ensures the Python bindings are available when {{page.lib_name}} starts up.

PythonInterface::Shutdown should be called after you've released all contexts but before you call `{{page.lib_ns}}::Shutdown()`. This ensures all Python objects are released before {{page.lib_name}} does its final cleanup.

At this point you'll need to add the relevant Python and Boost::Python build paths to your project and then compile and link your project.

### Step 2: Replacing the Event System

We can now completely remove the existing event system from RocketInvaders as the Python bindings will do all the event management for us. Remove all source and header files that begin with Event. You'll also need to comment out some code in `GameElement.cpp`{:.path} and `Game.cpp`{:.path} that call the `EventManager` directly. We'll get back to those later.

Also remove all the EventManager initialisation from `main.cpp`{:.path} as we'll replace it with a new Python script. I suggest you name it autoexec.py and place it in a python subfolder. It should look something like this:

```python
import rocket

context = rocket.GetContext('main')
context.LoadDocument('data/background.rml').Show()
context.LoadDocument('data/main_menu.rml').Show()
```

To run this script, we simply need to import it at application start up. Add an import helper to the `PythonInterface` and call it just before the main shell loop.

```cpp
bool PythonInterface::Import(const {{page.lib_ns}}::Core::String& name)
{
    PyObject* module = PyImport_ImportModule(name.CString());
    if (!module)
    {
        PyErr_Print();
        return false;
    }

    Py_DECREF(module);
    return true;
}

```

```cpp
PythonInterface::Import("autoexec");
Shell::EventLoop(GameLoop);
```

At this point the RocketInvaders will now run, however you'll get a script import error because autoexec cannot be found. To fix this we'll need to add the python folder to our Python search path.

*NOTE: On Windows this error will go to stdout, which will not be visible. I suggest you grab a copy of DoAllocConsole() from the pyinvaders sample and drop it into your project. Call DoAllocConsole() at the start of your main function and you'll get a console for reading Python error messages.*

My `PythonInterface::Initialise()` now looks like this:

```cpp
bool PythonInterface::Initialise()
{
	// Initialise Python.
	Py_Initialize();

	// Setup the Python search path.
	const char* python_path = Py_GetPath();
	char buffer[1024];
	snprintf(buffer, 1024, "../Samples/invaders/python;%s", python_path);
	buffer[1023] = '\0';
	PySys_SetPath(buffer);

	// Import Rocket.
	if (!Import("rocket"))
		return false;

	return true;
}
```

This will get us further, you should see the main menu load, however you'll notice a Python error on your console when Python attempts to execute the old onload event in mainmenu.rml. Update the onload and onunload events to use Python script which will correctly display and hide the logo.

```html
<body template="window" onload="document.context.LoadDocument('data/logo.rml').Show()" onunload="document.context.logo.Close()">
```

You will now have to go through each event defined in RML updating it with equivalent Python calls.

RocketPython parses any semi-colons in an event as a delimiter. So you can place multiple Python statements on a single line, semi-colon separated. This comes in useful when you want to execute two statements at once, for example you probably want to do the following for the Start Game button.

```
document.context.LoadDocument('data/start_game.rml').Show(); document.Close()
```

I've simplified this further by by placing a `LoadMenu()` function in the shared template `window.rml`{:.path}, that loads a new document, closing the existing one.

### Step 3: Exposing Game Functions

The above takes care of most of the menu flow, except for a couple items, including the starting of the actual game and exiting. Lets tackle exiting first as that the easier of the two.

Our Python interface class will now have to expose a Python module (with the help of boost::python - *for full documentation see http://www.boost.org*).

```cpp
BOOST_PYTHON_MODULE(game)
{
    python::def("Shutdown", &Shell::RequestExit);
}
```

This creates a module called game and places a Shutdown method within it. We now update the Initialise function to initialise this module at startup.

```cpp
bool PythonInterface::Initialise()
{
    // Initialise python
    Py_Initialize();

    // Setup the Python search path.
    const char* python_path = Py_GetPath();
    char buffer[1024];
    snprintf(buffer, 1024, "../Samples/invaders/python;%s", python_path);
    buffer[1023] = '\0';
    PySys_SetPath(buffer);

    // Import Rocket
    if (!Import("rocket"))
        return false;

    // Define our game specific interface
    initgame();

    return true;
}
```

We can now call the `Shutdown()` function from `main_menu.rml`{:.path} as follows

```html
<button onclick="import game;game.Shutdown()">Exit</button>
```

If you have a lot of functions that call game, you can place the import game in the document header, or in one of your template files.

Using the above code we can extrapolate this throughout the game and have a complete functioning menu system. You will however need to expose more of the `GameDetails` class to Python so that the start_game screen can save the difficulty and colour selection.

Your game module should look something like this:

```cpp
BOOST_PYTHON_MODULE(game)
{
    python::def("Shutdown", &Shell::RequestExit);
    python::def("SetPaused", &GameDetails::SetPaused);
    python::def("SetDifficulty", &GameDetails::SetDifficulty);
    python::def("SetDefenderColour", &GameDetails::SetDefenderColour);

    python::enum_<GameDetails::Difficulty>("difficulty")
        .value("HARD", GameDetails::HARD)
        .value("EASY", GameDetails::EASY)
    ;
}
```

### Step 4: Custom Elements

The next problem we'll hit when converting `RocketInvaders` is the `ElementGame` does not have a Python interface. Thus we can't give it focus when we start the game which means the defender cannot be moved until the user clicks the game with the mouse. To fix this, we need to define ElementGame to Python and register the Python instancer with {{page.lib_ns}}::Factory instead of the C++ instancer.

Let's define a static method on `ElementGame` to do this and call it from our game module's initialisation.

```cpp
void ElementGame::InitialisePythonInterface()
{
    PyObject* object = python::class_<ElementGame, 
                                      {{page.lib_ns}}::Core::Python::ElementWrapper<ElementGame>,
                                      python::bases<{{page.lib_ns}}::Core::Element>, 
                                      boost::noncopyable >("ElementGame", python::init<const char*>())
    .ptr();

    {{page.lib_ns}}::Core::Factory::RegisterElementInstancer("game", 
                                                    new {{page.lib_ns}}::Core::Python::ElementInstancer(object))->RemoveReference();
}
```

### Step 5: Key and end game bindings

We can now get into the game, however the game will never finish as there's no key bindings for processing the ESCAPE key and nothing will make the game exit when the game is over. Fixing the key binding is easy, simply drop in a `onkeydown`{:.evt} handler and make it launch the pause menu.

The game over event is a bit more tricky, as the old Invaders would call `EventManager::LoadWindow()` directly from C++. We're going to have to add a game_over flag to game and make the GameElement check this state every update and fire a custom `gameover`{:.evt} event.

```cpp
// Updates the game.
void ElementGame::OnUpdate()
{
	game->Update();

	if (game->IsGameOver())
		DispatchEvent("gameover", {{page.lib_ns}}::Core::Dictionary(), false);
}
```

### Step 6: Python Data Formatters

We're still using C++ data formatters for the high scores, these can be moved into Python for simplicity.

Here's my name formatter:

```python
class NameDataFormatter(rocket.DataFormatter):
    def __init__(self):
        rocket.DataFormatter.__init__(self, "name")
		
    def FormatData(self, raw_data):
	""" 
        Data format:
        raw_data[0] is the name.
        raw_data[1] is a bool - True means the name has to be entered. False means the name has been entered already.
        """
		
        formatted_data = ""

        if (raw_data[1] == "1"):
            formatted_data = "<input id=\"player_input\" type=\"text\" name=\"name\" onchange=\"game.SetHighScoreName(event.value)\" />"
        else:
            formatted_data = raw_data[0]
			
        return formatted_data
```

A lot more code could be moved from C++ into Python, for example the HighScore system. Its just a matter of taking the principles described here and applying them. 