# linked list implementation in python


# generic node class
class Node:
	def __init__(self):
		self.data = None
		self.link = None


# linked list class
class LinkedList:
	def __init__(self):
		# head of the linked list
		self.head = None
		# for size of the linked list
		self.size = 0
		# for implementing iteration
		self.iterator = self.head

	# making linked list iterable
	def __iter__(self):
		self.iterator = self.head
		return self

	def __next__(self):
		if self.iterator == None:
			raise StopIteration
		else:
			data =  self.iterator.data
			self.iterator = self.iterator.link
			return data

	# insert at the front, time complexity O(1)
	def insert(self, item):
		new = Node()
		new.data = item
		new.link = self.head
		self.head = new
		self.size += 1

	# returns the size of the linked list
	def __len__(self):
		return self.size

	# deletes a node from the front side(head side)
	def pop(self):
		if self.size > 0:
			self.head = self.head.link
			self.size -= 1
		else:
			raise Exception("cannot pop from empty list")

	
# main start
mylist = LinkedList()
for i in range(1, 10):
	mylist.insert(i)
for i in mylist:
	print(i)