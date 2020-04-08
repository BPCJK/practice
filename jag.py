# mama's first script
import os


def printMama(num):
    print("Mama " + str(num))
    val = num / 2.0
    return val


print(os.getcwd())
printMama(3)

for i in range(1, 10):
    printMama(i)

mamaList = [
    "Mama",
    "Jag",
    "Jag",
    "Jag",
    "Jag4",
    "Jag2",
]