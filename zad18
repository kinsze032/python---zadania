class Rectangle():
# Rectangle class using Point, width and height

    def __init__(self, a, w, h):

        self.a = a
        self.w = w
        self.h = h

        self.b = (self.a[0] + self.w, self.a[1] + self.h)
        self.c = (self.a[0] + self.w, self.a[1])
        self.d = (self.a[0], self.a[1] + self.h)


    def __str__(self):
        return("To jest nasz prostokat " + "A = " + str(self.a) + " B = " + str(self.b) + " C = " + str(self.c) + " D = " + str(self.d))
    
    def diagonal(self):

        diag = (self.w**2 + self.h**2) ** 0.5
        return (f"Przekątna wynosi: " + "%.2f" % diag)

    def centre_Point(self):
        x = [(self.a[0] + self.b[0])//2,(self.a[1] + self.b[1])//2] # przekątna |AB|
        y = [(self.d[0] + self.c[0])//2,(self.d[1] + self.c[1])//2] # przekątna |DC|

        if x == y:
            middle = [x[0],x[1]]
            return("Współrzędne środka prostokąta to " + "X = (" + str(middle[0]) + "," + str(middle[1]) + ")" )
        else:               
            cp = ((x[0],x[1]),(y[0],y[1]))
            return("Współrzędne środka prostokąta to: " + cp)

    def wsp(self):
        return self.a, self.b, self.c, self.d

    def obwod(self):
        obw = (2*abs(self.a[0]-self.b[0]))+(2*abs(self.a[1]-self.b[1]))  # obwód = 2a + 2b
        return ("Obwód wynosi: "  + str(obw))

    def area(self):
        pole = abs(self.w) * abs(self.h) # Pole = a * b
        return ("Pole wynosi: "  +  str(pole))


r = Rectangle((20,70), 50, 10)
print(r)

print(r.diagonal())
print(r.wsp())
print(r.obwod())
print(r.area())
print(r.centre_Point())
