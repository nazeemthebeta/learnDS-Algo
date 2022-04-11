class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print (currentNode.value)
            currentNode = currentNode.next

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next            
        self.length += 1
    
    def pop(self):
        if self.length == 0:
            return None
        currentNode = self.head
        previousNode = self.head
        while currentNode.next is not None:
            previousNode = currentNode
            currentNode = currentNode.next
        self.tail = previousNode
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
        return currentNode

    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            previousHead = self.head
            self.head = newNode
            self.head.next = previousHead
        self.length += 1

    def popFirst (self):
        previousHead = self.head
        self.head = self.head.next
        return previousHead.value

    def get(self, index):
        if self.length <= index or index < 0:
            return None
        currentNode = self.head
        for _ in range(index):
            currentNode = currentNode.next
        return currentNode
    
    def setValue(self, index, value):
        currentNode = self.get(index)
        if currentNode is not None:
            currentNode.value = value
            return True
        return False
    
    def insert(self, index, value):
        newNode = Node(value)
        if self.length <= index or index < 0:
            return None
        currentNode = self.head
        for _ in range(index-1):
            currentNode = currentNode.next
        previousNextNode = currentNode.next
        currentNode.next = newNode
        newNode.next = previousNextNode




first = linkedList(10)
first.append(15)
first.append(20)
first.prepend(5)

first.insert(1,12)
first.printList()