# arch
Use for select target architecture. Now support only x86 and x86-64.
**For MSVC**
**Compile with target x86-64 not avaible on 32-bit Windows**
### Syntax
```bash
python setup.py arch=32
python setup.py arch=64
```
### Default value
`32` for x86 host system and `64` for x86-64.