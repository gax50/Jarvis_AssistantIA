import math
import numpy as np
from preprocessing import nettoyer_phrase, nettoyer_dataset, charger_dataset

K_value = 3 #Pour l'algo KNN

#on appelle le resulat du chargement des données
contenu = charger_dataset()

#2 arguments car nettoyer dataset returne 2 valeurs
intentions, vocabulaire_global = nettoyer_dataset(contenu)

phrase_user = input("Entrez une commande: \n")

def vectoriser(phrase_user, vocabulaires):
    vecteur = np.zeros(len(vocabulaires) , dtype=int)
    clean = nettoyer_phrase(phrase_user)
    for word in vocabulaires:
        if word in clean:
            indice = vocabulaires.index(word)
            vecteur[indice] = 1

    print(vecteur)
    return(vecteur)

vectoriser(phrase_user,vocabulaire_global)

