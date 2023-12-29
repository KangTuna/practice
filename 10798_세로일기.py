import sys

input = sys.stdin.readline

data = []
for _ in range(5):
    data.append(input().rstrip())

ans = []

for j in range(15):
    for i in range(5):
        try:
            ans.append(data[i][j])
        except:
            pass

for i in ans:
    print(i,end="")
    
