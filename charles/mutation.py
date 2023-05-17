import random

def uniform_mutation(individual):
 
    for i in range(len(individual)):
        lower_bound= individual[i] - individual[i]*0.1
        upper_bound= individual[i] + individual[i]*0.1
        individual[i] = random.uniform(lower_bound, upper_bound)
    return individual

def swap_mutation(individual):
    """Swap mutation for a GA individual. Swaps the bits.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    

    mut_indexes = random.sample(range(0, len(individual)), 2)
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]
    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual. Reverts a portion of the representation.

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    mut_indexes = random.sample(range(0, len(individual)), 2)
    #mut_indexes = [0,3]
    mut_indexes.sort()
    individual[mut_indexes[0]:mut_indexes[1]] = individual[mut_indexes[0]:mut_indexes[1]][::-1]
    return individual





if __name__ == '__main__':
    print('a')

