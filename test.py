import random
import os
import time

class RandomNumberGenerator:
    def __init__(self, seed=None):
        self.seed = seed if seed else int(time.time())
        random.seed(self.seed)

    def generate_random_integer(self, limit):
        return random.randint(0, limit)

    def generate_random_set(self, n):
        return [self.generate_random_integer(500) for _ in range(n + 1)]

    def generate_and_save_random_sets(self, n, n_inst):
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        for j in range(1, n_inst + 1):
            set_name = f"pph_{n}_{j:02d}.dat"
            file_path = os.path.join(output_dir, set_name)

            with open(file_path, "w") as file:
                file.write(str(n) + "\n")
                random_set = self.generate_random_set(n)
                file.write(" ".join(map(str, random_set)) + "\n")
                file.write(str(self.generate_random_integer(1000)) + "\n")
                random_set = self.generate_random_set(n)
                file.write(" ".join(map(str, random_set)) + "\n")

    def print_pairs(self, n, n_inst):
        for j in range(1, n_inst + 1):
            set_name = f"pph_{n}_{j:02d}.dat"
            file_path = os.path.join("output", set_name)

            with open(file_path, "r") as file:
                lines = file.readlines()
                pairs = [int(x) for x in lines[1].split()]
                print(f"Pairs from {set_name}:")
                for i in range(0, len(pairs), 2):
                    print(f"({pairs[i]}, {pairs[i + 1]})")

def main():
    n = 10  # Valor pré-fixado para 'n'
    n_inst = 5  # Valor pré-fixado para 'n_inst'

    start_time = time.time()
    rng = RandomNumberGenerator()
    rng.generate_and_save_random_sets(n, n_inst)
    rng.print_pairs(n, n_inst)
    end_time = time.time()

    print(f"CPU Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()
