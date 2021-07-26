import sys

ponownie = "t"

def podstawa():
    if p >=2:
        return p
    else:
        raise ValueError
        
    
def DziesietnaDowolna(x, p):
    assert x > 0   # instrukcja zawiera warunek, który powinien być zawsze prawdziwy, jeśli nie to wyświetli AssertionError
    import string   # zawiera stałe takie jak digits i ascii_letters czy ascii_uppercase
    digs = string.digits + string.ascii_uppercase #'0123456789 + ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if x < 0:
        sign = -1
    else:
        sign = 1
        
    if x == 0:
        return digs[0]

    x = x * sign
    digits = []

    while x:
        digits.append(digs[x % p]) # modulo - reszta z dzielenia; kolejne wartości dodają się na koniec listy
        x = x // p  # dzielenie bez reszty

    if sign < 0:
        digits.append('-')

    digits.reverse()    # lista w odwrotnej kolejności

    return ' '.join(digits)    #połączenie wszystkich wartości i rozdzielenie ich spacją

if __name__ == '__main__':

    while ponownie != "n":
        
        try:
        
            x = int(input("Wprowadź liczbę: "))
            p = int(input("Z systemu dziesiętnego przelicz na system: "))
            podstawa()
            ponownie = "n"
            print(f"({x})10 ===> ({DziesietnaDowolna(x,p)}){p}")
        
        except ValueError:
            print("Podstawa p powinna być większa bądź równa 2")
            input("Press enter")
        
    
