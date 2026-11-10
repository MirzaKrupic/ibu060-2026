grade = lambda s: "Pass" if s >= 50 else "Fail"

score = int(input("Enter your score: "))
print("Result:", grade(score))
