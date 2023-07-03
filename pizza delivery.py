print("Welcome to miami pizza")

size = input("what size?")

add_pepp = input(" do you want pepperoni?")

cheeze = input("do you want extra cheeze?")

bill = 0

if size == "S":
    bill = 15
    if add_pepp == "Y":
        bill += 2
        if cheeze == "Y":
            bill += 1
            print(f" Your bill is {bill}")
        else:
            print(f" Your bill is {bill}")
    else:
        print(f" Your bill is {bill}")

elif size == "M":
    bill = 20
    if add_pepp == "Y":
        bill += 3
        if cheeze == "Y":
            bill += 1
            print(f" Your bill is {bill}")
        else:
            print(f" Your bill is {bill}")
    else:
        print(f" Your bill is {bill}")
elif size == "L":
    bill = 25
    if add_pepp == "Y":
        bill +=3
        if cheeze == "Y":
            bill += 1
            print(f" Your bill is {bill}")
        else:
            print(f" Your bill is {bill}")
    else:
        print(f" Your bill is {bill}")
else:
    print("incorrect input")

