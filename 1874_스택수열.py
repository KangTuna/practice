import sys
from collections import deque

dq = deque()

N = int(input().rstrip())
exam = []
for _ in range(N):
    exam.append(int(input().rstrip()))
idx = 1
index = 0
ans = []
while True:
    if len(dq) == 0:
        dq.append(idx)
        idx += 1
        ans.append('+')
    else:
        if exam[index] == dq[-1]:
            dq.pop()
            index += 1
            ans.append('-')
            if index == len(exam):
                break
        else:
            dq.append(idx)
            idx += 1
            ans.append('+')
    if idx > N+1:
        break

if ans.count('-') == N:
    for i in ans:
        print(i)
else:
    print('NO')
