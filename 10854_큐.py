import sys

class Queue():
    def __init__(self):
        self.queue = []
        
    def push(self, data):
        self.queue.append(data)
        
    def pop(self):
        pop_object = None
        if self.isEmpty():
            pop_object = -1
        else:
            pop_object = self.queue.pop(0)
            
        return pop_object
            
    def front(self):
        front_object = None
        if self.isEmpty():
            front_object = -1
        else:
            front_object = self.queue[0]
            
        return front_object

    def back(self):
        back_object = None
        if self.isEmpty():
            back_object = -1
        else:
            back_object = self.queue[-1]
            
        return back_object
            
    def isEmpty(self):
        is_empty = 0
        if len(self.queue) == 0:
            is_empty = 1
        return is_empty

    def size(self):
        return len(self.queue)

N = int(sys.stdin.readline())
queue = Queue()
for i in range(N):
    try:
        data = sys.stdin.readline().rstrip()
        command,Z = data.split()
        Z = int(Z)
    except:
        command = data

    if command == 'push':
        queue.push(Z)
    elif command == 'pop':
        print(queue.pop())
    elif command == 'size':
        print(queue.size())
    elif command == 'front':
        print(queue.front())
    elif command == 'back':
        print(queue.back())
    elif command == 'empty':
        print(queue.isEmpty())