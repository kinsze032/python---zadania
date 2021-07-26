import sys

cyfry_Slownie = {'0':'zero',
                 '1':'jeden',
                 '2':'dwa',
                 '3':'trzy',
                 '4':'cztery',
                 '5':'pięć',
                 '6':'sześć',
                 '7':'siedem',
                 '8':'osiem',
                 '9':'dzięć',
                 '-':'minus'}

liczba = str(input("Podaj liczbę: "))

for ithem in liczba:
    if ithem in cyfry_Slownie:
        sys.stdout.write("%s " % cyfry_Slownie[ithem])  #nie ma znaku nowej linii
