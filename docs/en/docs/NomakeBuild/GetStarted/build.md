# Build Nomake

## Build with Python Scripts

To start build print `python setup.py`

---

## Adittional options

## Arch

Use for select target architecture. Now support only x86 and x86-64.  
**For MSVC: Compile with target x86-64 not avaible on 32-bit Windows**

### Syntax

```bash
python setup.py arch=32
python setup.py arch=64
```

### Default value

`32` for x86 host system and `64` for x86-64.

---

## Cxx

This parameter tells the program which compiler to use.  
With this, she will be able to determine the necessary parameters for the compiler.  
If value not defined or value is `sysdefault` use g++(Linux) or MSVC(Windows).

### Syntax

```bash
python setup.py cxx=msvc
python setup.py cxx=clang
python setup.py cxx=gcc
```

### Default value

`sysdefault`

---

## Debug-prints

If value is `true` build system will prints some debug info.

### Syntax

```bash
python setup.py debug=true
python setup.py debug=false
```

### Default value

`true`

---

## Debug

If debug is `true` compiler and linker will not print errors, warings and anather info.

### Syntax

```bash
python setup.py debug=true
python setup.py debug=false
```

### Default value

`true`

---

## Linker

This parameter tells the program which linker to use.
With this, she will be able to determine the necessary parameters for the linker.
If value not defined or value is `cxx-default` using ld (for G++), mslink(for MSVC),
llvm-ld(for Clang on Linux) or llvm-link(for Clang on Windows).

### Syntax

```bash
python setup.py linker=mslink
python setup.py linker=ld
python setup.py linker=llvm-ld
python setup.py linker=llvm-link
```

### Default value

`cxx-default`
