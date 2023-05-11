from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from data.data import nutrients, data
from charles.selection import fps, tournament_sel
from charles.mutation import binary_mutation
# from charles.crossover import single_point_co
from random import choices
from copy import deepcopy
import pandas as pd
import numpy as np

df_nutrients = pd.DataFrame(nutrients, columns=['Nutrient', 'Amount'])

df_data = pd.DataFrame(data, columns=['Commodity', 'Unit', '1939 price (cents)', 'Calories (kcal)',
                                      'Protein (g)', 'Calcium (g)', 'Iron (mg)', 'Vitamin A (KIU)', 'Vitamin B1 (mg)',
                                        'Vitamin B2 (mg)', 'Niacin (mg)', 'Vitamin C (mg)'])
print(df_data)
print(df_nutrients.loc[0][1])


def fitness_function(self):
  fitness=0
  calories=0
  protein=0
  calcium=0
  iron=0
  vitamin_a=0
  vitamin_b1=0
  vitmain_b2=0
  niacin=0
  vitamin_c=0
  for i in range(len(self.representation)):
    fitness= fitness + df_data.loc[i][2]
    if check_constraints:
      return fitness
    else:
      return 1000

#def get_neighbours(self):


Individual.get_fitness = fitness_function
#Individual.get_neighbours = get_neighbours

pop = Population(size=len(df_data), optim="min", sol_size=len(data), valid_set=[0, 1], replacement=True)

'''pop.evolve(gens=100, xo_prob=0.9, mut_prob=0.2, select=tournament_sel,
           mutate=binary_mutation, crossover=single_point_co,
           elitism=True)'''


if __name__ == '__main__':
  print(data)