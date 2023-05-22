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

class Parser:

    def __init__(self,input_file:str):
        self.token_breaks:List[str] = [' ',",",]
        self.special_tokens:List[str] = []
        self.arithmetic:List[str] = ['=','+','-']

    def tokenize(self,line:str) -> List[Token.Token]:
        initial = 0
        length = len(line)
        tokens:List[Token.Token] = list()
        token = ""
        index = 0
        while index < length:
            # special token, variable and primitives handling
            if line[index] in self.token_breaks or index == length-1:
                if (initial - index) > 0:
                    new = Token.Token()
                    token = line[initial:index]
                    if token in self.special_tokens:
                        new.set_type("special")
                    new.set_val(token)
                    tokens.append(new)
                initial = index+1

            # arithmetic operation handling
            elif line[index] in self.arithmetic:
                token = line[index]
                if index+1 < length:
                    if line[index+1] in self.arithmetic:
                        index += 1
                        token += line[index]
                new = Token.Token(token_type="arithmetic")
                new.set_type()
                new.set_val(token)

            else:
                token += line[index]
            
        return tokens

    def build_parse_tree(self,tokens:List[str]) -> Token.Token:
        throw(UNIMPLIMENTED)
            

    def build_syntax_tree(self,root:Token.Token):
        throw(UNIMPLIMENTED)
    
    def convert_from_tree(self,root:Token.Token):
        throw(UNIMPLIMENTED)
