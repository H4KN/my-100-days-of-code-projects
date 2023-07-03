print("Welcome to the game@@@@@@@@@@@@@@@@@@@@@@@@@@")

dir = (input("left or right?")).lower()
swm = (input("swim or wait?")).lower()
door = (input("which door?")).lower()

if dir == "left" and swm == "wait" and door == "yellow":
    print("Congrates! you won.")
else:
    print("GAME OVER")
