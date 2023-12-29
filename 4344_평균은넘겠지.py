import sys

input = sys.stdin.readline

N = int(input().rstrip())

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

for _ in range(N):
    data = list(map(int,input().rstrip().split()))
    n = data.pop(0)
    avg = sum(data)/len(data)
    up = 0
    for i in data:
        if i > avg:
            up += 1
    ans = roundTraditional((up/n)*100,3)
    print(f'{ans:.3f}%')