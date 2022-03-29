import random as rd
from random import randint

import numpy as np


def selection(fitness, num_parents, population):
    # Find solution in population with max fitness value
    fitness = list(fitness)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        parents[i, :] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return parents


def cal_fitness(weight, value, population, max_weight):
    fitness = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        S1 = np.sum(population[i] * value)
        S2 = np.sum(population[i] * weight)
        if S2 <= max_weight:
            fitness[i] = S1
        else:
            fitness[i] = 0
    return fitness.astype(int)


def crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1] / 2)
    crossover_rate = 0.8
    i = 0
    while (parents.shape[0] < num_offsprings):
        parent1_index = i % parents.shape[0]
        parent2_index = (i + 1) % parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i % parents.shape[0]
        parent2_index = (i + 1) % parents.shape[0]
        offsprings[i, 0:crossover_point] = parents[parent1_index, 0:crossover_point]
        offsprings[i, crossover_point:] = parents[parent2_index, crossover_point:]
        i = +1
    return offsprings


def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = 0.4
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i, :] = offsprings[i, :]
        if random_value > mutation_rate:
            continue
        int_random_value = randint(0, offsprings.shape[1] - 1)
        if mutants[i, int_random_value] == 0:
            mutants[i, int_random_value] = 1
        else:
            mutants[i, int_random_value] = 0
    return mutants


def optimize(weight, value, population, population_size, num_generations, max_weight):
    parameters, fitness_history = [], []
    num_parents = int(population_size[0] / 2)

    # Select half of population as parents, e.g. when population size is 8 then num_parents = 4

    num_offsprings = population_size[0] - num_parents

    for i in range(num_generations):
        fitness = cal_fitness(weight, value, population, max_weight)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossover(parents, num_offsprings)
        mutants = mutation(offsprings)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants

    print('Last generation: \n{}\n'.format(population))
    fitness_last_gen = cal_fitness(weight, value, population, max_weight)
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))
    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0], :])
    return parameters, fitness_history


if __name__ == '__main__':
    item_number = np.arange(1, 11)
    weight = np.random.randint(1, 15, size=10)
    value = np.random.randint(10, 750, size=10)

    # item number [ 1  2  3  4  5  6  7  8  9 10]
    # weight example [ 9  1  2  4 13  3  3  4 10  6]
    # value example [ 68  37 677  88 555 480 253 186 645 696]

    max_weight = 35  # Maximum weight that the bag of thief can hold
    print('The list is as follows:')
    print('Item No.   Weight   Value')
    for i in range(item_number.shape[0]):
        print('{0}          {1}         {2}\n'.format(item_number[i], weight[i], value[i]))

    solutions_per_pop = 8
    population_size = (solutions_per_pop, item_number.shape[0])
    print('Population size = {}'.format(population_size))
    initial_population = np.random.randint(2, size=population_size)
    initial_population = initial_population.astype(int)

    """
    Example initial population 8 * 10
    [[0 1 0 0 0 1 0 1 0 0]
     [0 1 0 1 0 1 0 0 0 1]
     [1 1 0 1 1 0 0 1 0 1]
     [1 1 0 0 1 1 0 1 1 1]
     [0 1 1 0 1 0 0 1 1 0]
     [1 0 1 1 1 0 1 1 0 1]
     [1 0 0 1 1 1 0 1 0 1]
     [1 0 0 0 0 1 0 1 0 0]]
    """

    num_generations = 50
    print('Initial population: \n{}'.format(initial_population))

    parameters, fitness_history = optimize(weight, value, initial_population, population_size, num_generations,
                                           max_weight)
    print('The optimized parameters for the given inputs are: \n{}'.format(parameters))
    selected_items = item_number * parameters
    print('\nSelected items that will maximize the knapsack without breaking it:')
    for i in range(selected_items.shape[1]):
        if selected_items[0][i] != 0:
            print('{}'.format(selected_items[0][i]))
