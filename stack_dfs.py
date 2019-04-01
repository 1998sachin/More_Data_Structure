'''input
'''
# dfs using stack list, will be helpful if there is a recursion limit.

from sys import stdin, stdout
from collections import defaultdict, deque


def simulation(graph, visited, node, function_stack):
	'''
	this function simulate the calling during dfs traversal
	'''
	while True:
		'''
		condition for breaking the loop, all the adjacent nodes of 'node' has been traversed
		'''
		if len(function_stack) == 0: 
			break
		
		node = function_stack.pop()
		visited[node] = True
		
		for i in graph[node]:
			# traversing the neighbours(children) of node

			flag = 0 # this stores if there are any neighbour(child) of node, 0 means no neighbour
			if visited[i] == False:

				'''
				when one neighbour(child) is traversed completely and others remain
				this helps in identifying the parent
				'''
				function_stack.append(node) 

				# it will become node in next iteration, equivalent to calling dfs(graph, i)
				function_stack.append(i)
				
				flag = 1 # node has a child
				break

		# when no neighbour(child) remains 
		if flag == 0:
			'''
			place your code here
			'''
			print(node)
		

def dfs_using_stack(graph, n):
	# initialing the visited dictionary
	visited = dict()
	for i in range(1, n + 1):
		visited[i] = False

	# call stack is maintained using list function_stack
	function_stack = []
	for i in range(1, n + 1): # loop to check every vertex:
		if visited[i] == False and len(graph[i]) > 0: # second condition is not required if the graph is connected
			function_stack.append(i)
			simulation(graph, visited, i, function_stack)
				

# main starts
n, m = list(map(int, stdin.readline().split()))
graph = defaultdict(list) # defaultdict

# initializing every vertex, not necessary if the graph is connected
for i in range(1, n + 1):
	graph[i]

# taking graph input
for _ in range(m):
	u, v = list(map(int, stdin.readline().split()))
	graph[u].append(v)
	graph[v].append(u)

dfs_using_stack(graph, n)