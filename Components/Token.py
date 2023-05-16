'''
grumPy Token

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
4/13/2023
'''

class Token:

    def __init__(self):
        self._type = str()
        self._val = None
        self._leftChild = None
        self._rightChild = None

    def set_left(self,leftChild): 
        self._leftChild = leftChild

    def set_right(self,rightChild): 
        self._rightChild = rightChild
    
    def set_val(self,val):
        self._val = val

    def set_type(self,val_type):
        self._type = val_type
