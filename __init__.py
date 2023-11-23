import math
from djikstra.node import *



## Test Graph
# A = Node("A")
# B = Node("B")
# C = Node("C")
# D = Node("D")
# E = Node("E")
# F = Node("F")
# G = Node("G")
# H = Node("H")
# I = Node("I")
# J = Node("J")
# A.add_child(B,3)
# A.add_child(D,5)
# B.add_child(E,7)
# C.add_child(F,4)
# D.add_child(H,2)
# D.add_child(E,6)
# E.add_child(C,2)
# E.add_child(F,3)
# F.add_child(G,1)
# H.add_child(E,4)
# H.add_child(G,5)
# H.add_child(I,6)
# I.add_child(J,1)
# G.add_child(J,4)
# GRAPH=Graph([A,B,C,D,E,F,G,H,I,J])


def Dijkstra(Graph:Graph,source:Node):
    q=[]
    dist={}
    prev={}
    def sorter(e):
        return dist[str(e)]
    for v in Graph.Vertices:
        dist[str(v)]=math.inf
        prev[str(v)]=None
        q.append(v)
    dist[str(source)]=0

    while len(q) > 0:
        q.sort(key=sorter)
        u=q.pop(0)
        for v in u.children:
            if v[0] in q:
                alt=dist[str(u)]+v[1]
                if alt < dist[str(v[0])]:
                    dist[str(v[0])]=alt
                    prev[str(v[0])]=u
    return dist,prev


