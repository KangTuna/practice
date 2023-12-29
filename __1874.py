import sys
class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        pop_object = None
        if self.isEmpty():
            pop_object = -1
        else:
            pop_object = self.stack.pop()
            
        return pop_object
            
    def top(self):
        top_object = None
        if self.isEmpty():
            top_object = -1
        else:
            top_object = self.stack[-1]
            
        return top_object
            
    def isEmpty(self):
        is_empty = 0
        if len(self.stack) == 0:
            is_empty = 1
        return is_empty

    def size(self):
        return len(self.stack)
stack = Stack()
N = sys.stdin.readline().rstrip()
arr = []
for i in N:
    arr.append(sys.stdin.readline().rstrip())

for i in range(arr[0]):
    stack.push(i+1)
    