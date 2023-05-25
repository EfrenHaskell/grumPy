'''
grumPy Parser

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
4/13/2023
'''

from typing import List
import Token
from Error_Log import *
import nAryHeap

class Parser:

    def __init__(self,input_file:str):
        self.token_breaks:List[str] = [' ',",",]
        self.special_tokens:List[str] = []
        self.arithmetic:List[str] = ['=','+','-']

    def tokenize(self,line:str) -> Token.Token:
        initial = 0
        index = 0
        length = len(line)
        token = ""
        root = None
        temp = None
        while index < length:
            new = None
            # special token, variable and primitives handling
            if line[index] in self.token_breaks or index+1 == length:
                if index+1 == length:
                    index += 1
                if (index - initial) > 0:
                    new = Token.Token()
                    token = line[initial:index]
                    if token in self.special_tokens:
                        new.set_type("special")
                initial = index+1
                
            # arithmetic operation handling
            elif line[index] in self.arithmetic:
                token = line[index]
                if index+1 < length:
                    if line[index+1] in self.arithmetic:
                        index += 1
                        token += line[index]
                new = Token.Token(token_type="arithmetic")
                initial = index + 1

            #arithmetic variable handling
            elif line[index+1] in self.arithmetic:
                token = line[initial:index+1]
                new = Token.Token()
                initial = index
                
            else:
                token += line[index]
            if new != None:
                new.set_val(token)
                if root == None:
                    root = new
                if temp != None:
                    temp.set_next(new)
                temp = new
            index += 1
        return root

    def build_block_expression(self,tokens:List[Token.Token]) -> str:
        
    
    def build_parse_tree(self,tokens:List[str]) -> Token.Token:
        throw(UNIMPLIMENTED)
            

    def build_syntax_tree(self,root:Token.Token):
        throw(UNIMPLIMENTED)
    
    def convert_from_tree(self,root:Token.Token):
        throw(UNIMPLIMENTED)

