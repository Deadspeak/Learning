#losowe liczby do lotto
from random import randint
#x = 0
#
#while x < 6:
#    b = randint(1,49)
#    x = x + 1
#    print(b)
#
#print("Nowa linia \n")
wylosowane = []

def losowe():
    a = randint(1,49)
    return a

#przypisywanie wylosowanej liczby do tablicy
b = len(wylosowane)
while b < 6:
    a = losowe()
    wylosowane.append(a)
    b = b+1

print(wylosowane)
