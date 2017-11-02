import random
zakres= range(1,49)
LosoweLiczby = tuple(random.sample(zakres,6))

WybraneLiczby = [0,0,0,0,0,0]
try:
    for i in range (6):
        WybraneLiczby[i]= int(input("podaj {} liczbę: ".format(i+1)))
        if WybraneLiczby[i] <1 or WybraneLiczby[i]>=49:
            print ("liczba nie zawiera sie w zakresie 1-49!")
            break
    print ("Wybrane liczby to : {}".format(WybraneLiczby))
except ValueError:
    print ("podawaj liczby z zakresu 1-49!")