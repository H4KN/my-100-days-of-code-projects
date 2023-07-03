year = int(input("enter your year: "))

if year % 4 != 0:
    print(" Not a leap year")
if year % 4 == 0:
    if year % 100 != 0:
        print("a leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print("a leap year")
        else:
            print("not a leap year")


