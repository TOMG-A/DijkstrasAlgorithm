## Basic Node/Graph Implementations

class Node:
    def __init__(self,name):
        self.children=[]
        self.name=name
    def add_child(self,child,cost):
        self.children.append([child,cost])
    def __str__(self):
        return self.name

class Graph:
    def __init__(self,nodes:list):
        self.Vertices=nodes
        self.current=0
    def append(self,node:Node):
        self.Vertices.append(node)
    def __getitem__(self,item):
        return self.Vertices[item]
    def __iter__(self):
        for x in self.Vertices:
            yield x