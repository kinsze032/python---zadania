listaA = [43,12,48,12,11,18,98,57,28,19,27,49,10,74,-2]
najmniejsza = None  # nie wiadomo czy nie ma 0 na liście albo jeszcze mniejszej liczby; bezpieczniej wpisać None

print("Dana jest lista A, która zawiera [43,12,48,12,11,18,98,57,28,19,27,49,10,74,-2]")

for liczba in listaA:
    if najmniejsza == None or najmniejsza > liczba:  # sprawdzenie najmnniejszego elementu na liście
        najmniejsza = liczba


print("Najmniejszą liczbą listy A jest: ", najmniejsza)
