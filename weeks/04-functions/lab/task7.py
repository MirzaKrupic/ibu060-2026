def biggest(a, b, c):
    result = a
    if b > result:
        result = b
    if c > result:
        result = c
    return result


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("Biggest:", biggest(a, b, c))
