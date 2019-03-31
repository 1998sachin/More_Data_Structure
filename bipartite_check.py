'''input
'''
# code to check bipartite graph, complexity is O(n + m) 
from sys import stdin, stdout
from collections import defaultdict, deque


def check_bipartite(graph, set_a, set_b):

	visited = dict()  # visited dictionary
	for i in range(1, n + 1):
		visited[i] = False

	myq = deque()
	myq.append(1)
	set_a[1] = 1  # coloring the first vertex

	while len(myq) > 0:
		node = myq.popleft()
		visited[node] = True
		
		for i in graph[node]:
			if visited[i] == False:
				if set_a[node] == 1: 
					set_b[i] = 1
				else:
					set_a[i] = 1

				if set_a[i] == 1 and set_b[i] == 1:  # checking if vertex belongs to both the sets
					return False
				
				myq.append(i) # appending the child of node to queue

	return True


# main starts
n, m = list(map(int, stdin.readline().split())) # n is number of vertices, m is number of edges
graph = defaultdict(list) # to store adjacent vertices in list format

# taking input in the form u, v (edge from vertex u to v)
for _ in range(m):
	u, v = list(map(int, stdin.readline().split()))
	graph[u].append(v)
	graph[v].append(u)

# two sets for two colors
set_a = [0] * (n + 1)
set_b = [0] * (n + 1)

if check_bipartite(graph, set_a, set_b):
	print('graph is bipartite')
else:
	print('graph is not bipartite')