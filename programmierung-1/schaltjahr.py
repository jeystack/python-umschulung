year = int(input("Enter a year: "))

# leap year: divisible by 4 but not by 100, unless divisible by 400
# (and binds stronger than or, so no parentheses are needed)
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap year")
else:
    print("No leap year")
