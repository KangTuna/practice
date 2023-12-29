import sys

input = sys.stdin.readline

string = input().rstrip()
vo  = ['a', 'e', 'i', 'o', 'u']
while string != '#':
    temp = 0
    string = string.lower()
    for i in vo:
        temp += string.count(i)
    print(temp)
    string = input().rstrip()
    
