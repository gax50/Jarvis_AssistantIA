import math
import numpy as np
from preprocessing import nettoyer_phrase, nettoyer_dataset, charger_dataset

K_value = 3 #Pour l'algo KNN

#on appelle le resulat du chargement des données
contenu = charger_dataset()

#2 arguments car nettoyer dataset returne 2 valeurs
dataset_entrainement, vocabulaire_globale = nettoyer_dataset(contenu)


def vectoriser(phrase_commande, vocabulaire):
    vecteur = np.zeros(len(vocabulaire), dtype=int)
    for mot in phrase_commande:
        if mot in vocabulaire:
            indice = vocabulaire.index(mot)
            vecteur[indice] = 1

    return vecteur

#Vectoriser tous les lignes du dataset
def entrainer_modele(dataset, vocabulaire):

    #Matrice vide
    X_temp = []
    for ligne in dataset:
       mots_dataset = ligne[0]
       v_ligne = vectoriser(mots_dataset, vocabulaire)
       X_temp.append(v_ligne)
    
    return np.array(X_temp)

X_train = entrainer_modele(dataset_entrainement, vocabulaire_globale)
print(X_train)

def prompt_user():
    sentence = input("Que voulez vous faire? \n")
    clean_sentence = nettoyer_phrase(sentence)
    resultat = vectoriser(clean_sentence, vocabulaire_globale)
    return resultat


vecteur_user = prompt_user()


#Calcul de la distance eucludienne



def calcul_des_distances(v_user, v_dataset):
    distances = []

    #v_ligne represente dataset, v_dataset tous les lignes du dataset
    for v_ligne in v_dataset:

        #v_user represente vecteur de l'input user
        difference = v_user - v_ligne

        somme_carree = np.sum(difference**2)

        distance = math.sqrt(somme_carree)
        distances.append(distance)

        #la plus petite distance
        distance_min = np.argmin(distances)
    print(f"La commande la plus proche est a la ligne {distance_min}")
    commande_a_executer = dataset_entrainement[distance_min][1]
    print(f"Jarvis a decidé de",commande_a_executer)

calcul_des_distances(vecteur_user, X_train)