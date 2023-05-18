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
        self.token_breaks:List[str] = []
        self.special_tokens:List[str] = []

    def tokenize(self,line:str) -> List[Token.Token]:
        initial = 0
        length = len(line)
        tokens:List[Token.Token] = list()
        token = ""
        for index in range(length):
            if line[index] in self.token_breaks or index == length-1:
                new = Token.Token()
                if (initial - index) > 0:
                    new_token = line[initial:index]
                    if token in self.special_tokens:
                        new.set_type(token)
                        if new_token in self.special_tokens:
                            throw(mod(SYNTAXERROR," a special token must be followed by a non-special token"))
                            return None
                    new.set_val(new_token)
                    token = new_token
                    tokens.append(new)
                    initial = index+1
            token += line[index]
        return tokens

    def build_parse_tree(self,tokens:list) -> Token.Token:
        throw(UNIMPLIMENTED)

    def convert_from_tree(self,root:Token.Token):
        throw(UNIMPLIMENTED)
        
