import sys
high = 1000000
minus_infinite_distance = []
no_path = []
import queue
def negative_cycle(adj,n):
	q = queue.Queue()
	for _ in range(n-1):
		for ((u,v),w) in edges:
			if(dist[v-1]>dist[u-1]+w):
				dist[v-1]=dist[u-1]+w
	distchange=[]
	for i in range(len(dist)):
		distchange.append(dist[i])
	for ((u,v),w) in edges:
		if(distchange[v-1]>distchange[u-1]+w):
			distchange[v-1]=distchange[u-1]+w
	for v in range(n):
		if dist[v]!=distchange[v]:
			minus_infinite_distance.append(v)
		if dist[v]==high:
			no_path.append(v)
	for v in range(n):
		if dist[v]==high:
			no_path.append(v)
	for i in range(n):
			if i in minus_infinite_distance:
					print("-")
			elif i in no_path:
					print("*")
			else:
				print(dist[i])

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
	negative_cycle(adj,n)
