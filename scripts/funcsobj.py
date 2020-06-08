from baseobj import *
from subprocess import check_call
import os, os.path

class FuncsObject(BaseObject):

	def getSysArch(self): # get system arch by enviroment varisables
        if ("64" in os.getenv('PROCESSOR_ARCHITECTURE')) or ("64" in os.getenv('PROCESSOR_ARCHITEW6432')): 
            self.configs["arch"] = "X64" # x86-64
        else:
            self.configs["arch"] = "X86"  # only x86
    # end of function

    def execute(self, command): # execute program
        check_call(command, stderr=sys.stderr, stdout=sys.stdout)
    # end of function

    def isPathCorrectSet(self, name, path): # if path is correct add his to dict configs
        if path.exists(path):
            self.configs[name] = path
        else:
            raise EnvironmentError("Non exists path - {p}".format(p=path))
    # end of function

    def configSetBool(self, name, value): 		# set bool param to dictionary configs
        if value == "true":  # if param true
            self.configs[name] = True
        elif value == "false": # false
            self.configs[name] = False
        else:
            raise EnvironmentError("Param(%s) value(%s)  is not correct" % (name, value))
    # end of function

    def configSetString(self, name, value, values): 	# set string param to dictionary configs 
		if value in values:   # if param value correct
			self.configs[name] = value
        else:  #value is incorrect
            raise EnvironmentError("Param(%s) value(%s)  is not correct" % (name, value))
    # end of function