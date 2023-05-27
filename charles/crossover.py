import random 
from data.data import nutrients, data
import numpy as np

def two_point_crossover(parent1, parent2):
    """Implementation of two point crossover.

    Args:
        parent1 (Individual): First parent for crossover.
        parent2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Choose two random points in the genome
    pt1 = random.randint(0, len(parent1) - 1)
    pt2 = random.randint(0, len(parent1) - 1)

    # Ensure pt2 > pt1
    if pt1 > pt2:
        pt1, pt2 = pt2, pt1

    # Create the offspring
    offspring1 = parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]
    offspring2 = parent2[:pt1] + parent1[pt1:pt2] + parent2[pt2:]

    return offspring1, offspring2

def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = random.randint(1, len(p1)-2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2


def arithmetic_xo(p1, p2):
    """Implementation of arithmetic crossover/geometric crossover with constant alpha.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
    
        Individuals: Two offspring, resulting from the crossover.
    """
    alpha = random.uniform(0, 1)
    o1 = [None] * len(p1)
    o2 = [None] * len(p1)
    for i in range(len(p1)):
        o1[i] = round(p1[i] * alpha + (1-alpha) * p2[i], 3)
        o2[i] = round(p2[i] * alpha + (1-alpha) * p1[i], 3)
    return o1, o2


def sbx(parent1, parent2, eta=10):
    """Implementation of sbx crossover.

    Args:
        parent1 (Individual): First parent for crossover.
        parent2 (Individual): Second parent for crossover.
        eta: distribution index of the crossover

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Ensure parents are NumPy arrays
    parent1 = np.array(parent1)
    parent2 = np.array(parent2)

    # Initialize offspring
    offspring1 = np.empty_like(parent1)
    offspring2 = np.empty_like(parent2)

    # Loop over each gene
    for i in range(parent1.shape[0]):
        # Get the min and max values for the ith gene
        xmin = min(parent1[i], parent2[i])
        xmax = max(parent1[i], parent2[i])

        # Calculate the range of the ith gene
        dx = xmax - xmin

        if dx > 0:
            # Generate two random numbers between 0 and 1
            u1 = random.random()
            u2 = random.random()

            # Calculate the beta parameter
            if u1 <= 0.5:
                beta = (2 * u1) ** (1 / (eta + 1))
            else:
                beta = (1 / (2 * (1 - u1))) ** (1 / (eta + 1))

            # Calculate the child values
            child1 = 0.5 * ((1 + beta) * parent1[i] + (1 - beta) * parent2[i])
            child2 = 0.5 * ((1 - beta) * parent1[i] + (1 + beta) * parent2[i])

            # Clip the child values to the range of the ith gene
            child1 = np.clip(child1, xmin, xmax)
            child2 = np.clip(child2, xmin, xmax)

            # Assign the child values to the offspring
            offspring1[i] = child1
            offspring2[i] = child2
        else:
            # If the range is zero, just copy the parents to the offspring
            offspring1[i] = parent1[i]
            offspring2[i] = parent2[i]

    return offspring1.tolist(), offspring2.tolist()


