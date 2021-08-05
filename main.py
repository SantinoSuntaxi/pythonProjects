# read data.txt with line break
# dataUser = []
# with open('user.txt') as g:
#     for lineUser in g:
#         dataUser.append(lineUser)
#
# print(dataUser)
dataUser = []
dataUserLength = 0
dataResult = []
def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words
dataUser = readFile('user.txt')
dataUserNotFound = dataUser

print(dataUser)
# dataUserLength = len(dataUser)
# print(dataUserLength)

with open('data.txt') as f:
    for line in f:
        nineChars = line[0:9]
        if nineChars in dataUserNotFound:
            dataUserNotFound.remove(nineChars)
            dataResult.append(line)
        else:
            print("")

print(dataResult)
print(dataUserNotFound)
       #print(nineChars)

# f = open("result.txt", "w")
# f.write("dataResult")
# f.close()

outF = open("result.txt", "w")
for line in dataResult:
  # write line to output file
  outF.write(line)
outF.close()

outF = open("result.txt", "a")
for line in dataUserNotFound:
  # write line to output file
  outF.write(line)
  outF.write("\n")
outF.close()