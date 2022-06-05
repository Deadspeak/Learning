
def collatz(number):
    
    if number % 2 == 0:
        print(number //2)
        return number // 2
    else:
        print(3 * number +1)
        return 3 * number +1
    


def dzielenie():
    print('Type number:')
    try:
        liczba = int(input())
        while collatz(liczba) > 1:
            liczba = collatz(liczba) 
            print(liczba)
        print(collatz(liczba))
    except :
        print('Error chuju podaj liczbe!!!!')

    

dzielenie()