# mama's first script
import os


def printMama(num):
    print("Mama is back " + str(num))
    val = num / 2.0
    return val


print(os.getcwd())
printMama(3)

for i in range(1, 10):
    printMama(i)

mamaList = [
    "Mama",
    "Jag",
    "Sou",
    "Jag",
    "Jag4",
    "Jag2",
    "Jsdfgsvag",
    "Jag4dsfgf",
]

for j in range(2, 10):
    printMama(i)