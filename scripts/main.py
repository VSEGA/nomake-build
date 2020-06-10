# This file will check compatibility and start compilation.

from compileobj import *  
from moduleobj import *
from os.path import normpath, join


def joinsrcpath(path, name):
	return normpath(join(path, "src", name))

def main(path, args):
	'''
	Main function
	'''
	mobj = CompileObject() # class contains all scripts functions
	mobj.configs["pathroot"] = path # set program root path
	mobj.initArgs(args) # Init program args
	mobj.checkSup() # Check program requiemnts
	module = Module(joinsrcpath(path, "main.cpp"), "main.exe") # create module object
	mobj.compile_link(module) # compile object