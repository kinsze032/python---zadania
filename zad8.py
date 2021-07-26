listaA = [2,3,4,5,4,3,2,1,2]
najmniejsza = None # nie wiadomo czy nie ma 0 na liście albo jeszcze mniejszej liczby; bezpieczniej wpisać None

print("Dana jest lista A, która zawiera ['2','3','4','5','4','3','2','1','2'] elementów")
for liczba in listaA:
    if najmniejsza == None or najmniejsza > liczba: # sprawdzenie najmnniejszego elementu na liście
        najmniejsza = liczba
        
result = listaA.index(najmniejsza)
             
print(f"Najmniejszy element to {najmniejsza}, a jej najmniejszy index to: {result}")
