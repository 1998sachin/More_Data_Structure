# Iterative Inorder Binary Tree Traversal
# Source: Tushar Roy Youtube video
# Time Complexity is O(number of nodes)
# Space Complexity is O(max height in the tree)


# defining the structure of tree node
class TreeNode:
	# typical node structure of binary tree
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None



# Iterative Inorder Traversal
def iterative_inorder(root):
	# 	if root is null 
	if root == None:
		return

	mystack = []   # to store the nodes
	while True:
		if root != None:
			mystack.append(root)
			root = root.left  # going to the left
		else:
			if len(mystack) == 0:
				break
			else:
				# no more left
				root = mystack.pop()
				'''
					one can any thing here
					I am printing the node
				'''
				print(root.data)

				root = root.right 	# going to the right


# main starts
'''
	tree structure
				  1
			   /	 \
			  2       3
			 / \     / \
			4   5   6   7		
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

iterative_inorder(root)
