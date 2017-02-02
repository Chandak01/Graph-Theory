
import operator
#for i in range(n):
	#sameset.append(i)
def root(parent,a):
	while parent[a]!=a:
		a = parent[a]
	return a

def union(parent,a,b):
	root_a = root(parent,a)
	root_b = root(parent,b)
	parent[root_a]=root_b

def find(parent,a,b):
	#print("root(a)root(b)",root(parent,a),root(parent,b))
	if root(parent,a)==root(parent,b):
		return 1
	return 0


n,m=map(int,input().strip().split())
vertex_cost=[]
parent = []
for i in range(n):
	parent.append(i)
for i in range(m):
	u,v,w=map(int,input().strip().split())
	vertex_cost.append((u-1,v-1,u-1+v-1,w)) #to sort the list by multiple elements first by w and by summation of verices
vertex_cost.sort(key = operator.itemgetter(3,2)) #sort the list first by w and by summation of vertices
#print(vertex_cost)
total_weight=0
for (u,v,_,w) in vertex_cost:
	#print("u,v",u,v)
	if find(parent,u,v)!=1:
		#print("yesu,v",u,v)
		total_weight+=w
		union(parent,u,v)
		#print(parent)
print(total_weight)


####################################################################################

#https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
