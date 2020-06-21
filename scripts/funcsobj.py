from scripts.baseobj import *
from platform import machine
from os import getenv, walk
from re import search
from os.path import join

class FuncsObject(BaseObject):
    '''
    Contains a functions used other classes
    '''
    def ifprint(self, msg):
        if self.configs["debug-prints"] == "true":
            print(msg)
    def getProgramFiles32(self):
        return getenv("ProgramFiles")
    def getVisualStudio(self):
        for dirs in list(walk(self.getProgramFiles32())):
            if search(r"Microsoft Visual Studio", dirs[0]) != None:
                for i in dirs[1]:
                    if search(r"VC", i) != None:
                        return dirs[0]
    def getVisualCpp(self):
        return str(join(self.getVisualStudio(), "VC"))

    def getSetSysArch(self):
        '''
        Get and set to configs system arch by enviroment variables.
        '''
        if machine()[3:] == "64":
            self.configs["arch"] = "64"  # amd64
        else:
            self.configs["arch"] = "32"  # i386
    # end of function

    def setPath(self, name, path):
        '''
        If path is correct add his to dict configs.
        '''
        self.configs[name] = path
    # end of function

    def configSetBool(self, name, value):
        '''
        Set bool param to dictionary configs.
        '''
        if value == "true" or value == "false":  # if param true or false
            self.configs[name] = value
    # end of function

    def configSetString(self, name, value, values):
        '''
        Set string param to dictionary configs.
        '''

        if value in values:
            self.configs[name] = value  # if param value correct
        else:  # value is incorrect
            raise EnvironmentError(f"Param(name) value(value)  is not correct")
    # end of function
