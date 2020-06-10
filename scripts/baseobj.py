from sys import platform
from os import name


class BaseObject(object):
    '''
    This class contains default values.
    '''
	# no rewritable
	configs = dict()  # This list will store the configs
    configs["name"] = name # This is a system name. Example: "posix" or "nt"
    configs["platform"] = platform # This is a another system name. Example: "linux" or "win32"
    configs["obj-format"] = ".obj" if configs["name"]=="nt" else ".o" # object file format
    configs["base_compile_command"] = dict() # schemes for compile files with any support compiler
    configs["base_compile_command"]["gcc"] = "{path} -Wall -c -std=c++11 -x none \
                                            -m{arch} -march={cputype} -o {output} {input}"
    configs["base_compile_command"]["msvc"] = "{path} {input} /EHsc /O2 \
    											/utf-8 /Wall /c /MACHINE:{arch} /Fo {output}"
    configs["base_compile_command"]["clang"] = "{path} -Wall -c -std=c++11 -x none \
                                            -m{arch} -march={cputype} -o {output} {input}"
    configs["base_compile_command"]["ld"] = "{path} {inputs} -o {output}"
    configs["base_compile_command"]["mslink"] = "{path} {inputs} /nologo /out:{output}"
    configs["cpu-types"] = ["native", "i386", "i486", "i586", "pentium"\
                    , "lakemont", "pentium-mmx", "pentiumpro", "i686", "pentium2", "pentium3", "pentium3m"\
                    , "pentium-m", "pentium4", "pentium4m", "presscott", "nocona", "core2", "nehalem"\
                    , "westmere", "sandybridge", "ivybridge", "haswell", "broadwell", "skylake", "bonnell"\
                    , "silvermont", "knl", "skylake-avx512", "k6", "k6-2", "k6-3", "athlon", "athlon-tbird"\
                    , "athlon-4", "athlon-xp", "athlon-mp", "k8", "opteron", "athlon64", "athlon-fx"\
                    , "k8-sse3", "opteron-sse3", "athlon64-sse3", "amdfam10", "barcelona", "bdver1", "bdver2"\
                    , "bdver3", "bdver4", "znver1", "btver1", "btver2", "winchip-c6", "winchip2", "c3", "c3-2"\
                    , "c7", "samuel-2", "nehemiah", "esther", "eden-x2", "eden-x4", "nano", "nano-1000"\
                    , "nano-2000", "nano-3000", "nano-x2", "nano-x4", "geode"]
    # rewritable
    configs["cpu-type"] = "native" # Improved version of Intel Pentium 4 CPU 
                                   # with 64-bit extensions. Only for g++
    configs["arch"] = "32" # program arch
    configs["cxx"] = "sysdefault"  # default compiler. sysdefault - the default compiler, 
                                    #determined by the type of system.
    configs["linker"] = "cxx-default" # recomended compiler by system
    configs["cxx-path"] = "nopath" # not use path
    configs["linker-path"] = "nopath"

    configs["force-python3"] = "False"  # use python 3 or throw an error
    configs["pathroot"] = "" # root path to folder with program