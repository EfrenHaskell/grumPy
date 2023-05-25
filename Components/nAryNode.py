'''
nAryNode stores a value and sibling count pair siblings keeps track of how many children a node has
'''


class nAryNode:

    def __init__(self,val,assemb_equiv:str,siblings:int = 0):
        self._siblings = siblings # number of siblings connected to a node
        self._val = val
        self._assemb_equiv:str = assemb_equiv

    #return value of node
    def get_val(self):
        return self._val

    #return number of siblings of node
    def get_siblings(self) -> str:
        return self._siblings

    #return assembly equivalent of specific token
    def get_assembly(self) -> str:
        return self._assemb_equiv
