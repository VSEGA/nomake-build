# This file contains one class - Module.
# This class - scheme for compilation and linking

class Module(object):
	output = "" # output file. Examples: "hello.exe"
	inputs = list() # source files
	def __init__(self, inputs, output): # set inputs and output param 
		self.inputs = inputs
		self.output = output
