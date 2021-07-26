listaA = [1,2,3,4,1,5,4,3,2,1,2]
najmniejsza = None
result = []    # lista zawierająca pozycje indexu z najmniejszą wartością jaka nam wyjście

print("Dana jest lista A, która zawiera [1,2,3,4,1,5,4,3,2,1,2] elementów")
for liczba in listaA:
    if najmniejsza == None or najmniejsza > liczba: # sprawdzenie najmnniejszego elementu na liście
        najmniejsza = liczba
        
for pos, value in enumerate(listaA):  #enumerate() gdy jest potrzeba zliczenia iteracji przez listęA
    if value == najmniejsza:
        result.append(pos)    # dodaje do listy result[] numery indexu   [0,4,9]

najwiekszyIndex = result[-1]     # [-1] ostatnia pozycja od końca; tutaj największy index

             
print(f"Najmniejszy element to {najmniejsza}, a jej największy index to: {najwiekszyIndex}")
