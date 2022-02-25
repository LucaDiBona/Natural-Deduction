
from typing import Dict
import Errors.exceptions as nde
import sys, os, json

def getDialects(folder:str) -> list:

    dialectFiles = os.listdir(folder)
    dialects = {}
    for i in dialectFiles:
        f = open(folder + "/" + i,"r")
        try:
            newDialect = Dialect(json.load(f))
            dialects[newDialect.name] = newDialect
        except json.JSONDecodeError:
            pass
        except nde.MissingDialectKey:
            pass
        f.close()
    return(dialects)

class Proof():

    def __init__(self,pdict:dict,dialects:list) -> None:
        try:
            self.name=pdict["Name"]
            self.dialectName = pdict["Dialect"]
            try:
                self.dialect = dialects[self.dialectName]
            except KeyError:
                raise nde.DialectNotFound
        except:
            pass


def loadProof(filepath:str):
    print("hi")

class Dialect():

    #TODO specify bracketing conventions

    def __init__(self, ddict: dict) -> None:
        try:
            self.name = ddict["Name"]
            self.connectives = {}
            for i in ddict["Connectives"]:
                self.connectives[i] = Connective(ddict["Connectives"][i])
            self.letters = {}
            for i in ddict["Letters"]:
                self.letters[i] = Letter(ddict["Letters"][i])
            self.rules = {}
            for i in ddict["Rules"]:
                self.rules[i] = Rule(ddict["Rules"][i])

                for j, jVal in enumerate(self.rules[i].inputs):
                    for k, kVal in enumerate(jVal):
                        for l, lVal in enumerate(kVal):
                            if isinstance(lVal, ConnectivePlaceholder):
                                try:
                                    self.rules[i].inputs[j][k][l] = self.connectives[lVal.name]
                                except KeyError:
                                    print("ERRROR")   #TODO raise proper error - invalid connective name

                for j, val in enumerate(self.rules[i].output):
                    if isinstance(val, ConnectivePlaceholder):
                        try:
                            self.rules[i].output[j] = self.connectives[val.name]
                        except KeyError:
                            print("ERRROR")   #TODO raise proper error - invalid connective name

        except KeyError:
            # raises error with the name of the missing key
            raise nde.MissingDialectKey(sys.exc_info()[1])

        # TODO check dialect produced same length as input dict - ie working correctly


class Connective():

    def __init__(self, cdict: dict) -> None:
        try:
            self.inputs = cdict["Inputs"]
            self.display = cdict["Display"]
            self.latex = cdict["LaTeX"]
        except KeyError:
            # raises error with the name of the missing key
            raise nde.MissingDialectKey(sys.exc_info()[1])


class Letter():

    def __init__(self, ldict: dict) -> None:
        try:
            self.input = ldict["Input"]
            self.display = ldict["Display"]
            self.latex = ldict["LaTeX"]
        except KeyError:
            # raises error with the name of the missing key
            raise nde.MissingDialectKey(sys.exc_info()[1])


class Metavariable():
    """
    Only used internally
    """

    def __init__(self, name: str) -> None:
        self.name = name


class MvPlaceholder():
    """
    Only used internally - generates a placeholder metavariable
    """

    def __init__(self, name: str) -> None:
        self.name = name


class ConnectivePlaceholder():
    """
    Only used internally - generates a placeholder connective
    """

    def __init__(self, name: str) -> None:
        self.name = name


class Rule():

    global parse

    def parse(string):

        output = string.split(" ")

        for i, val in enumerate(output):
            if len(val) < 1:
                pass  # TODO this should be an error
            elif val[0] == "$":
                if len(val) < 2:
                    pass  # TODO this should be an error
                else:
                    output[i] = MvPlaceholder(val[1:])  # strips $

            else:
                output[i] = ConnectivePlaceholder(val)

        return(output)

    def __init__(self, rdict: dict) -> None:
        try:
            self.display = rdict["Display"]
            self.latex = rdict["LaTeX"]
            self.inputs = []
            for i in rdict["Inputs"]:
                if isinstance(i, str):
                    self.inputs.append([[], parse(i)])
                else:
                    self.inputs.append([parse(i[0]), parse(i[1])])
            self.output = parse(rdict["Output"])

            # handle metavariables
            self.metavariables = []
            for i, iVal in enumerate(self.inputs):
                for j, jVal in enumerate(iVal):
                    for k, kVal in enumerate(jVal):
                        if isinstance(kVal, MvPlaceholder):
                            failing = True
                            l = 0
                            while failing and l < len(self.metavariables):
                                if kVal.name == self.metavariables[l].name:
                                    failing = False
                                    self.inputs[i][j][k] = self.metavariables[l]
                                l += 1
                            if failing:
                                newMv = Metavariable(kVal.name)
                                self.metavariables.append(newMv)
                                self.inputs[i][j][k] = newMv

            for i, val in enumerate(self.output):
                if isinstance(val, MvPlaceholder):
                    failing = True
                    j = 0
                    while failing and j < len(self.metavariables):
                        if val.name == self.metavariables[j].name:
                            failing = False
                            self.output[i] = self.metavariables[j]
                        j += 1
                    if failing:
                        newMv = Metavariable(kVal.name)
                        self.metavariables.append(newMv)
                        self.output[i] = newMv


        except KeyError:
            # raises error with the name of the missing key
            raise nde.MissingDialectKey(sys.exc_info()[1])
