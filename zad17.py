A = [1,2,3,4]

ponownie = "t"

def podstawa():
    if p >=2:
        return p
    else: 
        raise ValueError
        
  
def DziesietnaDowolna(A, p):
  
    import string
    digits = [0]
    x = 0
    
    for i in range(len(A)):
        x =(digits[i] * p) + A[i]
        digits.append(x)
            

    digits.reverse()    # lista w odwrotnej kolejności

    return digits[0]    #zwrócenie wartości pierwszego indeksu, czyli wyniku


if __name__ == '__main__':
    

    while ponownie != "n":
        
        try:
                
            p = int(input("Wskaż podstawę liczby 1234, aby wyświetlić jej reprezentację dziesiętną: "))
            podstawa()
            ponownie = "n"
        
            print(f"(1 2 3 4){p} ===> ({DziesietnaDowolna(A,p)})10")
        
        except ValueError:
            print("Podstawa p powinna być większa bądź równa 2")
            input("Press enter")
