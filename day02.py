# Read it in
lines = []
with open("inputDay02.txt", "r") as file:
    lines = file.readlines()


# A for rock
# B for paper
# C for Scissors

# X for rock -> 1
# Y for paper -> 2
# Z for scissors -> 3

# 0 for loss
# 3 for a draw
# 6 for a win

# X for lose
# Y for draw
# Z for win

victories = {"A": "Y", "B": "Z", "C": "X"}

loss = {"A": "Z", "B": "X", "C": "Y"}

values = {"X": 1, "Y": 2, "Z": 3}

flip = {"A": "X", "B": "Y", "C": "Z"}


def computeResult(a, b):
    print(a, b)
    if b == "X":  # Lose
        return 0 + values[loss[a]]
    elif b == "Y":
        return 3 + values[flip[a]]
    elif b == "Z":
        return 6 + values[victories[a]]


totalScore = 0
count = 0
for line in lines:
    line.replace("\n", "")
    totalScore += computeResult(line[0:1], line[2:3])


print(totalScore)
