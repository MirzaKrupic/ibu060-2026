n = int(input("Number: "))
is_prime = True
for d in range(2, n):
    if n % d == 0:
        is_prime = False
        break
if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")
