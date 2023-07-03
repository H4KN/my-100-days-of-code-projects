print("Funny love calculator!!!")

name1 = (input("enter your name: ")).lower()
name2 = (input("enter their name: ")).lower()

name3 = name1 + name2

T = name3.count("t")
R = name3.count("r")
U = name3.count("u")
E = name3.count("e")

a = str(T + R + U + E)

L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")

b = str(L + O + V + E)

score = int(a + b)

if score < 10 or score > 90:
    print("score < 10 or score > 90")
elif score > 40 and score < 50:
    print("score > 40 and score < 50")
else:
    print("else")


