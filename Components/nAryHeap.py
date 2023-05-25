'''
nAryHeap will store string values
Heap will be structured based on an nAry Node field which will contain the number of children a parent node has

@author Efren Haskell
efrenhask@gmail.com
efrenhask@brandeis.edu
'''

import nAryNode as Node
import Token
from Error_Log import *

class nAryHeap:

    #build heap from a list of nAryNodes
    def __init__(self,list_inp = None):
        self._internal:list = list_inp
        size = 0
        if list_inp != None:
            size = len(list_inp)

    #assemble node list based on regular expression match
    def unordered_assemble(self,val:Token.Token) -> bool:
        assemb = ""
        if size > 0:
            index = 0
            remainder = 0
            while index < size:
                curr_node = self._internal[index]
                index += 1
                remainder -= 1
                if remainder < 0:
                    throw(SYNTAXERROR)
                if (curr_node.get_val() == val.get_val()) or (curr_node.get_val() == val.get_type()):
                    index = curr_node.get_siblings() - remainder
                    remainder = curr_node.get_siblings()
                    assemb += curr_node.get_assembly()
        return assemb
