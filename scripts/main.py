# This file will check compatibility and start compilation.

from compileobj import *  
from moduleobj import *

def main(path, args):
	mobj = CompileObject() # class contains all scripts functions
	mobj.configs["pathroot"] = path # set program root path
	mobj.initArgs(args) # Init program args
	mobj.checkSup() # Check program requiemnts
	module = Module(["main.cpp"], "main.exe") # create module object
	mobj.compile() # compile object