from os import path, listdir, remove                             #import to check if file exists, count, files, delete files
from random import randint

meowFiles = listdir("meow-poems")                                #delete files in new directory if 10 or more
if len(meowFiles) >= 10:
    for file in meowFiles:
        remove(f"meow-poems/{file}")

fileList = listdir("poems")                                      #select a random file from the "poems" directory
fileNum = randint(0, len(fileList) - 1)
inputFile = fileList[fileNum]
originalFile = open(f"poems/{inputFile}", "r")                    #open in read mode
print(f"File opened: {inputFile}")                                

while(True):
    newFileName = f"{input('What do you want to call your new text file? (do not include .txt) ')}.txt"
    if path.exists(f"meow-poems/{newFileName}"): 
        print("File already exists. Please select a new name")          #handle conflicting file names
    else:
        break

newFile = open(f"meow-poems/{newFileName}", "w")                        #create new file in write mode

lines = originalFile.readlines()                                  #parse lines from each file

for line in lines:                                                #split lines into lists of words
    wordList = line.split()                                         
    lineLength = len(wordList)
    if lineLength != 0:
        for i in range(lineLength):
            if i % randint(1, lineLength - 1) == randint(0, 1):
                newFile.write(wordList[i] + " MEOW ")              #write method returns length, in bytes, of string written
            else:
                newFile.write(wordList[i] + " ")
        newFile.write("\n")

newFile.close()                                                  #always close files!
originalFile.close()                                             #alternatively, use a with statement - it will automatically close files after running
