# Importation du module math

# Permet d'utiliser sqrt() pour les racines carrées réelles

import math

# Importation du module cmath

# Permet de calculer les racines carrées de nombres négatifs

# et de manipuler les nombres complexes

import cmath

# ==================================================

# CLASSE : EquationSecondDegre

# Représente une équation de la forme :

# ax² + bx + c = 0

# ==================================================

class EquationSecondDegre:

```
# ----------------------------------------------
# Constructeur de la classe
# Initialise les coefficients a, b et c
# ----------------------------------------------
def __init__(self, a, b, c):

    # Coefficient de x²
    self.a = a

    # Coefficient de x
    self.b = b

    # Terme constant
    self.c = c

# ----------------------------------------------
# Méthode : afficher_equation
# Affiche l'équation saisie par l'utilisateur
# ----------------------------------------------
def afficher_equation(self):
    print(f"{self.a}x² + {self.b}x + {self.c} = 0")

# ----------------------------------------------
# Méthode : calculer_delta
# Calcule le discriminant Δ = b² - 4ac
# ----------------------------------------------
def calculer_delta(self):
    return self.b ** 2 - 4 * self.a * self.c

# ----------------------------------------------
# Méthode : resoudre
# Résout l'équation et retourne les résultats
# sous forme de dictionnaire
# ----------------------------------------------
def resoudre(self):

    # ==========================================
    # CAS 1 : a = 0
    # L'équation n'est plus du second degré
    # ==========================================
    if self.a == 0:

        # Cas bx + c = 0
        if self.b != 0:

            # Calcul de la solution
            x = -self.c / self.b

            return {
                "type": "lineaire",
                "solution": x
            }

        # Cas 0x + 0 = 0
        elif self.c == 0:

            return {
                "type": "indetermine"
            }

        # Cas 0x + c = 0 avec c ≠ 0
        else:

            return {
                "type": "impossible"
            }

    # ==========================================
    # CAS 2 : véritable équation du second degré
    # ==========================================

    # Calcul du discriminant
    delta = self.calculer_delta()

    # ==========================================
    # CAS 2.1 : Δ > 0
    # Deux solutions réelles distinctes
    # ==========================================
    if delta > 0:

        x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
        x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)

        return {
            "type": "deux_solutions_reelles",
            "x1": x1,
            "x2": x2
        }

    # ==========================================
    # CAS 2.2 : Δ = 0
    # Une solution réelle double
    # ==========================================
    elif delta == 0:

        x = -self.b / (2 * self.a)

        return {
            "type": "une_solution",
            "x": x
        }

    # ==========================================
    # CAS 2.3 : Δ < 0
    # Deux solutions complexes
    # ==========================================
    else:

        # Calcul de √Δ avec cmath
        sqrt_delta = cmath.sqrt(delta)

        x1 = (-self.b - sqrt_delta) / (2 * self.a)
        x2 = (-self.b + sqrt_delta) / (2 * self.a)

        return {
            "type": "solutions_complexes",
            "x1": x1,
            "x2": x2
        }
```
