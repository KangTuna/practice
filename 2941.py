word = input()

count = len(word)
for i in word:
    if i == "=":
        count -= 1
    elif i == "-":
        count -= 1
print(count)
while True:
    if "lj" in word:
        word = word.replace("lj","a",1)
        count -= 1
    else:
        break
print(count)

while True:
    if "nj" in word:
        word = word.replace("nj","a",1)
        count -= 1
    else:
        break
print(count)

while True:
    if "dz=" in word:
        word = word.replace("dz=","a",1)
        count -= 1
    else:
        break

print(count)
