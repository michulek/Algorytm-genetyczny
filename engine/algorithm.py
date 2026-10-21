import math
from engine.chromosome import Chromosome
from engine.selection import Selection
from engine.crossover import Crossover
from engine.mutation import Mutation

class GeneticAlgorithm:
    def __init__(self, pop_size, epochs, num_variables, bit_precision, bounds, fitness_func, opt_type="min", elite_percent=0.1):
        self.pop_size = pop_size
        self.epochs = epochs
        self.fitness_func = fitness_func
        self.opt_type = opt_type
        self.elite_percent = elite_percent
        self.num_variables = num_variables
        self.bit_precision = bit_precision
        self.bounds = bounds
        
        self.population = []
        self._initialize_population()
        
    def _initialize_population(self):
        for _ in range(self.pop_size):
            self.population.append(Chromosome(self.num_variables, self.bit_precision, self.bounds))


    #None, None w krzyżowaniu, mutacji itd
    def evaluate_population(self):
        for osobnik in self.population:
            if osobnik.fitness is None:  
                decoded_values = osobnik.decode()
                osobnik.fitness = self.fitness_func(decoded_values)

    #strategia elitarna
    def run(self, selection_method, crossover_method, mutation_method, cross_prob=0.8, mut_prob=0.05):
        """Główna pętla ewolucyjna."""
        #wstępna ocena populacji
        self.evaluate_population()
        
        for epoch in range(self.epochs):
            new_population = []
            
            #strategia elitarna (elite_percent)
            elite_count = math.ceil(self.pop_size * self.elite_percent) #ilosc osobnikow najlepszych
            elity = Selection.best(self.population, elite_count, self.opt_type) # wybór elite_count osobników najlepszych
            new_population.extend(elity) # dodanie ich do populacji
            
            #tworzenie krzyżowek, mutacji, reszty populacji
            while len(new_population) < self.pop_size:
                #wybor rodzicow z calej populacji \
                rodzice = selection_method(self.population, 2, self.opt_type)
                
                #krzyzowanie z prawdopodobienstwem = cross_prob 
                dziecko1, dziecko2 = crossover_method(rodzice[0], rodzice[1], cross_prob)
                
                #mutacja z prawdopodobieństwem = mut_prob
                mutation_method(dziecko1, mut_prob)
                mutation_method(dziecko2, mut_prob)
                
                #dodajemy nowych osobnikow (dzieci)
                new_population.append(dziecko1)
                if len(new_population) < self.pop_size:
                    new_population.append(dziecko2)
            
            #nowa populacja wskakuje za stara i jest oceniana
            self.population = new_population
            self.evaluate_population()
            
            #wypisanie najlepszego wyniku w danej epoce
            najlepszy = Selection.best(self.population, 1, self.opt_type)[0]
            print(f"Epoka {epoch+1}/{self.epochs} | Najlepszy fitness: {najlepszy.fitness}")