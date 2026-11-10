def digit_count(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


number = int(input("Number: "))
print(digit_count(number))
