#Uses python3

import sys
import queue
high=1000000 #assuming there are nodes no more than 100000
max_dist=0 #maximum distance from source
dist=[] #distance of a node from source
code=[] #let '1' and '-1' be two code of vertices across an edge
vertices_on_island=[]
isbipartite=2
def bfs(adj,s,n):
    dist[s]=0
    code[s]=1 #let source be coded as '1'
    q = queue.Queue(n)
    q.put(s)
    vertices_on_island.append(s)
    while not q.empty():
        u=q.get()
        for v in adj[u]:        
            if dist[v]==high:
                q.put(v)
                vertices_on_island.append(v)
                dist[v]=dist[u]+1
                code[v]=(-1)*code[u]  #vertice v and u will have opposite code if they share an edge
                max_dist=dist[v]
                vertices_on_island.append(v)

def bipartite(adj):
    if isbipartite==-1:
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    for s in range(n):
        dist.append(high)
        code.append(0) #initially all have code = 0
    for s in range(n):
        if dist[s]>=n:      #will be true once at starting i.e. at s=0 if there is one island,will be true as no of times as the no of islands
            bfs(adj,s,n) 
            for (u,v) in edges:
                if ((u-1 in vertices_on_island) and (v-1 in vertices_on_island)):
                    if code[u-1]==code[v-1]:
                        isbipartite=-1
                        break
            for item in vertices_on_island[:]:
                vertices_on_island.remove(item)
        if isbipartite==-1:
            break
    print(bipartite(adj))
