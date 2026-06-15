from programme.equation import EquationSecondDegre


def main():
    """
    Programme principal :
    - Demande les coefficients
    - Crée l'objet équation
    - Affiche et résout l'équation
    """

    print("=====================================")
    print("   RÉSOLUTION ÉQUATION 2ND DEGRÉ")
    print("=====================================\n")

    try:
        # =========================
        # SAISIE UTILISATEUR
        # =========================
        a = float(input("Entrer la valeur de a : "))
        b = float(input("Entrer la valeur de b : "))
        c = float(input("Entrer la valeur de c : "))

        # =========================
        # CRÉATION DE L'ÉQUATION
        # =========================
        equation = EquationSecondDegre(a, b, c)

        # =========================
        # AFFICHAGE DE L'ÉQUATION
        # =========================
        equation.afficher_equation()

        # =========================
        # RÉSOLUTION
        # =========================
        resultat = equation.resoudre()

        # =========================
        # AFFICHAGE DES RÉSULTATS
        # =========================
        print("\n========== RÉSULTAT ==========")

        if resultat["type"] == "deux_solutions_reelles":
            print("✔ Deux solutions réelles :")
            print(f"x1 = {resultat['x1']}")
            print(f"x2 = {resultat['x2']}")

        elif resultat["type"] == "une_solution":
            print("✔ Une seule solution réelle :")
            print(f"x = {resultat['x']}")

        elif resultat["type"] == "solutions_complexes":
            print("✔ Solutions complexes :")
            print(f"x1 = {resultat['x1']}")
            print(f"x2 = {resultat['x2']}")

        elif resultat["type"] == "lineaire":
            print("✔ Équation du premier degré :")
            print(f"x = {resultat['solution']}")

        elif resultat["type"] == "indetermine":
            print("♾ Infinité de solutions")

        elif resultat["type"] == "impossible":
            print("❌ Aucune solution")

        print("=================================\n")

    except ValueError:
        print("❌ Erreur : veuillez entrer uniquement des nombres valides.")


# =========================
# LANCEMENT DU PROGRAMME
# =========================
if __name__ == "__main__":
    main()