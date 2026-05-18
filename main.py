l="test"
l1=["_","_","s","_"]
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
