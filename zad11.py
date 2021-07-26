rok = int(input("Wpisz rok: ")) 

def rokPrzestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        print("%s jest rokiem przestępnym" % rok)
    else:
        print("%s nie jest rokiem przestępnym" % rok)

rokPrzestepny(rok)


#Rok jest przestępny, gdy jest podzielny przez 4 i nie jest podzielny przez 100 lub jest podzielny przez 400.
