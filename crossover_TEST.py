import random 
from data.data import nutrients, data
import numpy as np

def two_point_crossover(parent1, parent2):
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


if __name__ == '__main__':
    # Define the indices of the two parents
    parent1_index = 0
    parent2_index = 1

    # Generate the two parents
    parent1 = data[parent1_index][2:]
    parent2 = data[parent2_index][2:]

    # Perform the two-point crossover
    # offspring1, offspring2 = two_point_crossover(parent1, parent2)
    offspring1, offspring2 = arithmetic_xo(parent1, parent2)

    # Print the parents and child
    print(f"Parent 1: {data[parent1_index]}")
    print(f"Parent 2: {data[parent2_index]}")
    print(f"Offspring 1: {data[parent1_index][:2] + offspring1}")
    print(f"Offspring 2: {data[parent2_index][:2] +offspring2}")