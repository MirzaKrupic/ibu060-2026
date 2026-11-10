def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


limit = int(input("Limit: "))
for n in range(2, limit + 1):
    if is_prime(n):
        print(n)
