from equation import EquationSecondDegre


def main():
    print("=" * 50)
    print("      RÉSOLUTION D'UNE ÉQUATION DU 2ᵉ DEGRÉ")
    print("=" * 50)

    try:
        # Saisie des coefficients
        a = float(input("Entrez la valeur de a : "))
        b = float(input("Entrez la valeur de b : "))
        c = float(input("Entrez la valeur de c : "))

        # Création de l'objet équation
        equation = EquationSecondDegre(a, b, c)

        print("\nÉquation saisie :")
        equation.afficher_equation()

        # Résolution
        resultat = equation.resoudre()

        print("\n" + "=" * 50)
        print("RÉSULTAT")
        print("=" * 50)

        if resultat["type"] == "deux_solutions_reelles":
            print("Deux solutions réelles :")
            print(f"x1 = {resultat['x1']}")
            print(f"x2 = {resultat['x2']}")

        elif resultat["type"] == "une_solution":
            print("Une seule solution réelle :")
            print(f"x = {resultat['x']}")

        elif resultat["type"] == "solutions_complexes":
            print("Deux solutions complexes :")
            print(f"x1 = {resultat['x1']}")
            print(f"x2 = {resultat['x2']}")

        elif resultat["type"] == "lineaire":
            print("Équation du premier degré :")
            print(f"x = {resultat['solution']}")

        elif resultat["type"] == "indetermine":
            print("L'équation admet une infinité de solutions.")

        elif resultat["type"] == "impossible":
            print("L'équation n'admet aucune solution.")

        print("=" * 50)

    except ValueError:
        print("Erreur : veuillez saisir uniquement des nombres.")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")


if __name__ == "__main__":
    main()