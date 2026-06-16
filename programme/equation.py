# Importation du module math

# Permet d'utiliser sqrt() pour les racines carrées réelles

import math

# Importation du module cmath

# Permet de manipuler les nombres complexes

import cmath

# ==================================================

# CLASSE : EquationSecondDegre

# Représente une équation de la forme :

# ax² + bx + c = 0

# ==================================================

class EquationSecondDegre:

    # ----------------------------------------------
    # Constructeur
    # Initialise les coefficients a, b et c
    # ----------------------------------------------
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # ----------------------------------------------
    # Affiche l'équation
    # ----------------------------------------------
    def afficher_equation(self):
        print(f"{self.a}x² + {self.b}x + {self.c} = 0")

    # ----------------------------------------------
    # Calcule le discriminant Δ = b² - 4ac
    # ----------------------------------------------
    def calculer_delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    # ----------------------------------------------
    # Résout l'équation
    # ----------------------------------------------
    def resoudre(self):

        # ==========================================
        # CAS 1 : Équation du premier degré
        # ==========================================
        if self.a == 0:

            if self.b != 0:
                x = -self.c / self.b

                return {
                    "type": "lineaire",
                    "solution": x
                }

            elif self.c == 0:

                return {
                    "type": "indetermine"
                }

            else:

                return {
                    "type": "impossible"
                }

        # ==========================================
        # CAS 2 : Équation du second degré
        # ==========================================

        delta = self.calculer_delta()

        # Δ > 0 : Deux solutions réelles
        if delta > 0:

            x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)

            return {
                "type": "deux_solutions_reelles",
                "x1": x1,
                "x2": x2
            }

        # Δ = 0 : Une solution réelle double
        elif delta == 0:

            x = -self.b / (2 * self.a)

            return {
                "type": "une_solution",
                "x": x
            }

        # Δ < 0 : Deux solutions complexes
        else:

            sqrt_delta = cmath.sqrt(delta)

            x1 = (-self.b - sqrt_delta) / (2 * self.a)
            x2 = (-self.b + sqrt_delta) / (2 * self.a)

            return {
                "type": "solutions_complexes",
                "x1": x1,
                "x2": x2
            }
