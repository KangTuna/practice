import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    blank = input()
    person_count = int(input().rstrip())
    count = 0
    for i in range(person_count):
        count += int(input().rstrip())
    if count % person_count == 0:
        print('YES')
    else:
        print('NO')
