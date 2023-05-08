from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from data.data import nutrients, data
from random import choices
from copy import deepcopy
import pandas as pd
import numpy as np

df_nutrients = pd.DataFrame(nutrients, columns=['Nutrient', 'Amount'])

df_data = pd.DataFrame(data, columns=['Commodity', 'Unit', '1939 price (cents)', 'Calories (kcal)',
                                      'Protein (g)', 'Calcium (g)', 'Iron (mg)', 'Vitamin A (KIU)', 'Vitamin B1 (mg)',
                                        'Vitamin B2 (mg)', 'Niacin (mg)', 'Vitamin C (mg)'])
print(df_data)
print(df_nutrients)



