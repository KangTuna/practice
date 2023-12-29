word_list = []
count = int(input())

for i in range(count):
    word_list.append(input())


for j in range(len(word_list)):
    prev = ""
    test = []
    for i in word_list[j]:
        if prev == i:
            continue
        else:
            if i in test:
                count -= 1
                break
            else:
                test.append(i)
        prev = i

print(count)