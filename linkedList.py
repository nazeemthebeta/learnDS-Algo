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
        if self.length == 0:
            return None
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            oldHead.next = None
        self.length -= 1
        return oldHead

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
        if self.length < index or index < 0:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        newNode = Node(value)
        currentNode = self.get(index-1)
        nextNode = currentNode.next
        currentNode.next = newNode
        newNode.next = nextNode
        self.length += 1
        return True

    def remove(self, index):
        if self.length <= index or index < 0:
            return False
        elif index == 0:
            return self.popFirst()
        elif index == self.length - 1:
            return self.pop()
        previousNode = self.get(index-1)
        currentNode = previousNode.next
        previousNode.next = currentNode.next
        self.length -= 1
        return currentNode

    def reverse(self):
        nodeSwitcher = self.head
        self.head = self.tail
        self.tail = nodeSwitcher
        afterNode = nodeSwitcher.next
        previousNode = None
        for _ in range(self.length):
            afterNode = nodeSwitcher.next
            nodeSwitcher.next = previousNode
            previousNode = nodeSwitcher
            nodeSwitcher = afterNode

first = linkedList(10)
first.append(15)
first.append(20)
first.prepend(5)
first.popFirst()
first.printList()