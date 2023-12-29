import sys

input = sys.stdin.readline

def trans(n,type):
    if type == 'kg':
        return round(n * 2.2046,4),'lb'
    elif type == 'lb':
        return round(n * 0.4536,4),'kg'
    elif type == 'l':
        return round(n * 0.2642,4),'g'
    elif type == 'g':
        return round(n * 3.7854,4),'l'
    
n = int(input().rstrip())

for _ in range(n):
    a,b = input().rstrip().split()
    a = float(a)
    a,b = trans(a,b)
    print(f'{a:.4f} {b}')