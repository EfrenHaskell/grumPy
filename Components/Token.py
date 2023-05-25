'''
grumPy Tokens are singly linkedlist nodes

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
4/13/2023
'''

from Error_Log import *

class Token:

    def __init__(self,val = str(), token_type = str()):
        self._val = val
        self._next = None
        self._type = token_type

    #compare type and value
    #throw error if they are incompatible
    def type_val_comp(self):
        throw(UNIMPLIMENTED)
    
    #set next node
    def set_next(self,next_node):
        self._next = next_node

    #get next node
    def get_next(self):
        return self._next

    #set value of node
    def set_val(self,new_val):
        self._val = new_val

    #get value of node   
    def get_val(self) -> str:
        return self._val

    #set token type
    def set_type(self,token_type):
        self._type = token_type

    #get token type
    def get_type(self) -> str:
        return self._type

    #tests if the node has a next node
    def has_next(self) -> bool:
        if self._next == None:
            return False
        return True

    def __str__(self) -> str:
        return self._val
