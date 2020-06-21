"""
This file contains class with all required methods to compiling nomake.
"""

from scripts.checkobj import *
from os import mkdir, rmdir, remove, walk
from os.path import join
from scripts.pytools.data_cmd import *


# Main class


# noinspection PyInconsistentIndentation
class CompileObject(CheckObject):
    """
    Class contains compile and all superclass methods(from CheckObject, FuncObject and BaseObject).
    """
    linker = list()

    def gccCompile(self, inputs, outputs):
        """
        Compilation program with g++.
        """
        self.ifprint("Compile file with g++ {inputs} -> {outputs}")
        execute(self.configs["debug"], self.configs["base_compile_command"]["gcc"]
                .format(path=self.configs["cxx-path"], output=outputs, input=inputs, cputype=self.configs["cpu-type"],
                        arch=self.configs["arch"]))

    def msvcCompile(self, inputs, outputs):
        """
        Compilation program with msvc.
        """
        self.ifprint(f"Compile file with msvc {inputs} -> {outputs}")
        execute(self.configs["debug"], self.configs["base_compile_command"]["msvc"]
                .format(path=self.configs["cxx-path"], output=outputs,
                	input=inputs))

    def clangCompile(self, inputs, outputs):
        """
        Compilation program with clang.
        """
        self.ifprint(f"Compile file with g++ {inputs} -> {outputs}")
        execute(self.configs["debug"], self.configs["base_compile_command"]["clang"]
                .format(path=self.configs["cxx-path"], output=outputs, input=inputs, cputype=self.configs["cpu-type"],
                        arch=self.configs["arch"]))

    def ldLink(self, inputs, outputs):
        """
        Ld linking for g++ and clang.
        """
        self.ifprint(f"Linking files {inputs} -> {outputs}")
        execute(self.configs["debug"], self.configs["base_compile_command"]["ld"]
                .format(path=self.configs["linker-path"], output=outputs, inputs=inputs))

    def msLink(self, inputs, outputs):
        """
        Mslink linking for msvc.
        """

        self.ifprint(f"Linking files {inputs} -> {outputs}")
        execute(self.configs["debug"], self.configs["base_compile_command"]["mslink"]
                .format(path=self.configs["linker-path"], output=outputs, inputs=inputs))

    def link(self, inputs, outputs):
        """
        Selct method to linking.
        """
        if self.configs["linker"] == "mslink":
            self.msLink(inputs, outputs)
        else:
            self.ldLink(inputs, outputs)

    def compile(self, func, inps, src: str, outfold: str, objfrm: str):
        """
        Compile the module
        @param func: func to compile.(msvcCompile, gccCompile, clangCompile)
        @param inps: Inputs files.(["main.cpp", "print.cpp"])
        @param src: Path to src folder.("/nomake/src")
        @param outfold: Path to out folder.("/nomake/out")
        @param objfrm: Object file extension.(".o")
        """
        for i in inps:
            func(join(src, i), join(outfold, i) + objfrm)
            self.linker.append('"' + join(outfold, i) + objfrm + '"')

    def compile_link(self, module):
        """
        Compile modules.
		"""

        path = self.configs["pathroot"]  # program root path
        # object format. Examples: ".obj"(on nt), ".o"(on unixs)
        objfrm = self.configs["obj-format"]
        outfold = join(path, self.configs["out-folder"])
        src = join(path, self.configs["src-folder"])

        for _current_dir, _dirs, files in walk(outfold):
            for f in files:
                remove(join(outfold, f))
        try:
            rmdir(outfold)  # delete out folder
        except:
            mkdir(outfold)  # create out folder
        else:
            mkdir(outfold)  # create out folder

        self.linker = list()
        if self.configs["cxx"] == "msvc":  # compile-function for msvc
            self.compile(self.msvcCompile, module.inputs, src, outfold, objfrm)

        elif self.configs["cxx"] == "clang":  # for clang
            self.compile(self.clangCompile, module.inputs, src, outfold, objfrm)
        else:  # for g++
            self.compile(self.gccCompile, module.inputs, src, outfold, objfrm)

        self.link(toString(self.linker), '"' + join(outfold, module.output) + '"')
# end of function
