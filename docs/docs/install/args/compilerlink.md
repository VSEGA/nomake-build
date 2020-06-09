# Compiler and linking Args

## compiler
This parameter tells the program which compiler to use. With this, she will be able to determine the necessary parameters for the compiler.	
If compiler parameter not defined or value is `sysdefault` use gcc(for Unix-likes systems users) or msvc(for Windows users).
### Syntax

```bash
python setup.py compiler=msvc
python setup.py compiler=clang
python setup.py compiler=gcc
```
### Default value

`sysdefault`

### Dependencies
Dependencies not required.

This is an optional parameter.

Recomended use with [compiler-path](#compiler-path), [linker-path](#linker-path), [linker](#linker) params.


---



## compiler-path
Use to set path to compiler.
If this parameter not defined or value is `nopath` build system not use path(***The path to it shuld be in the PATH environment variable!!!!***).

### Syntax

```bash
python setup.py compiler-path=/usr/bin/g++
python setup.py compiler-path=c:\Program Files(x86)\Microsoft Visual Studio 2017\VC\cl.exe
python setup.py compiler-path=/usr/bin/clang
```
### Default value

`nopath`

### Dependencies
Dependencies not required.

This is an optional parameter.

Recomended use with [compiler](#compiler), [linker-path](#linker-path), [linker](#linker) params.


---



## linker
This parameter tells the program which linker to use. With this, she will be able to determine the necessary parameters for the linker.	
If linker parameter not defined or value is `cxx-default` using ld (for gcc and clang) or mslink(for msvc).
### Syntax

```bash
python setup.py linker=mslink
python setup.py linker=ld
```
### Default value

`cxx-default`

### Dependencies
Dependencies not required.

This is an optional parameter.

Recomended use with [compiler-path](#compiler-path), [linker-path](#linker-path), [compiler](#compiler) params.


---


## linker-path
Use to set path to linker.
If this parameter not defined or value is `nopath` build system not use path(***The path to it shuld be in the PATH environment variable!!!!***)..

### Syntax

```bash
python setup.py compiler-path=/usr/bin/ld
python setup.py compiler-path=c:\Program Files(x86)\Microsoft Visual Studio 2017\VC\link.exe
```
### Default value

`nopath`

### Dependencies
Dependencies not required.

This is an optional parameter.

Recomended use with [compiler-path](#compiler-path), [linker](#linker), [compiler](#compiler)  params.

---

## arch
Use for select target architecture. Now support only x86 and x64.
### Syntax

```bash
python setup.py arch=msvc
python setup.py arch=clang
```
### Default value

`x86` for x86 host system and `x64` for amd64.

### Dependencies
Dependencies not required.

This is an optional parameter.