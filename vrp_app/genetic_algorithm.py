import random
import numpy as np

class GeneticAlgorithm:
    def __init__(self, locations, vehicle_capacity, population_size=50, generations=100):
        self.locations = locations
        self.vehicle_capacity = vehicle_capacity
        self.population_size = population_size
        self.generations = generations
        self.population = self._create_initial_population()

    def _create_initial_population(self):
        return [random.sample(self.locations, len(self.locations)) for _ in range(self.population_size)]

    def fitness(self, route):
        return sum(np.sqrt((route[i][0] - route[i+1][0])**2 + (route[i][1] - route[i+1][1])**2) for i in range(len(route) - 1))

    def selection(self):
        return sorted(self.population, key=self.fitness)[:10]

    def crossover(self, parent1, parent2):
        start, end = sorted(random.sample(range(len(parent1)), 2))
        child = [None] * len(parent1)
        child[start:end] = parent1[start:end]
        for item in parent2:
            if item not in child:
                child[child.index(None)] = item
        return child

    def mutate(self, route, mutation_rate=0.1):
        if random.random() < mutation_rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]

    def evolve(self):
        for _ in range(self.generations):
            selected = self.selection()
            self.population = selected + [self.crossover(random.choice(selected), random.choice(selected)) for _ in range(self.population_size - len(selected))]

    def get_best_route(self):
        return min(self.population, key=self.fitness)
