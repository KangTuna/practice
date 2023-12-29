import sys

input = sys.stdin.readline

T = int(input().rstrip())
print('Gnomes:')

for _ in range(T):
    data = list(map(int,input().rstrip().split()))
    if data[0] - data[1] < 0 and data[1] - data[2] < 0:
        print('Ordered')
    elif data[0] - data[1] > 0 and data[1] - data[2] > 0:
        print('Ordered')
    else:
        print('Unordered')
        
        
    
    
