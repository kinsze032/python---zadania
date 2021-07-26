listaA = [0,11,12,13,-6,-7,14,15,6,7,8,19,10,1,12,3] # 16 elementów listy
resultParzyste = []
resultNieparzyste = []

print("Dana jest lista A, która zawiera [0,11,12,13,-6,-7,14,15,6,7,8,19,10,1,12,3] elementów.")
        
for pos, value in enumerate(listaA):  #enumerate() gdy jest potrzeba zliczenia iteracji przez listęA
    if pos % 2 == 0:          # czy parzysty index
        resultParzyste.append(value)
        
    else:
        resultNieparzyste.append(value)  
        
maximum = max(resultParzyste)  # max() zwraca największą wartość
minimum = min(resultNieparzyste) #min() zwraca najmniejszą wartość

print(f"Wartość spełniająca warunek - maksymalna wartosc i parzysty index to: {maximum}")
print(f"Wartość spełniająca warunek - minimalna wartosc i nieparzysty index to: {minimum}")
