import sys
litery = ["a","c","t","g","A","C","T","G"]

ponownie = "t"

class ZawieraInneWartosci(Exception):
    pass

   
def inneLitery():
    for i in dna: 
        if i not in litery:                
            raise ZawieraInneWartosci()

def duzeMale():
    if dna.islower():                
        print("Twój łańcuch dna to: ", dna)
    elif dna.isupper():
        print("Twój łańcuch dna to: ", dna)
    else: 
        raise ZawieraInneWartosci()



def wypisz():
    litera_a = dna.count("a",0,len(dna))  # string.count(substring, start=..., end=...)
    litera_t = dna.count("t",0,len(dna))
    litera_c = dna.count("c",0,len(dna))
    litera_g = dna.count("g",0,len(dna))
    litera_A = dna.count("A",0,len(dna))
    litera_T = dna.count("T",0,len(dna))
    litera_C = dna.count("C",0,len(dna))
    litera_G = dna.count("G",0,len(dna))
    

    print("Ilość a: ", litera_a)
    print("Ilość t: ", litera_t)
    print("Ilość c: ", litera_c)
    print("Ilość g: ", litera_g)
    print("Ilość A: ", litera_A)
    print("Ilość T: ", litera_T)
    print("Ilość C: ", litera_C)
    print("Ilość G: ", litera_G)
                    



while ponownie != "n":
   
    
    try:
        dna = input("Podaj kod DNA : ")   

        x = 1/(dna.isalpha()) # sprawdza czy podane wartości to litery
        
        inneLitery()
        duzeMale()
        wypisz()
        ponownie = "n"

    except ZeroDivisionError as e:
        print("Wpisałeś cyfrę")
        input("Press enter")
        
        
    except KeyboardInterrupt as e:
        print("Nie poddawaj się tak łatwo. Nie wyłączaj jeszcze... ", sys.exc_info()[0])
        input("Press enter")

    except ZawieraInneWartosci:
        print("Podany kod DNA jest błędny. Zawiera wartości z poza zakresu.")
        input("Press Enter")
