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

''' TEM DE SE CORRIGIR PARA OS CASOS EM QUE A QUANTIDADE É No. 2 1/2'''

def extract_quantity(string):
    # First, we'll use regular expressions to extract the numerical quantity
    pattern = r'(\d+(\.\d+)?)/?(\d+(\.\d+)?)?'
    match = re.search(pattern, string)
    if match is None:
        return None
    whole = match.group(1)
    fraction = match.group(3)
    
    # If there's a fraction, we'll divide it by 2 to get the decimal equivalent
    if fraction is not None:
        fraction = str(float(fraction) / 2)
    
    # If there's both a whole and a fraction, we'll add them together
    if whole is not None and fraction is not None:
        return float(whole) + float(fraction)
    
    # Otherwise, we'll just return whichever one is not None
    if whole is not None:
        return float(whole)
    else:
        return float(fraction)
    

# print( extract_quantity ('1/2 stalk'))

# Print the representation of each individual in the population
for i, ind in enumerate(pop.individuals):
    print(f"Individual {i}: {ind.representation}")

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
            #get the quantity in data
            original_qtd = extract_quantity(food[1]) #this quantity costs 1 dollar
            
            #if original quantity costs 1 dollar, then ind.representation[i] costs x dollars
            total_cost += ind.representation[i] / original_qtd

            # print(food[0] + ' - ' + str(food[2]))

            calories += ind.representation[i] * food[3] / original_qtd
            protein += ind.representation[i] * food[4] / original_qtd
            calcium += ind.representation[i] * food[5] / original_qtd
            iron += ind.representation[i] * food[6] / original_qtd
            vitamin_A += ind.representation[i] * food[7] / original_qtd
            vitamin_B1 += ind.representation[i] * food[8] / original_qtd
            vitamin_B2 += ind.representation[i] * food[9] / original_qtd
            niacin += ind.representation[i] * food[10] / original_qtd
            vitamin_C += ind.representation[i] * food[11] / original_qtd

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


# if __name__ == '__main__':
#   print(data)