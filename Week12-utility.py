# https://github.com/bpshearer19/csci102-wk12-git
# Brett Shearer
# CSCI 102 - Section B
# Week 12 Part B

def PrintOutput(myString):
    return "OUTPUT " + myString

def LoadFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")

    file.close()
    return lines

def UpdateString(original, replacement, index):
    return "OUTPUT " + original[:index] + replacement + original[index + 1:]

def FindWordCount(myList, myString):
    count = 0
    for element in myList:
        if element == myString:
            count += 1
    return count

def ScoreFinder(players, scores, name):
    name = name.upper()
    for i in range(len(players)):
        if players[i].upper() == name:
            return "OUTPUT " + players[i] + " got a score of " + str(scores[i])
    return "OUTPUT player not found"

def Union(scores, players):
    newList = scores + players
    return newList

def Intersection(players, players2):
    newList = []
    for player in players:
        if player in players2:
            newList.append(player)
    return newList

def NotIn(myList, myList2):
    newList = []
    for player in myList:
        if player not in myList2:
            newList.append(player)
    return newList
