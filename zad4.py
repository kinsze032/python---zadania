# importujemy biblotekę datatime
import datetime
 
# metodą .datatime.now() odczytujemy aktualną datę i czas z naszego systemu operacyjnego
czas = datetime.datetime.now()
teraz = int(czas.year)
dzisiaj = int(czas.day)

    
def index():
               

    def sprawdz_pesel():
        sum, ct = 0, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
        for i in range(11):
            sum += (int(pobranie[i]) * ct[i])
        return (str(sum)[-1] == '0')

    
    pobranie = input('Podaj PESEL: ')
    

    zgodny_pesel = len(pobranie)
    
    if zgodny_pesel == 11 and sprawdz_pesel() == 1:
        
        parzyste = [0,2,4,6,8] # Kobieta
        p = int(pobranie[9])  # płeć
        r = int(pobranie[0:2]) # rok urodzenia
        m = int(pobranie[2:4]) # miesiąc
        d = int(pobranie[4:6]) # dzień

        if d >=dzisiaj and r >=32:

       
            if p in parzyste:  # even
                plec = "Kobieta"
            else:  # odd: 13579
                plec = "Mężczyzna"
        
            #sprawdzamy rok urodzenia
            if m >= 1 and m <= 12:
                rocznik = 1900
            elif m >= 21 and m <= 32:
                rocznik = 2000
            elif m >= 81 and m <= 92:
                rocznik = 1800
            elif m >= 41 and m <= 52:
                rocznik = 2100
            elif m >= 61 and m <= 72:
                rocznik = 2200         
            else:
                return("Podałeś błędne dane")
                
            data = rocznik + r
            wiek = teraz - data
      
            #sprawdzamy miesiac
            if m == 1 or m == 21 or m == 81 or m == 41 or m == 61:
                mies = "Stycznia"
            elif m == 2 or m == 22 or m == 82 or m == 42 or m == 62:
                mies = "Lutego"
            elif m == 3 or m == 23 or m == 83 or m == 43 or m == 63:
                mies = "Marca"
            elif m == 4 or m == 24 or m == 84 or m == 44 or m == 64:
                mies = "Kwietnia"
            elif m == 5 or m == 25 or m == 85 or m == 45 or m == 65:
                mies = "Maja"
            elif m ==6 or m == 26 or m == 86 or m == 46 or m == 66:
                mies = "Czerwca"
            elif m == 7 or m == 27 or m == 87 or m == 47 or m == 67:
                mies = "Lipca"
            elif m == 8 or m == 28 or m == 88 or m == 48 or m == 68:
                mies = "Sierpnia"
            elif m == 9 or m == 29 or m == 89 or m == 49 or m == 69:
                mies = "Wrzesnia"
            elif m == 10 or m == 30 or m == 90 or m == 50 or m == 70:
                mies = "Pazdziernika"
            elif m == 11 or m == 31 or m == 91 or m == 51 or m == 71:
                mies = "Listopada"
            elif m == 12 or m ==32 or m == 92 or m == 52 or m == 72:
                mies = "Grudnia"
       
            print(f"Twoja data urodzenia to: {d} {mies} {data} roku.")
            print(f"Twój wiek to: {wiek}")
            print("Twoja płeć to: " ,plec)
        else:
            print("Jeszcze się nie urodziłeś")
        
    else:
        print("Wprowadziłeś błędny pesel")

index()
