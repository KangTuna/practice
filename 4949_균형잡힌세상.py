import sys
from collections import deque

deq = deque()
input = sys.stdin.readline

while True:
    deq.clear()
    ans = "yes"
    string = input().rstrip()
    if string == ".":
        break
    else:
        for i in string:
            if i == "(" or i == "[":
                deq.append(i)
            if i == ")":
                try:
                    check = deq.pop()
                    if check == "[":
                        ans = "no"
                        break
                except:
                    ans = "no"
                    break
            elif i == "]":
                try:
                    check = deq.pop()
                    if check == "(":
                        ans = "no"
                        break
                except:
                    ans = "no"
                    break
        if len(deq) != 0:
            ans = "no"
        print(ans)