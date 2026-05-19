import random

def modifier_mot_cache(lettre, mot_solution,mot_cache):
    compteur = 0  # pour identifier la position de lettre dans le mot caché
    nb_lettres_modifiees=0
    for i in mot_solution :
        if lettre==i: #On regarde à chaque élément du mot solution si la lettre apparaît
            nb_lettres_modifiees +=1 #Elle apparait donc on a +1 lettre modifiée
            mot_cache[compteur]=lettre #Elle apparaît dans mot caché donc on la "révèle" en remplaçant _ par lettre
        compteur+=1
    return mot_cache, nb_lettres_modifiees

def initialiser_mot_cache(mot_solution) :
    mot_cache=[]
    for i in mot_solution : #On parcourt chaque lettre du mot_solution
        mot_cache.append("_") #Pour chaque lettre on va ajouter un "_" pour cacher le mot
    return mot_cache

def deroulement_partie_pendu(mot_solution) :
    mot_cache=initialiser_mot_cache(mot_solution)
    essais=6
    vie=essais
    while "_" in mot_cache and vie>0:
        print(f"Il vous reste {vie} vies")
        print(mot_cache)
        lettre=input("Ecrivez la lettre à essayer : ")[0] #le [0] permet de s'assurer que l'on prend la 1ère lettre
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


def choisir_fichier():
    print("Voulez-vous utiliser le fichier par défaut ?")
    choix = input("Tapez 'o' pour oui, 'n' pour utiliser votre fichier perso : ").lower()
    while choix not in ["o", "n"]:
        print("Saisie invalide.")
        choix = input("Tapez 'o' pour oui, 'n' pour utiliser votre fichier perso : ").lower()
    if choix == "o":
        return "fichier_par_defaut.txt"
    else:
        return "mots_pendu.txt"

def choisir_mot(nom_fichier):
    with open(nom_fichier, "r", encoding="utf-8") as f:
        mots = f.readlines()

    mots = [mot.strip() for mot in mots]
    return random.choice(mots)

def demarrer_partie_pendu() :
    nom_fichier=choisir_fichier()
    mot_solution=choisir_mot(nom_fichier)
    deroulement_partie_pendu(mot_solution)


