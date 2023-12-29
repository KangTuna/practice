import sys

input = sys.stdin.readline

data = input().rstrip()

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
     'u','v','w','x','y','z']

dict1 = {}

for i in a:
    dict1[i] = 0

for i in data:
    dict1[i] += 1

for i in a:
    print(dict1[i],end = ' ')