import random

data = ["Manchester", "Barcelona", "Riyadh", "Torino", "Madrid"]
selectCity = random.choice(data)
print(selectCity)


displayList = ['_'] * len(selectCity)
print(displayList)

totScore = 3
totLen = len(selectCity)
while True:
    makeGuess = input("Make a guess: ")
    hanger = False
    for char in  range(len(selectCity)):
        if makeGuess == selectCity[char] and displayList[char] == "_":
            hanger = True 
            displayList[char] = makeGuess 
            totLen -= 1
            break
    if not hanger: 
        totScore -= 1 
    if not totScore or not totLen:
        break

    print(displayList)
if not totLen:
    print(("You won!"))
else:
    print("You Lost")