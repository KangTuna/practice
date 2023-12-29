prime = [True for i in range(10001)]
prime[0] = False
prime[1] = False

for i in range(101):
    if prime[i] == True:
        j = 2
        while i*j <= 10000:
            prime[i*j] = False
            j += 1


T = int(input())

prime = [x for x in range(10001) if prime[x] == True]
prime_set = set(prime)
for i in range(T):
    N = int(input())
    N_list = [(x,N-x) for x in prime if N-x in prime_set]
    index = len(N_list)
    if index % 2 == 0:
        index = int(index / 2 - 1)
        print(N_list[index][0],N_list[index][1])
    else:
        index = int(index / 2)
        print(N_list[index][0],N_list[index][1])
            