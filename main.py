import math

class EquationSecondDegre:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def afficher_equation(self):
        print(f"Équation : {self.a}x² + {self.b}x + {self.c} = 0")

    def calculer_delta(self):
        return self.b**2 - 4*self.a*self.c

    def resoudre(self):
        a, b, c = self.a, self.b, self.c

        if a == 0:
            print("Ce n'est pas une équation du second degré.")
            if b == 0:git
                if c == 0:
                    print("Infinité de solutions.")
                else:
                    print("Aucune solution.")
            else:
                x = -c / b
                print(f"Solution unique : x = {x}")
            return

        delta = self.calculer_delta()
        print(f"Delta (Δ) = {delta}")

        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2*a)
            x2 = (-b + math.sqrt(delta)) / (2*a)
            print(f"Deux solutions réelles :")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")

        elif delta == 0:
            x = -b / (2*a)
            print("Une seule solution réelle :")
            print(f"x = {x}")

        else:
            print("Aucune solution réelle (delta négatif).")
            x1 = complex(-b, math.sqrt(-delta)) / (2*a)
            x2 = complex(-b, -math.sqrt(-delta)) / (2*a)
            print(f"Solutions complexes :")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")

a = float(input("Entrer a : "))
b = float(input("Entrer b : "))
c = float(input("Entrer c : "))

eq = EquationSecondDegre(a, b, c)
eq.afficher_equation()
eq.resoudre()