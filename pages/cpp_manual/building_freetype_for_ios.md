---
layout: page
title: Building FreeType for iOS
parent: cpp_manual
status: review
status-desc: Not tested, help wanted for testing and bringing it up-to-date.
---

The only dependencies RmlUi has is on the [FreeType](http://www.freetype.org) library. The library has build configurations for most platforms, but unfortunately not iOS. This document describes how to build libfreetype.a as a universal binary for iOS and the Mac (i386, x86_64, arm6, arm7).

### Download the Source

Download the latest freetype sourcecode from [sourceforge](http://sourceforge.net/projects/freetype).

Open a terminal and extract the archive:

```
$ tar -jxf libfreetype-2.4.2.tar.bz2
$ cd libfreetype-2.4.2
```

### Compiling the library

We have to compile the library four times, once for each architecture.

#### i386

```
$ ./configure CFLAGS="-arch i386"
$ make
```

This forces configure to use the i386 architecture and build the library. The built library is located at objs/.libs/libfreetype.a. We copy this to our top level folder and build the next architecture.

```
$ cp objs/.libs/libfreetype.a libfreetype-i386.a
```

#### x86_64

Similar build setup for x86_64, notice the addition of make clean, we want to completely remove the i386 code.

```
$ ./configure CFLAGS="-arch x86_64";make clean;make
$ cp objs/.libs/libfreetype.a libfreetype-x86_64.a
```

#### arm6

Arm6 is used on iPhone 3G and earlier. There are quite a few arguments that need to be passed to configure to make it build for arm6. I'm going under the assumption that you're targeting iOS 3.2 using gcc-4.2 as your compiler. If this is not what you want, please update the arguments below accordingly.

```
$ ./configure --prefix=/usr/local/iphone --host=arm-apple-darwin --enable-static=yes --enable-shared=no CC=/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/gcc-4.2  CFLAGS="-arch armv6 -pipe -mdynamic-no-pic -std=c99 -Wno-trigraphs -fpascal-strings -O2 -Wreturn-type -Wunused-variable -fmessage-length=0 -fvisibility=hidden -miphoneos-version-min=3.2 -I/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS3.2.sdk/usr/include/libxml2 -isysroot /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS3.2.sdk" CPP=/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/cpp AR=/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/ar LDFLAGS="-arch armv6 -isysroot /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS3.2.sdk -miphoneos-version-min=3.2"
$ make clean;make
$ cp objs/.libs/libfreetype.a libfreetype-arm6.a
```

#### arm7

Arm7 is used on iPhone 3GS and newer. We do the exact same options as above, but pass arm7 as the architecture (remember to update the CFLAGS and the LDFLAGS)

```
$ ./configure --prefix=/usr/local/iphone --host=arm-apple-darwin --enable-static=yes --enable-shared=no CC=/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/gcc-4.2  CFLAGS="-arch armv7 -pipe -mdynamic-no-pic -std=c99 -Wno-trigraphs -fpascal-strings -O2 -Wreturn-type -Wunused-variable -fmessage-length=0 -fvisibility=hidden -miphoneos-version-min=3.2 -I/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS3.2.sdk/usr/include/libxml2 -isysroot /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS3.2.sdk" CPP=/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/cpp AR=/Developer/Platforms/iPhoneOS.platform/Developer/usr/bin/ar LDFLAGS="-arch armv7 -isysroot /Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS3.2.sdk -miphoneos-version-min=3.2"
$ make clean;make
$ cp objs/.libs/libfreetype.a libfreetype-arm7.a
```

### Bringing it all together as a universal library

We now have 4 individual libraries. To combine them into a single universal library use the lipo tool.

```
$ lipo -create -output libfreetype.a libfreetype-i386.a libfreetype-x86_64 libfreetype-arm6.a libfreetype-arm7.a
```

And thats it.

You can check which architectures are in a library with the -info argument.

```
$ lipo -info libfreetype.a
Architectures in the fat file: libfreetype.a are: armv6 armv7 i386 x86_64 
```
