# linker
Этот флаг говорит программе, какой линкер использовать.
Вместе с этим, она выберет нужные параметры для линкера.
Если параметр не определён или значение `cxx-default`, используется ld (для G++), mslink(для MSVC),
llvm-ld(для Clang на Linux) или llvm-link(для Clang на Windows).
### Синтаксис
```bash
python setup.py linker=mslink
python setup.py linker=ld
python setup.py linker=llvm-ld
python setup.py linker=llvm-link
```
### Значение поумолчанию
`cxx-default`
### Смотрите также
[cxx](cxx.md)