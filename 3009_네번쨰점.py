import sys

first = tuple(map(int,sys.stdin.readline().rstrip().split()))
second = tuple(map(int,sys.stdin.readline().rstrip().split()))
third = tuple(map(int,sys.stdin.readline().rstrip().split()))
ans = [0,0]
if third[0] == first[0]:
    ans[0] = second[0]
elif third[0] == second[0]:
    ans[0] = first[0]
else:
    ans[0] = third[0]

if third[1] == first[1]:
    ans[1] = second[1]
elif third[1] == second[1]:
    ans[1] = first[1]
else:
    ans[1] = third[1]

for i in ans:
    print(i,end=" ")