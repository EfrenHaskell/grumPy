'''
Basic HashTable Implimentation for string

@author Efren Haskell
efrenhask@gmail.com
efrenhask@brandies.edu
'''

class HashTable:

    def __init__(self,list_inp:list = None,size:int = 11):
        if list_inp != None:
            for val in list_inp:
                self.insert(val)
        self._internal = [None]*size
        self._capacity = size
        self._size = 0

    #currently impliments basic linear probe due to the expected small size of ElementTable
    #considering using a tree chained implimentation in the event that I add more elements
    def insert(self,val:str):
        index = self.hash(val)
        for i in range(self._capacity):
            if self._internal[index] == None:
                self._internal[index] = val
                self._size += 1
                break
            index += 1
        if self._size * 1.5 >= self._capacity:
            self._capacity *= 2
            temp = self._internal.copy()
            self._internal = [None]*self._capacity
            self.rehash(temp)

    #basic method to delete specified val
    def delete(self,val:str):
        index = self.hash(val)
        for i in range(self._capacity):
            if self._internal[index] == val:
                self._internal[index] = None
                self._size -= 1
                break
            index += 1

    #basic method to check for a value in the hash table
    def hasVal(self, val:str):
        found = False
        index = self.hash(val)
        for i in range(self._capacity):
            if self._internal[index] == val:
                return True
            index += 1
        return False

    #basic hash function with ascii conversion
    def hash(self,val:str):
        asciival = sum([ord(char) for char in val])
        return asciival % self._virtual_size

    #rehash method for growing hash table     
    def rehash(self,vals:list):
        for val in vals:
            self.insert(val)

    def __str__(self):
        str_val = ','.join(self._internal)
        return "[" + str_val + "]"
