def sieveoferatosthenes(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers
num = int(input("Enter a number: "))
print("following prime number are those ones that are less than or equal to", num)
primes = sieveoferatosthenes(num)
print(primes)