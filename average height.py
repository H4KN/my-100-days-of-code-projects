heights = input("enter students height: ").split()

print(heights)

for n in range(0, len(heights)):
    heights[n] = int(heights[n])
print(n)
print(heights)

sum = 0

for height in heights:
    sum = height + sum
print(sum)

average = sum / (n + 1)

print(f"average is {average}")