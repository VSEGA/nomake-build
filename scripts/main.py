"""
This file will check compatibility and start compilation.
"""
from typing import List
from scripts.compileobj import CompileObject
from scripts.moduleobj import Module


def main(path: str, args: List[str]) -> None:
    """
    Main function.
    :param path: Program root path.
    :param args: Args to prog without script name.
    """
    try:
        mobj = CompileObject(args, path)  # class contains all scripts functions
        module = Module(["print.cpp", "main.cpp"], "main.exe")  # create module object
        mobj.compile_link(module)  # compile object
    except BaseException:
        pass
