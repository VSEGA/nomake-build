"""
This file will check compatibility and start compilation.
"""
from scripts.compileobj import *
from scripts.moduleobj import *


def main(path, args):
    """
    Main functions
    """
    mobj = CompileObject()  # class contains all scripts functions
    mobj.configs["pathroot"] = path  # set program root path
    mobj.initArgs(args)  # Init program args
    module = Module(["print.cpp", "main.cpp"], "main.exe")  # create module object
    mobj.compile_link(module)  # compile object
