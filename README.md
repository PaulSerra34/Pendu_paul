# Jeu du Pendu

**Auteur :** Paul SERRA  
**Date :** 18 Mai 2026  

---

## Description

Programme Python implémentant le jeu du pendu en ligne de commande. Le joueur doit deviner un mot caché lettre par lettre avant d'épuiser ses tentatives. Le mot est sélectionné aléatoirement depuis un fichier texte, et le joueur peut personnaliser le nombre de vies ainsi que le fichier de mots utilisé.

---

## Contenu du dépôt

```
Pendu/
├── main.py                  # Script principal contenant toutes les fonctions
├── fichier_par_defaut.txt   # Banque de mots fournie par défaut
├── mots_pendu.txt           # Fichier de mots personnalisé (optionnel)
└── README.md                # Ce fichier
```

---

## Fonctionnalités

- Sélection aléatoire d'un mot depuis un fichier texte
- Affichage de l'état du mot avec `_` pour les lettres non devinées
- Gestion des tentatives (6 par défaut, modifiable)
- Normalisation des accents et des majuscules (ex : `é` → `e`)
- Validation des saisies utilisateur
- Possibilité d'utiliser un fichier de mots personnalisé
- Proposition de recommencer ou quitter en fin de partie
- **Bonus :** Indice automatique lorsqu'il ne reste qu'une seule vie

---

## Utilisation

### Prérequis

- Python 3.x installé
- Les modules `random` et `unicodedata` (inclus dans la bibliothèque standard Python, aucune installation requise)

### Lancement

```bash
python main.py
```

### Déroulement d'une partie

1. **Choix du fichier** : le programme demande si vous souhaitez utiliser le fichier par défaut ou votre fichier personnel `mots_pendu.txt`
2. **Choix du nombre de vies** : 6 par défaut, modifiable avant le début de la partie
3. **Partie** : à chaque tour, l'état du mot est affiché et le programme demande une lettre
4. **Fin de partie** : le programme indique si vous avez gagné ou perdu, puis propose de rejouer

### Fichier de mots personnalisé

Vous pouvez fournir votre propre liste de mots en créant un fichier `mots_pendu.txt` à la racine du projet, avec **un mot par ligne** :

```
chat
maison
ordinateur
...
```

---

## Structure du code

Le programme est entièrement composé de fonctions :

| Fonction | Rôle |
|---|---|
| `choisir_fichier()` | Sélectionne le fichier de mots à utiliser |
| `choisir_mot()` | Pioche un mot aléatoire dans le fichier |
| `initialiser_mot_cache()` | Crée la version cachée du mot (`_ _ _ _`) |
| `modifier_mot_cache()` | Révèle les lettres trouvées dans le mot caché |
| `normaliser_lettre()` | Supprime les accents et met en minuscule une lettre |
| `normaliser_mot()` | Applique la normalisation à un mot entier |
| `modifier_nombre_tentatives()` | Permet de modifier le nombre de vies |
| `aider_joueur()` | Révèle une lettre indice quand il reste une vie |
| `deroulement_partie_pendu()` | Gère la boucle principale de jeu |
| `demarrer_partie_pendu()` | Point d'entrée du programme |
