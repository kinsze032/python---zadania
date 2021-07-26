# binary_search = wersja z literą "k"
print('Dana jest lista: "h","i", "j", "k", "l", "m", "n","a","b","c", "d", "e","f", "g", "o", "p", "r", "s", "t", "u", "w", "x", "y", "z"')
      
A = ["h","i", "j","k","l", "m", "n","a", "b", "c", "d", "e","f","g", "o", "p", "r", "s", "t", "u", "w", "x", "y", "z"]

     
# sortowanie listy na początku obowiązkowe przy przeszukiwaniu binarnym
A.sort()
print()
szukana = str(input("wpisz literę 'k': ")).lower()  # by przy wpisaniu 'K' odnalazł element


def binary_search(key, lista):

    #poczatkowe zainicjowanie granic szukania
    left = 0
    right = len(lista)-1   # right = 23, bo 24 elementy, ale ostatni index to 23

    #szukaj dopoki granica lewa jest mniejsza od prawej
    while left < right:
        middle = (left+right)//2  #wybor elementu srodkowego
        if lista[middle] < key:  #jezeli element srodkowy jest mniejszy od szukanego
            left = middle + 1     #to odrzuc lewa polowke (przesun lewa granice)
        else:                     #w przeciwnym razie
            right = middle        #odrzuc prawa polowke (przesun prawa granice , dla k=11

        #sprawdz czy znaleziono szukany element
    if lista[right] == key:
        return right
    else:
        return False
 

print(binary_search(szukana,A))




# binary_search = wersja bez litery "k"
print('Dana jest lista: "h","i", "j","l", "m", "n","a", "b", "c", "d", "e","f", "g", "o", "p", "r", "s", "t", "u", "w", "x", "y", "z"')
      
A = ["h","i", "j","l", "m", "n","a", "b", "c", "d", "e","f","g","o", "p", "r", "s", "t", "u", "w", "x", "y", "z"]

      
# sortowanie listy na początku obowiązkowe przy przeszukiwaniu binarnym
A.sort()

szukana = str(input("wpisz literę 'k': ")).lower()  # by przy wpisaniu 'K' odnalazł element


def binary_search(key, lista):

    #poczatkowe zainicjowanie granic szukania
    left = 0
    right = len(lista)-1   # right =22, bo 23 elementy, ale ostatni index to 22

    #szukaj dopoki granica lewa jest mniejsza od prawej
    while left < right:
        middle = (left+right)//2  #wybor elementu srodkowego
        if lista[middle] < key:  #jezeli element srodkowy jest mniejszy od szukanego
            left = middle + 1     #to odrzuc lewa polowke (przesun lewa granice)
        else:                     #w przeciwnym razie
            right = middle        #odrzuc prawa polowke (przesun prawa granice , dla k=11

        #sprawdz czy znaleziono szukany element
    if lista[right] == key:
        return right
    else:
        return False
 


print(binary_search(szukana,A))
