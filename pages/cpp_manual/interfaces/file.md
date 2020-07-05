---
layout: page
title: File interface
parent: cpp_manual/interfaces
grandparent: cpp_manual
next: font_engine
---

The file interface controls how RmlUi opens and reads from files, such as fonts, RCSS and RML files. If you do not install a custom file interface, RmlUi will default to using the standard C file I/O API and attempt to open files from the current working directory. If this is satisfactory for your application you will not need to provide a custom file interface.

The file interface is given in `<RmlUi/Core/FileInterface.h>`{:.incl}. To develop a custom file interface, create a class derived from `Rml::FileInterface` and provide function definitions for the pure virtual functions:

```cpp
// Opens a file.
virtual Rml::FileHandle Open(const Rml::String& path) = 0;

// Closes a previously opened file.
virtual void Close(Rml::FileHandle file) = 0;

// Reads data from a previously opened file.
virtual size_t Read(void* buffer, size_t size, Rml::FileHandle file) = 0;

// Seeks to a point in a previously opened file.
virtual bool Seek(Rml::FileHandle file, long offset, int origin) = 0;

// Returns the current position of the file pointer.
virtual size_t Tell(Rml::FileHandle file) = 0;
```

These function prototypes should be fairly self-explanatory. The `Rml::FileHandle` type that is returned from the `Open()` function, and passed into the other functions, is a void pointer type. This can be any value you need to uniquely identify each opened file, however the NULL (0) value is reserved for the invalid file handle, so make sure you don't use it to represent a valid handle!

`Open()` takes the string value that was given to whatever system is opening the file; this could have been through the font database, a style sheet reference in an RML document, etc. Depending on how you've configured your file interface, it needn't be a file path. The function should return a non-NULL file handle for a successful open, or NULL if the open failed.

RmlUi will call `Close()` when it is done reading from a previously opened file.

The `Read()` function should read size bytes from the file, starting at the current position of the file pointer, into buffer. The actual number of bytes read should be returned, and the file pointer should be incremented by the same.

`Seek()` seeks the file pointer to a given location within the file. The parameters are identical to the C function `fseek()`; origin is one of `SEEK_SET` (the beginning of the file), `SEEK_CUR` (the current position of the file pointer) or `SEEK_END` (the end of the file), and offset is an offset from the origin (measured in bytes). Return false if the seek operation failed for some reason, true otherwise.

`Tell()` should return the position of the file pointer, as an offset in bytes from the origin of the file.
