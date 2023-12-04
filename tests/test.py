from djikstra import *

#### Test Graph
## Instantiate nodes
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
J = Node("J")

## Create edges between nodes
A.append(B,3)
A.append(D,5)
B.append(E,7)
C.append(F,4)
D.append(H,2)
D.append(E,6)
E.append(C,2)
E.append(F,3)
F.append(G,1)
H.append(E,4)
H.append(G,5)
H.append(I,6)
I.append(J,1)
G.append(J,4)

## Instantiate graph
GRAPH=Graph([A,B,C,D,E,F,G,H,I,J])
dist,prev,time=Dijkstra(GRAPH,A)
print(dist)
