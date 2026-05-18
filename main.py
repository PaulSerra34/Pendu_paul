l="test"
l1=["_","_","s","_"]


def f(lettre, mot_s,mot_c):
    compteur = 0  # pour identifier la position de lettre dans le mot caché
    nb_lettres_modifie=0
    for i in mot_s:
        if lettre==i: #On regarde à chaque élément du mot si la lettre apparaît
            nb_lettres_modifie +=1
            mot_c[compteur]=lettre #Si elle apparait dans mot caché alors on la "révèle"
        compteur+=1
    return mot_c, nb_lettres_modifie

print(f("t",l,l1))