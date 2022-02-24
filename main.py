import os, sys, json, curses
from dialects import *
import Errors.exceptions as nde


DIALECTS_FOLDER = "Dialects"

def init():
    #Load user settings

    #Load dialects
    dialectFiles = os.listdir(DIALECTS_FOLDER)
    dialects = []
    for i in dialectFiles:
        f = open(DIALECTS_FOLDER + "/" + i,"r")
        try:
            dialects.append(Dialect(json.load(f)))
        except json.JSONDecodeError:
            pass
        except nde.MissingDialectKey:
            pass
        f.close()
    print(dialects)



def main():

    init()

    pass

if __name__ == "__main__":
    main()