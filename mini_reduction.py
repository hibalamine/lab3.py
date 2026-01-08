def calcul_reduction(prix, est_etudiant, annees_fidelite):
    """Calcule la réduction totale basée sur les règles métier."""
    remise = 0.0

    # Règle 1 : Étudiant (10%)
    if est_etudiant:
        remise += prix * 0.10
        print(f"-> Remise étudiant appliquée : {prix * 0.10:.2f} €")

    # Règle 2 : Fidélité >= 5 ans (15%)
    if annees_fidelite >= 5:
        remise += prix * 0.15
        print(f"-> Remise fidélité appliquée : {prix * 0.15:.2f} €")

    # Règle 3 : Seuil de prix > 100€ (5€ fixe)
    if prix > 100:
        remise += 5.0
        print(f"-> Remise 'Grand Achat' appliquée : 5.00 €")

    return remise

def main():
    print("--- Calculateur de Réduction ---")
    
    try:
        # 1. Saisie et validation du prix
        prix_initial = float(input("Prix du produit (€) : "))
        if prix_initial <= 0:
            print("Le prix doit être supérieur à zéro.")
            return

        # 2. Informations client
        statut = input("Êtes-vous étudiant ? (o/n) : ").strip().lower()
        est_etudiant = (statut == "o")
        
        fidelite_input = input("Années de fidélité : ").strip()
        fidelite = int(fidelite_input)
        if fidelite < 0:
            print("La fidélité ne peut pas être négative.")
            return

        # 3. Calcul
        total_remise = calcul_reduction(prix_initial, est_etudiant, fidelite)
        
        # 4. Calcul du prix final avec garde-fou
        prix_final = prix_initial - total_remise
        if prix_final < 0:
            prix_final = 0.0

        # 5. Affichage final
        print("-" * 30)
        print(f"Réduction totale : {total_remise:.2f} €")
        print(f"Prix final à payer : {prix_final:.2f} €")
        print("-" * 30)

    except ValueError:
        print("Erreur : Veuillez saisir des valeurs numériques valides.")

if __name__ == "__main__":
    main()