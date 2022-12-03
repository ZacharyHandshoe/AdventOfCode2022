import string
from collections import Counter


def getScore(char):
    if char.isupper():
        return string.ascii_uppercase.index(char) + 27
    else:
        return string.ascii_lowercase.index(char) + 1


lines = []
with open("inputDay03.txt", "r") as file:
    lines = file.readlines()

totalScore = 0
lineCount = 0
lineNumber = 0
while lineNumber < len(lines):
    # Get the next 3 lines
    line01 = lines[lineNumber].replace("\n", "")
    line02 = lines[lineNumber + 1].replace("\n", "")
    line03 = lines[lineNumber + 2].replace("\n", "")
    # Use a set to find the shared character
    finalSet = "".join((set(line01).intersection(line02)).intersection(line03))

    totalScore += getScore(finalSet)
    lineNumber += 3


print(totalScore)
