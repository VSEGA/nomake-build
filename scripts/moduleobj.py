"""
This file contains one class - Module.
"""
from typing import Dict


class Module:
    """
    This class - scheme for compilation and linking.
    """
    output = ""  # output file. Examples: "hello.exe"
    inputs = dict()  # source files

    def __init__(self, inputs: Dict[str, str], output: str) -> None:  # init function
        """
        Set inputs and output param.
        :param inputs: Input source Files
        :param output: Output executable file
        """
        self.inputs = inputs  # input files
        self.output = output  # linker out file
