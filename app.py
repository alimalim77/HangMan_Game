import random
import stage

data = ["Manchester", "Barcelona", "Riyadh", "Torino", "Madrid"]
selectCity = random.choice(data)
print(selectCity)


displayList = ['_'] * len(selectCity)
print(displayList)

wordDict = stage.alphaPlace(selectCity)



lives = 6
dashes = len(selectCity)
while True:
    makeGuess = input("Make a guess: ")
    hanger = False
    if makeGuess in wordDict and wordDict[makeGuess] == 0:
        print("You have already consumed the maximum occurence of this character!")
    for char in  range(len(selectCity)):
        if makeGuess == selectCity[char] and displayList[char] == "_":
            hanger = True 
            displayList[char] = makeGuess 
            wordDict[makeGuess] -= 1
            dashes -= 1
            break
    
    if not hanger: 
        lives -= 1 
        print(stage.stages[lives])
    if not lives or not dashes:
        break

    print(displayList)
if not dashes:
    print(("You won!"))
else:
    print("You Lost")