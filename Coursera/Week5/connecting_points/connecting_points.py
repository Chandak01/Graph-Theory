#Uses python3
import sys
import math
def distance(x1,y1,x2,y2):
	sq1 = (x1-x2)*(x1-x2)
	sq2 = (y1-y2)*(y1-y2)
	return math.sqrt(sq1+sq2)

def minimum_distance(dist,n):
	e=[]   # e contains the index of pairs which share edge
	mini_distance=0
	sameset = [[] for _ in range(n)] #if ith indexed point share edge with jth indexed point then i contain j and vice versa
	for i in range(n):
		sameset[i].append(i)
	while len(e)<n-1:
		mini_edge=1000000
		for i in range(n):
			for j in range(n):
				if(dist[i][j]<mini_edge):
					if((not j in sameset[i]) and (not i in sameset[j])):
						mini_edge=dist[i][j]
						I,J = i,j
		
		sameset[I].append(J)
		sameset[J].append(I)
		for i in range(n):
			if I in sameset[i]:
				sameset[i].append(J)     #if i share edge with j and j share edge with k then list of i contain j and as well as k, hence so does j contains i and k
			if J in sameset[i]:
				sameset[i].append(I)
		mini_distance=mini_distance+mini_edge
		e.append((I,J))
	return mini_distance

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	dist = [[] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			dist[i].append(distance(x[i],y[i],x[j],y[j]))
	print("{0:.9f}".format(minimum_distance(dist,n)))
