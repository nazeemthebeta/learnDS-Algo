class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1

    def printStack(self):
        currentNode = self.top
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
    
    def push(self, value):
        newNode = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1
        return True
    
    def pop (self):
        if self.height == 0:
            return None
        oldTop = self.top
        self.top = oldTop.next
        oldTop.next = None
        self.height -= 1
        return oldTop




firstStack=Stack(10)
firstStack.push(15)
firstStack.push(20)
firstStack.pop()
firstStack.printStack()