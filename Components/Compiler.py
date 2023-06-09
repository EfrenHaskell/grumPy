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
Some data for token differentiation+
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
data_types:dict = {"int":"DD","long":"DQ"}
Token_Set = [HashTable(),HashTable(),HashTable(),HashTable()]

'''
Data structures to keep track of register status - general registers will range from r8-15
I will be only using the r 64-bit registers for simplicity
special registers are organized in the order - rax, rbx, rcx, rdx, rbp, rsp, rsi, rdi
'''
general_registers = [None] * 8



reserved_registers = {"ax":None,"bx":None,"cx":None,"dx":None,"bp":None,"sp":None,"si":None,"di":None}

def read_file(file_name:str):
    source = open(file_name,"r")
    lines = source.readlines()
    source.close()
    return lines

def trash_disposal():
    throw(UNIMPLIMENTED)

def write_asmfile(file_name:str,data_list:list,text_list:list):
    dest_file = open(file_name,"w")
    for data in data_list:
        if data != None:
            dest_file.write(data + "\n")
    for text in text_list:
        if text != None:
            dest_file.write(text + "\n")


def generate_code() -> (list,list):
    data = list()
    text = list()
    data.append("section .data")
    text.append("section .text\nglobal _start\n_start:")
    vals = Token_Set[0]
    variables = vals.get_all()
    sys = Token_Set[1]
    
    if len(variables) > 0:
        for variable in variables:
            root = variable[0]
            child = root.get_next()
            while True:
                if child != None:
                    first_char = child.get_val()[0]
                    if first_char == '=':
                        data.append(root.get_val() + " " + data_types[root.get_type()] + " " + child.get_val()[1:])
                    else:
                        pos = variable[2]
                        length = len(text)
                        while pos >= length:
                            text.append(None)
                            length += 1
                        while text[pos] != None:
                            if pos + 1 >= length:
                                text.append(None)
                            pos += 1
                        set_statement = None
                        register = None
                        for i in range(8):
                            if set_statement == None and general_registers[i] == None:
                                set_statement = "mov r" + str(i+8) + ", [" + root.get_val() + "]\n"
                                register = i
                            if general_registers[i] == root:
                                set_statement = str()
                                register = i
                                break
                        if set_statement == None:
                            for j in reserved_registers.keys():
                                if reserved_registers[j] == None:
                                    set_statement = "mov r" + j + ", [" + root.get_val() + "]"
                                    register = j
                        elif set_statement != str():
                            general_registers[register] = root
                        if first_char == '+':
                            text[pos] = (set_statement + "add r" + str(register+8) + ", " + child.get_val()[1:])
                        elif first_char ==  '-':
                            text[pos] = (set_statement +  "sub r" + str(register+8) + ", " + child.get_val()[1:])
                    child = child.get_next()
                else:
                    break
    return data,text

def token_typing(token:Token.Token):
    val = token.get_val()
    if val in data_types.keys():
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
    else:
        return 4


def parse(lines:List[str]):
    index = 0
    for line in lines:
        root,tail = tokenize(line)
        if root != None:
            if Token_Set[0].has_val(root):
                Token_Set[0].extend(root,tail)
            else:
                tokens = Token_Set[token_typing(root)]
                root = root.get_next()
                if tokens.has_val(root):
                    tokens.extend(root,tail)
                else:
                    tokens.insert(root,tail,index)
            index += 1
'''
Create a linked list of tokens from a line of code
Alternative to the traditional use of a parse tree
'''
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
                if (index+1 == length and char not in special_tokens) or (char in arithmetic and (len(token) == 0 or token[-1] in arithmetic)):
                    token += char
                elif char in arithmetic and len(token) > 0:
                    index -= 1
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
    parse(["int a = 36","a-10+6"])
    data_set,text_set = generate_code()
    for data in data_set:
        print(data)

    for text in text_set:
        print(text)
