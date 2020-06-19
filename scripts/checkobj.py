# This file contains class check compatibility with system


from scripts.funcsobj import *

# Base class


class CheckObject(FuncsObject):
    '''
    This class contains function for init flags.
    '''

    def initArgs(self, args):
        '''
        Init the program flags.
        '''

        self.getSetSysArch()

        for arg in args:
            name = arg.split("=", 1)[0].lower()  # set flag name,
            value = arg.split("=", 1)[1]         # value

            if name == "compiler":  # what kind compiler to use ?
                self.configSetString("cxx", value.lower(), [
                                     "gcc", "clang", "msvc", "sysdefault"])

            elif name == "compiler-path":  # path to compiler
                self.setPath("cxx-path", value)

            elif name == "linker":  # what kind linker to use?
                self.configSetString("linker", value.lower(), [
                                     "ld", "mslink", "cxx-default"])

            elif name == "linker-path":  # path to linker
                self.setPath("linker-path", value)

            elif name == "arch":  # target arch. Now support only x86 and amd64
                self.configSetString("arch", value.lower(), ["64", "32"])

            elif name == "cpu-type":
                self.configSetString(
                    "cpu-type", value.lower(), self.configs["cpu-types"])

            elif name == "debug":
                self.configSetBool(name, value.lower())
            elif name == "debug-prints":
                self.configSetBool(name, value.lower())

            # unkown flag
            else:  
                print(f"ARGS WARING: Ignore unkown parameter ({name})")
        # end of cycle

        if self.configs["cxx"] == "sysdefault":
            if self.configs["name"] == "win32":
                self.configs["cxx"] = "msvc"
            else:
                self.configs["cxx"] = "gcc"
        if self.configs["linker"] == "cxx-default":
            if self.configs["cxx"] == "msvc":
                self.configs["linker"] = "mslink"
            else:
                self.configs["linker"] = "ld"
        if self.configs["cxx-path"] == "nopath":
            if self.configs["cxx"] == "msvc":
                self.configs["cxx-path"] = "cl"
            elif self.configs["cxx"] == "clang":
                self.configs["cxx-path"] = "clang++"
            else:
                self.configs["cxx-path"] = "g++"
        if self.configs["linker-path"] == "nopath":
            if self.configs["linker"] == "mslink":
                self.configs["linker-path"] = "link"
            elif self.configs["linker"] == "ld" and self.configs["cxx"] == "clang":
                self.configs["linker-path"] = "ld.lld"
            else:
                self.configs["linker-path"] = "ld"
