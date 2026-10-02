# Ask user for a year
year = int(input("Enter a year: "))
# leap year:
# if it is divisible by 4 but not by 100 or divisible by 400
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    # it is a leap year
    print("Leap year")
# else
else:
    # it is not a leap year
    print("No leap year")
