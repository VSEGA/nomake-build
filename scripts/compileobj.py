from checkobj import *
from os import mkdir
from os.path import normpath, join

# Main class
class CompileObject(CheckObject):

	def gccCompile(self, inputs, outputs):
		'''
		Compilation program this g++.
		'''
		self.execute(self.configs["base_compile_command"]["gcc"]\
			.format(path=self.configs["cxx-path"],output=outputs,input=inputs, arch=self.configs["cpu-type"]))
	# end of function

	def msvcCompile(self, inputs, outputs):
		'''
		Compilation program this msvc.
		'''
		self.execute(self.configs["base_compile_command"]["msvc"]\
			.format(path=self.configs["cxx-path"],output=outputs,input=inputs, arch=self.configs["arch"]))
	# end of function

	def clangCompile(self, inputs, outputs):
		'''
		Compilation program this clang.
		'''
		self.execute(self.configs["base_compile_command"]["clang"]\
			.format(path=self.configs["cxx-path"],output=outputs,input=inputs))
	# end of function

	# select function to compile
	def compile(self, module):
		'''
		Compile modules.
		'''
		path = self.configs["pathroot"] # program root path
		objfrm = self.configs["obj-format"] # obkect format. Examples: ".obj"(on nt), ".o"(on unixs) 
		try:
			mkdir(normpath(join(path, "out"))) # create out folder
		except:
			pass

		if self.configs["cxx"] == "msvc": # compile-function for msvc
			for i in module.inputs:
				msvcCompile(normpath(join(path, "src", i)), normpath(join(path, "src", i, ))+objfrm)

		elif self.configs["cxx"] == "clang": # for clang
			for i in module.inputs:
				clangCompile(normpath(join(path, "src", i)), normpath(join(path, "src", i, ))+objfrm)
		
		else: 
			for i in module.inputs: # for g++ 
				gccCompile(normpath(join(path, "src", i)), normpath(join(path, "src", i, ))+objfrm)
	# end of function
