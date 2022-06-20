#losowe liczby do lotto
import random

wylosowane = []
# losowanie liczby z zakresu
def losowe():
    a = random.sample(range(1,50), 6)
    return a


print(losowe())