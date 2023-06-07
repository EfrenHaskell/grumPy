'''
Main Compiler Class

------
Notes:
    - I've decided to limit myself to a single file for the compiler
    - I plan on reorganizing all of my functions when I have a base class
    - My goal is to make my Compiler "plug-and-play"
    - Optimizations will be built off the Compiler class to speed up compilation

------

@author Efren Haskell
efrenhask@gmail.com
efrenhask@brandeis.edu

'''

from typing import List
import Token
from Error_Log import *
from HashTable import *

'''
Some data for token differentiation
'''
special_tokens:List[str] = ['=','+','-','/','*',' ',',','(',')',':']
arithmetic:List[str] = ['=','+','-','/','*']

'''
Data structure to group similar tokens
Tokens are organized by types:
    0. Variable
    1. Sys_calls
    2. Class
    3. Function declaration

'''
data_types:List[str] = ["int","long"]
Token_Set = [HashTable(),HashTable(),HashTable(),HashTable()]

def read_file(file_name:str):
    source = open(file_name,"r")
    lines = source.readlines()
    source.close()
    return lines

def write_asm():
    throw(UNIMPLIMENTED)

def generate_code():
    throw(UNIMPLIMENTED)

def token_typing(token:Token.Token):
    val = token.get_val()
    if val in data_types:
        token.get_next().set_type(val)
        return 0
    elif val == "sys":
        token.get_next().set_type("sys_call")
        return 1
    elif val == "class":
        token.get_next().set_type("class")
        return 2
    elif val == "fun":
        token.get_next().set_type("fun")
        return 3

def parse(lines:List[str]):
    for line in lines:
        root,tail = tokenize(line)
        if root != None:
            tokens = Token_Set[token_typing(root)]
            if tokens.has_val(root.get_next()):
                tokens.extend(root.get_next(),tail)
            else:
                tokens.insert(root.get_next(),tail)

# create a linked list of tokens from a line of code
def tokenize(line:str) -> (Token.Token, Token.Token):
        index = 0
        length = len(line)
        token = str()
        root = None
        temp = None
        while index < length:
            new = None
            char = line[index]
            if char in special_tokens or index+1 == length:
                if (index+1 == length and char not in special_tokens) or char in arithmetic:
                    token += char
                if token[-1] not in arithmetic:
                    new = Token.Token()
            
            else:
                token += char
            
            if new != None:
                new.set_val(token)
                token = str()
                if root == None:
                    root = new
                if temp != None:
                    temp.set_next(new)
                temp = new
            index += 1
        return root,new
    
if __name__ == "__main__":
    root = tokenize("print(a)")[0]
    while True:
        if root == None:
            break
        print(root)
        root = root.get_next()
    parse(["int a = 36","sys:print(a)"])
    for table in Token_Set:
        print(table)
        
