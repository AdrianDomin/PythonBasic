import random
zakres= range(1,49)
WybraneLiczby = [0,0,0,0,0,0]
liczbaZakladow = int (input ("podaj liczbe zakładów :"))

jeden= 0
dwa= 0
trzy= 0
cztery= 0
piec= 0
szesc= 0
try:
    for i in range(6):
        WybraneLiczby[i] = int(input("podaj {} liczbę: ".format(i + 1)))
        if WybraneLiczby[i] < 1 or WybraneLiczby[i] >= 49:
            print("liczba nie zawiera sie w zakresie 1-49!")
            break
    WybraneLiczby = set(WybraneLiczby)
    if len(WybraneLiczby) != 6:
        print("Liczby nie mogą sie powtarzać !")
    print("Wybrane liczby to : {}".format(WybraneLiczby))
except ValueError:
    print("podawaj liczby z zakresu 1-49!")


for i in range (liczbaZakladow):
    LosoweLiczby = set(random.sample(zakres, 6))
    trafione = LosoweLiczby.intersection(WybraneLiczby)
    if len(trafione) == 1: jeden += 1
    if len(trafione) == 2: dwa += 1
    if len(trafione) == 3: trzy += 1
    if len(trafione) == 4: cztery += 1
    if len(trafione) == 5: piec += 1
    if len(trafione) == 6: szesc += 1



print ("Wygrane !! ")
print ("jedynka {}".format (jeden))
print ("dwojki {}".format (dwa))
print ("trójki {}".format (trzy))
print("czwórki {}".format (cztery))
print("piątki {}".format (piec))
print("szóstki {}".format (szesc))