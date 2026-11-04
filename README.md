# Mini-projet Python — Gestion des étudiants

## Présentation du projet
Ce projet a été réalisé dans le cadre d'un mini-projet d'apprentissage du langage Python. Il s'agit d'un programme permettant de gérer les notes d'une classe de 7 étudiants. 

Le script traite les données des étudiants, calcule leurs moyennes, leur attribue des mentions selon un barème précis, et réalise des statistiques globales sur la classe avant d'exporter les résultats.

## Fonctionnalités
Le code est structuré en plusieurs parties répondant aux consignes :
*   **Partie 1 :** Création et organisation des données (listes et dictionnaires).
*   **Partie 2 :** Calcul des moyennes individuelles, attribution des mentions et identification du meilleur étudiant.
*   **Partie 3 :** Analyse globale (moyenne générale, taux de validation, répartition des mentions).
*   **Partie 4 :** Sauvegarde automatique de tous les résultats dans un fichier `resultats.txt`.
*   **Partie 5 :** Fonction de recherche permettant de retrouver les informations d'un étudiant via son prénom.
*   **Partie 6 (Bonus) :** Ajout interactif d'un nouvel étudiant avec saisie sécurisée des notes (comprises entre 0 et 20).

## Technologies utilisées
*   **Langage :** Python 3.x
*   **Bibliothèques :** Aucune bibliothèque externe n'est requise. Le code utilise uniquement les structures de contrôle et de données natives de Python (boucles, conditions, listes, dictionnaires).

## Comment utiliser ce programme ?
1. Clonez ce dépôt ou téléchargez le fichier principal Python (par exemple `main.py`).
2. Ouvrez un terminal dans le dossier contenant le fichier.
3. Exécutez le script avec la commande suivante :
   ```bash
   python main.py
   ```
4. Le programme affichera les analyses dans la console et générera automatiquement un fichier `resultats.txt` dans le même dossier.
5. *(Optionnel)* Pour tester l'ajout interactif d'un étudiant (Partie 6), décommentez la dernière ligne du script `ajouter_etudiant()`.