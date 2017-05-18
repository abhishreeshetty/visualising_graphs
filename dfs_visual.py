import networkx as nx
import matplotlib.pyplot as plt


dfs_stk=[] #A list that stores all the DFS Forest's

 
#~~functions used by DFS~~#
def DFSUtil(G, v, visited,sl): 
	visited[v]= True
	sl.append(v) #and appends it to the stack list 
	for i in G[v]:
		if visited[i] == False:
			DFSUtil(G, i, visited,sl)
		return sl
 
 
def DFS(G,source): 
	global dfs_stk
	visited =[False]*(len(G.nodes()))
 	sl=[]
	dfs_stk.append(DFSUtil(G,source, visited,sl))
	for i in range(len(G.nodes())):
		if visited[i] == False:
			sl=[]
			dfs_stk.append(DFSUtil(G, i, visited,sl))

				
#~~INPUT~~#

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



#~~ Graph creation with weights on the edges~~#
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



#~~DFS Traversal~~#
DFS(G,source)
#marks all edges traversed through DFS with red
for i in dfs_stk:
	if(len(i)>1):
		for j in i[:(len(i)-1)]:
			if i[i.index(j)+1] in G[j]:
				nx.draw_networkx_edges(G,pos,edgelist=[(j,i[i.index(j)+1])],width=8,alpha=0.5,edge_color='r')
			else:
				for k in i[1::-1]: #if in case the path was reversed coz all the possible neighbours were visited, we need to find the adj path now!
					if k in G[j]:
						nx.draw_networkx_edges(G,pos,edgelist=[(j,k)],width=8,alpha=0.5,edge_color='r')
						break

plt.show()
