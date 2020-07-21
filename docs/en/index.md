# Welcome to Nomake docs
## What is Nomake?
Nomake is free automation build system, written on C++.
Nomake support C++ compilation by G++, Clang, MSVC(only for Windows users).

Also Nomake use [MkDocs](https://www.mkdocs.org/) for generate this docs.
## Build Nomake
#### System requiments
- GNU/Linux or Windows
- Python 3.6 (For build with Base Build System)
- G++ or Clang with support C++11 or MSVC 2015+

If your system meets these requirements, you can continue.
### Build with Basic Build System
Select this if you don't have any Nomake build. 
If you build Nomake with build system some functionality may not be available.
#### Init the build 
To start building write:
`python setup.py`
## Versions Format
***0***.0.1a-1

A large program update.

0.***0***.1a-1

A small or medium update that affects old functionality.

0.0.***1***a-1

A small or medium update that does not affect old functionality.

0.0.1***a***-1

A bug fix or micro update

0.0.1a-***1***

A build system update
## See Also 
Basic Build System Args:

[cxx](NomakeBuild/BuildSystem/cxx.md)

[arch](NomakeBuild/BuildSystem/arch.md)

[linker](NomakeBuild/BuildSystem/linker.md)

[debug](NomakeBuild/BuildSystem/debug.md)

[debug-prints](NomakeBuild/BuildSystem/debug-prints.md)