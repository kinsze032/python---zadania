import sys

menu = '''
Wybierz jednostkę:
1 - Celsjusz
2 - Farenhait
3 - Kelvin
---------------
Aby wyjść wciśnij 0"
'''

stCelcjusza = 0
stFarenheita = 0
stKelvina = 0

class TooColdException(Exception):
    pass

def zaZimno():
    if temp < -273.15:
        raise TooColdException()
    
def konwersja(temp, jednostka):
    if jednostka == "1":
        stKelvina = ((temp + 273.15))
        stFarenheita = ((temp * 1.8) + 32)
        zaZimno()
        print(temp, "stopni ", jednostka, "to : ", "%.2f" % stKelvina, "stopni Kelvina i", "%.2f" % stFarenheita, "stopni Farenheita")

    elif jednostka == "2":
        stCelcjusza = (temp - 273.15)
        stFarenheita = ((temp * 1.8) - 459.67)
        zaZimno()
        print(temp, "stopni ", jednostka, "to : ", "%.2f" % stCelcjusza, "stopni Celcjusza i", "%.2f" % stFarenheita, "stopni Farenheita")    

    elif jednostka == "3":
        stCelcjusza = ((temp - 32)/1.8)
        stKelvina =  ((temp + 459.67) * 5/9)
        zaZimno()
        print(temp, "stopni ", jednostka, "to : ", "%.2f" % stCelcjusza, "stopni Celcjusza i", "%.2f" % stKelvina, "stopni Kelvina")


while True:

    print(menu)
    try:
        tempStr = input("Podaj stopnie: ")
        temp = int(tempStr)
        jednostka = input("Podaj Jednostkę: ").upper()

        if jednostka == "1":
            print("Wybrałeś stopnie Celsjusza")
            konwersja(temp, jednostka)
            input('Press enter')
            continue
        
        elif jednostka == "2":
            print("Wybrałeś stopnie Farenheita")
            konwersja(temp, jednostka)
            input('Press enter')
            continue

        elif jednostka == "3":
            print("Wybrałeś stopnie Kelvina")
            konwersja(temp, jednostka)
            input('Press enter')
            continue
        
        elif jednostka == "0":
            print("Wybrałeś 0. Spróbuj ponownie")
            input('Press enter')
            break
        else:
            print("Nie wybrałeś jednstki ze wskazanego zakresu. Spróbuj ponownie")
            input('Press enter')
            continue
            


    except ValueError as e:
        print("Przykro mi - musisz wpisać właściwy typ ", e)
        input('Press enter')
    except TooColdException:
        print("Temperatura {} jest poniżej zera absolutnego".format(temp))
        input('Press enter')

    except:
        print("Coś poszło nie tak...", sys.exc_info()[0])
        input('Press enter')
    
