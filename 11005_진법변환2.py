import sys

input = sys.stdin.readline

def change_i_to_s(i):
    if i < 10:
        return i
    else:
        return chr(i + 55)

n,b = map(int,input().rstrip().split())
ans = []
for i in range(31,-1,0-1):
    count = b**i
    ans.append(n//count)
    n %= count

while True:
    if ans[0] == 0:
        ans.pop(0)
    else:
        break

ans = list(map(change_i_to_s,ans))
for i in ans:
    print(i,end = '')


