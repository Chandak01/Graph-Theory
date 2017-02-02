import sys
high = 100000000
def prim(adj,cost,n,s):
	total_wt=0
	dist = []
	final_dist = []
	for i in range(s):
		dist.append(high)
		final_dist.append(high)
		
	dist.append(0)
	final_dist.append(0)
	
	for i in range(s+1,n):
		dist.append(high)
		final_dist.append(high)
		
	for _ in range(n):
		u = min(dist)
		
		index_of_min = dist.index(u)
		
		total_wt+=u
		dist[index_of_min]=high+1
		
		for element in range(len(adj[index_of_min])):
			
			if dist[adj[index_of_min][element]] != high+1:
				
				if dist[adj[index_of_min][element]]>cost[index_of_min][element]:
					
					dist[adj[index_of_min][element]]=cost[index_of_min][element]  
	print(total_wt)
	
if __name__=="__main__":
	input = sys.stdin.readline()
	n,m = map(int,input.split())
	adj = [[] for _ in range(m)]
	cost = [[] for _ in range(m)]
	for i in range(m):
		input = sys.stdin.readline()
		u,v,w = map(int,input.split())
		adj[u-1].append(v-1)
		adj[v-1].append(u-1)
		cost[u-1].append(w)
		cost[v-1].append(w)
	s = int(sys.stdin.readline())-1
	prim(adj,cost,n,s)
