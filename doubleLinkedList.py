class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class doubleLinkedList:
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
    
    def pop(self):
        if self.length == 0:
            return None
        oldTail = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            oldTail.prev = None
        self.length -= 1
        return oldTail

    def prepend(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def popFirst (self):
        previousHead = self.head
        self.head = self.head.next
        previousHead.next = None
        self.head.prev = None
        return previousHead    

firstDoubleLinkedList = doubleLinkedList(10)
firstDoubleLinkedList.append(15)
firstDoubleLinkedList.append(20)
firstDoubleLinkedList.prepend(5)
firstDoubleLinkedList.prepend(0)
firstDoubleLinkedList.popFirst()
firstDoubleLinkedList.printList()

