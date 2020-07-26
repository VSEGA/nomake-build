# cxx
Этот флаг говорит программе, какой компилятор использовать.
Вместе с этим, она выберет нужные параметры для компилятора.	
Если параметр не определён или значение флага `sysdefault`, используется g++(для Linux) или MSVC(для Windows).
### Синтаксис
```bash
python setup.py cxx=msvc
python setup.py cxx=clang
python setup.py cxx=gcc
```
### Значение поумолчанию
`sysdefault`
### Смотрите также
[linker](linker.md)