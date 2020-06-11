from scripts.checkobj import *
from os import mkdir
from os.path import normpath, join
import scripts.universalfunctions.main as m
# Main class
class CompileObject(CheckObject):

	def gccCompile(self, inputs, outputs):
		'''
		Compilation program with g++.
		'''
		self.execute(self.configs["base_compile_command"]["gcc"]\
			.format(path=self.configs["cxx-path"],output=outputs,input=inputs\
				, cputype=self.configs["cpu-type"], arch=self.configs["arch"]))
	# end of function

	def msvcCompile(self, inputs, outputs):
		'''
		Compilation program with msvc.
		'''
		self.execute(self.configs["base_compile_command"]["msvc"]\
			.format(path=self.configs["cxx-path"],output=outputs,input=inputs, arch="x" + self.configs["arch"]))
	# end of function

	def clangCompile(self, inputs, outputs):
		'''
		Compilation program with clang.
		'''
		self.execute(self.configs["base_compile_command"]["clang"]\
			.format(path=self.configs["cxx-path"],output=outputs,input=inputs\
				, cputype=self.configs["cpu-type"], arch=self.configs["arch"]))
	# end of function

	def ldLink(self, inputs, outputs):
		'''
		Ld linking for g++ and clang.
		'''
		self.execute(self.configs["base_compile_command"]["ld"]\
			.format(path=self.configs["linker-path"],output=outputs,inputs=inputs))
	# end of function

	def msLink(self, inputs, outputs):
		'''
		Mslink linking for msvc.
		'''
		self.execute(self.configs["base_compile_command"]["mslink"]\
			.format(path=self.configs["linker-path"],output=outputs,inputs=inputs))
	# end of function
	def link(self, inputs, outputs):
		if self.configs["linker"] == "mslink":
			self.msLink(inputs, outputs)
		else:
			self.ldLink(inputs, outputs)
	# end of function
	# select function to compile
	def compile_link(self, module):
		'''
		Compile modules.
		'''
		path = self.configs["pathroot"] # program root path
		objfrm = self.configs["obj-format"] # obkect format. Examples: ".obj"(on nt), ".o"(on unixs) 
		try:
			mkdir(normpath(join(path, "out"))) # create out folder
		except:
			pass
		linker = list()
		if self.configs["cxx"] == "msvc": # compile-function for msvc
			for i in module.inputs:
				self.msvcCompile(normpath(join(path, "src", i)), normpath(join(path, "out", i))+objfrm)
				linker.append(normpath(join(path, "out", i)) + objfrm)
			self.link(m.toString(linker), module.output)

		elif self.configs["cxx"] == "clang": # for clang
			for i in module.inputs:
				self.clangCompile(normpath(join(path, "src", i)), normpath(join(path, "out", i))+objfrm)
				linker.append(normpath(join(path, "out", i)) + objfrm)
			self.link(m.toString(linker), module.output)
		else: 								# for g++ 
			for i in module.inputs: 
				self.gccCompile(normpath(join(path, "src", i)), normpath(join(path, "out", i))+objfrm)
				linker.append(normpath(join(path, "out", i)) + objfrm)
			self.link(m.toString(linker), module.output)
	# end of function
