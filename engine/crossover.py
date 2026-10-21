import random
import copy

class Crossover:

    #prawdopodobieństwo krzyżowania
    @staticmethod
    def should_be_crossovered(prob):
        return random.random() <= prob

    #Krzyżowanie 1 bitu
    @staticmethod
    def onepoint_crossover(parent1, parent2, prob):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        if Crossover.should_be_crossovered(prob):
            point = random.randint(1, parent1.total_length - 1)
            child1.genes[point:] = parent2.genes[point:]
            child2.genes[point:] = parent1.genes[point:]

            child1.fitness, child2.fitness = None, None

        return child1, child2   

    #Krzyżowanie bitów między 2 losowymi punktami
    @staticmethod
    def twopoint_crossover(parent1, parent2, prob):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        if Crossover.should_be_crossovered(prob):
            point1 = random.randint(1, parent1.total_length - 1)
            point2 = random.randint(point1 + 1, parent1.total_length - 1)
            
            child1.genes[point1:point2] = parent2.genes[point1:point2]
            child2.genes[point1:point2] = parent1.genes[point1:point2]
        
            child1.fitness, child2.fitness = None, None
        print(point1)
        print(point2)
        return child1, child2  


    #50/50 na zamianę bitu z rodzicem
    @staticmethod
    def uniform_crossover(parent1, parent2, prob):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        if Crossover.should_be_crossovered(prob):
            for i in range(parent1.total_length):
                if random.random() < 0.5:
                    child1.genes[i] = child2.genes[i] 
                    child2.genes[i] = child1.genes[i]
        
        child1.fitness, child2.fitness = None, None

        return child1,child2


    #Zamiana całych zmiennych (całego bloku bitów odpowiadającego za tą zmienną)
    @staticmethod
    def granular(parent1, parent2, prob):

        child1, child2 = copy.deepcopy(parent1), copy.deepcopy(parent2)
        
        if Crossover.should_be_crossovered(prob):
            for i in range(parent1.num_variables):
                if random.random() < 0.5:
                    start = i * parent1.bit_precision
                    end = start + parent1.bit_precision
                    
                    child1.genes[start:end], child2.genes[start:end] = child2.genes[start:end], child1.genes[start:end]
                    
                    
            child1.fitness, child2.fitness = None, None
            
        return child1, child2    