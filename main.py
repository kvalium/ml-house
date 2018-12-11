# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# On charge le dataset
house_data = pd.read_csv('house_data.csv')

# house_training = house_data.sample(n=int(len(house_data) * 0.8))

house_arrondissement = house_data.loc[house_data['arrondissement'] == 10.]
# On affiche le nuage de points dont on dispose
plt.plot(house_arrondissement['surface'], house_arrondissement['price'], 'ro', markersize=4)
plt.show()
