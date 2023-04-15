'''
grumPy Token

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
4/13/2023
'''

class Token:

    def __init__(self,str: val):
        self._val = val
        self._type = self.det_type()

    def det_type(self) -> str:
        self._val
        
