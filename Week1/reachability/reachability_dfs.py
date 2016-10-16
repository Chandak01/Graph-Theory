#Uses python3

import sys
visited = []
isin = []   #list of all those vertices which are reachable from x
def explore(v):
    visited.append(v)
    isin.append(v)
    for w in adj[v]:
        if not w in visited:
            explore(w)   
def dfs(adj,n):
    for v in adj[x]:
        if not v in visited:
            explore(v)
def reach(adj, x, y,n):
    isin.append(x)
    visited.append(x)
    dfs(adj,n)
    if y in isin:        #checking whether y is reachable from x or not
        print("Yes")
    else:
        print("no")

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2] # n=no of vertices and m=no of edges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2])) # results edges=[(v1,v2),(v1,v3),.........(vi,vj)], where there is an edge between vi and vj
    x, y = data[2 * m:] #whether there exit path between x and y
    adj = [[] for i in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    reach(adj, x, y,n)
#enter ctrl+D after entering the input 