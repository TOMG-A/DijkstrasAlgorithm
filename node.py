## Basic Node/Graph Implementations

class Node:
    def __init__(self,name):
        self.children=[]
        self.name=name
    def append(self,child,cost):
        self.children.append([child,cost])
    def __str__(self):
        return self.name

class Graph:
    def __init__(self,nodes:list):
        self._Vertices=nodes
        self.current=0
    def append(self,node:Node):
        self._Vertices.append(node)

    ## Makes class subscriptable
    def __getitem__(self,item):
        return self._Vertices[item]
    ## Allows for iteration over class as if it is an array
    def __iter__(self):
        for x in self._Vertices:
            yield x