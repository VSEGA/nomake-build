# cxx
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
### See Also
[linker](linker.md)