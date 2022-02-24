class Error():

    def __init__(self,message:str="") -> None:
        self.errorMessage = message
        print(self.errorMessage)

    def message():
        return(self.errorMessage)

class FileError(Error):

    def __init__(self, file:str,message:str="") -> None:
        self.file = file
        self.errorMessage = message
        super().__init__(self,self.errorMessage)

class DialectError(FileError):

    def __init__(self,message:str="") -> None:
        self.errorMessage = message
        super().__init__(self,self.errorMessage)
