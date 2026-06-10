# Importation du module math pour utiliser la racine carrée
import math


# Déclaration de la classe EquationSecondDegre
class EquationSecondDegre:

    # Constructeur de la classe
    def __init__(self, a, b, c):

        # Initialisation du coefficient a
        self.a = a

        # Initialisation du coefficient b
        self.b = b

        # Initialisation du coefficient c
        self.c = c


    # Méthode qui calcule le discriminant Δ
    def calculer_delta(self):

        # Retourne la valeur de Δ = b² - 4ac
        return self.b ** 2 - 4 * self.a * self.c


    # Méthode qui résout l'équation
    def resoudre(self):

        # Vérifie si a est nul
        if self.a == 0:

            # Vérifie si b est différent de zéro
            if self.b != 0:

                # Calcul de la solution du premier degré
                x = -self.c / self.b

                # Affichage de la solution
                print("Équation du premier degré.")
                print("x =", x)

            else:

                # Vérifie si c est nul
                if self.c == 0:

                    # Affichage du résultat
                    print("Infinité de solutions.")

                else:

                    # Affichage du résultat
                    print("Aucune solution.")

        else:

            # Appel de la méthode calculer_delta()
            delta = self.calculer_delta()

            # Affichage de la valeur du discriminant
            print("Δ =", delta)

            # Cas où Δ est positif
            if delta > 0:

                # Calcul de la première solution
                x1 = (-self.b - math.sqrt(delta)) / (2 * self.a)

                # Calcul de la deuxième solution
                x2 = (-self.b + math.sqrt(delta)) / (2 * self.a)

                # Affichage des solutions
                print("x₁ =", x1)
                print("x₂ =", x2)

            # Cas où Δ est nul
            elif delta == 0:

                # Calcul de la solution double
                x = -self.b / (2 * self.a)

                # Affichage de la solution
                print("x =", x)

            # Cas où Δ est négatif
            else:

                # Affichage du résultat
                print("Pas de solution réelle.")