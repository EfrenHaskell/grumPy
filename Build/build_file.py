'''
Key builds:
 - Procedures
 - Modules
 - Untyped data
 - Control structures
 - Sys_calls

'''

'''Build Components
 - file_nm stores the grum core file
 - sections holds lists for data and text sections
'''
file_nm = "Compiler0.0.grum"
data = list()
text = list()
sections = [data,text]

'''Identifiers'''
arithmetic = ['+','-']
token_breaks = [' ',',']
sys_calls = []

'''Build Constants
 - BUMP references a parentheses bump up
     - In the event that a token is a BUMP object, build_file will
        "bump up" to a new parentheses level for parsing
     
'''
BUMP = object()

'''auxiliary storage'''
variables = list()
procedures = list()

''' fetch gets the contents of our compiler file
 - The method does simple file reading to access the compiler's contents for asm translation
'''
def fetch() -> list:
    comp_file = open(file_nm, 'r')
    lines = comp_file.readlines()
    comp_file.close()
    return lines

def build(lines:list):
    for line in lines:
        units = token_build(' ' + line)
        lengthi = len(units)
        for i in reversed(range(lengthi)):
            unit = units[i]
            lengthj = len(unit)
            for j in reversed(range(lengthj)):
                curr = unit[j]
                if unit[0] == ':':
                    if curr == "proc":
                        
                    elif curr == "mod":
                        
                    elif curr == "for":
                        print("UNIMPLIMENTED")
                    elif curr == "if":
                        print("UNIMPLIMENTED")  
                elif curr is BUMP:
                    print("UNIMPLIMENTED")
                elif curr == "var":
                    print("UNIMPLIMENTED")
                elif curr in sys_calls:
                    print("UNIMPLIMENTED")
                elif curr in variables:
                    print("UNIMPLIMENTED")
                elif curr in procedures:
                    print("UNIMPLIMENTED")
                else:
                    print("UNIMPLIMENTED")

''' add_token is a helper method for the token_build method
 - Tokens are first determined to be workable or not
 - Then the tokens are appended to a token_sections level
 - An empty string is returned
'''
def add_token(token_section:list,token:str):
    if token != '':
        token_section.append(token)
    return str()

''' token_build acts as the build_file's tokenizer
 - The method takes a string line and produces a list of string tokens
 - Units designated by parentheses are then separated into different list levels
'''
def token_build(line:str) -> list:
    token_sections = [list()]
    token = str()
    mov_amt = 1
    level = 0
    index = len(line)-1
    length = 1
    while index >= 0:
        char = line[index]
        if char == '(':
            token = add_token(token_sections[level],token)
            level -= mov_amt
            mov_amt = 1
        elif char == ')':
            token_sections[level].append(BUMP)
            if level <= length:
                mov_amt = length - level
            level = length
            token_sections.append(list())
        elif char in token_breaks:
            token = add_token(token_sections[level],token)
        elif char in arithmetic:
            add_token(token_sections[level],token)
            token = char
            if index > 0 and line[index-1] in arithmetic:
                index -= 1
                token += line[index]
            token = add_token(token_sections[level],token)
        else:
            token = line[index] + token
        index -= 1
    return token_sections

build(["var a = (3-4) +6"])
