import math
from dijkstra.node import *
import timeit

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
