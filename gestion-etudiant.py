# === PARTIE 1 - Organiser les données ===

# 1.1 Créer la liste des étudiants
etudiants = ["Samba", "Evan", "Princia Céleste", "Noâm", "Jean", "Alexandre", "Clément"]

# 1.2 Enregistrer les notes dans un dictionnaire
notes = {
    "Samba": [12, 15, 14],
    "Evan": [16, 14, 17],
    "Princia Céleste": [13, 14, 12],
    "Noâm": [9, 10, 8],
    "Jean": [11, 10, 12],
    "Alexandre": [17, 18, 19],
    "Clément": [14, 15, 13]
}

# 1.3 Affichage des données
for etudiant in etudiants:
    n = notes[etudiant]
    # Affichage des trois notes de chaque étudiant
    print(f"{etudiant} : {n[0]}, {n[1]}, {n[2]}")

print("\n") # Saut de ligne pour espacer les résultats dans le terminal

# === PARTIE 2 - Calculer les moyennes et attribuer les mentions ===

# 2.1 Calculer la moyenne d'un étudiant
def moyenne(liste_notes):
    somme = 0
    # On additionne chaque note manuellement sans utiliser sum()
    for note in liste_notes:
        somme += note
    # On divise par le nombre total de notes
    return somme / len(liste_notes)

# 2.2 Résultats individuels
for etudiant in etudiants:
    moy = moyenne(notes[etudiant])
    n = notes[etudiant]
    # L'expression :.2f permet d'arrondir à deux chiffres après la virgule
    print(f"{etudiant} — Notes : {n[0]}, {n[1]}, {n[2]} — Moyenne : {moy:.2f}")

print("\n")

# 2.3 Attribuer une mention
def mention(moy):
    if moy >= 16:
        return "Excellent"
    elif moy >= 14:
        return "Bien"
    elif moy >= 12:
        return "Assez bien"
    elif moy >= 10:
        return "Passable"
    else:
        return "Insuffisant"

# Affichage des Moyennes et Mentions
for etudiant in etudiants:
    moy = moyenne(notes[etudiant])
    ment = mention(moy)
    print(f"{etudiant} — Moyenne : {moy:.2f} — Mention : {ment}")

# 2.4 Trouver le meilleur étudiant
def meilleur_etudiant(dictionnaire_notes):
    meilleur_nom = ""
    meilleure_moyenne = -1
    
    # On parcourt chaque étudiant et sa liste de notes
    for nom, liste in dictionnaire_notes.items():
        moy = moyenne(liste)
        # Si la moyenne calculée est supérieure à la meilleure moyenne actuelle, on la remplace
        if moy > meilleure_moyenne:
            meilleure_moyenne = moy
            meilleur_nom = nom
            
    return meilleur_nom, meilleure_moyenne

nom_meilleur, moy_meilleur = meilleur_etudiant(notes)
print(f"\nLe meilleur étudiant est {nom_meilleur} avec une moyenne de {moy_meilleur:.2f}.\n")

# === PARTIE 3 - Analyser les résultats de la classe ===

somme_generale = 0
valides = 0
non_valides = 0

# On prépare un dictionnaire pour compter les différentes mentions
repartition = {
    "Excellent": 0,
    "Bien": 0,
    "Assez bien": 0,
    "Passable": 0,
    "Insuffisant": 0
}

for etudiant in etudiants:
    moy = moyenne(notes[etudiant])
    somme_generale += moy
    
    # 3.2 Compter les étudiants ayant validé
    if moy >= 10:
        valides += 1
    else:
        non_valides += 1
        
    # 3.3 Répartition des mentions
    ment = mention(moy)
    repartition[ment] += 1

# 3.1 Calcul de la moyenne générale
moyenne_generale = somme_generale / len(etudiants)

print(f"Moyenne générale de la classe : {moyenne_generale:.2f}")
print(f"Étudiants ayant validé : {valides}")
print(f"Étudiants n'ayant pas validé : {non_valides}")
print("\nRépartition des mentions :")

# On affiche le contenu du dictionnaire de répartition
for ment, quantite in repartition.items():
    print(f"{ment} : {quantite} étudiant(s)")

# === PARTIE 4 - Enregistrer les résultats dans un fichier ===

# Utilisation de 'with open' avec le mode 'w' (write) pour créer/écraser le fichier
with open("resultats.txt", "w", encoding="utf-8") as fichier:
    fichier.write("RESULTATS DE LA CLASSE\n")
    fichier.write("======================\n\n")
    
    # On boucle pour inscrire les données de chaque étudiant
    for etudiant in etudiants:
        n = notes[etudiant]
        moy = moyenne(n)
        ment = mention(moy)
        
        fichier.write(f"{etudiant}\n")
        fichier.write(f"Notes : {n[0]}, {n[1]}, {n[2]}\n")
        fichier.write(f"Moyenne : {moy:.2f}\n")
        fichier.write(f"Mention : {ment}\n\n")
        
    fichier.write(f"Moyenne générale : {moyenne_generale:.2f}\n")
    fichier.write(f"Étudiants ayant validé : {valides}/{len(etudiants)}\n")

print("\nLes résultats ont été enregistrés dans le fichier 'resultats.txt'.")

# === PARTIE 5 - Rechercher un étudiant ===

def recherche_etudiant(nom):
    # La méthode lower() permet de comparer sans se soucier des majuscules/minuscules
    nom_minuscule = nom.lower()
    trouve = False
    
    for etudiant in etudiants:
        if etudiant.lower() == nom_minuscule:
            trouve = True
            n = notes[etudiant]
            moy = moyenne(n)
            ment = mention(moy)
            
            print(f"\nPrénom recherché : {etudiant}")
            print(f"Notes : {n[0]}, {n[1]}, {n[2]}")
            print(f"Moyenne : {moy:.2f}")
            print(f"Mention : {ment}")
            break # On arrête de chercher puisqu'on a trouvé la personne
            
    if trouve == False:
        print(f"\nAucun étudiant ne correspond au prénom '{nom}'.")

# Test de la recherche
recherche_etudiant("Samba")

# === PARTIE 6 - Ajouter un nouvel étudiant (Bonus) ===

def ajouter_etudiant():
    nouveau_nom = input("\nEntrez le prénom du nouvel étudiant : ")
    
    # Empêcher l'ajout d'un étudiant existant
    for etudiant in etudiants:
        if etudiant.lower() == nouveau_nom.lower():
            print("Cet étudiant existe déjà dans la liste !")
            return
            
    nouvelles_notes = []
    
    # Boucle pour demander exactement 3 notes
    for i in range(3):
        note_valide = False
        # On insiste tant que la note n'est pas correcte
        while note_valide == False:
            saisie = input(f"Entrez la note {i+1} (entre 0 et 20) : ")
            note = float(saisie) # Conversion du texte tapé en nombre à virgule
            
            if note >= 0 and note <= 20:
                nouvelles_notes.append(note)
                note_valide = True
            else:
                print("Erreur : la note doit être comprise entre 0 et 20.")
                
    etudiants.append(nouveau_nom)
    notes[nouveau_nom] = nouvelles_notes
    print(f"\n{nouveau_nom} a été ajouté avec ses notes {nouvelles_notes}.")

# Décommentez la ligne ci-dessous pour tester l'ajout d'étudiant interactif
# ajouter_etudiant()
