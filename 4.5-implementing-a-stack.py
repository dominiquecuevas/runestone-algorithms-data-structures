class Stack:
    """
    LIFO
    use the built-in data structure list
    choosing to use the end of the list to push/pop
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return not self.items

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())