'''
grumPy error object

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
5/14/2023
'''

class error:

    def __init__(self,error_type:str):
        self._error_type = error_type
        self._descriptor = str()

    #set descriptor field
    def set_descriptor(self,descriptor:str):
        self._descriptor = descriptor

    #modify toString to incorporate both error type and descriptor
    #return a string representation of the error
    def __str__(self) -> str:
        return self._error_type + self._descriptor
