from datetime import datetime
import sys



class Osoba(object):

    

    def __init__(self, first_name, last_name, pesel, plec, data_wydania, data_waznosci, id_number):

        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel
        self.plec = plec
        self.data_wydania = data_wydania
        self.data_waznosci = data_waznosci
        self.id_number = id_number
        

    def fullname(self): # instance method
        # instance object accessible through self
        return "%s %s" % (self.first_name.title(), self.last_name.title())


    def update_last_name(self, new_name):

        
        while new_name != self.last_name:
            self.last_name = new_name
            print("Dokonałeś zmiany w nazwisku na:", new_name.title())


    def ustal_daty(self):
        import datetime     # jawnie ponownie zaimportowany moduł
        inputDate = input("Wpisz datę wydania w formacie dd/mm/yyyy: ")  
        day,month,year = inputDate.split("/")

        isValidDate = True
        try:
            datetime.datetime(int(year),int(month),int(day))
        except ValueError:
            isValidDate = False

        if(isValidDate):
            print("Podana data jest poprawna")
            user_01.data_wydania = datetime.date(int(year),int(month),int(day))
            user_01.data_waznosci = datetime.date(int(year)+10,int(month),int(day))
            if user_01.data_waznosci < datetime.date.today():
                user_01.data_waznosci = "Dokument nieważny"
            elif user_01.data_waznosci == datetime.date.today():
                user_01.data_waznosci = "Data ważności kończy się dzisiaj."
            
        else:
            print("Podana data jest błędna")

    def nr_dowodu(self, new_number):
        
        while new_number != self.id_number:
            self.id_number = new_number

            letter_values = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            
            
            def get_letter_value(letter):
                for i in range(0, len(letter_values)):
                    if letter == letter_values[i]:
                        return i
                return -1
             
            def check_id_number(id_number):
                # nieprawidlowa dlugosc
                if len(id_number) != 9:
                    print("Twój nr dowodu nie jest poprawny")
                    return
                # nieprawidlowa seria dowodu
                for i in range(0, 3):
                    if get_letter_value(id_number[i]) < 10:
                        print("Twój nr dowodu nie jest poprawny")
                        return
                # nieprawidlowy numer dowodu
                for i in range(3, 9):
                    if get_letter_value(id_number[i]) < 0 \
                        or get_letter_value(id_number[i]) > 9:
                            print("Twój nr dowodu nie jest poprawny")
                            return
             
                checkSum = 7 * get_letter_value(id_number[0])
                checkSum += 3 * get_letter_value(id_number[1])
                checkSum += 1 * get_letter_value(id_number[2])
                checkSum += 7 * get_letter_value(id_number[4])
                checkSum += 3 * get_letter_value(id_number[5])
                checkSum += 1 * get_letter_value(id_number[6])
                checkSum += 7 * get_letter_value(id_number[7])
                checkSum += 3 * get_letter_value(id_number[8])
                checkSum = checkSum % 10
                
                if checkSum != get_letter_value(id_number[3]):
                    
                    print("Twój nr dowodu nie jest poprawny")
                    
                    
                else:
                    print("Twój nr ID jest poprawny")
                    return id_number
                    


            check_id_number(new_number)

            
    def ustal_plec(self,pobranie):

        parzyste = [0,2,4,6,8]
        p = int(pobranie[9])    #płeć
        
        if p in parzyste:   # even
            self.plec = "K"
        else:               # odd: 13579
            self.plec = "M"


    def index(self, pobranie):

        def pesel():
            import datetime     # jawnie ponownie zaimportowany moduł
            czas = datetime.datetime.now()
            teraz = int(czas.year)
            dzisiaj = int(czas.day)

            while pobranie != self.pesel:
                self.pesel = pobranie
                       

                def sprawdz_pesel():
                    sum, ct = 0, [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
                    for i in range(11):
                        sum += (int(pobranie[i]) * ct[i])
                    return (str(sum)[-1] == '0')

                
               # pobranie = input('Podaj PESEL: ')
                

                zgodny_pesel = len(pobranie)
                
                if zgodny_pesel == 11 and sprawdz_pesel() == 1:
                    

                    r = int(pobranie[0:2]) # rok urodzenia
                    m = int(pobranie[2:4]) # miesiąc
                    d = int(pobranie[4:6]) # dzień

                    if d >=dzisiaj and r >=32:

                   

                    
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
                   
                        print("Twój pesel jest poprawny")
                        return pesel

                    else:
                        print("Jeszcze się nie urodziłeś")
                        return
                    
                else:
                    print("Wprowadziłeś błędny pesel")
                    return
        pesel()

    def describe_user(self):
        print()
        print('--------------------------------------')
        print("DOWÓD OSOBISTY - informacje:")
        print("Imię i nazwisko: {} {}".format(self.first_name, self.last_name).title())
        print("PESEL: {}".format(self.pesel))
        print("Płeć: {}".format(self.plec))
        print("Nr dowodu: {}".format(self.id_number))
        print("Twoj dokument zostal wydany: {}".format(self.data_wydania))
        print("Data ważności dokumentu: {}".format(self.data_waznosci))


           
user_01 = Osoba("","","","","","","")

print("Witaj w programie E-Dokument")
print()

today = datetime.utcnow()
today.strftime('%Y-%m-%d')
print("Data i godzina:", today)
print('--------------------------------------')

while True:
    
    print()
    user_01.first_name = input("Podaj imię: ")
    user_01.last_name = input("Podaj nazwisko: ")
    print()

    while True:
        y1 = int(input("Wybierz 1 jeżeli chcesz zmienić nazwisko, wybierz 2- jeżeli nie: "))
        if y1 == 1:
            new_name = input("Wpisz nowe nazwisko: ") 
            user_01.update_last_name(new_name)
            continue
            
        if y1 == 2:
            print("Nie chce zmieniać nazwiska")
            break
    print()
    while True:
        pobranie = str(input("Wpisz nr PESEL: ").strip())
        user_01.index(pobranie)
        print()
        
        y3 = int(input("""
        Wybierz:
        1 - jeżeli chcesz zmienić nr PESEL,
        2 - jeżeli nie chcesz wprowadzić zmian
        3 - jeżeli chcesz pozostawić puste pole: """))
        if y3 == 1:
            pobranie = str(input("Wpisz nr PESEL: ").strip())
            user_01.index(pobranie)
            if user_01.index(pobranie)== True:
                user_01.ustal_plec(pobranie)
            continue
            
        if y3 == 2:
            print("Nie chce zmieniać nr PESEL")
            user_01.ustal_plec(pobranie)
            break
        if y3 == 3:
            user_01.pesel = "brak_danych"
            user_01.plec = "brak_danych"
            break

    print()
    while True:
        new_number = str(input("Wpisz nr dowodu: ").strip())
        user_01.nr_dowodu(new_number)
        print()
        y2 = int(input("""
        Wybierz:
        1 - jeżeli chcesz zmienić nr dowodu,
        2 - jeżeli nie chcesz zmieniać,
        3-  jeżeli chcesz zostawić puste pole: """))
        
        if y2 == 1:
            new_number = str(input("Wpisz nr dowodu: ").strip())
            user_01.nr_dowodu(new_number)
            True
            
        if y2 == 2:
            print("Nie chce zmieniać nr dowodu")
            
        if y2 ==3:
            print("Nie uzupełniono nr dowodu")
            user_01.id_number = "brak_danych"
            user_01.data_wydania = "brak_danych"
            user_01.data_waznosci = "brak_danych"
            
            
        print()
        if (y2 == 1 or y2 ==2):
            user_01.ustal_daty()
            print(user_01.describe_user())
            break
        elif y2 ==3:
            print(user_01.describe_user())
            break
        
    break
