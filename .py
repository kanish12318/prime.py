def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n):
    return sum(int(d) for d in str(n))


num = int(input("Enter a number: "))

if is_prime(num) and is_prime(sum_of_digits(num)):
    print(num, "is a prime number and the sum of its digits is also prime.")
else:
    print(num, "is not a special prime number.")
