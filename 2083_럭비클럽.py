import sys

input = sys.stdin.readline

while True:
    name,age,weight = input().rstrip().split()
    age = int(age)
    weight = int(weight)
    if name == '#' and age+weight == 0:
        break
    if age>17 or weight >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')

