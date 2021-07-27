from math import sqrt
from fractions import Fraction
import unicodedata


class LiczbyZespolone(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return LiczbyZespolone(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return LiczbyZespolone(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return LiczbyZespolone(self.real*other.real - self.imag*other.imag, self.imag*other.real + self.real*other.imag)

    def __div__(self, other):
        sr, si, otr, oi = self.real, self.imag, other.real, other.imag  # kwprowadzenie skrótów
        r = float(other.real**2 + other.imag**2)    # 
        return LiczbyZespolone((sr*otr+si*oi)/r, (si*otr-sr*oi)/r)

    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        return '(%d , %d)' % (self.real, self.imag)

    def cos(self):
        return self.real/sqrt(self.real**2 + self.imag**2)

    def sin(self):
        return self.imag/sqrt(self.real**2 + self.imag**2)
        
    def p_tryg(self):

        phi = unicodedata.lookup("GREEK SMALL LETTER PHI")
        pi = unicodedata.lookup("GREEK SMALL LETTER PI")
        sr, si = self.real, self.imag  # skrócenie
            
        if abs(round(sr/sqrt(sr**2 + si**2), 2)) == 1 and abs(round(si/sqrt(sr**2 + si**2), 2)) == 0:   # abs. - wartość bezwzględna
            kat = 0
        if abs(round(sr/sqrt(sr**2 + si**2), 2)) == round(sqrt(3)/2, 2) and abs(round(si/sqrt(sr**2 + si**2), 2)) == round(1/2, 2):
            kat = 1/6
        if abs(round(sr/sqrt(sr**2 + si**2), 2)) == round(sqrt(2)/2, 2) and abs(round(si/sqrt(sr**2 + si**2), 2)) == round(sqrt(2)/2, 2):
            kat = 1/4
        if abs(round(sr/sqrt(sr**2 + si**2), 2)) == round(1/2, 2) and abs(round(si/sqrt(sr**2 + si**2), 2)) == round(sqrt(3)/2, 2):
            kat = 1/3
        if abs(round(sr/sqrt(sr**2 + si**2), 2)) == 0 and abs(round(si/sqrt(sr**2 + si**2), 2)) == 1:
            kat = 1/2

        if sr/sqrt(sr**2 + si**2) > 0 and si/sqrt(sr**2 + si**2) > 0:
            fi = kat
        elif sr/sqrt(sr**2 + si**2) < 0 and si/sqrt(sr**2 + si**2) >= 0:
            fi = 1 - kat
        elif sr/sqrt(sr**2 + si**2) < 0 and si/sqrt(sr**2 + si**2) <= 0:
            fi = 1 + kat
        elif sr/sqrt(sr**2 + si**2) > 0 and si/sqrt(sr**2 + si**2) < 0:
            fi = 2*1 - kat
        
        print("z = |z|*(cos", phi, "+ i sin", phi, ")")
        print("z = ", round(sqrt(sr**2 + si**2)), "(cos",  round(fi, 2), pi, "+ sin" , round(fi, 2), pi, ")")
    

x = LiczbyZespolone(4, -7)
y = LiczbyZespolone(-3, 2)

add = x.__add__(y)
sub = x.__sub__(y)
mul = x.__mul__(y)
div = x.__div__(y)

z = LiczbyZespolone(3, -4)
modul = z.__abs__()

print(x)
if x.imag < 0:
    print('Postać kartezjańska     z = %d %di' % (x.real, x.imag))
else:
    print('Postać kartezjańska     z = %d + %di' % (x.real, x.imag))
    
print(y)
if y.imag < 0:
    print('Postać kartezjańska     z = %d %di' % (y.real, y.imag))
else:
    print('Postać kartezjańska     z = %d + %di' % (y.real, y.imag))


print()
print("Dodawanie: ", add)
print("Odejmowanie: ", sub)
print("Mnożenie: ", mul)
print("Dzielenie: ", div)
print("Wartość bezwzględna: %d" % modul)
print()

w = LiczbyZespolone(1, -sqrt(3))
print(w)

cos = w.cos()
sin = w.sin()
print()
print("Cosinus: ", round(cos, 2))
print("Sinus: ", round(sin, 2))
print(w.p_tryg())
