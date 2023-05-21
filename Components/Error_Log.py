'''
grumPy error logger

@author Efren Haskell
efrenhask@brandeis.edu
efrenhask@gmail.com
5/14/2023
'''

from error import *

#defualt errors
SYNTAXERROR = error("Syntax Error: ")
UNIMPLIMENTED = error("Method Unimplimented")

#modify error to include a specific descriptor
def mod(err:error,descriptor:str) -> error:
    err.set_descriptor(descriptor)
    return err

#basic throw statement implimentation to differentiate from print
def throw(err:error):
    print(err)
