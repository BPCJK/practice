# mama's first script
import os


def printMama(num):
    print("MSou " + str(num))
    val = num / 2.0
    return val


print(os.getcwd())
printMama(3)

for i in range(1, 10):
    printMama(i)

for j in range(10):
    print(10)

mamaList = [
    "Mama",
    "Jag",
    "Sou",
    "Jag",
    "Jag4",
    "Jag2",
]