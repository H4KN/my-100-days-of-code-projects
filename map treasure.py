row1 = ["😶", "😶", "😶"]
row2 = ["😶", "😶", "😶"]
row3 = ["😶", "😶", "😶"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

choice = input("choose your position: ")

row = int(choice[0])
column = int(choice[1])

map[column - 1][row - 1] = "X"

print(f"{row1}\n{row2}\n{row3}\n")