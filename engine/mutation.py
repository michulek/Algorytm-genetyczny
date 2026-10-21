import random


class Mutation:

    #prawdopodobieństwo mutacji
    @staticmethod
    def should_be_mutated(prob):
        return random.random() <= prob

    #prawdopodobieństwo inwersji
    @staticmethod
    def should_use_inversion(prob):
        return random.random() <= prob

    #mutacja 1 bitu z końca lub z początku (50/50)
    @staticmethod
    def edge_mutation(chromosome, prob):
        if Mutation.should_be_mutated(prob):
            if random.random() < 0.5:
                chromosome.genes[chromosome.total_length - 1] = 1 - chromosome.genes[chromosome.total_length - 1]
            else:
                chromosome.genes[0] = 1 - chromosome.genes[0]
            
            # Zerujemy ocenę tylko wtedy, gdy zaszła mutacja
            chromosome.fitness = None

    #mutacja 1 losowego bitu
    @staticmethod
    def onepoint_mutation(chromosome, prob):
        if Mutation.should_be_mutated(prob):
            point = random.randint(0, chromosome.total_length - 1)
            chromosome.genes[point] = 1 - chromosome.genes[point]
            
            chromosome.fitness = None

    #mutacja 2 losowych bitów
    @staticmethod
    def twopoint_mutation(chromosome, prob):
        if Mutation.should_be_mutated(prob):
            point1 = random.randint(0, chromosome.total_length - 1)
            point2 = random.randint(0, chromosome.total_length - 1)
            
            chromosome.genes[point1] = 1 - chromosome.genes[point1]
            chromosome.genes[point2] = 1 - chromosome.genes[point2]
            
            chromosome.fitness = None

    #2 losowe punkty -> zamiana kolejności między nimi [0,1,0,0] -> [0,0,1,0]
    @staticmethod
    def inversion(chromosome, prob):
        if Mutation.should_use_inversion(prob):
            point1 = random.randint(0, chromosome.total_length - 2)
            point2 = random.randint(point1 + 1, chromosome.total_length - 1)
            
            chromosome.genes[point1:point2+1] = chromosome.genes[point1:point2+1][::-1]
            chromosome.fitness = None
    
