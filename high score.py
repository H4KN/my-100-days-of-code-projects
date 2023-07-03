scores = input("enter students scores: ").split()

for n in range(0, len(scores)):
    scores[n] = int(scores[n])
    
max = scores[0]

for n in range(0, len(scores)):
    if n <= (len(scores) - 2):
        if max >= scores[n + 1]:
            max = max

        elif max < scores[n + 1]:
            max = scores[n + 1]
    else:
        max = max
print(max)










