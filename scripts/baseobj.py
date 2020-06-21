from sys import platform


class BaseObject:
	'''
	This class contains default values in dict configs.
	'''
	# no rewritable
	configs = dict()  # This list will store the configs
	configs["name"] = platform  # This is a system name. Example: "linux" or "win32"
	configs["out-folder"] = "out"
	configs["src-folder"] = "src"
	# object file format
	configs["obj-format"] = ".obj" if configs["name"] == "win32" else ".o"
	# schemes for compile files with any support compiler
	configs["base_compile_command"] = dict()
	configs["base_compile_command"][
		"gcc"] = "{path} -Wall -Wextra -Werror -c -std=c++11 -lstdc++ -x none -m{arch} \
		-march={cputype} -o {output} {input}"
	configs["base_compile_command"]["msvc"] = "{path} {input} /EHsc /nologo /O2 /Wall /c /Fo{output}"
	configs["base_compile_command"][
		"clang"] = "{path} -Wall -c -m{arch} {input} -o {output}"

	configs["base_compile_command"]["ld"] = "{path} {inputs} -o {output}"
	configs["base_compile_command"][
		"mslink"] = "{path} {inputs} /nologo /out:{output}"

	configs["cpu-types"] = ("native", "i386", "i486", "i586", "pentium", "lakemont", "pentium-mmx", "pentiumpro",
							"i686", "pentium2", "pentium3", "pentium3m", "pentium-m", "pentium4", "pentium4m",
							"presscott", "nocona", "core2", "nehalem", "westmere", "sandybridge", "ivybridge",
							"haswell", "broadwell", "skylake", "bonnell", "silvermont", "knl", "skylake-avx512", "k6",
							"k6-2", "k6-3", "athlon", "athlon-tbird", "athlon-4", "athlon-xp", "athlon-mp", "k8",
							"opteron", "athlon64", "athlon-fx", "k8-sse3", "opteron-sse3", "athlon64-sse3",
							"amdfam10", "barcelona", "bdver1", "bdver2", "bdver3", "bdver4", "znver1", "btver1",
							"btver2", "winchip-c6", "winchip2", "c3", "c3-2", "c7", "samuel-2", "nehemiah",
							"esther", "eden-x2", "eden-x4", "nano", "nano-1000", "nano-2000", "nano-3000", "nano-x2",
							"nano-x4", "geode")
	# rewritable
	configs["cpu-type"] = "native"  # Cpu-type. Only for g++
	configs["arch"] = "32"  # program arch
	# default compiler. sysdefault - the default compiler,
	configs["cxx"] = "sysdefault"
	# determined by the type of system.
	configs["debug"] = "true"
	configs["vcdir"] = "nopath"
	configs["linker"] = "cxx-default"  # recomended compiler by system
	configs["cxx-path"] = "nopath"  # not use path
	configs["linker-path"] = "nopath"
	configs["pathroot"] = ""  # root path to folder with program
	configs["debug-prints"] = "true" # internal debug info
	configs["include-path"] = "nopath"
	configs["lib-path"] = "nopath"
