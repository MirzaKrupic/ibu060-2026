def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year):
    if month == 2:
        if is_leap(year):
            return 29
        return 28
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31


month = int(input("Month: "))
year = int(input("Year: "))
print("Days:", days_in_month(month, year))
