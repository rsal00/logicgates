#
# Logic Gates Program
#

def AND(x: int, y: int):
    return x and y

def OR(x: int, y: int):
    return x or y

def NOT(x: int):
    if (x == 0):
        return x + 1
    else:
        return x * 0

def NAND(x: int, y: int):
    return NOT(AND(x, y))

def NOR(x: int, y:int):
    return NOT(OR(x, y))

def XOR(x: int, y: int):
    if (x == y):
        return 0
    return OR(x, y)

def XNOR(x: int, y: int):
    return NOT(XOR(x, y))

print("1) AND\n2) OR\n3) NOT\n4) NAND\n5) NOR\n6) XOR\n7) XNOR")
gateChoice = input("Choose a gate: ")

xstr = ''
ystr = ''

while (True):
    xstr = input("x: ")
    if (gateChoice != '3'):
        ystr = input("y: ")

    if ((xstr == '0' or xstr == '1') and (ystr == '0' or ystr == '1')):
        break;

    print("Invalid input!! Try again...\n")

if (gateChoice == '1'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", AND(x, y))
elif (gateChoice == '2'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", OR(x, y))
elif (gateChoice == '3'):
    x = int(xstr)
    print("\nOUTPUT:", NOT(x))
elif (gateChoice == '4'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", NAND(x, y))
elif (gateChoice == '5'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", NOR(x, y))
elif (gateChoice == '6'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", XOR(x, y))
elif (gateChoice == '7'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", XNOR(x, y))
elif (gateChoice == '8'):
    x = int(xstr)
    y = int(ystr)
    print("\nOUTPUT:", XORR(x, y))
else:
    print("Invalid input!! Try again...\n\n")
