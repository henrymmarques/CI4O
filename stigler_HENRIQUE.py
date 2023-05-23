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
import time
import matplotlib.pyplot as plt

#Define population size (number of individuals)
pop_size = 50

# Define the range of valid values for each quantity
valid_set = range(0,len(data))

#define solution size
sol_size=len(data)

#define optimization type
optim="min"


# Calculate an individual's fitness value (based on the sum of the amount of money spent on each food item)
# Printable argument is set to false when running epochs in order to don't see too many prints
def get_fitness(self, printable=False):
    if printable:
        print(f"Individual : {self.representation}")
    # Define nutritional variables (to check and evaluate if solutions are enought to cover nutritional needs) and also defines
    # fitness and total cost variables.
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
    # Iterate over each food item
    for i, food in enumerate(data):
        if self.representation[i] > 0:
            
            total_cost += self.representation[i]

            # Calculate the total nutritional values based on the amount spent on each food item
            calories += self.representation[i] * food[3]
            protein += self.representation[i] * food[4]
            calcium += self.representation[i] * food[5]
            iron += self.representation[i] * food[6]
            vitamin_A += self.representation[i] * food[7]
            vitamin_B1 += self.representation[i] * food[8] 
            vitamin_B2 += self.representation[i] * food[9] 
            niacin += self.representation[i] * food[10] 
            vitamin_C += self.representation[i] * food[11]

            fitness=total_cost # Set fitness as the total cost

    # Check if the nutritional requirements are satisfied for yearly values (obtained by multiplying daily values for the number of days that a year has)
    if calories < nutrients[0][1]*365:
        fitness += nutrients[0][1]*365 - calories
        all_satisfied=False #all_satified is defined as False in case any of the requirements is not satisfied)

    if protein < nutrients[1][1]*365:
        fitness += nutrients[1][1]*365 - protein
        all_satisfied=False     

    if calcium < nutrients[2][1]*365:
        fitness += nutrients[2][1]*365 - calcium
        all_satisfied=False

    if iron < nutrients[3][1]*365:
        fitness += nutrients[3][1]*365 - iron
        all_satisfied=False

    if vitamin_A < nutrients[4][1]*365:
        fitness += nutrients[4][1]*365 - vitamin_A
        all_satisfied=False

    if vitamin_B1 < nutrients[5][1]*365:
        fitness += nutrients[5][1]*365 - vitamin_B1
        all_satisfied=False

    if vitamin_B2 < nutrients[6][1]*365:
        fitness += nutrients[6][1]*365 - vitamin_B2
        all_satisfied=False

    if niacin < nutrients[7][1]*365:
        fitness += nutrients[7][1]*365 - niacin
        all_satisfied=False

    if vitamin_C < nutrients[8][1]*365:
        fitness += nutrients[8][1]*365 - vitamin_C
        all_satisfied=False

    if all_satisfied and printable:
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
    if printable:
        print('Fitness = ' + str(fitness))
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

#Create a population variable
pop = Population(
    size=pop_size,
    sol_size=sol_size,
    valid_set=valid_set,
    replacement=True,
    optim=optim)


#----------------------------------------------------------------------------------------------------------#


def run_multiple_configurations(configurations, epochs=None, printable=True):
    """function to run population evolution over a list of configurations 

    Args:
        configurations: List of dictionaries configurations
        epochs: define if it is called inside the run_epochs function. If false prints a plot
        printable: boolean to define if it prints

    Returns:
        fit_list: list of the size of the configurations list, containing the best fitness for each configuration
    """

    all_fitness_values = []  # List to store fitness values for all configurations
    selection_types = []  # List to store selection types for labeling

    for config in configurations: #Iterate over a set of configurations
        selection_type = config["select"]  # Get the selection type from the configuration
        selection_types.append(selection_type)  # Store the selection type for labeling

        pop = Population(
            size=pop_size,
            sol_size=sol_size,
            valid_set=valid_set,
            replacement=True,
            optim=optim
        )
        fitness_values = pop.evolve(config["gens"], config["xo_prob"], config["select"], config["crossover"],
                                    config["elitism"], config["mutate"], config["mut_prob"], printable=printable)

        all_fitness_values.append(fitness_values)  # Store the fitness values for this configuration

    if epochs is False:
        plt.figure(figsize=(10,6))
        # Plot the fitness values for all configurations
        for i, fitness_values in enumerate(all_fitness_values):
            generation_numbers = range(1, len(fitness_values) + 1)
            plt.plot(generation_numbers, fitness_values, label=create_labels(configurations[i]))  # Set the label as the selection type
            # Find the lowest fitness value and its index
            lowest_fitness = min(fitness_values)

            # Add a text label for the lowest value
            plt.text(len(fitness_values), lowest_fitness, f"Min: {round(lowest_fitness, 2)}", ha='right')
        plt.xlabel("Generation")
        plt.ylabel("Fitness")
        plt.title("Evolution Fitness Progress")
        plt.legend()
        plt.ylim(0, 250)
        plt.show()
        return

    fit_list = [min(fitness_values) for fitness_values in all_fitness_values] #List with the minimum fitness values
    return fit_list


def create_labels(config):
    '''
    creates personalized label given a configuration
    '''

    label = "SEL: " + config['select'].__name__ + " | XO: " + config['crossover'].__name__ + '(' + str(config['xo_prob']) + ')' \
            + " | MUT: " + config['mutate'].__name__ + '(' + str(config['mut_prob']) + ')'
    return label


def run_epochs(numb_epochs):
    """function to run n epochs using the run_multiple_configurations function

    Args:
        numb_epochs: number of epochs

    Returns:
        mean_values: list of the mean values of all best fitness for each configuration
    """
    best_list = [] # List to store the best fitness values for each epoch
    start_time = time.time()  # Start time for the epochs

    for epoch in range(1, numb_epochs + 1):
        epoch_start_time = time.time()  # Start time for the current epoch
        best_list.append(run_multiple_configurations(configurations=configurations, epochs=True, printable=False))
        epoch_elapsed_time = time.time() - epoch_start_time  # Elapsed time for the current epoch

        # Estimate remaining time based on the average elapsed time
        average_elapsed_time = (time.time() - start_time) / epoch  # Average elapsed time per epoch
        remaining_epochs = numb_epochs - epoch
        remaining_time = remaining_epochs * average_elapsed_time

        print(f"Epoch {epoch}/{numb_epochs} completed. Estimated time remaining: {remaining_time:.2f} seconds")

    best_list = np.array(best_list) # Convert best_list to a numpy array
    mean_values = np.mean(best_list, axis=0) # Calculate the mean of the best fitness values of all epochs
    return print(mean_values)

#----------------------------------------------------------------------------------------------------------#

# Create a set of configurations
configurations = [
    {
        "gens": 100,
        "xo_prob": 0.5,
        "select": tournament_sel,
        "crossover": two_point_crossover,
        "elitism": True,
        "mutate": inversion_mutation,
        "mut_prob": 0.5,
    },
   {
        "gens": 100,
        "xo_prob": 0.5,
        "select": rank_selection,
        "crossover": two_point_crossover,
        "elitism": True,
        "mutate": inversion_mutation,
        "mut_prob": 0.5,
    },
   {
        "gens": 100,
        "xo_prob": 0.5,
        "select": fps,
        "crossover": two_point_crossover,
        "elitism": True,
        "mutate": inversion_mutation,
        "mut_prob": 0.5,
    },
]


''' TO RUN EPOCHS'''
run_epochs(30)

'''TO RUN A SINGLE EPOCH WITH A PLOT'''
run_multiple_configurations(configurations, epochs=False, printable=False)

