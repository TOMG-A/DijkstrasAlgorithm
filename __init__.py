import math
from djikstra.node import *
import timeit



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
# A.append(B,3)
# A.append(D,5)
# B.append(E,7)
# C.append(F,4)
# D.append(H,2)
# D.append(E,6)
# E.append(C,2)
# E.append(F,3)
# F.append(G,1)
# H.append(E,4)
# H.append(G,5)
# H.append(I,6)
# I.append(J,1)
# G.append(J,4)
# GRAPH=Graph([A,B,C,D,E,F,G,H,I,J])


def Dijkstra(Graph:Graph,source:Node):
    q=[]
    dist={}
    prev={}
    def sorter(e):
        return dist[str(e)]
    for v in Graph:
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
    return dist,prev,timeit.default_timer()


