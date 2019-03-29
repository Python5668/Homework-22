"""
Lecture(s): 29, 30, & 31 combined
This covers Linked Lists and various functins that can be utilized for linked lists
"""
## Lecture 29
class Node:
    def __init__(self, data):
        self.data = data # kind of like 'int info'
        self.next = None # Setting the node pointing to null
        
class linkedList:
    def __init__(self):
        self.head = None # Setting the head pointer pointing to null
        
    def append(self, item):
        newNode = Node(item) # creating a new node
        if self.head == None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            print('<', item, 'appended into the list >')
            return
        
    def prepend(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
            print('<' ,item, 'prepended into the list >')
            return
        
    def printList(self):
        if self.head == None:
            print('The list is empty!')
        else:       
            current = self.head
            print('Start:')
            while current != None:
                print(current.data)
                current = current.next
            print('Finish')

    def deleteNode(self, key):
        current = self.head
        if current != None and current.data == key:
            self.head = current.next
            current = None
            print('<', key, 'deleted >')
            return
        else:
            prev = None
            while current != None and current.data != key:
                prev = current
                current = current.next
            if current == None:
                print('Item was not found in list!')
                return
            else:
                prev.next = current.next
                current = None
                print('<', key, 'deleted >')
## Lecture 30
    def deleteAtPos(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            current = None
            print('< 1st item deleted >')
            return
        else:
            cnt = 0
            prev = None
            while current != None and cnt != pos:
                prev = current
                current = current.next
                cnt += 1
            if current == None:
                print('Invalid position!')
                return
            else:
                print(current.data, 'has been deleted from the list')
                prev.next = current.next
                current = None
                return

    def len_iterative(self):
        cnt = 0
        current = self.head
        while current != None:
            current = current.next
            cnt += 1
        print('Length currently is:', cnt)
        return

    def swapNode(self, key1, key2):
        if key1 == key2:
            print("Don't need to swap identical values")
            return
        else:
            prev1 = None
            current1 = self.head
            while current1 != None and current1.data != key1:
                prev1 = current1
                current1 = current1.next
            
            prev2 = None
            current2 = self.head
            while current2 != None and current2.data != key2:
                prev2 = current2
                current2 = current2.next
                
            if current1 == None and current2 == None:
                print('One or both of these nodes were not found in the list!')
                return
            else:
                if prev1 == None:
                    self.head = current2
                    prev2.next = current1
                elif prev2 == None:
                    self.head = current1
                    prev1.next = current2
                else:
                    prev1.next = current2
                    prev2.next = current1
                    
                temp1 = current1.next
                temp2 = current2.next
                current1.next = temp2
                current2.next = temp1
                
    def reverse_interative(self):
        prev = None
        current = self.head
        while current != None:
            nxt_temp = current.next
            current.next = prev
            prev = current
            current = nxt_temp
        self.head = prev
        print('List reversed')
## Lecture 31
    def remove_duplicates(self):
        prev = None
        current = self.head
        data_freq = dict()
        while current != None:
            if current.data not in data_freq:
                data_freq[current.data] = 1
                prev = current
                current = current.next
            else:
                prev.next = current.next
                current = None
            current = prev.next
            
    def print_nth_from_last(self, n): # Fixed
        total_len = self.len_iterative()
        distance = total_len -1
        current = self.head
        while current != None:
            if distance == n-1:
                print(current.data)
                return
            else:
                distance -= 1
                current = current.next
    
    def occurances(self, data): # Fixed
        cnt = 0
        current = self.head
        while current != None:
            if current.data == data:
                cnt += 1
            current = current.next
        return cnt
    
    def rotate(self, k): # Still buggy
        p = self.head
        q = self.head
        prev = None
        prev2 = None
        cnt = 0
        while p != None and cnt < k:
            prev = p
            p = p.next
            cnt += 1
        p = prev
        
        while q != None:
            prev2 = q
            q = q.next
        q = prev2
        
        self.head = p.next
        q.next = prev
        prev = self.head
        prev.next = p
        
    def tail_to_head(self): # Still buggy, I wasn't able to figure out how to get the tail's next to point to the head without getting an error.
        lastNode = self.head
        secondLast = None
        while lastNode.next != None:
            secondLast = lastNode
            lastNode = lastNode.next
        secondLast.next = self.head
        self.head = lastNode
        secondLast.next = None
        

lst = linkedList()
lst.append('A'); lst.append('B'); lst.append('C'); lst.append('D')
lst.printList()
lst.tail_to_head()
#lst.swapNode(1,8)
lst.printList()