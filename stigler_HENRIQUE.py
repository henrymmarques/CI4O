from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from charles.crossover import two_point_crossover, sbx, arithmetic_xo, single_point_co
from charles.selection import tournament_sel, fps, rank_selection
from charles.mutation import inversion_mutation, swap_mutation, uniform_mutation
from data.data import nutrients, data
from random import choices
from copy import deepcopy
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pop_size = 50

# Define the range of valid values for each quantity
# valid_set = range(0,50)
valid_set = range(0,len(data))

foods = [food[2:] for food in data]
sol_size=len(data)
optim="min"

def get_fitness(self):
    print(f"Individual : {self.representation}")

    fitness = 0
    total_cost = 0
    calories = 0
    protein = 0
    calcium = 0
    iron = 0
    vitamin_A = 0
    vitamin_B1 = 0
    vitamin_B2 = 0
    vitamin_C = 0
    niacin = 0
    all_satisfied=True
    for i, food in enumerate(data):
        if self.representation[i] > 0:
            
            total_cost += self.representation[i]

            calories += self.representation[i] * food[3]
            protein += self.representation[i] * food[4]
            calcium += self.representation[i] * food[5]
            iron += self.representation[i] * food[6]
            vitamin_A += self.representation[i] * food[7]
            vitamin_B1 += self.representation[i] * food[8] 
            vitamin_B2 += self.representation[i] * food[9] 
            niacin += self.representation[i] * food[10] 
            vitamin_C += self.representation[i] * food[11]
            fitness=total_cost

    if calories < nutrients[0][1]*365:
        fitness += nutrients[0][1]*365 - calories
        all_satisfied=False
        # print('Calories not sufficient')
        # print(calories, nutrients[0][1]*365)
    if protein < nutrients[1][1]*365:
        fitness += nutrients[1][1]*365 - protein
        all_satisfied=False        
        # print('Protein not sufficient')
        # print(protein, nutrients[1][1]*365)
    if calcium < nutrients[2][1]*365:
        fitness += nutrients[2][1]*365 - calcium
        all_satisfied=False
        # print('Calcium not sufficient')
        # print(calcium, nutrients[2][1]*365)

    if iron < nutrients[3][1]*365:
        fitness += nutrients[3][1]*365 - iron
        all_satisfied=False
        # print('Iron not sufficient')
        # print(iron, nutrients[3][1]*365)

    if vitamin_A < nutrients[4][1]*365:
        fitness += nutrients[4][1]*365 - vitamin_A
        all_satisfied=False
        # print('Vitamin A not sufficient')
        # print(vitamin_A, nutrients[4][1]*365)

    if vitamin_B1 < nutrients[5][1]*365:
        fitness += nutrients[5][1]*365 - vitamin_B1
        all_satisfied=False
        # print('Vitamin B1 not sufficient')
        # print(vitamin_B1, nutrients[5][1]*365)

    if vitamin_B2 < nutrients[6][1]*365:
        fitness += nutrients[6][1]*365 - vitamin_B2
        all_satisfied=False
        # print('Vitamin B2 not sufficient')
        # print(vitamin_B2, nutrients[6][1]*365)

    if niacin < nutrients[7][1]*365:
        fitness += nutrients[7][1]*365 - niacin
        all_satisfied=False
        # print('Niacin not sufficient')
        # print(niacin, nutrients[7][1]*365)

    if vitamin_C < nutrients[8][1]*365:
        fitness += nutrients[8][1]*365 - vitamin_C
        all_satisfied=False
        # print('Vitamin C not sufficient')
        # print(vitamin_C, nutrients[8][1]*365)

    if all_satisfied==True:
        print('##############################################################')
        print('________________________ALL SATISFIED______________________')
        print('##############################################################')


        print(' ')
        print('cost = ' + str(round(total_cost,3)))
        print('calories = ' + str(round(calories,3)))
        print('protein = ' + str(round(protein,3)))
        print('calcium = ' + str(round(calcium,3)))
        print('iron = ' + str(round(iron,3)))
        print('vitamin_A = ' + str(round(vitamin_A,3)))
        print('vitamin_B1 = ' + str(round(vitamin_B1,3)))
        print('vitamin_B2 = ' + str(round(vitamin_B2,3)))
        print('niacin = ' + str(round(niacin,3)))
        print('vitamin_C = ' + str(round(vitamin_C,3)))
        print('_____________________________________________')
    print('Fitness = ' + str(fitness))
    # print('_____________________________________________')
    # print('_____________________________________________')
    return fitness



def get_neighbours(self):
    """
    Generates neighbors of an individual by slightly changing the amount of money spent on each food item.

    Returns:
        list: A list of neighbor individuals.
    """
    epsilon = 0.1  # The amount by which the money spent is changed

    neighbors = []
    for i, amount_spent in enumerate(self):
        if amount_spent > 0:
            # Increase the money spent on the food item by epsilon
            increased_neighbor = self.copy()
            increased_neighbor[i] += epsilon
            neighbors.append(increased_neighbor)

            # Decrease the money spent on the food item by epsilon
            decreased_neighbor = self.copy()
            decreased_neighbor[i] -= epsilon
            neighbors.append(decreased_neighbor)

    return neighbors

# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(
    size=pop_size,
    sol_size=sol_size,
    valid_set=valid_set,
    replacement=True,
    optim=optim)

pop.evolve(gens=100, select=tournament_sel, crossover=two_point_crossover,
           xo_prob=0.9, elitism=True, mutate=uniform_mutation, mut_prob=0.7)
pop.evolve(gens=100, select=tournament_sel, crossover=two_point_crossover,
           xo_prob=0.9, elitism=True, mutate=inversion_mutation, mut_prob=0.7)




# if __name__ == '__main__':
#   print(get_neighbours([10.49, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.46, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3.33, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11.45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10.2, 0, 0, 0, 0, 0, 0, 11.39, 14.39, 0, 0, 0, 0, 0, 0, 0, 0, 13.8, 0, 0, 0, 0, 0, 0, 0, 0]))