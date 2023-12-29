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

T = int(sys.stdin.readline().rstrip()) # 횟수 받기
stack = Stack() 
for i in range(T):
    try:
        order = sys.stdin.readline().rstrip() 
        command,Z = order.split() # push 일떄 
        Z = int(Z)
    except:
        command = order # push 이외 다른거일때
    if command == "push": 
        stack.push(Z)
    elif command == "pop":
        print(stack.pop())
    elif command == "size":
        print(stack.size())
    elif command == "empty":
        print(stack.isEmpty())
    elif command == "top":
        print(stack.top())

