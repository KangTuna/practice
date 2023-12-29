M,N = map(int,input().split())
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

prime = prime_arr(N)
prime = [x for x in range(M,N+1) if prime[x] == True]

for i in prime:
    print(i)