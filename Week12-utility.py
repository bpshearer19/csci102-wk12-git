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
