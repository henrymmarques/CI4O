from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from data.data import nutrients, data
from random import choices
from copy import deepcopy
import pandas as pd
import numpy as np
import re

pop_size = 10

# Define the range of valid values for each quantity
# valid_set = range(0,50)
valid_set = range(0,len(data))

foods = [food[2:] for food in data]

sol_size=len(data)

optim="min"




def get_fitness(self):
    # total_cost = sum([data[i][2] * self.representation[i] for i in range(len(data))])
    # nutrient_values = [sum([nutrients[i][1] * nutrients[i][j] * self.representation[j] for j in range(len(data))]) for i in range(len(nutrients))]
    # nutrient_deficits = [max(0, nutrients[i][1] - nutrient_values[i]) for i in range(len(nutrients))]
    # nutrient_costs = [sum([nutrients[i][2][j] * nutrients[i][j] * self.representation[j] for j in range(len(data))]) for i in range(len(nutrients))]
    # nutrient_costs = [cost if nutrient_deficits[i] > 0 else 0 for i, cost in enumerate(nutrient_costs)]
    # total_nutrient_cost = sum(nutrient_costs)
    # fitness = total_cost + total_nutrient_cost
    # return fitness
    return 1

def get_neighbours(self):
    
    return 1

# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(
    size=pop_size,
    sol_size=sol_size,
    valid_set=valid_set,
    replacement=True,
    optim=optim)



# $%$$$$$$$$$$$$$$ TESTES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# print( extract_quantity ('1/2 stalk'))

# Print the representation of each individual in the population
for i, ind in enumerate(pop.individuals):
    print(f"Individual {i}: {ind.representation}")
    fitness=0
    total_cost = 0
    calories = 0
    protein = 0
    calcium = 0
    iron = 0
    vitamin_A = 0
    vitamin_B1 = 0
    vitamin_B2 = 0
    niacin = 0
    vitamin_C = 0
    for i, food in enumerate(data):
        if ind.representation[i] > 0:
            #print(ind.representation[i])
            
            
            #if original quantity costs 1 dollar, then ind.representation[i] costs x dollars
            ## tirei em todas as variáveis a divisao pela original qtd!!!
            total_cost += ind.representation[i]

            #print(food[0] + ' - ' + str(food[2]))

            calories += ind.representation[i] * food[3]
            protein += ind.representation[i] * food[4]
            calcium += ind.representation[i] * food[5]
            iron += ind.representation[i] * food[6]
            vitamin_A += ind.representation[i] * food[7]
            vitamin_B1 += ind.representation[i] * food[8] 
            vitamin_B2 += ind.representation[i] * food[9] 
            niacin += ind.representation[i] * food[10] 
            vitamin_C += ind.representation[i] * food[11]
            fitness=total_cost

    if calories < nutrients[0][1]*365:
        fitness=1000
        print('Calories not sufficient')
        print(calories, nutrients[0][1]*365)
    if protein < nutrients[1][1]*365:
        fitness=1000
        print('Protein not sufficient')
        print(protein, nutrients[1][1]*365)
    if calcium < nutrients[2][1]*365:
        fitness=1000
        print('Calcium not sufficient')
        print(calcium, nutrients[2][1]*365)

    if iron < nutrients[3][1]*365:
        fitness=1000
        print('Iron not sufficient')
        print(iron, nutrients[3][1]*365)

    if vitamin_A < nutrients[4][1]*365:
        fitness=1000
        print('Vitamin A not sufficient')
        print(vitamin_A, nutrients[4][1]*365)

    if vitamin_B1 < nutrients[5][1]*365:
        fitness=1000
        print('Vitamin B1 not sufficient')
        print(vitamin_B1, nutrients[5][1]*365)

    if vitamin_B2 < nutrients[6][1]*365:
        fitness=1000
        print('Vitamin B2 not sufficient')
        print(vitamin_B2, nutrients[6][1]*365)

    if niacin < nutrients[7][1]*365:
        fitness=1000
        print('Niacin not sufficient')
        print(niacin, nutrients[7][1]*365)

    if vitamin_C < nutrients[8][1]*365:
        fitness=1000
        print('Vitamin C not sufficient')
        print(vitamin_C, nutrients[8][1]*365)


    print(' ')
    print('cost = ' + str(total_cost))
    print('calories = ' + str(calories))
    print('protein = ' + str(protein))
    print('calcium = ' + str(calcium))
    print('iron = ' + str(iron))
    print('vitamin_A = ' + str(vitamin_A))
    print('vitamin_B1 = ' + str(vitamin_B1))
    print('vitamin_B2 = ' + str(vitamin_B2))
    print('niacin = ' + str(niacin))
    print('vitamin_C = ' + str(vitamin_C))
    print('_____________________________________________')
    print('Fitness = ' + str(fitness))

# if __name__ == '__main__':
#   print(data)