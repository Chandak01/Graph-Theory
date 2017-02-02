import sys
high = 1000000
def negative_cycle(adj,n):
	for _ in range(n-1):
	for ((u,v),w) in edges:
		if(dist[v-1]>dist[u-1]+w):
			dist[v-1]=dist[u-1]+w
	for ((u,v),w) in edges:
		if(dist[v-1]>dist[u-1]+w):
			return 1
	return 0

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int,input.split()))
	n,m = data[:2]
	data=data[2:]
	edges = list(zip(zip(data[0:3*m:3],data[1:3*m:3]),data[2:3*m:3]))
	data = data[3*m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((u,v),w) in edges:
		adj[u-1].append(v-1)
		adj[v-1].append(u-1)
		cost[u-1].append(w)
	s = data[0]-1
	dist=[high]*n
	dist[s]=0
	print(negative_cycle(adj,n))
