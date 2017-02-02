#Uses python3
#Shortest path from source to destination

import sys
import queue
high=1000000 #assuming there are nodes no more than 100000
dist=[] #distance of a node from source
def bfs(adj,s,t,n):
    for node in range(s): #setting distance of every node except source from source to be infinite
        dist.append(high)
    dist.append(0)             #setting distance of source from itself to be 0
    for node in range(s+1,n):  #setting distance of every node except source from source to be infinite
        dist.append(high)
    q = queue.Queue(n)
    q.put(s)
    while not q.empty():
        u=q.get()
        for v in adj[u]:        
            if dist[v]==high:
                q.put(v)
                dist[v]=dist[u]+1

def distance(adj, s, d,n):
    bfs(adj,s,t,n)
    if dist[t]<n:
        return dist[t]
    else:
        return -1

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
    s,t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t,n))
#source = coursera/graph