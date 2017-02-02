#link to the problem statement https://www.hackerrank.com/challenges/bfsshortreach


import sys
import queue
high = 100000

def bfs(adj,n,s,dist):
	for _ in range(s):
		dist.append(high)
	dist.append(0)
	for _ in range(s+1,n):
		dist.append(high)
	q = queue.Queue(n)
	q.put(s)
	while not q.empty():
		u = q.get()
		for v in adj[u]:
			if dist[v]==high:
				q.put(v)
				dist[v] = dist[u]+6
def distance(adj,n,s,dist):
	bfs(adj,n,s,dist)
	for i in range(s):
		if dist[i]<high:
			print(dist[i],end=' ')
		else:
			print(-1,end=' ')
	for i in range(s+1,n):
		if dist[i]<high:
			print(dist[i],end=' ')
		else:
			print(-1,end=' ')
	print()

if __name__=="__main__":
	input = sys.stdin.readline()
	T = int(input)
	while T>0:
		input = sys.stdin.readline()
		n,m = map(int,input.split())
		adj = [[] for _ in range(n)]
		dist = []
		for _ in range(m):
			input = sys.stdin.readline()
			u,v = map(int,input.split())
			adj[u-1].append(v-1)
			adj[v-1].append(u-1)
		s = int(sys.stdin.readline())
		distance(adj,n,s-1,dist)
		T=T-1


