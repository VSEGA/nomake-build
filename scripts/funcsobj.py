from scripts.baseobj import *
from subprocess import check_call
import platform, sys, os

class FuncsObject(BaseObject):
    '''
    Contains a functions used other classes
    '''

    def getSysArch(self):
        '''
        Get system arch by enviroment variables.
        '''
        if platform.machine()[3:] == "64":
            self.configs["arch"] = "64" # amd64
        else:
            self.configs["arch"] = "32" # i386
    # end of function

    def execute(self, command): 
        '''
        Execute command.
        '''
        check_call(command, stderr=sys.stderr, stdout=sys.stdout)
    # end of function

    def isPathCorrectSet(self, name, path):
        '''
        If path is correct add his to dict configs.
        '''
        if os.path.exists(path):
            self.configs[name] = path
        else:
            raise EnvironmentError("Non exists path - {p}".format(p=path))
    # end of function

    def configSetBool(self, name, value):
        '''
        Set bool param to dictionary configs.
        '''
        if value == "true":  # if param true
            self.configs[name] = True
        elif value == "false": # false
            self.configs[name] = False
        else:
            raise EnvironmentError("Param(%s) value(%s)  is not correct" % (name, value))
    # end of function

    def configSetString(self, name, value, values):
        '''
        Set string param to dictionary configs.
        '''

        if value in values:
            self.configs[name] = value # if param value correct
        else: # value is incorrect
            raise EnvironmentError("Param(%s) value(%s)  is not correct" % (name, value))
    # end of function