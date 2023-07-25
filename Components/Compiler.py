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
from PNode import *

'''
Some data for token differentiation
'''
token_breaks:List[str] = [' ',',']
arithmetic:List[str] = ['=','+','-','/','*']

'''
Data structure to group similar tokens
Tokens are organized by types:
    0. Variable Declarations
    1. Variable Calls
    2. System Calls
    3. 

'''
spec_types = ["fun","class"]
code_set = [HashTable(),list(),HashTable()]


'''
Data structures to keep track of register status - general registers will range from r8-15
I will be only using the r 64-bit registers for simplicity
special registers are organized in the order - ax, bx, cx, dx, bp, sp, si, di
'''
registers = [None] * 16

special_id = ["ax","bx","cx","dx","bp","sp","si","di"]

def read_file(file_name:str):
    source = open(file_name,"r")
    lines = source.readlines()
    source.close()
    return lines

def trash_disposal():
    throw(UNIMPLIMENTED)

def write_asmfile(file_name:str,data_list:list,text_list:list):
    dest_file = open(file_name,"w")
    dest_file.write("section .data\n")
    for data in data_list:
        if data != None:
            dest_file.write(data + "\n")
    for text in text_list:
        if text != None:
            dest_file.write(text + "\n")


'''

operation destination, source

det_operation() -> operation
 -> destination
 -> source

if destination not in registers
    mov register, destination
else
    operation register, source

if source not in registers
    operation register, source (variable)


'''

registers = [None] * 16
special_id = ["ax","bx","cx","dx","bp","sp","si","di"]
arithmetic:List[str] = ['=','+','-','/','*']
asm_arithmetic:List[str] = ['mov','add','sub','div','mul']

def algorithmic_parse(sections:List[Token.Token]) -> list:
    code = list()
    index = len(sections)-1
    mov_amt = len(sections)-1
    while index >= 0:
        root = sections[index]
        temp = root
        op_set = [None]*3
        pos = 0
        highprior = 0
        while True:
            if temp.get_next() == None:
                break
            curr = root.get_val()
            if root.get_next() == None:
                if curr == "``":
                    root.set_val(sections[mov_amt].get_val())
                    mov_amt -= 1
                op_set[2] = root
            if curr[0] in arithmetic or root.get_next() == None:
                if op_set[1] == None or priority(curr) > highprior:
                    if op_set[2] != None:
                        op_set[0] = op_set[2]
                    op_set[1] = root
                    pos = 2
                    highprior = priority(curr)
                else:
                    val1 = op_set[0].get_val()
                    val2 = op_set[2].get_val()
                    if not (is_constant(val1) or val1[0] == ':'):
                        val1 = '[' + val1 + ']'
                    if not (is_constant(val2) or val2[0] == ':'):
                        val2 = '[' + val2 + ']'
                    res,reg = operation_generate(op_set[1].get_val(),val1,val2)
                    if reg != None:
                        op_set[0].set_val(':' + reg)
                    op_set[0].set_next(op_set[2].get_next())
                    code.append(res)
                    root = temp
                    op_set = [root,None,None]
            elif curr == "``":
                root.set_val(sections[mov_amt].get_val())
                mov_amt -= 1
                op_set[pos] = root
            else:
                op_set[pos] = root
            root = root.get_next()
        index -= 1
    return code

def priority(operation:str) -> int:
    if len(operation) == 2:
        operation = operation[1]
    if operation == '+' or operation == '-' or operation == '=':
        return 1
    elif operation == '*' or operation == '/':
        return 2
    elif operation == '**':
        return 3
    else:
        return 0

def det_operation(operation:str):
    

def convert(op_code:list()):
    res = str()
    for val in op_code:
        if val != None:
            res += val
    return res

'''
test for double operation
get asm operqtion equiv
assign registers
produce operations
'''
'''
def operation_generate(operation,val1,val2) -> (str,str):
    res = str()
    if len(operation) == 2 and operation[0] == '=':
        res,reg = operation_generate(operation[1],val1,val2)
        operation = operation[0]
        res += "\n"
     = det_operation(operation)
     '''

'''
elements of operation generation

 - get operation from arithmetic symbol
 - 


'''
#NEW
def operation_generate(operation,val1,val2) -> (str,str):
    res = str()
    reg = None
    if len(operation) == 2 and operation[0] == '=':
        res,reg = operation_generate(operation[1],val1,val2)
        operation = operation[0]
        res += "\n"
    
    if operation == '=':
        
    elif operation == '/' or operation == '*':
        
    else:
        
    has_reg = val1[0] == ':'
    if has_reg:
        op_code[1] = val1[1:]
        reg = op_code[1]
        op_code[2] = val2
    if val2[0] == ':':
        if has_reg:
            op_code[2] = op_code[2][1:]
        else:
            op_code[1] = val2[1:]
            reg = op_code[1]
            op_code[2] = val1
            has_reg = True
    if not has_reg:
        reg = find_reg(val1)
        op_code[1] = reg
        res = "mov " + reg + ", " + val1 + "\n"
        op_code[2] = val2
    
        if registers[8] != None:
            throw(UNIMPLIMENTED)
        if reg != ":rax":
            if 
            res = "mov rax, " + op_code[2] + "\n" + res
        op_code[2] = None
        reg = "rax"
    res += convert(op_code)
    return res, reg

#ORIGINAL
def operation_generate(operation,val1,val2) -> (str,str):
    op_code = [None]*3
    res = str()
    reg = None
    if len(operation) == 2 and operation[0] == '=':
        res,reg = operation_generate(operation[1],val1,val2)
        operation = operation[0]
        res += "\n"
    op_code[0] = det_operation(operation)
    has_reg = val1[0] == ':'
    if has_reg:
        op_code[1] = val1[1:]
        reg = op_code[1]
        op_code[2] = val2
    if val2[0] == ':':
        if has_reg:
            op_code[2] = op_code[2][1:]
        else:
            op_code[1] = val2[1:]
            reg = op_code[1]
            op_code[2] = val1
            has_reg = True
    if not has_reg:
        reg = find_reg(val1)
        op_code[1] = reg
        res = "mov " + reg + ", " + val1 + "\n"
        op_code[2] = val2
    if operation == '/' or operation == '*':
        if registers[8] != None:
            throw(UNIMPLIMENTED)
        if reg != ":rax":
            if 
            res = "mov rax, " + op_code[2] + "\n" + res
        op_code[2] = None
        reg = "rax"
    res += convert(op_code)
    return res, reg


def is_constant(var:str) -> bool:
    var_ascii = ord(var[0])
    if var_ascii > 47 and var_ascii < 58:
        return True
    return False

def find_reg(var:str):
    reg = -1
    for index in range(16):
        curr = registers[index]
        if curr == None and reg == -1:
            reg = index
        if curr == var:
            reg = index
            break
    registers[reg] = var
    if reg >= 8:
        return 'r' + special_id[reg-8]
    return 'r' + str(reg + 8)


data_types = ["int","long","char"]

def build_datablock(root):
    code_bit = list()
    while True:
        if root == None:
            break
        code_bit.append(root.get_val())
        root = root.get_next()
    if len(code_bit) != 4 or not is_constant(code_bit[3]):
        return None
    else:
        if code_bit[0] == "int":
            return code_bit[1] + " db " + code_bit[3]
        
def syscall_generate(root:Token.Token) -> str:
    syscall = root.get_val()
    if syscall == "print":
        if root.get_type() == "dd":
            throw(UNIMPLIMENTED)
        return "mov e"

'''
def operation_generate(var1:str,var2:str,operation:str) -> str:
    supplemental = str()
    if '=' in operation:
        if len(operation) == 1:
            if var1 in registers:
                if var2[0] == ':':
                    return 'mov [' + var1 + ']' + ', ' + var2[1:], None
                else:
                    if is_constant(var2):
                        return 'mov [' + var1 + ']' + ', ' + var2, None
                    return 'mov [' + var1 + ']' + ', ' + '[' + var2 + ']', None
        else:
            supplemental = '\nmov [' + var1 + ']' + ', '
            operation = operation[0]
    res = det_operation(operation)
    destination = str()
    if var1[0] == ':':
        destination = var1[1:]
    else:
        det_constant = is_constant(var1)
        potential = -1
        for index in range(16):
            curr = registers[index]
            if curr == None and potential == -1:
                potential = index
            elif not det_constant and curr == var1:
                potential = index
                destination = convert_register(potential)
                break
            if index == 15:
                destination = convert_register(potential)
                registers[potential] = var1
                source = var1
                if not det_constant:
                    source = '[' + source + ']'
                res = "mov " + destination + ", " + source + "\n" + res
    if var2[0] == ':':
        res += destination + ", " + var2[1:]
    else:
        if not is_constant(var2):
            source = '[' + var2 + ']'
            for index in range(16):
                if registers[index] == var2:
                    source = convert_register(index)
                    break
            res += destination + ", " + source
        else:
            res += destination + ", " + var2
    if supplemental != "":
        res += supplemental + destination
    return res,':' + destination
'''

def print_linked(root:Token.Token):
    res = '['
    while True:
        if root == None:
            break
        res += root.get_val()
        root = root.get_next()
    print(res + ']')

'''
def algorithmic_parse(line:Token.Token):
    root = line
    code = list()
    op_set = [None]*3
    index = 0
    isPriority = False
    while True:
        if root == None:
            break
        curr = root.get_val()
        if curr == '(':
            op_set[1] = ' '
        elif curr == ')':
            isPriority = True
        elif curr[0] in arithmetic:
            prior = priority(curr)
            index = 2
            if op_set[1] == None or prior > priority(op_set[1]):
                op_set[1] = curr
                if op_set[2] != None:
                    op_set[0] = op_set[2]
            else:
                isPriority = True
        else:
            op_set[index] = root
        root = root.get_next()
        if index == 2 and isPriority and op_set[1] != ' ': # full operation set created
            # generate code
            code_bit,reg = operation_generate(op_set[0].get_val(),op_set[2].get_val(),op_set[1])
            code.append(code_bit)
            # trash dispose operations and variables
            temp = op_set[0]
            temp.set_val(reg) # save register
            new = op_set[2].get_next()
            temp.set_next(new)
            new.set_prev(temp)
            # remove unneeded parentheses
            remove_p(temp.get_prev(),temp,new)
            isPriority = False
            # reset pointer to beginning
            root = line
            index = 0
            op_set = [None]*3
    return code
'''

def process(lines:List[str]):
    data_set = code_set[0]
    text_set = code_set[1]
    function_set = code_set[2]
    for line in lines:
        tokens = tokenize(' ' + line)
        root = tokens[0]
        val = root.get_val()
        if val in data_types:
            tokens[0] = root.get_next()
            if not data_set.has_val(tokens[0].get_val()):
                code_bit = build_datablock(root)
                if code_bit == None:
                    next_val = tokens[0].get_next()
                    if next_val == None or next_val.get_val() != '=':
                        throw(mod(SYNTAXERROR,"a variable can not be operated on before being initialized"))
                        return
                else:
                    data_set.insert(code_bit)
                    continue
            if val == "bool":
                throw(UNIMPLIMENTED)
            elif val == "str":
                throw(UNIMPLIMENTED)
            elif val == "int":
                for line in algorithmic_parse(tokens):
                    text_set.append(line)
            elif val == "double":
                throw(UNIMPLIMENTED)
            else:
                throw(UNIMPLIMENTED)
        elif val in registers:
            throw(UNIMPLIMENTED)

def add_token(new:Token.Token,token_sections:list,level:int):
    if token_sections[level] != None:
        new.set_next(token_sections[level])
    token_sections[level] = new


def tokenize(line:str) -> List[Token.Token]:
    token_sections = [None]
    level = 0
    mov_amt = 1
    token = str()
    index = len(line)-1
    length = 1
    while index >= 0:
        char = line[index]
        if char == ')':
            add_token(Token.Token("``"),token_sections,level)
            if level + 1 < length:
                mov_amt = length - level
            level = length
            token_sections.append(None)
            length += 1
        elif char == '(':
            if token != '':
                add_token(Token.Token(token),token_sections,level)
            token = str()
            level -= mov_amt
            mov_amt = 1
        elif char in arithmetic:
            if token != '':
                add_token(Token.Token(token),token_sections,level)
            token = char
            if index > 0 and line[index-1] in arithmetic:
                index -= 1
                token += line[index]
            add_token(Token.Token(token),token_sections,level)
            token = str()
        elif char in token_breaks:
            if token != '':
                add_token(Token.Token(token),token_sections,level)
                token = str()
        else:
            token = line[index] + token
        index -= 1
    return token_sections

'''
Create a linked list of tokens from a line of code
Alternative to the traditional use of a parse tree
'''
'''
def tokenize(line:str) -> Token.Token:
    if line != None:
        token = str()
        root = None
        new = Token.Token()
        length = len(line)
        index = 0
        while index < length:
            char = line[index]
            if char in arithmetic:
                if len(token) > 0:
                    index -= 1
                else:
                    token = char
                    if line[index+1] == '=':
                        token += '='
                        index += 1
                char = " "
            if char in token_breaks:
                if len(token) > 0:
                    if new.get_next() != None:
                        new = new.get_next()
                    mod_token(new,token)
                    if root == None:
                        root = new
                    token = str()
            else:
                token += line[index]
            index += 1
        if new.get_next() != None:
            new.get_next().set_val(')')
        return root
'''

def mod_token(new:Token.Token,token:str):
    if token in data_types.keys():
        new.set_type(data_types[token])
    elif token in spec_types:
        new.set_type(token)
    else:
        new.set_val(token)

if __name__ == "__main__":
    #parse(["int a = 36","a-10+6"])
    #data_set,text_set = generate_code()
    lines = ["int a = 0","int a += (4 + 5 * 6) / 8"]
    process(lines)
    print("section .data")
    print("\n".join(code_set[0].get_all()))
    print("section .text\nglobal _start\n_start:")
    print("\n".join(code_set[1]))
