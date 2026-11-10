def grade_letter(points):
    if points >= 90:
        return "A"
    elif points >= 80:
        return "B"
    elif points >= 70:
        return "C"
    elif points >= 60:
        return "D"
    else:
        return "F"


points = int(input("Points: "))
print("Grade:", grade_letter(points))
