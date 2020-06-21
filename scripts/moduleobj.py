"""
This file contains one class - Module.
"""


class Module:
    """
    This class - scheme for compilation and linking.
    """
    output = ""  # output file. Examples: "hello.exe"
    inputs = list()  # source files

    def __init__(self, inputs, output):
        """
        Set inputs and output param .
        """
        self.inputs = inputs
        self.output = output
