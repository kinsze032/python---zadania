import math  # dołączamy bibliotekę matematyczną

ponownie = "t"  # deklarujemy i inicjujemy zmienną pomocniczą
while ponownie != "n":  # dopóki wartość zmiennej "ponownie" jest inna niż znak "n"
    a = float(input("Wprowadź pierwszy bok trójkąta: "))
    b = float(input("Wprowadź drugi bok trójkąta: "))
    c = float(input("Wprowadź trzeci bok trójkąta: "))

    if a + b > c and a + c > b and b + c > a:  # warunek złożony
        print("Z podanych boków można zbudować trójkąt.")
        
        # sprawdzenie czy trójkąt jest prostokątny?
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Podany trójkąt jest trójkątem prostokątnym!")

        print("Obwód wynosi:", (a + b + c)) # obliczamy obwód
       
        
        p = 0.5 * (a + b + c)  # obliczmy współczynnik wzoru Herona
        # liczymy pole ze wzoru Herona
        P = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print("Pole wynosi:", P)
        ponownie = "n"  # ustawiamy zmienną na "n", aby wyjść z pętli while
    else:
        print("Z podanych odcinków nie można utworzyć trójkąta prostokątnego.")
        ponownie = input("Spróbujesz jeszcze raz (t/n): ")
