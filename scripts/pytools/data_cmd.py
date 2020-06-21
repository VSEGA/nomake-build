from subprocess import run
from sys import stderr as err, stdout as out
from os import devnull
# this file contains random functions

# converts list to string


def toString(inputs, division=" "):
    output = ""  # output variable
    for i in inputs:
        output = output + i + division
    return output


def execute(debug, command, env=None):
    '''
    Execute command.
    '''
    if debug == "true":
    	run(command, stderr=err, stdout=out, check=True, env=env)

    else:
        with open(devnull, "wb") as null:
            run(command, stderr=null, stdout=null, check=True, env=env)
# end of function
