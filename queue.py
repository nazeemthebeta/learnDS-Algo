import queue


class Node():
    def __init__(self,value):
        self.value = value
        self.next  = None

class Queue():
    def __init__(self, value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1
    
    def printQueue(self):
        currentNode = self.first
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        currentNode = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            currentNode.next = None
        self.length -= 1
        return currentNode
