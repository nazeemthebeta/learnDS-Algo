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
        if self.length == 0:
            return None
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            oldHead.next = None
        self.length -= 1
        return oldHead 

    def get(self, index):
        if self.length <= index or index < 0:
            return None
        currentNode = self.head
        if index <= self.length/2:
            for _ in range(index):
                currentNode = currentNode.next
        else:
            currentNode = self.tail
            for _ in range(self.length-1, index, -1):
                currentNode = currentNode.prev
        return currentNode.value
    
    def setValue(self, index, value):
        currentNode = self.get(index)
        if currentNode is not None:
            currentNode.value = value
            return True
        return False

firstDoubleLinkedList = doubleLinkedList(10)
firstDoubleLinkedList.append(15)
firstDoubleLinkedList.append(20)
firstDoubleLinkedList.prepend(5)
firstDoubleLinkedList.prepend(0)

print(firstDoubleLinkedList.get(4))
