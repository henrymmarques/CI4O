import random


####   ESTA MUTATION FALTA ADICIONAR UMA PERCENTAGEM PARA MUDAR A QUANTIDADE ############
def random_mutation(individual, mutation_rate=0.1):
    # Make a copy of the individual to avoid changing the original
    mutated_individual = individual.copy()
    
    # # Mutate the quantity by a random percentage
    # quantity_mutated = round(mutated_individual[2] * (1 + random.uniform(-mutation_rate, mutation_rate)), 1)
    # mutated_individual[2] = quantity_mutated
    
    # Mutate the nutrient values by adding a random value
    for i in range(3, len(mutated_individual)):
        nutrient_mutated = round(mutated_individual[i] + random.uniform(-mutation_rate, mutation_rate), 1)
        mutated_individual[i] = nutrient_mutated
        
    return mutated_individual





if __name__ == '__main__':
    data= ['Wheat Flour (Enriched)', '10 lb.', 36, 44.7, 1411, 2, 365, 0, 55.4, 33.3, 441, 0]

    new_individual = random_mutation(data)
    print(new_individual)

