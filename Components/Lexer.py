'''
grumPy Lexer

-- CONSIDERING REMOVING --

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

    


if __name__ == "__main__":
    lexer = Lexer()
    lexer.build_tree("")
