import os, sys, json, curses


DIALECTS_FOLDER = "Dialects"

def init():
    #Load user settings

    #Load dialects
    dialectFiles = os.listdir(DIALECTS_FOLDER)
    dialects = []
    for i in dialectFiles:
        f = open(DIALECTS_FOLDER + "/" + i,"r")
        dialects.append(json.loads(f.read()))
        f.close()
    print(dialects)


def main():

    init()

    pass

if __name__ == "__main__":
    main()