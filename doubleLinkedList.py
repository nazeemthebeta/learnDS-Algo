class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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
            newNode.prev = self.tail
            self.tail = self.tail.next            
        self.length += 1
    