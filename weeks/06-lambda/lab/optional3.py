apply_twice = lambda f, x: f(f(x))
add3 = lambda n: n + 3
double = lambda n: n * 2

x = int(input("Number: "))
print("Add 3 twice:", apply_twice(add3, x))
print("Double twice:", apply_twice(double, x))
