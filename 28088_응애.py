import sys

input = sys.stdin.readline

N,M,K = map(int,input().rstrip().split())

data = [False for _ in range(N)]

for _ in range(M):
    i = int(input().rstrip())
    data[i] = True
for _ in range(K):
    tf = []
    for i in range(len(data)):
        if data[i] == True:
            tf.append(i)
    
    for k in tf:
        if data[k] == True:
            data[k] = False
        else:
            data[k] = True
        up = (k+1) % N
        down = (k-1) % N
        if data[up] == True:
            data[up] = False
        else:
            data[up] = True
        
        if data[down] == True:
            data[down] = False
        else:
            data[down] = True
            
            
    
print(data.count(True))