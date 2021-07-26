# wersja 1
import sys

zadaniaNaOsobe = 0

try:
    zadania = 5
    osobyStr = input("Ile osób jest w zespole? ")
    osoby = int(osobyStr)

    zadaniaNaOsobe = zadania / osoby

except ValueError as e: #e - wyświelenie dodatkowych info użytkownikowi
    print("Przykro mi - musisz wpisać numer cyfrą(integer): ",e)

except ZeroDivisionError as e:
    print("Przykro mi - musisz wprowadzić wartość > 0: ",e)

except:
    print("Coś poszło nie tak...", sys.exc_info()[0]) # pozostałe błędy, do których mogłoby dochodzić

else: print("Każda osoba powinna mieć ok ", zadaniaNaOsobe, " zadań") # wykonuje się tylko, gdy nie obsłuży wyjątku



####################################
"""
# wersja 2

import sys

zadaniaNaOsobe = 0

try:
    zadania = 5
    osobyStr = input("Ile osób jest w zespole? ")
    osoby = int(osobyStr)

    zadaniaNaOsobe = zadania / osoby

except (ValueError,ZeroDivisionError) as e: #e - wyświelenie dodatkowych info użytkownikowi
    print("Przykro mi - coś poszło nie tak ", e)
    
else: print("Każda osoba powinna mieć ok ", zadaniaNaOsobe, " zadań") # wykonuje się tylko, gdy nie obsłuży wyjątku
"""
