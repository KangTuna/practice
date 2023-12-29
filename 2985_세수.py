import sys

input = sys.stdin.readline

a,b,c = map(int,input().rstrip().split())

or1,or2 = '=','='

if a+b == c:
    or1 = '+'
elif a-b == c:
    or1 = '-'
elif a*b == c:
    or1 = '*'
elif a//b == c:
    or1 = '/'
else:
    if a == b+c:
        or2 = '+'
    elif a == b-c:
        or2 = '-'
    elif a == b*c:
        or2 = '*'
    elif a == b//c:
        or2 = '/'

print(f'{a}{or1}{b}{or2}{c}')