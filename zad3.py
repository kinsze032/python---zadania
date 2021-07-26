import math
sumaOcen = 0
liczba = int(input("Podaj ilosc wprowadzanych ocen:"))

for ocena in range(0,liczba):
    i = float(input("Wpisz ocenę ocenę: "))
    sumaOcen = sumaOcen + i
    srednia = sumaOcen/liczba
    
    if srednia >= 2.8 and srednia < 3.3:
        print("Uzyskujesz ocenę: dst")
    elif srednia >= 3.3 and srednia < 3.8:
        print("Uzyskujesz ocenę: dst +")
    elif srednia >= 3.8 and srednia < 4.3:
        print("Uzyskujesz ocenę: dobry")
    elif srednia >= 4.3 and srednia < 4.8:
        print("Uzyskujesz ocenę: dobry +")
    elif srednia >= 4.8 and srednia < 5.3:
        print("Uzyskujesz ocenę: bdb")
        
print("Twoja srednia to: ", srednia)




import math

oceny = []
liczba = int(input("Podaj ilosc wprowadzanych ocen:"))

    #zbieraj podane liczby w tablicy
for ocena in range(0,liczba):
    i = float(input("Wpisz ocenę: "))
    oceny.append(i)
       
        #srednia to suma liczba w tablicy podzielona przez ilosc tych liczb
    srednia = sum(oceny)/liczba
    
    if srednia >= 2.8 and srednia < 3.3:
        print("Uzyskujesz ocenę: dst")
    elif srednia >= 3.3 and srednia < 3.8:
        print("Uzyskujesz ocenę: dst +")
    elif srednia >= 3.8 and srednia < 4.3:
        print("Uzyskujesz ocenę: dobry")
    elif srednia >= 4.3 and srednia < 4.8:
        print("Uzyskujesz ocenę: dobry +")
    elif srednia >= 4.8 and srednia < 5.3:
        print("Uzyskujesz ocenę: bdb")
    
        
print("Twoja srednia to: ", srednia) 
