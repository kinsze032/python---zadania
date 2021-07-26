lista= [10,43,12,48,12,11,18,-1,57,28,19,27,49,19,74]

najmniejsza = lista[0]
i = 0

print("Dana jest lista A, która zawiera [10,43,12,48,12,11,18,-1,57,28,19,27,49,19,74]")

while i < len(lista):
    #print (i+1, "Para liczb: ", listaA[i], listaA[i+1])  # wyświetli analizę każdej pary liczb osobno

    if lista[i] < najmniejsza:
        najmniejsza = lista[i]
    i+=1
        

   #print("Największą liczbą z tej pary jest ", wieksza)  # wyświetli największą liczbę z pary

print("Największą liczbą listy A jest: ", najmniejsza)
