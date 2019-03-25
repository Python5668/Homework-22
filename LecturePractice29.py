"""
Lecture 29 Singly Linked List 1
"""
class Node:
	def __init__(self, data):
		self.data = data # kind of like 'int info'
		self.next = None # Setting the node pointing to null

class linkedList:
	def __init__(self):
		self.head = None # Setting the head pointer pointing to null

	def append(self, data):
		newNode = Node(data) # Creating a new node
		if self.head == None: # Case one, if the head pointer is pointing to null (list is empty)
			self.head = newNode # setting the head pointer to the newNode
			return
		else: # Case two
			lastNode = self.head # Make a duplicate of the head pointer
			while lastNode.next != None: # If the pointer is still not reaching the real 'lastNode' yet, just keep moving it forward
				lastNode = lastNode.next
			lastNode.next = newNode
			print(data, 'appended onto the list')
		# Once lastNode pointer reaches the real 'lastNode', connect the lastNode.next pointer to the newNode to complete the 'Append' method

	def prepend(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			return
		else:
			newNode.next = self.head # Points the new node to the old head
			self.head = newNode # resets the head pointer to the new node
			print(data, 'prepended into the list')

	def insertAfterNode(self, prevNode, data):
		if self.head == None:
			print(); print("The list is empty, so there's nothing to insert after"); print()
		else:
			newNode = Node(data)
			newNode.next = prevNode.next # points to the node infront of the one you want to insert after
			prevNode.next = newNode # resets the pointer to point to the newNode
			print(data,  'added after another node')

	def printList(self):
		if self.head == None:
			print(); print('Cannot print an empty list'); print()
		else:
			curNode = self.head
			print(); print('List Begins')
			while curNode.next != None:
				print(curNode.data)
				curNode = curNode.next
			print(curNode.data)
			print('List Ends'); print()

	def deleteNode(self, key):
		curNode = self.head # make a duplicate of the head pointer
		if curNode != None and curNode.data == key:
			self.head = curNode.next
			curNode = None
			print(key,'Deleted')
			return
		else:
			prev = None
			while curNode != None and curNode.data != key:
				prev = curNode
				curNode = curNode.next
			if curNode == None:
				print(key, 'was not found in the list'); print()
				return
			else:
				prev.next = curNode.next
				curNode = None
				print(key, 'Deleted')

## Tests
lst = linkedList()
lst.printList()
lst.append(2); lst.append(4); lst.append(6); lst.append(8)
lst.printList()
lst.deleteNode(8)
lst.printList()
lst.insertAfterNode(lst.head.next, 5)
lst.prepend(10)
lst.printList()
lst.deleteNode(2); lst.deleteNode(10); lst.deleteNode(4); lst.deleteNode(6); lst.deleteNode(5)
lst.printList()
