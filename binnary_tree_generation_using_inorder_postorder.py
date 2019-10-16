# generates a binary tree from inorder and postorder traversal
from sys import stdin

 
# Binary Tree Class
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def find_left(inorder, postorder, pivot, start, end):
	# it finds all the nodes which are left of the parent(pivot)

	# finds it in inorder-way
	new_inorder = []
	new = set() # for optimisation for search in postorder-way
	for i in range(start, end + 1):
		if inorder[i] != pivot:
			new_inorder.append(inorder[i])
			new.add(inorder[i])
		else:
			break

	# finds it in postorder-way
	new_postorder = []
	for i in range(start, end + 1):
		if postorder[i] in new: # being optimised since new is a set
			new_postorder.append(postorder[i])

	return new_inorder, new_postorder


def find_right(inorder, postorder, pivot, start, end):
	# it finds all the nodes which are left of the parent(pivot)

	# finds it in inorder-way
	new_inorder = []
	new = set() # for optimisation for search in postorder-way
	for i in range(start, end + 1):
		if inorder[i] == pivot:
			for j in range(i + 1, end + 1):
				new_inorder.append(inorder[j])
				new.add(inorder[j])
			break
	
	# finds it in postorder-way
	new_postorder = []
	for i in range(start, end + 1):
		if postorder[i] in new:
			new_postorder.append(postorder[i])

	return new_inorder, new_postorder


def buildit(inorder, postorder, start, end):

	# buildit fundtion recursively build the tree
	parent = TreeNode(postorder[end]) # last node of postorder traversal is root(parent)

	# gets the left part
	new_inorder, new_postorder = find_left(inorder, postorder, postorder[end], start, end)
	# generates the left subtree
	if len(new_inorder) > 0:
		parent.left = buildit(new_inorder, new_postorder, 0, len(new_inorder) - 1)

	# gets the right part
	new_inorder, new_postorder = find_right(inorder, postorder, postorder[end], start, end)
	# generates the right subtree
	if len(new_inorder) > 0:
		parent.right = buildit(new_inorder, new_postorder, 0, len(new_inorder) -1)

	return parent


# to test....inorder traversal
def inorder(root):
	if root is None:
		return 
	
	inorder(root.left)
	print(root.val)
	inorder(root.right)


# main starts
inord = [ 7, 5, 6, 2, 3, 1, 4 ]
postord = [ 5, 6, 3, 1, 4, 2, 7 ]
parent = buildit(inord, postord, 0, len(inord) - 1)
inorder(parent)