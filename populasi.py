import random

POP_SIZE = 20
CHROM_LENGTH = 16
X_MIN, X_MAX = -10, 10

def generate_population():
    population = []
    for _ in range(POP_SIZE):
        chromosome = ''.join(random.choice(['0', '1']) for _ in range(CHROM_LENGTH * 2))
        population.append(chromosome)
    return population