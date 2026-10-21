import random

class Selection:

    #selekcja najlepszych, wybiera (num_parents) z najwyższy fitness score
    @staticmethod
    def best(population, num_parents, opt_type):
        is_reverse = True if opt_type == "max" else False
        
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=is_reverse)

        return sorted_population[:num_parents]

    #selekcja najgorszych, wybiera (num_parents) z najgorszych fitness score
    @staticmethod
    def worst(population, num_parents, opt_type):
        is_reverse = True if opt_type == "min" else False
            
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=is_reverse)
            
        return sorted_population[:num_parents]

    #selekcja turniejowa, zależnie od rozmiaru ilość pojedynków, wygrany przechodzi dalej
    @staticmethod
    def tournament(population, num_parents, opt_type, tournament_size=3):
        parents = []
        is_reverse = True if opt_type == "max" else False
        
        for _ in range(num_parents):
            contenders = random.sample(population, tournament_size)

            contenders.sort(key=lambda x: x.fitness, reverse=is_reverse)

            parents.append(contenders[0])
            
        return parents

    #selekcja za pomoca ruletki, im wiekszy fitness tym wieksza szansa na uzycie tego genu
    @staticmethod
    def roulette(population, num_parents, opt_type):
        parents = []
        fitness_values = [ind.fitness for ind in population]
        
        #elimacja liczb ujemnych i wyrównanie do 0
        if opt_type == "max":
            min_fit = min(fitness_values)
            #przesuniecie w gore tak aby najmniejsza wartosc byla 0
            adjusted_fitness = [f - min_fit + 1e-6 for f in fitness_values]
        else:
            max_fit = max(fitness_values)
            #odwrotnie
            adjusted_fitness = [max_fit - f + 1e-6 for f in fitness_values]
            
        #wagi
        total_fitness = sum(adjusted_fitness)
        probabilities = [f / total_fitness for f in adjusted_fitness]
        
        #ruletka
        for _ in range(num_parents):
            selected = random.choices(population, weights=probabilities, k=1)[0]
            parents.append(selected)
            
        return parents