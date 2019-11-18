def PrintOutput(myString):
    return "OUTPUT " + myString

def LoadFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n", "")

    file.close()
    return lines
