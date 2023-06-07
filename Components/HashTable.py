'''
Basic HashTable Implimentation for nAryNode

@author Efren Haskell
efrenhask@gmail.com
efrenhask@brandies.edu
'''

import Token as Tk

class HashTable:

    def __init__(self,list_inp:list = None,size:int = 11):
        if list_inp != None:
            for val in list_inp:
                self.insert(val)
        self._internal:(Tk.Token,Tk.Token) = [None]*size
        self._capacity = size
        self._size = 0

    #currently impliments basic linear probe due to the expected small size of ElementTable
    #considering using a tree chained implimentation in the event that I add more elements
    def insert(self, val:Tk.Token,tail:Tk.Token):
        index = self.hash(val)
        for i in range(self._capacity):
            if self._internal[index] == None:
                self._internal[index] = (val,tail)
                self._size += 1
                break
            index += 1
        if self._size * 1.5 >= self._capacity:
            self._capacity *= 2
            temp = self._internal.copy()
            self._internal = [None]*self._capacity
            self.rehash(temp)

    #basic method to delete specified val
    def delete(self,val:Tk.Token):
        index = self.hash(val)
        for i in range(self._capacity):
            if self._internal[index][0] == val:
                self._internal[index] = None
                self._size -= 1
                break
            index = (index + 1) % self._capacity

    #basic method to check for a value in the hash table
    def has_val(self, val:Tk.Token):
        index = self.hash(val)
        for i in range(self._capacity):
            if self._internal[index] != None and self._internal[index][0].get_val() == val.get_val():
                return True
            index = (index + 1) % self._capacity
        return False

    def extend(self, root:Tk.Token,tail:Tk.Token):
        index = self.hash(root)
        for i in range(self._capacity):
            val = self._internal[index]
            if val != None and val[0].get_val() == root.get_val():
                val[0].set_next(root.get_next())
                self._internal[index] = (val[0],tail)
            index = (index + 1) % self._capacity

    #basic hash function with ascii conversion
    def hash(self,val:Tk.Token):
        val = val.get_val()
        asciival = sum([ord(char) for char in val])
        return asciival % self._capacity

    #rehash method for growing hash table     
    def rehash(self,vals:list):
        for val in vals:
            self.insert(val)

    #tostring implimentation
    def __str__(self):
        res = ""
        for i in range(self._capacity):
            char = self._internal[i]
            if char != None:
                if len(res) > 0:
                    res += ","
                root = char[0]
                res += "["
                while True:
                    if root == None:
                        break
                    res += str(root)
                    if root.get_next() != None:
                        res += ","
                    root = root.get_next()
                    
                res += "]"
        return "[" + res + "]"
