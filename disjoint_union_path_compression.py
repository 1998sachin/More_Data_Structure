# disjoint union find using path compression
# source Tushar Roy: Youtube
# time complexity is O(m) where m is the number of operations
from collections import defaultdict


# creates a size dictionary where size[i] = 1 (i being the node).
# Size will be used as rank of the node
def create_size(graph):
	size = dict()
	for i in graph:
		size[i] = 1
	return size


# creates a link dictionary that will serve as the representative of the set.
def create_link(graph):
	link = dict()
	for i in graph:
		link[i] = i
	return link


# find function, it returns the link(parent) of node i
# recursively return for path compression
def find(node, link):
	if link[node] == node:
		return node
	
	link[node] = find(link[node], link)
	return link[node]
	

# same function checks if two nodes belong to the same set or not
def same(a, b, link):
	return find(a, link) == find(b, link)


# unite function joins two set
def unite(a, b, link, size):
	a = find(a, link)
	b = find(b, link)

	if size[a] < size[b]:
		size[b] += size[a]
		link[a] = b
	else:
		size[a] += size[b]
		link[b] = a
	return


# main starts
graph =  defaultdict(list)
for i in range(1, 8):
	graph[i]

# essential steps
size = create_size(graph)
link = create_link(graph)

# unite operation
unite(1, 2, link, size)
unite(2, 3, link, size)
unite(4, 5, link, size)
unite(6, 7, link, size)
unite(5, 6, link, size)
unite(3, 7, link, size)
unite(3, 7, link, size)
