# Importation du module math
# Permet d'utiliser sqrt() pour les racines carrées
import math

# Importation de cmath pour gérer les racines complexes
# (utile quand delta < 0)
import cmath


# ==========================================
# CLASSE : EquationSecondDegre
# Représente une équation : ax² + bx + c = 0
# ==========================================
class EquationSecondDegre:

    # Constructeur : initialise les coefficients
    def __init__(self, a, b, c):

        # Coefficient de x²
        self.a = a

        # Coefficient de x
        self.b = b

        # Terme constant
        self.c = c

    # ======================================
    # MÉTHODE : calculer_delta
    # Calcule le discriminant Δ = b² - 4ac
    # ======================================
    def calculer_delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    # ======================================
    # MÉTHODE : resoudre
    # Résout complètement l'équation
    # ======================================
    def resoudre(self):

        # ==============================
        # CAS 1 : a = 0 (pas du 2nd degré)
        # ==============================
        if self.a == 0:

            # Équation du type bx + c = 0
            if self.b != 0:

                # Calcul de la solution linéaire
                x = -self.c / self.b

                print("Équation du premier degré")
                print("Solution unique : x =", x)

            else:

                # Cas 0x + c = 0
                if self.c == 0:

                    print("Infinité de solutions (0 = 0)")

                else:

                    print("Aucune solution (équation impossible)")

            return  # arrêt de la fonction

        # ==============================
        # CAS 2 : équation du 2nd degré
        # ==============================
        delta = self.calculer_delta()

        print("Δ =", delta)

        # ----------------------------------
        # CAS 2.1 : delta > 0 (2 solutions)
        # ----------------------------------
        if delta > 0:

            x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)

            print("Deux solutions réelles :")
            print("x₁ =", x1)
            print("x₂ =", x2)

        # ----------------------------------
        # CAS 2.2 : delta = 0 (1 solution)
        # ----------------------------------
        elif delta == 0:

            x = -self.b / (2 * self.a)

            print("Une solution réelle double :")
            print("x =", x)

        # ----------------------------------
        # CAS 2.3 : delta < 0 (complexes)
        # ----------------------------------
        else:

            # Utilisation de cmath pour les complexes
            sqrt_delta = cmath.sqrt(delta)

            x1 = (-self.b - sqrt_delta) / (2 * self.a)
            x2 = (-self.b + sqrt_delta) / (2 * self.a)

            print("Solutions complexes :")
            print("x₁ =", x1)
            print("x₂ =", x2)