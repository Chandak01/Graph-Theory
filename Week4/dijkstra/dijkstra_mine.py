#Pyhton3
import sys
dist=[]
sptSet = [] #when len(sptSet)==n then all points are assigned their minimum distance, hence it is to check that all edges have been relaxed
SUMOFCOST=0
high=1000000
def minn(list):
	minitem=high+1
	for i in range(len(list)):
		if ((-1<list[i]<minitem)):
			if list[i]<SUMOFCOST:
				minitem = list[i]
				minindex = i
	return minitem,minindex
def minimumdistance(l1,l2):
	#we need to return vertex and its distance from list dist, the vertex should not be present in sptSep
	list3 = []
	for item in l1:
		if item in l2: 
			list3.append(-1)
		else:
			list3.append(item)
	dis,u = minn(list3)
	return dis,u


def dijkstra(adj,s,n):
	for u in range(s):
		dist.append(high)
	dist.append(0)
	for u in range(s+1,n):
		dist.append(high)
	while(len(sptSet)<n):
		dis,u = minimumdistance(dist,sptSet)  #u is having shortest distance
		sptSet.append(u)
		for i in range(len(adj[u])):
			if(dis+cost[u][i]<dist[adj[u][i]]): #dis = dist[u]
				dist[adj[u][i]]=dis+cost[u][i]
	for i in range(n):
		if dist[i]>SUMOFCOST:
			dist[i]=-1

def shortestpath(adj,cost,s,t,n):
	dijkstra(adj,s,n)
	return dist[t]

if __name__=='__main__':
	input = sys.stdin.read()
	data = list(map(int,input.split()))
	n,m = data[:2]
	data = data[2:]
	edges = list(zip(zip(data[0:3*m:3],data[1:3*m:3]),data[2:3*m:3]))
	data=data[3*m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((u,v),w) in edges:
		adj[u-1].append(v-1)
		cost[u-1].append(w)
		SUMOFCOST=SUMOFCOST+w
	s,t = data[0]-1,data[1]-1
	print(shortestpath(adj,cost,s,t,n))



	

