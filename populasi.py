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

def decode_gene(gene):
    decimal = int(gene, 2)
    max_decimal = 2**CHROM_LENGTH - 1
    return X_MIN + (decimal / max_decimal) * (X_MAX - X_MIN)

def decode_chromosome(chromosome):
    gene1 = chromosome[:CHROM_LENGTH]
    gene2 = chromosome[CHROM_LENGTH:]
    x1 = decode_gene(gene1)
    x2 = decode_gene(gene2)
    return x1, x2
