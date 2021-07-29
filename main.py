# read data with line break
# dataUser = []
# with open('user') as g:
#     for lineUser in g:
#         dataUser.append(lineUser)
#
# print(dataUser)

def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words

dataUser = readFile('user')
print(dataUser)

with open('data') as f:
    for line in f:
        nineChars = line[0:9]
        print(nineChars)

f = open("result", "w")
f.write("hola Paul")
f.close()

