import sys

class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        pop_object = None
        if self.isEmpty():
            pop_object = 0
        else:
            pop_object = self.stack.pop()
            
        return pop_object
            
    def top(self):
        top_object = None
        if self.isEmpty():
            top_object = 0
        else:
            top_object = self.stack[-1]
            
        return top_object
            
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty

T = int(sys.stdin.readline())

for i in range(T):
    ans = "YES"
    stack = Stack()
    string = sys.stdin.readline()
    for k in string:
        if k == "(":
            stack.push("(")
        elif k == ")":
            if stack.pop() == 0:
                ans = "NO"
    if stack.top() != 0:
        ans = "NO"

    print(ans)
    