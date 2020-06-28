"""
Contains BaseObject class need for compileobj.
"""
from re import search
from sys import platform
from typing import List


class BaseObject:
    """
    This class contains default values and some functions.
    """
    nomake_version = "0.0.1"  # nomake version format describes in docs(index.md)
    name = platform  # This is a system name. Example: "linux" or "win32"
    out_folder = "out"  # out folder
    src_folder = "src"  # src folder
    obj_format = ".obj" if name == "win32" else ".o"  # object file format
    arch = "32"  # program arch
    cxx = "sysdefault"  # sysdefault - the default compiler, determined by the type of system
    debug = "true"  # debug info from external program
    linker = "cxx-default"  # recomended linker by compiler
    pathroot = ""  # root path to folder with program, should be configured by main script
    debug_prints = "true"  # internal program debug info

    @staticmethod
    def value_correct(value: str, values: List[str]) -> None:
        """
        If value not in value throw an error
        :param value: Value itself
        :param values: List of correct values
        """
        if value not in values:
            raise TypeError(f"Not correct flag value - {value}")

    def __init__(self, args: List[str], pathroot: str) -> None:
        """
        Init the program flags.
        """
        self.pathroot = pathroot  # sets path to nomake root folder
        name = ""
        value = ""
        for arg in args:
            try:
                name = arg.split("=", 1)[0].lower()  # set flag name,
                value = arg.split("=", 1)[1].lower()  # value
            except:  # Incorrect arg
                if search(r"-v", arg) is None:
                    raise TypeError(f"Failed to init arg: {arg}")

            if name == "cxx":  # Sets compiler
                self.value_correct(value, ["gcc", "clang", "msvc", "sysdefault"])
                self.cxx = value
            elif name == "linker":  # Sets linker
                self.value_correct(value, ["ld", "mslink", "llvm-ld", "llvm-link", "cxx-default"])
                self.linker = value
            elif arg == "-v":
                print(self.nomake_version)
                raise BaseException("Internal Exception")
            elif name == "arch":  # Target arch. If target arch is 64 and cxx is msvc host system should be x86-64
                self.value_correct(value, ["64", "32"])
                self.arch = value
            elif name == "debug":  # external debug info. Describes in docs(NomakeBuild/BuildSystem/debug)
                self.value_correct(value, ["true", "false"])
                self.debug = value
            elif name == "debug-prints":  # internal debug info. Describes in docs(NomakeBuild/BuildSystem/debug-prints)
                self.value_correct(value, ["true", "false"])
                self.debug_prints = value
            else:  # If flag incorrect
                raise TypeError(f"ARG ERROR: Ignore unkown flag {name}")

        if self.cxx == "sysdefault":  # If compiler is not defined
            if self.name == "win32":  # for Windows
                self.cxx = "msvc"  # Visual C++
            else:  # For Linux
                self.cxx = "gcc"  # g++

        if self.linker == "cxx-default":  # If linker is not defined
            if self.cxx == "msvc":  # for MSVC
                self.linker = "mslink"  # MSlink(Linker from MSVC package)
            elif self.cxx == "clang":  # for Clang
                if self.name == "win32":  # Windows
                    self.linker = "llvm-link"  # I don't know why llvm-ld don't support win32 executable format
                else:  # for Linux
                    self.linker = "llvm-ld"
            else:  # for G++
                self.linker = "ld"
