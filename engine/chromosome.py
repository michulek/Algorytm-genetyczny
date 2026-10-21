import random

class Chromosome:
    def __init__(self, num_variables, bit_precision, bounds):
        """
        Inicjalizacja pojedynczego osobnika (chromosomu). 
        :param num_variables: Ile zmiennych ma funkcja (np. 2 zmienne to x1 i x2).
        :param bit_precision: Ile bitów przypada na jedną zmienną (nasza dokładność).
        :param bounds: Lista przedziałów dla zmiennych, np. [(-10, 10), (-5, 5)].
        """
        self.num_variables = num_variables
        self.bit_precision = bit_precision
        self.bounds = bounds
        
        #całkowita długość chromosomu
        self.total_length = num_variables * bit_precision
        #losowanie genomu 
        self.genes = [random.choice([0, 1]) for _ in range(self.total_length)]
        #ocena (fitness)
        self.fitness = None 

    #rozkodowanie zmiennych 
    def decode(self):
        decoded_values = []
        
        for i in range(self.num_variables):
            #wyciagniecie fragmentu genów dla konkretnej zmiennej
            start_index = i * self.bit_precision
            end_index = start_index + self.bit_precision
            variable_bits = self.genes[start_index:end_index]
            
            #zamiana ciagu bitów na liczbe
            bit_string = "".join(str(bit) for bit in variable_bits)
            decimal_value = int(bit_string, 2)
            
            #przedzial 
            min_val, max_val = self.bounds[i]
            #prawdziwa wartosc, ze wzoru: a + dec * (b - a) / (2^m - 1)
            real_value = min_val + decimal_value * (max_val - min_val) / ((2 ** self.bit_precision) - 1)
            
            decoded_values.append(real_value)
            
        return decoded_values