# This file will check compatibility and start compilation.  
from os.path import normpath, join
from scripts.compileobj import *
from scripts.moduleobj import *

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
	module = Module(["main.cpp"], "main.exe") # create module object
	mobj.compile_link(module) # compile object