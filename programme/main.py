# Importation de la classe EquationSecondDegre
from equation import EquationSecondDegre


# Saisie du coefficient a
a = float(input("Entrez la valeur de a : "))

# Saisie du coefficient b
b = float(input("Entrez la valeur de b : "))

# Saisie du coefficient c
c = float(input("Entrez la valeur de c : "))


# Affichage de l'équation
print(f"\nÉquation : {a}x² + {b}x + {c} = 0")


# Création d'un objet de la classe EquationSecondDegre
equation = EquationSecondDegre(a, b, c)


# Appel de la méthode resoudre()
equation.resoudre()