'''
grumPy error logger

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
5/14/2023
'''

from error import *

SYNTAXERROR = error("Syntax Error: ")
UNIMPLIMENTED = error("Method Unimplimented")

def mod(err:error,descriptor:str) -> error:
    err.set_descriptor(descriptor)
    return err

def throw(err:error):
    print(err)
