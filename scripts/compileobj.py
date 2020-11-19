"""
This file contains class with all required methods to compiling nomake.
"""
import os
from os.path import join
from platform import machine, system
from re import search
from subprocess import run
from typing import List, Dict

if system() == "Windows":
    import winreg

from scripts import moduleobj
from scripts.baseobj import BaseObject, InternalException


class CompileObject(BaseObject):
    """
    Class contains compile and all superclass methods(from CheckObject, FuncObject and BaseObject).
    """
    linker_lst: List[str] = list()  # Contains name of object files for link
    vscpp: str

    def ifprint(self, msg: str) -> None:
        """
        Print msg if self.configs["debug-prints"] == "true"
        :param msg: itself message
        """
        if self.debug_prints == "true":
            print(msg)

    def execute(self, debug: str, command: str) -> None:
        """
        Execute command.
        :param debug: if debug is "true" prints program output
        :param command: command itself
        """
        self.ifprint(command)
        if debug.lower() == "true":
            run(command, check=True)

        else:
            with open(os.devnull, "wb") as null:
                run(command, stderr=null, stdout=null, check=True)

    def getSetSysArch(self) -> None:
        """
        Get and set to configs system arch by enviroment variables.
        """
        if machine()[3:] == "64":
            self.arch = "64"  # x86-64
        else:
            self.arch = "32"  # x86

    @property
    def getProgramFiles32(self) -> str:
        """
        Returns path to program Files 32
        :return: Program Files 32 location
        """
        if os.getenv("ProgramFiles(x86)") is not None:  # On some computers(Example my laptop) with 64-bits Windows
            # ProgramFiles(x86) returns None
            return os.getenv("ProgramFiles(x86)")
        else:
            return os.getenv("ProgramFiles")

    @property
    def getVisualStudio2015(self) -> str:  # This function tested with VS2005
        """
        Gets Visual Studio 2015 location.
        :returns: Visual Studio location
        """
        for current_dir, dirs, _files in list(os.walk(self.getProgramFiles32)):
            if search(r"Microsoft Visual Studio 14", current_dir) is not None:
                if "VC" in dirs:
                    return current_dir

    @property
    def getNewVisualStudio(self) -> str:  # This function is not tested
        """
        Gets New(After VS 2017) Visual Studio loaction.
        :returns: Visual Studio location
        """
        for current_dir, _dirs, _files in list(os.walk(self.getProgramFiles32)):
            if search(r"Microsoft Visual Studio", current_dir) is not None:
                if search(r"201[579]", current_dir) is not None:
                    if search(r"Community", current_dir) is not None or \
                            search(r"Professional", current_dir) is not None or \
                            search(r"Enterprise", current_dir) is not None:
                        if search(r"VC", current_dir) is not None and search(r"MSVC", current_dir) is not None:
                            if search(r"[0-9][0-9]\.", current_dir) is not None:
                                return current_dir

    @staticmethod
    def getVerDir(dir_path: str) -> str:
        """
        Return dir_path/version
        :param dir_path: dir
        """
        for current_dir, dirs, _files in os.walk(dir_path):
            return join(current_dir, dirs[0])

    def arch_dep_winkit(self, dir_path: str, arch: str = "64", crt: str = "ucrt") -> str:
        """
        Comabinate paths.
        :param dir_path: $dir_path$
        :param arch: Add x86 or x64
        :param crt: Crt folder
        :returns: Path $dir_path$/10.**.***/crt/x86 or x64
        """

        if arch == "64":
            return join(self.getVerDir(dir_path), crt, "x64")
        else:
            return join(self.getVerDir(dir_path), crt, "x86")

    @property
    def getVisualCpp(self) -> str:
        """
        Gets Visual C++ location.
        :returns: Visual C++ location
        """
        try:
            try:
                return str(join(self.getNewVisualStudio, "VC"))
            except TypeError:
                return str(join(self.getVisualStudio2015, "VC"))
        except:
            print("ERROR: Could not get Visual Studio")
            raise

    def arch_dep_vcdir(self, bdir: str, arch: str = "32") -> str:
        """
        Gets path to VCDIR/bdir/amd64 (If arch is 64) or VCDIR/bdir.
        :param bdir: name of dir
        :param arch: Add amd64 folder if arch is 64
        :returns: path to dir
        """
        if arch == "64":
            return str(join(self.vscpp, bdir, "amd64"))
        else:
            return str(join(self.vscpp, bdir))

    def link(self, inputs: List[str], outputs: str) -> None:
        """
        Linking the input files.
        :param inputs: Input object files
        :param outputs: Output file
        """
        if self.linker == "ld":
            self.ifprint(f"Linking with ld: {' '.join(inputs)} -> {outputs}")
            if self.name == "win32":
                self.execute(self.debug, f"g++ {' '.join(inputs)} -o {outputs} -lstdc++")
            else:
                self.execute(self.debug, f"ld {' '.join(inputs)} -o {outputs} -lstdc++")
        elif self.linker == "llvm-ld":
            self.ifprint(f"Linking with llvm-ld: {' '.join(inputs)} -> {outputs}")
            self.execute(self.debug, f"lld.ld {' '.join(inputs)} -o {outputs} -lstdc++")
        elif self.linker == "llvm-link":
            self.ifprint(f"Linking with llvm-link: {' '.join(inputs)} -> {outputs}")
            self.execute(self.debug, f"lld-link {' '.join(inputs)} /out:{outputs} /debug")
        else:
            self.ifprint(f"Linking with mslink: {' '.join(inputs)} -> {outputs}")
            self.execute(self.debug, f"{self.linkpath} {' '.join(inputs)} /out:{outputs} /debug /nologo")

    def compile(self, inps: Dict[str, str], srcfold: str, outfold: str, objfrm: str) -> None:
        """
        Compile the input files.
        :param inps: In/Out files. Example: ({"main.cpp" : "main.cpp", "print.cpp" : "print.cpp"})
        :param srcfold: Path to src folder. Example: ("/nomake/src")
        :param outfold: Path to out folder. Example: ("/nomake/out")
        :param objfrm: Object file extension. Example: (".o")
        """
        if self.cxx == "gcc":
            for i in inps:
                self.ifprint(f"Compiling with g++: {join(srcfold, i)} -> {join(outfold, inps[i]) + objfrm}")
                self.execute(self.debug, f"g++ {join(srcfold, i)} -o "
                                         f"{join(outfold, inps[i]) + objfrm} -c -Wall -Wextra")
                self.linker_lst.append('"' + join(outfold, inps[i]) + objfrm + '"')
        elif self.cxx == "clang":
            for i in inps:
                self.ifprint(f"Compiling with clang: {join(srcfold, i)} -> {join(outfold, inps[i]) + objfrm}")
                self.execute(self.debug, f"clang++ {join(srcfold, i)} -o "
                                         f"{join(outfold, inps[i]) + objfrm} -c -Wall -Wextra")
                self.linker_lst.append('"' + join(outfold, inps[i]) + objfrm + '"')
        else:
            for i in inps:
                self.ifprint(f"Compiling with msvc: {join(srcfold, i)} -> {join(outfold, inps[i]) + objfrm}")
                self.execute(self.debug, f"{self.clpath} {join(srcfold, i)} "
                                         f"/Fo{join(outfold, inps[i]) + objfrm} /c /EHsc /nologo")
                self.linker_lst.append('"' + join(outfold, inps[i]) + objfrm + '"')

    def compile_link(self, module: moduleobj.Module) -> None:
        """
        Compile modules.
        :param module: Module for compile
        """
        path = self.pathroot  # program root path
        objfrm = self.obj_format  # object format. Examples: ".obj"(on nt), ".o"(on unixs)
        outfold = join(path, self.out_folder)
        src = join(path, self.src_folder)

        self.linker_lst = list()
        self.compile(module.inputs, src, outfold, objfrm)
        self.link(self.linker_lst, '"' + join(outfold, module.output) + '"')

    def __init__(self, args: List[str], pathroot: str) -> None:  # The init method in BaseObject non contains some
        # functions released in CompileObject
        """
        Init the program flags.
        """
        super(CompileObject, self).__init__(args, pathroot)

        self.getSetSysArch()
        self.vscpp = self.getVisualCpp
        if self.cxx == "msvc":
            self.clpath = join(self.arch_dep_vcdir('bin', self.arch), 'cl')
        if self.linker == "mslink":
            self.linkpath = join(self.arch_dep_vcdir('bin', self.arch), 'link')
        try:
            os.mkdir(join(self.pathroot, self.out_folder))
        except (NotImplementedError, FileExistsError):
            for _current_dir, _dirs, files in os.walk(join(self.pathroot, self.out_folder)):
                for f in files:
                    os.remove(join(join(self.pathroot, self.out_folder), f))
        if self.name == "win32":
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows Kits\\Installed Roots")
            kit10 = winreg.QueryValueEx(key, "KitsRoot10")[0]
            kit81 = winreg.QueryValueEx(key, "KitsRoot81")[0]
            kit8 = winreg.QueryValueEx(key, "KitsRoot")[0]
            winreg.CloseKey(key)
            os.putenv("LIB", ";".join([self.arch_dep_vcdir("lib", arch=self.arch),
                                       self.arch_dep_winkit(join(kit10, "Lib"), arch=self.arch),
                                       self.arch_dep_winkit(join(kit81, "Lib"), arch=self.arch, crt="um")]))
            os.putenv("INCLUDE", ";".join([join(self.getVerDir(join(kit10, "Include")), "ucrt"),
                                           join(kit81, "Include", "um"),
                                           join(kit81, "Include", "shared"),
                                           join(self.getVisualCpp, "include")]))


def main(pathf: str, args: List[str]):
    """
    Main Function.
    """
    try:
        mobj = CompileObject(args, pathf)
        inp = ""
        while(inp.lower() != "yes" and inp.lower() != "no"):
            print("Use Color: Yes/No")
            inp = input()
        
        if inp.lower() == "yes":
            module = moduleobj.Module({join("Sys", "color.cpp"): "color",
                                      join("Preprocessor", "fdescriptor.cpp"): "preprocessor",
                                      join("Preprocessor", "comments.cpp"): "comments",
                                      join("Sys", "win32.cpp" if mobj.name == "win32" else "unix.cpp"): "sys",
                                      join("Api", "debug.cpp"): "debug", "NApp.cpp": "NApp",
                                      "main.cpp": "main"}, "nomake" + ".exe" if mobj.name == "win32" else "")
        else:
            module = moduleobj.Module({join("Sys", "no_color.cpp"): "color",
                                      join("Tools", "Preprocessor", "fdescriptor.cpp"): "preprocessor",
                                      join("Tools", "Preprocessor", "comments.cpp"): "comments",
                                      join("Sys", "win32.cpp" if mobj.name == "win32" else "unix.cpp"): "sys",
                                      join("Api", "debug.cpp"): "debug", "NApp.cpp": "NApp",
                                      "main.cpp": "main"}, "nomake" + ".exe" if mobj.name == "win32" else "")
        mobj.compile_link(module)
    except InternalException:
        pass
