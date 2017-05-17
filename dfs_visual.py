import networkx as nx
import matplotlib.pyplot as plt




from collections import defaultdict
 

dfs_stk=[] #A list that stores all the DFS Forest's

class Graph:
 
	
	def __init__(self):
		self.graph = defaultdict(list)
 
	def addEdge(self,u,v):
		self.graph[u].append(v)
 
	# A function used by DFS
	def DFSUtil(self, v, visited,sl):
 
		# Mark the current node as visited 
		visited[v]= True
		sl.append(v) #and appends it to the stack list 
 
		# Recur for all the vertices adjacent to
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited,sl)
		return sl
 
 
	# The function to do DFS traversal using recursive fn
	def DFS(self,source):
		V = len(self.graph)  #total nodes
		global dfs_stk
 
		# Mark all the vertices as not visited
		visited =[False]*(V)
 
		
		sl=[]
		dfs_stk.append(self.DFSUtil(source, visited,sl))

		for i in range(V):
			if visited[i] == False:
				sl=[]
				dfs_stk.append(self.DFSUtil(i, visited,sl))
				


print ("Enter Number of Vertices:")
n = int(input())
wtMatrix = []

print ("Enter The Weight Matrix:")
#PS for not connected vetices put any negative number
for i in range(n):
	list1 = list(map(int,input().split(' ')))
	wtMatrix.append(list1)

print (wtMatrix)


print ("Enter Source Vertex:")
source = int(input())

print ("Weighted Graph creation:")



g = Graph()

#creates graph from the input weight matrix
for i in range(n):
	for j in range(n):
		if wtMatrix[i][j]>0:
			g.addEdge(i,j)


 
print "Following is Depth First Traversal"
g.DFS(source)

#prints the DFS traversal stack onto the terminal
for i in dfs_stk:
	print i


G = nx.Graph()


#draws the weighted graph 
for i in range(n) :
	for j in range(n) :
		if wtMatrix[i][j]>0 :
			G.add_edge(i,j,weight=wtMatrix[i][j]) 



pos = nx.spring_layout(G)
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels,edge_color='r',alpha=0.5 )    #prints weight on all the edges

#marks all edges traversed through DFS with red
for i in dfs_stk:
	if(len(i)>1):
		for j in i[:(len(i))-1]:
			nx.draw_networkx_edges(G,pos,edgelist=[(j,i.index(j)+1)],width=8,alpha=0.5,edge_color='r')

plt.show()