import random 

name_str = input(" Give me your name: ")

names = name_str.split(", ")

name_len = len(names)

selected = random.randint(0, (name_len - 1))

selected_person = names[selected]

print(f" {selected_person} is going to pay today. ")
print(selected)
print(name_len)