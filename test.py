import os
import random
import time

MaxDim = 100
Rand_Max = 100000

def generate_random_numbers(n):
    return [random.randint(0, 999) for _ in range(n)]

def generate_instance(n):
    random_numbers = generate_random_numbers(n)
    x = random.choice([117] + random_numbers)
    return [n] + random_numbers + [x]

def generate_and_save_instances(n, n_inst):
    for j in range(1, n_inst + 1):
        num = str(n)
        print(f"Num: {num}")

        j_str = str(j).zfill(2)
        file = f"pph_{num}_{j_str}.dat"

        instance = generate_instance(n)

        with open(file, "w") as p_in:
            p_in.write("\n".join(map(str, instance)))

if __name__ == "__main__":
    Dim = int(input("n: "))
    v = int(input("n_inst: "))
    
    cputime = time.process_time()
    generate_and_save_instances(Dim, v)
    print(f"CPU Time: {time.process_time() - cputime}")
