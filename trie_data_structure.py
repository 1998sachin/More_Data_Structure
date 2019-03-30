# implementing basic trie data structure 
# support 1. Insert 2. Search 3. Delete operation
# Resource: Tushar Roy's video lecture Youtube


class Trie_node:
	def __init__(self):
		# stores the chilren of trie node in dictionary
		self.children = dict()
		# to mark if its the end of word in the trie
		self.word_finished = False


def insert(root, string):
	node = root

	for c in string:		
			if c in node.children: 	# time complexity is the length of the dictionary, O(no of unicode character)
				node = node.children[c]
			else:
				new = Trie_node()
				node.children[c] = new
				node = new

	node.word_finished = True


def search(root, string):
	node = root
	for c in string:
		if c in node.children:
			node = node.children[c]
		else:
			return False

	if node.word_finished is True:
		return True
	else:
		return False


def delete(root, string):
	node = root
	stack = [] 	# using a stack to avoid recursive implementation
	for c in string:
		if c in node.children:
			stack.append([node, c])
			node = node.children[c]
			
		else:
			print("string does not exist")
			return

	if node.word_finished is True:
		while len(node.children) == 0 and len(stack) > 0:
			node, key = stack.pop()
			del node.children[key]
	else:
		print("string does not exist")



# main starts
root = Trie_node()
insert(root, 'sactry')
delete(root, 'sach')