'''
@author Efren Haskell
efrenhask@gmail.com
efrenhask@brandeis.edu
'''

class TreeNode:

    def __init__(self, val = None):
        self._val = val
        self._leftChild = None
        self._rightChild = None


    #set left child of root node
    def set_left(self,leftChild): 
        self._leftChild = leftChild

    #set right child of root node
    def set_right(self,rightChild): 
        self._rightChild = rightChild

    #get left child
    def get_left(self):
        return self._leftChild

    #get right child
    def get_right(self):
        return self._rightChild

   #set node's value: necessary when initializing a node object
    def set_val(self,val):
        self._val = val

    def get_val(self):
        return self._val

