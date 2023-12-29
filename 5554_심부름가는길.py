import sys

input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())
d = int(input().rstrip())

temp = a+b+c+d

ans1 = temp//60
ans2 = temp%60
print(ans1)
print(ans2)