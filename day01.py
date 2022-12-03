# Create the elf counts
lines = []
elfCounts = [[]]
with open("inputDay01.txt", "r") as file:
    lines = file.readlines()

current = []
for line in lines:
    if line == "\n":
        elfCounts.append(current)
        current = []
    else:
        current.append(int(line.replace("\n", "")))

# Sum the elf counts
sums = []
for count in elfCounts:
    sums.append(sum(count))

sums.sort()
print(sums)
print(69528 + 68878 + 67746)
