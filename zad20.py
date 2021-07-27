class Konto():

    # constructor or initializer
    def __init__(self, name, money, pin):
        self.name = name
        self.balance = money        # saldo
        self.pin = pin

    def pincheck(self):
        if self.pin == pin2:
            return True
        else:
            print("Błąd. Wprowadź ponownie PIN")

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):          # wypłata
        if self.balance > money:
            self.balance -= money
            print(f"Wypłacono: {money} zł")
        else:
            print("Nie masz wystarczających środków")

    def checkbalance(self):
        return self.balance


user1 = Konto("Kinga", 5000, 1111)
user2 = Konto("Klaudia", 12000, 2222)
user3 = Konto("Paweł", 7000, 3333)
d1 = 0
d2 = 0
d3 = 0

print("Witaj w bankomacie")

while True:
    x = input("Wprowadź swoje imię: ")
    pin2 = int(input("Wprowadź PIN: "))

    if x == user1.name and user1.pincheck():

        print("Hej ", user1.name, " twój stan konta to ", user1.checkbalance(), " zł")
        y1 = int(input('Wybierz "1" aby wypłacić, wybierz "2" - aby wpłacić: '))
        if y1 == 1:
            w1 = int(input("Ile chcesz wypłacić: "))
            user1.withdraw(w1)
            print("Saldo: ", user1.checkbalance(), " zł")
        elif y1 == 2:
            d1 = int(input("Ile chcesz wpłacić: "))
            user1.deposit(d1)
            print("Saldo: ", user1.checkbalance(), " zł")

        continue

    if x == user2.name and user2.pincheck():

        print("Hej ", user2.name, " twój stan konta to ", user2.checkbalance(), " zł")
        y1 = int(input('Wybierz "1" aby wypłacić, wybierz "2" - aby wpłacić: '))
        if y1 == 1:
            w2 = int(input("Ile chcesz wypłacić: "))
            user2.withdraw(w2)
            print("Saldo: ", user1.checkbalance(), " zł")
        elif y1 == 2:
            d2 = int(input("Ile chcesz wpłacić: "))
            user2.deposit(d2)
            print("Saldo: ", user2.checkbalance(), " zł")
        continue
    
    if x == user3.name and user3.pincheck():
        print("Hej ", user3.name, " twój stan konta to ", user3.checkbalance(), " zł")
        y1 = int(input('Wybierz "1" aby wypłacić, wybierz "2" - aby wpłacić: '))
        if y1 == 1:
            w3 = int(input("Ile chcesz wypłacić: "))
            user3.withdraw(w3)
            print("Saldo: ", user1.checkbalance(), " zł")
        elif y1 == 2:
            d3 = int(input("Ile chcesz wpłacić: "))
            user3.deposit(d3)
            print("Saldo: ", user3.checkbalance(), " zł")
        continue
    if x == "q".lower() or pin2 == 0:
        print("Wybrałeś q - quit.")
        break
