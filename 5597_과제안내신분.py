import sys

yes = []
no = []
for _ in range(28):
    yes.append(int(sys.stdin.readline().rstrip()))
yes = set(yes)
for i in range(1,31):
    if i in yes:
        continue
    else:
        no.append(i)

for i in no:
    print(i)
