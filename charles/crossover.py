import random 
from data.data import nutrients, data




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



if __name__ == '__main__':
    # # Define the indices of the two parents
    # parent1_index = 0
    # parent2_index = 1

    # # Generate the two parents
    # parent1 = data[parent1_index][2:]
    # parent2 = data[parent2_index][2:]

    # # Perform the two-point crossover
    # child = two_point_crossover(parent1, parent2)

    # # Print the parents and child
    # print(f"Parent 1: {data[parent1_index]}")
    # print(f"Parent 2: {data[parent2_index]}")
    # print(f"Child: {[''] + [''] + child}")  # Add empty elements to match data format
    print('asda0')