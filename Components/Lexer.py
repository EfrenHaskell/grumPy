'''
grumPy Lexer

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
4/13/2023
'''
import Token
from Error_Log import *

class Lexer:

    def __init__(self):
        self.token_breaks = []
        self.special_tokens = []

    def build_tree(self,line:str) -> Token.Token:
        throw(UNIMPLIMENTED)
        return None

    def tokenize(self,line:str) -> list:
        initial = 0
        length = len(line)
        tokens = list()
        token = ""
        for index in range(length):
            if line[i] in self.token_breaks:
                new = Token.Token()
                if token in self.special_tokens:
                    new.set_type(token)
                token = line[initial:index]
                if token in self.special_tokens:
                    throw(mod(SYNTAXERROR," a special token must be followed by either a  or "))
                    break
                
                tokens.append()
                initial = index+1


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build_tree("")
