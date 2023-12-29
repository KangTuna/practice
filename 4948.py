def prime_arr(N):
        prime = [True for i in range(N+1)]
        prime[0] = False
        prime[1] = False

        for i in range(N+1):
            if prime[i] == True:
                j = 2
                while i*j <= N:
                    prime[i*j] = False
                    j += 1
        return prime

while True:
    N = int(input())
    if N == 0:
        break

    prime = prime_arr(2*N)
    prime = [x for x in range(N+1,2*N+1) if prime[x] == True]
    print(len(prime))
    