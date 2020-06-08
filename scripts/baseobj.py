from sys import platform
from os import name


class BaseObject(object):
	# no rewritable
	configs = dict()  # This list will store the configs
    configs["name"] = name # This is a system name. Example: "posix" or "nt"
    configs["platform"] = platform # This is a another system name. Example: "linux" or "win32"
    configs["obj-format"] = ".o" # object file format
    configs["base_compile_command"] = dict() # schemes for compile files with any support compiler
    configs["base_compile_command"]["gcc"] = "{path} -o {output} {input}"
    configs["base_compile_command"]["msvc"] = "{path} {input} /EHsc /nologo /O2 \
    											/utf-8 /Wall /c /MACHINE:{arch} /Fo {output}"
    configs["base_compile_command"]["clang"] = "{path} -o {output} {input}"
    # rewritable
    configs["arch"] = "X86" # program arch
    configs["cxx"] = "sysdefault"  # default compiler. sysdefault - the default compiler, 
                                    #determined by the type of system.
    configs["linker"] = "cxx-default" # recomended compiler by system
    configs["cxx-path"] = "nopath" # not use path
    configs["linker-path"] = "nopath"

    configs["force-python3"] = "False"  # use python 3 or throw an error
    configs["pathroot"] = "" # root path to folder with program