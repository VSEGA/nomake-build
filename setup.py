"""
Start Build System Main Script.
"""

# Please do not modify this file.
from os import getcwd  # this function get path to script
import sys

from scripts.main import main  # program main script

if __name__ == '__main__':
    main(getcwd(), sys.argv[1:])
