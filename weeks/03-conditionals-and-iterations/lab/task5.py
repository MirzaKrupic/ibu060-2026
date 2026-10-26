a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == b and b == c:
    kind = "equilateral"
elif a == b or b == c or a == c:
    kind = "isosceles"
else:
    kind = "scalene"
print("Triangle:", kind)
