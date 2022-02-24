
from typing import Dict
import Errors.exceptions as nde
import sys


class Dialect():

    def __init__(self,ddict:dict) -> None:
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
        except KeyError:
            raise nde.MissingDialectKey(sys.exc_info()[1])         #raises error with the name of the missing key


        #TODO check dialect produced same length as input dict - ie working correctly

class Connective():

    def __init__(self,cdict:dict) -> None:
        try:
            self.inputs = cdict["Inputs"]
            self.display = cdict["Display"]
            self.latex = cdict["LaTeX"]
        except KeyError:
            raise nde.MissingDialectKey(sys.exc_info()[1])         #raises error with the name of the missing key

class Letter():

    def __init__(self,ldict:dict) -> None:
        try:
            self.input = ldict["Input"]
            self.display =ldict["Display"]
            self.latex = ldict["LaTeX"]
        except KeyError:
            raise nde.MissingDialectKey(sys.exc_info()[1])         #raises error with the name of the missing key

class Rule():

    global parse
    def parse(string):

        output = string.split(" ")

    def __init__(self,rdict:dict) -> None:
        try:
            self.display = rdict["Display"]
            self.latex = rdict["LaTeX"]
            self.inputs = []
            for i in rdict["Inputs"]:
                if isinstance(i,str):
                    self.inputs.append([None,parse(i)])
                else:
                    self.inputs.append([parse(i[0]),parse(i[1])])
            self.output = rdict["Output"]
        except KeyError:
            raise nde.MissingDialectKey(sys.exc_info()[1])         #raises error with the name of the missing key