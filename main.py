import os
import sys
import json
import curses
import parse
# from parse import *
import Errors.exceptions as nde


DIALECTS_FOLDER = "Dialects"

def init():
    #Load user settings

    #Load dialects
    dialects = parse.getDialects(DIALECTS_FOLDER)
    print(dialects)




def main():

    init()

    pass

if __name__ == "__main__":
    main()