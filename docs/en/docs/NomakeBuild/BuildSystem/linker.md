# linker
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
### See Also
[cxx](cxx.md)