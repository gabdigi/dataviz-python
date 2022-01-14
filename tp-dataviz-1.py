"""
l'origine vient du site coincap un site qui permet de récupérer
100 cryptomonnaie les plus connu en concurence.
J'ai pris cette api pour une utilisation sans demande d'identification par clé api 
et sans protection spécifique que je peut réutiliser plus tard pour d'autre projet.
j'ai pris l'utilisation du bar chart pour bien différencier les prix entre monnaies

"""

import matplotlib.pyplot as pyplot

import requests
import json

x_value = []
y_value = [] 

response = requests.get("https://api.coincap.io/v2/assets")

data = response.json()

for i in range(len(data['data'])):
    
    x = data['data'][i]['id']
    y = float(data['data'][i]['priceUsd'])

    x_value.append(x)
    y_value.append(round(y, 2))
    


pyplot.bar(x_value, y_value, color = "purple", width = 0.8)
pyplot.gca() # Ordre croissant de date .invert_xaxis()
pyplot.xticks(rotation='vertical') # Retourner les labels
pyplot.xlabel("nom des cryptomonnaies") # Légende à X
pyplot.ylabel("prix des cryptomonnaies") # Légende pour Y
pyplot.ylim(ymin=0)
#pyplot.xlim(xmin=100)


# On ajoute un titre et on modifie sa taille
titre = pyplot.title('Prix des cryptomonnaies en dollar')
titre.set_fontsize(14)

# On affiche notre chart avec toutes ses configurations
pyplot.show()