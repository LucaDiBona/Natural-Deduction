
from typing import Dict


class Dialect():

    def __init__(self,ddict:dict) -> None:
        self.name = ddict["Name"]
        self.connectives = []
        for i in ddict["Connectives"]:
            self.connectives[i] = ddict["Connectives"][i]
        self.letters = []
        for i in ddict["Letters"]:
            self.letters.append()
        self.rules = []
        for i in ddict["Rules"]:
            self.rules.append()

class Connective():

    def __init__(self,cdict:dict) -> None:
        self.inputs = cdict["Inputs"]
        self.display = cdict["Display"]
        self.latex = cdict["LaTeX"]

class Letter():

    def __init__(self,ldict:dict) -> None:
        self.input = ldict["Input"]
        self.display =ldict["Display"]
        self.latex = ldict["LaTeX"]

class Rule():

    def parse(string):

        output = string.split(" ")

    def __init__(self,rdict:dict) -> None:
        self.display = rdict["Display"]
        self.latex = rdict["LaTeX"]
        self.inputs = []
        for i in rdict["Inputs"]:
            if isinstance(i,str):
                inputs.append([None,parse(i)])
            else:
                inputs.append([parse(i[0]),parse(i[1])])
        self.outputs = rdict["Outputs"]