import random
from operator import attrgetter
from copy import deepcopy
import matplotlib.pyplot as plt

num_selected=5

def generate_individual(num_foods=77, num_selected=num_selected):
    # Select 5 unique food indices
    selected_indices = set()
    while len(selected_indices) < num_selected:
        selected_indices.add(random.randint(0, num_foods-1))
    selected_indices = list(selected_indices)

    # Generate random quantities for the selected foods
    individual = [0] * num_foods
    for i in selected_indices:
        individual[i] = random.randint(100, 1500) / 100.0  # Generate a random quantity between 0.01 and 10.00

    return individual

class Individual:
    def __init__(
        self,
        representation=None,
        size=None,
        replacement=True,
        valid_set=None,):

        if representation is None:
            self.representation = generate_individual(num_foods=len(valid_set), num_selected=num_selected)
        else:
            self.representation = representation
        self.valid_set = valid_set
        self.fitness = self.get_fitness()

    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness path.")

    def get_neighbours(self, func, **kwargs):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f"Individual(size={len(self.representation)}); Fitness: {self.fitness}"
    

  
  
class Population:
    def __init__(self, size, optim, **kwargs):
        self.individuals = []
        self.size = size
        self.optim = optim
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    replacement=kwargs["replacement"],
                    valid_set=kwargs["valid_set"],
                )
            )
    def evolve(self, gens, xo_prob, select, crossover, elitism, mutate, mut_prob, unchanged_stop=None):
        '''
        Args:
        unchanged_stop: max of consecutive generatios with the same fitness
        '''
        prev_best_fitness = 0
        unchanged_generations = 0


        fitness_values = []  # List to store the fitness values

        for _ in range(gens):
            new_pop = []

            if elitism:
                if self.optim == "max":
                    elite = deepcopy(max(self.individuals, key=attrgetter("fitness")))
                elif self.optim == "min":
                    elite = deepcopy(min(self.individuals, key=attrgetter("fitness")))

            while len(new_pop) < self.size:
                parent1, parent2 = select(self), select(self)

                if random.random() < xo_prob:
                    offspring1, offspring2 = crossover(parent1, parent2)
                else:
                    offspring1, offspring2 = parent1.representation, parent2.representation

                if random.random() < mut_prob:
                    offspring1 = mutate(offspring1)
                if random.random() < mut_prob:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2))

            if elitism:
                if self.optim == "max":
                    worst = min(new_pop, key=attrgetter("fitness"))
                    if elite.fitness > worst.fitness:
                        new_pop.pop(new_pop.index(worst))
                        new_pop.append(elite)

                elif self.optim == "min":
                    worst = max(new_pop, key=attrgetter("fitness"))
                    if elite.fitness < worst.fitness:
                        new_pop.pop(new_pop.index(worst))
                        new_pop.append(elite)

            self.individuals = new_pop

            if self.optim == "max":
                best_individual = max(self, key=attrgetter("fitness"))
                print(f'Best Individual: {best_individual}')
                current_best_fitness = best_individual.fitness

            elif self.optim == "min":
                best_individual = min(self, key=attrgetter("fitness"))
                print('')
                print(f'Best Individual: {best_individual}')
                print(best_individual.representation)
                # print(best_individual.get_cost())
                current_best_fitness = best_individual.fitness

            fitness_values.append(current_best_fitness)  # Store the best fitness value

            if unchanged_stop is not None:
                # Check if the fitness remains the same
                if prev_best_fitness is not None and current_best_fitness == prev_best_fitness:
                    unchanged_generations += 1
                else:
                    unchanged_generations = 0

                if unchanged_generations == unchanged_stop:
                    print("Fitness remained the same for " + str(unchanged_stop) + " generations. Stopping evolution.")
                    break

            prev_best_fitness = current_best_fitness
        return fitness_values

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]
