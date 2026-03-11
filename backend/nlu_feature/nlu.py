import pandas as pd
import numpy as np

#On lit le fichier du dataset 
try: 
    data = pd.read_csv('dataset.csv',encoding="utf-8")
    print("Fichier chargé avec succès")
    print(data)

except FileNotFoundError: 
    print("Erreur, fichier non trouvé")

except Exception as e:
    print("Une erreur est survenue")   
