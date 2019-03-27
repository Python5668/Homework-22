"""
Lecture(s): 29, 30, & 31 combined
This covers Linked lists and various functions that can be utilized for linked lists
"""
## Lecture 29
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
			print(data, 'prepended onto the list')

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
			while curNode != None:
				print(curNode.data)
				curNode = curNode.next
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

## Lecture 30				
	def deleteAtPos(self, pos):
		curNode = self.head
		if pos == 0:
			self.head = curNode.next
			curNode = None
			print("Deleted the first position")
			return
		else:
			cnt = 0
			prev = None
			while curNode != None and cnt != pos:
				prev = curNode
				curNode = curNode.next
				cnt += 1
			if curNode == None:
				print("The node doesn't exsist or the position exceeds the length of the list") # Maybe the index is longer than the list
				return
			else:
				print("Entry", curNode.data, "at Position", cnt, "has been deleted")
				prev.next = curNode.next
				curNode = None
				
	def len_iterative(self):
		cnt = 0
		curNode = self.head
		while curNode != None:
			curNode = curNode.next
			cnt += 1
		return cnt
	def len_recursive(self, headNode):
        	if headNode is None:
            		return 0
        	else:
            		return 1+self.len_recursive(headNode.next)
	
	def swapNode(self, key1, key2):
		if key1 == key2:
			print("The two nodes are the same, cannot be swapped")
			return
		else:
			prev1 = None
			curNode1 = self.head
			while curNode1 != None and curNode1.data != key1:
				prev1 = curNode1
				curNode1 = curNode1.next

			prev2 = None
			curNode2 = self.head
			while curNode2 != None and curNode2.data != key2:
				prev2 = curNode2
				curNode2 = curNode2.next
		
			if curNode1 == None and curNode2 == None:
				print("These nodes don't exsist in the list")
				return
			else:
				if prev1 == None: # key1 is in the head node, key2 is not
					self.head = curNode2 # red
					prev2.next = curNode1 # black
				elif prev2 == None: # key2 is in the head node, key1 is not
					self.head = curNode1
					prev1.next = curNode2
				else: # None are the head nodes
					prev1.next = curNode2
					prev2.next = curNode1

				# Sawp the .next pointer
				temp1 = curNode1.next
				temp2 = curNode2.next
				curNode1.next = temp2
				curNode2.next = temp1

	def reverse_interative(self):
		prev = None
		curNode = self.head
		while curNode != None:
			nxt_temp = curNode.next
			curNode.next = prev # flip the .next point to point to the front 
			# Think about why it is not  prev = curNode.nex...
			prev = curNode
			curNode = nxt_temp
		self.head = prev
		print('List reversed')

lst = linkedList()
lst.append('A')
lst.append('B')
lst.append('C')
lst.prepend('D')
lst.printList()
#lst.deleteNode('C')
#lst.deleteAtPos(3)
#print("The length of the list:", lst.len_iterative())
#print("The length of the list:", lst.len_recursive(lst.head))
print("1. swap A and C"); lst.swapNode('A','C')
lst.printList()
print("2. swap A and A"); lst.swapNode('A','A')
lst.printList()
print("3. swap E and F"); lst.swapNode('E','F')
lst.printList()
print("4. swap B and C"); lst.swapNode('B','C')
lst.printList()
print("5. swap A and B"); lst.swapNode('A','B')
lst.printList()
#lst.reverse_interative()
