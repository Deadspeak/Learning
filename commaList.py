#Comma list    

import random

spam1 = ['jabłka', 'banany', 'tofu', 'koty']

def comma(items):
    for i in range(len(items) -2):
        print(items[i], end=", ")
    print(items[-2] + ' and ' + items[-1])


print(comma(spam1))  
