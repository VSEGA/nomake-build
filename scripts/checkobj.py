# This file contains class check compatibility with system


import sys.version_info
from funcsobj import *

# Base class
class CheckObject(FuncsObject):
    '''
    This class contains functions for init args and check requiments
    '''
    def checkPython(self): 
        '''
        Check the python intrpretator version. Required a 2.7.x versions.
        '''
        vmajor = version_info[0] # version of Python interpreter: major,
        vminor = version_info[1] # minor
        if vmajor != 2 and self.configs["force-python3"] == "False": # if python 3.x.x
                                                                     # and force-python3 flag is not enabled
            print ("Python 2.7.x is required")
            raise EnvironmentError("Python 3 is not supported, use flag \
                                    force-python3=true to ignore this waring")
        elif vminor != 7: # if python2 isn't 2.7
            print ("Python 2.7.x is required")
            raise EnvironmentError("Python 2 is older version")
    # end of function
`
    def checkSystem(self):
        '''
        Checks system compatibility.
        '''
        if self.configs["name"] != "nt" or self.configs["name"] != "posix": # Check for system: 
                                                                            # windows, unix or another
            print("Your system (%s) is not supported now." % self.platform)
            raise EnvironmentError("System is not supported")
    # end of function

    def initArgs(self, args): 
        '''
        Init the program arguments.
        '''
        name = ""  # parameter name
        value = ""  # parameter value

        self.getSysArch()

        for arg in args:
            name = arg.split("=", 1)[0].lower()  # set param name,
            value = arg.split("=", 1)[1]         # value

            if name == "force-python3": # force use python3 param enable 
                self.configSetBool(name, value.lower())

			elif name == "compiler": # what kind compiler to use?
				self.configSetString("cxx", value.lower(), ["gcc", "clang", "msvc", "sysdefault"]) 
                        
            elif name == "compiler-path": # path to compiler
                self.isPathCorrectSet("cxx-path", value)
            
            elif name == "linker": # what kind linker to use?
                self.configSetString("cxx", value.lower(), ["ld", "mslink", "cxx-default"])
            
            elif name == "linker-path": # path to linker
                self.isPathCorrectSet("linker-path", value)

            elif name == "arch": # target arch. Now support only x86 and amd64
                self.configSetString("arch", value.lower(), ["x64", "x86"])
            
            else: # unkown param
                print("Unkown parameter ({n})".format(n=name))
                raise EnvironmentError("Unkown Parameter")
        #end of cycle

        if self.configs["cxx"] == "sysdefault": # if param "cxx" in dict configs = sysdefault,
                                                # set recommended compiler by system
                                                # clang is not recommended now
            if self.configs["name"] == "nt": # Windows
                self.configs["cxx"] == "msvc" # msvc (Microsoft Visual C++ compiler)

            else:                            # Posix (anothers systems not supported)
                self.configs["cxx"] == "gcc" # g++(GNU C++ compiler (gcc - compilers collection, isn't compiler))

        if self.configs["linker"] == "cxx-default": # if param "linker" in dict configs = cxx-default,
                                                    # set recommended linker by compiler
            if self.configs["cxx"] == "msvc":           # if msvc
                self.configs["linker"] == "mslink"      # msvc linker

            else:                                       # for gcc and clang
                self.configs["linker"] == "ld"          # GNU ld(from package GNU Binutils)

        if self.configs["cxx-path"] == "nopath": # nopath - not use path to compiler. 
                                                # The path to it shuld be in the PATH environment variable!
            if self.configs["cxx"] == "msvc": # for msvc
                self.configs["cxx-path"] == "cl" # name of compiler file
            elif self.configs["cxx"] == "clang":  # for clang
                self.configs["cxx-path"] == "clang"  # compiler file
            else:                                   # for g++
                self.configs["cxx-path"] == "g++"
        
        if self.configs["linker-path"] == "nopath": # if path isn't set
            if self.configs["linker"] == "mslink": # for msvc
                self.configs["linker-path"] == "link" # name of main linker file
            else:                                   # for g++ and clang(I don't know whats linker use clang)
                self.configs["linker-path"] == "ld"
    # end of function

    def checkSup(self) : # checks requiemnts
        self.checkPython()
        self.checkSystem()
        if self.configs["name"] == "posix" and self.configs["cxx"] == "msvc": # if msvc not on Windows
            print("Msvc not supported *nixs systems!")
            raise EnvironmentError("Msvc not supported *nixs systems!")
    # end of function

