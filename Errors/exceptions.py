"""
    Defines the custom exceptions necessary for this to work, they are converted into errors (which the program displays without crashing)
"""

class Error(Exception):

    def __init__(self) -> None:
        super().__init__()

class FileError(Error):

    def __init__(self,file:str="") -> None:
        self.file = file
        super().__init__()

class DialectError(FileError):

    def __init__(self,file:str="") -> None:
        self.file = file
        super().__init__(self.file)

class MissingDialectKey(DialectError):

    def __init__(self,key:str,file:str="") -> None:
        self.key = key
        self.file = file
        print(key)
        super().__init__(self.file)

class ProofError(FileError):

    def __init__(self,file:str="") -> None:
        self.file = file
        super().__init__(self.file)

class DialectNotFound(FileError):

    def __init__(self,dialect:str,file:str="") -> None:
        self.dialect = dialect
        self.file = file
        super().__init__(self.file)