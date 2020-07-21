"""
Start Build System Main Script.
Please do not modify this file.
"""
from os import getcwd  # this function get path to script
import sys

import scripts.compileobj as co  # program main script

if __name__ == '__main__':
    co.main(getcwd(), sys.argv[1:])
