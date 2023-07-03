import random

letters = ['J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A', 'T' ,'S','R','Q','P'
,'O','N','M','L' ,'K','d' ,'c','b' ,'a','Z' ,'Y','X' ,'W','V' ,'U',
'n','m','l','k','j','i','h','g','f','e','x','w','v','u','t','s','r','q','p','o','z','y']
numbers = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
symbols = ['}', '{',']','[','@','?','/','*',')','(']

print("Password generator.")

letnmbr = int(input("How many letters?"))
nmbrnmbr = int(input("How many letters?"))
symnmbr = int(input("How many letters?"))

rndlet = []

for a in range(0, letnmbr):
    b = random.randrange(0, 52)
    print(b)
    rndlet.append(letters[b])
    print(rndlet)
print(rndlet)

rndnm = []

for c in range(0, nmbrnmbr):
    d = random.randrange(0, 10)
    print(d)
    rndnm.append(numbers[d])
    print(rndnm)
print(rndnm)

rndsym = []

for e in range(0, symnmbr):
    f = random.randrange(0, 10)
    print(f)
    rndsym.append(symbols[f])
    print(rndsym)
print(rndsym)

total_pass = rndlet + rndsym + rndnm

total_length = letnmbr + nmbrnmbr + symnmbr

print(total_pass)

pass_part1 = []
pass_part2 = []

for p in range(0, total_length, 2):
    pass_part1.append(total_pass[p])
    
print(pass_part1)

for k in range(1, total_length, 2):
    pass_part2.append(total_pass[k])

final_pass = pass_part2 + pass_part1

for m in final_pass:
    print(m, end='')

