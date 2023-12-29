import sys

input = sys.stdin.readline

n = int(input().rstrip())
while n != -1:
    factors = []
    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
    factors = list(set(factors))
    factors.sort()
    sum1 = sum(factors)
    if n == sum1:
        factors = map(str,factors)
        string = ' + '.join(factors)
        print(f'{n} = {string}')
    else:
        print(f'{n} is NOT perfect.')
    n = int(input().rstrip())
