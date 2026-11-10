cube = lambda n: n * n * n
print(cube(3) - cube(1))

diff = lambda a, b: a - b
print(diff(10, 4))
print(diff(4, 10))

size = lambda n: "Big" if n > 9 else "Small"
print(size(9), size(10))

nums = [5, 2, 8]
print(sorted(nums, key=lambda n: -n))
