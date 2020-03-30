import sys

sysArgs = sys.argv[1:]

def rectifyString(inputString):
    inputString = inputString.replace ("\"", "\\\"")
    return (inputString)
    
def convertFile(fileName, outputFile):
    f = open(fileName, "r")
    lines = f.readlines()
    mystr = "".join([line.strip() for line in lines])
    mystr = "document.write(\""+rectifyString(mystr)+"\");"
    outFile = open(outputFile, "w")
    outFile.write(mystr)

convertFile(sysArgs[0], sysArgs[1])