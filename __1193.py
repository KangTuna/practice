count = int(input())
max = 1
i = 1 
j = 1
num = 1
while True:
    j = max
    while j != 1:
        num += 1
        if num == count:
            break

        j -= 1
        i += 1
    if num == count:
        break
    i = max
    while i != 1:
        num += 1
        if num == count:
            break
        i -= 1
        j += 1

    if num == count:
        break
    max += 1

print(f"{i}/{j}")
    
