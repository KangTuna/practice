import sys

class Queue():
    def __init__(self,n):
        self.queue = [x for x in range(1,n+1)]
        
    def push(self, data):
        self.queue.append(data)
        
    def pop(self,k):
        pop_object = None
        if self.isEmpty():
            pop_object = -1
        else:
            pop_object = self.queue.pop(k-1)
            
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

N,K = map(int,sys.stdin.readline().rstrip().split())

queue = Queue(N)
i = -1
arr = []
while queue.size() > 1:
    i += K
    if i >= N:
        i = i%N
    arr.append(queue.pop(i))

print(arr)