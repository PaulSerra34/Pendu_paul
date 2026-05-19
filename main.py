"""
18 Mai 2026
Auteur : Paul SERRA
Titre : Jeu du pendu
"""

import random
import unicodedata

def choisir_fichier(): #Fonction permettant de sélectionner le fichier contenant les mots
    print("Voulez-vous utiliser le fichier par défaut ?")
    choix = input("Tapez 'o' pour oui, 'n' pour utiliser votre fichier perso : ").lower()
    while choix not in ["o", "n"]: #Pour éviter les erreurs de saisie
        print("Saisie invalide.")
        choix = input("Tapez 'o' pour oui, 'n' pour utiliser votre fichier perso : ").lower()
    if choix == "o":
        return "fichier_par_defaut.txt"
    else:
        return "mots_pendu.txt"

def choisir_mot(nom_fichier): #Fonction permettant de choisir un mot dans un fichier spécifique de manière aléatoire
    with open(nom_fichier, "r", encoding="utf-8") as f:
        mots = f.readlines()
    mots = [mot.strip() for mot in mots]
    return random.choice(mots)

def initialiser_mot_cache(mot_solution) : #Fonction recréant une copie cachée du mot à trouver
    mot_cache=[]
    for i in mot_solution : #On parcourt chaque lettre du mot_solution
        mot_cache.append("_") #Pour chaque lettre on va ajouter un "_" pour cacher le mot
    return mot_cache


def modifier_mot_cache(lettre, mot_solution,mot_cache): #Permet de révéler les lettres trouvées
    compteur = 0  # pour identifier la position de lettre dans le mot caché
    nb_lettres_modifiees=0
    for i in mot_solution :
        if lettre==i: #On regarde à chaque élément du mot solution si la lettre apparaît
            nb_lettres_modifiees +=1 #Elle apparait donc on a +1 lettre modifiée
            mot_cache[compteur]=lettre #Elle apparaît dans mot caché donc on la "révèle" en remplaçant _ par lettre
        compteur+=1
    return mot_cache, nb_lettres_modifiees

def normaliser_lettre(lettre): #Permet d'éviter les soucis d'accents et de majuscule pour les lettres (ex : a et à sont différents au départ)
    return unicodedata.normalize("NFD", lettre)[0].lower()

def normaliser_mot(mot):
    return "".join(unicodedata.normalize("NFD", lettre)[0].lower() for lettre in mot) #uniformise les lettres au sein d'un mot

def deroulement_partie_pendu(mot_solution, mot_cache, vie) : #Fonction consistant en l'itération d'une partie
    aide=1 #défini le nombre de fois que le joueur va être aidé
    while "_" in mot_cache and vie>0:
        print(f"Il vous reste {vie} vies")
        print("".join(mot_cache)) #Le join permet de "lisser" le mot
        if vie==1 and aide==1:
            mot_cache=aider_joueur(mot_solution, mot_cache) #Dévoile une lettre au joueur
            aide=0
            if "_" not in mot_cache:
                continue #Court-cicuite la boucle dans le cas où l'aide dévoilerait la dernière lettre
        lettre=input("Ecrivez la lettre à essayer : ")
        while len(lettre) == 0 or not lettre.isalpha(): #Permet de s'assurer qu'on a écrit une seule lettre
            print("Saisie invalide.")
            lettre = input("Ecrivez la lettre à essayer : ")
        lettre=normaliser_lettre(lettre)  #Pour avoir les lettres en minuscules et sans accents
        mot_cache,nb_lettres_modifiees=modifier_mot_cache(lettre,mot_solution,mot_cache)
        print(f"La lettre {lettre} est présente {nb_lettres_modifiees} fois dans le mot")
        if nb_lettres_modifiees==0: #Si aucune lettre n'est modifiée on perd une vie
            vie-=1
    if vie==0:
        print(f"Vous avez perdu, il ne vous reste plus aucune vie. Le mot était {mot_solution}")
    else:
        print(f"Félicitations, vous avez gagné ! Le mot était bien {mot_solution}")
    print("Voulez-vous redémarrer une partie ?")
    choix=input("Tapez 'o' pour oui, 'n' pour non et arrêter le jeu : ").lower()
    while choix not in ["o", "n"]:
        print("Saisie invalide.")
        choix = input("Tapez 'o' pour oui, 'n' pour non et arrêter le jeu : ").lower()
    if choix=="o":
        demarrer_partie_pendu()
    else :
        print("Merci d'avoir joué !")

def demarrer_partie_pendu() : #Fonction initiale qui permet de lancer le jeu du pendu
    nom_fichier=choisir_fichier()
    mot_solution=normaliser_mot(choisir_mot(nom_fichier))
    tentatives=modifier_nombre_tentatives()
    mot_cache=initialiser_mot_cache(mot_solution)
    deroulement_partie_pendu(mot_solution, mot_cache, tentatives)

def modifier_nombre_tentatives(): #Fonction pour modifier le nombre de tentatives
    tentatives=6 #valeur par défaut
    print("Voulez-vous modifier le nombre de vies (6 par défaut) ?")
    choix = input("Tapez 'o' pour oui, 'n' pour garder la valeur par défaut (6) : ").lower()
    while choix not in ["o", "n"]:
        print("Saisie invalide.")
        choix = input("Tapez 'o' pour oui, 'n' pour utiliser la valeur par défaut (6) : ").lower()
    if choix == "o":
        tentatives= input("Veuillez écrire le nombre de tentatives : ")
        while not tentatives.isdigit() or int(tentatives)<=0: #empêche la saisie d'autre chose que d'un nombre strictement positif
            print("Saisie invalide, veuillez entrer un nombre strictement positif.")
            tentatives = input("Veuillez écrire le nombre de tentatives : ")
        tentatives = int(tentatives)
    return tentatives

def aider_joueur(mot_solution, mot_cache):
    compteur=0
    while mot_cache[compteur]!="_": #On part du principe qu'il existe un "_" dans mot caché car sinon le joueur aurait gagné
        compteur+=1
    lettre_aide=mot_solution[compteur]
    mot_cache=modifier_mot_cache(lettre_aide,mot_solution,mot_cache)[0] #On affiche la lettre indice
    print(f"Pour vous aider voici une lettre bonus : {lettre_aide} !")
    print("Le mot que vous cherchez devient :")
    print("".join(mot_cache))
    return mot_cache

demarrer_partie_pendu()
