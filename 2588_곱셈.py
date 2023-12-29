import sys

input = sys.stdin.readline

A,B = map(int,input().rstrip().split())
ans = A*B
baek = B//100
B %= 100
sib = B//10
B %= 10
il = B

three = A*baek
four = A*sib
five = A*il

print(three)
print(four)
print(five)
print(ans)

