from random import uniform, choice,choices
from operator import attrgetter


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":

        # Sum total fitness
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        # Sum total inverse fitness
        total_inverse_fitness = sum([1 / i.fitness for i in population])
        # Get a 'position' on the wheel
        spin = uniform(0, total_inverse_fitness)
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += 1 / individual.fitness
            if position > spin:
                return individual

    else:
        raise Exception("No optimization specified (min or max).")
    
## estava size=4
def tournament_sel(population, size=15):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: The best individual in the tournament.
    """

    # Select individuals based on tournament size
    # with choice, there is a possibility of repetition in the choices,
    # so every individual has a chance of getting selected
    tournament = [choice(population.individuals) for _ in range(size)]

    # with sample, there is no repetition of choices
    # tournament = sample(population.individuals, size)
    if population.optim == "max":
        return max(tournament, key=attrgetter("fitness"))
    if population.optim == "min":
        return min(tournament, key=attrgetter("fitness"))
    

def rank_selection(population, num_parents=100):
    """Rank selection implementation

    Args:
        population (list): List of individuals.
        num_parents (int): Number of parents to select.

    Returns:
        list: List of selected parents.
    """

    if population.optim == 'max':
        ranked_population = sorted(population, key=lambda x: x.fitness, reverse=True)
    elif population.optim == 'min':
        ranked_population = sorted(population, key=lambda x: x.fitness)
    else:
        raise ValueError("Invalid optimization type. Expected 'min' or 'max'.")
    ranks = list(range(1, len(ranked_population) + 1))
    #print(ranks)
    probabilities = [rank / sum(ranks) for rank in ranks]
    probabilities=probabilities[::-1]
    #print(probabilities)
    selected_parents = choices(ranked_population, probabilities, k=num_parents)[0]
    return selected_parents