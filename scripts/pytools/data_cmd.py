from subprocess import check_call
from sys import stderr as err, stdout as out
from os import devnull
# this file contains random functions

# converts list to string


def toString(inputs):
    output = ""  # output variable
    for i in inputs:
        output = output + i + " "
    return output


def execute(debug, command):
    '''
    Execute command.
    '''
    if debug == "false":
        with open(devnull, "wb") as null:
            check_call(command, stderr=null, stdout=null)

    else:
        check_call(command, stderr=err, stdout=out)
# end of function
