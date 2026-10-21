from engine.algorithm import GeneticAlgorithm
from engine.selection import Selection
from engine.crossover import Crossover
from engine.mutation import Mutation

#funkcja jest min = 0 (dla x1=0 i x2=0).
def funkcja_test(zmienne):
    wynik = 0
    for x in zmienne:
        wynik += x**2
    return wynik

#konfiguracja głównego algorytmu
wielkosc_populacji = 50      
liczba_epok = 100
liczba_zmiennych = 2          
dokladnosc_bitowa = 16        
przedzialy = [(-10, 10), (-10, 10)] 

print("--- INICJALIZACJA ALGORYTMU ---")
ag = GeneticAlgorithm(
    pop_size=wielkosc_populacji,
    epochs=liczba_epok,
    num_variables=liczba_zmiennych,
    bit_precision=dokladnosc_bitowa,
    bounds=przedzialy,
    fitness_func=funkcja_test,
    opt_type="min",
    elite_percent=0.1  #10% strategia elitarna
)

print("\n--- START EWOLUCJI ---")
ag.run(
    selection_method=Selection.tournament,       #wybór selekcji
    crossover_method=Crossover.granular,        #wybór krzyżowania
    mutation_method=Mutation.onepoint_mutation,  #wybór mutacji i inwersji
    cross_prob=0.8,   #prawdopodobieństwo krzyżowania
    mut_prob=0.05     #prawodpodobieństwo mutacji
)

#ostateczny wynik
najlepszy_koncowy = Selection.best(ag.population, 1, ag.opt_type)[0]
wartosci_roz = [round(w, 5) for w in najlepszy_koncowy.decode()]

print("\n--- WYNIK KOŃCOWY ---")
print(f"Najlepsze znalezione argumenty: {wartosci_roz}")
print(f"Wartość funkcji (Fitness): {najlepszy_koncowy.fitness:.6f}")

