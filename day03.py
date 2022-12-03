import string


def getCompartments(line):
    line = line[0 : len(line) - 1]  # removes the \n
    middle = int(len(line) / 2)  # gets middle inital
    return [line[0:middle], line[middle:]]


def getScore(char):
    if char.isupper():
        return string.ascii_uppercase.index(char) + 27
    else:
        return string.ascii_lowercase.index(char) + 1


lines = []
with open("inputDay03.txt", "r") as file:
    lines = file.readlines()

totalScore = 0
for line in lines:
    sacks = getCompartments(line)
    for char in sacks[0]:
        if char in sacks[1]:
            totalScore += getScore(char)
            break
print(totalScore)