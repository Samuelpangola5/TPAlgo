
"""
PANGOLA BANKANDJA SAMUEL L2/GC
Le programme utilse une classe appelée Fraction
pour représenter des fractions mathematiques.Chaque instance de la classe
Fraction contient un numérateur et un dénominateur.Le contsructeur de classe
s'assure que le dénominateur est strictement positif .La classe a également
une méthode pour afficher la fraction en que chaine de caractères et
une autre méthode pour vérifier si les deux fractions sont égales .Le
programme crée quatre instances de la classe Fraction avec différentes valeurs
et affiche leur représentation.
"""


class Fraction :
    def __init__(self,num, den,):
        assert den > 0
        self.num = num
        self.den = den
    def __str__(self):
        if self.den == 1 :
            
            return str(self.num)
        else :
            return (str(self.num) + "/" + str(self.den))
    def __egalite__(self,other) :
        if self.num*other.den == self.den * other.num :
            return True
        else :
            return False
   
F1,F2,F3,F4 = Fraction(3,4) , Fraction(-8,1) , Fraction(2,3), Fraction(21,28)
print(F1)
print(F2)
print(F3)
print(F4)

print(F1.__egalite__(F3))
print(F2.__egalite__(F3))
print(F4.__egalite__(F4))
print(F4.__egalite__(F2))



