'''
grumPy Token

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
4/13/2023
'''

class Token:

    def __init__(self,token_type = str(), val = None):
        self._type = token_type
        self._val = val
        self._leftChild = None
        self._rightChild = None

    #compare type to value to make certain the two are compatible
    #if not, throw error
    def type_val_comp(self):
        throw(UNIMPLIMENTED)

    #set left child of root node
    def set_left(self,leftChild): 
        self._leftChild = leftChild

    #set right child of root node
    def set_right(self,rightChild): 
        self._rightChild = rightChild

    #get left child
    def get_left(self):
        return self._leftChild

    #get right child
    def get_right(self):
        return self._rightChild

   #set node's value: necessary when initializing a node object
    def set_val(self,val):
        self._val = val

    def get_val(self):
        return self._val

    #set node's type: necessary when initializing a node object
    def set_type(self,val_type):
        self._type = val_type

    def get_type(self) -> str:
        return self._type

