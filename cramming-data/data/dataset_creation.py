import random
import os

def generate_symmetric_pairs(max_digits: int, num_pairs: int, seed: int = 42, type: int = 1):
    
    # Generate `num_pairs` random number pairs (a b and b a) and write to a dataset.txt.
    # Each number has up to `max_digits` digits.

    # Args:
    #     max_digits (int): Maximum number of digits for each number.
    #     num_pairs (int): Number of random pairs to generate.
    #     seed (int): Random seed for reproducibility.
    #     type (int): Type of generation. 1 for only {max_digits}, 2 up to {max_digits}, 2 for 2 digits.
    
    random.seed(seed)
    # if operator == "+":
    max_val = 10 ** max_digits - 1
    min_val = 10 ** (max_digits - 1)
    filename = os.path.join(os.getcwd(), "cramming-data", "data", f"dataset_{max_digits}_digit.txt")

    if type == 1:
        with open(filename, 'w') as f:
            for _ in range(num_pairs):
                a = random.randint(1, max_val)
                b = random.randint(1, max_val)
                c = a + b
                f.write(f"{a} {b}\n")
                f.write(f"{b} {a}\n")

    if type == 2:
        with open(filename, 'w') as f:
            for _ in range(num_pairs):
                a = random.randint(min_val, max_val)
                b = random.randint(min_val, max_val)
                c = a + b
                f.write(f"{a} {b}\n")
                f.write(f"{b} {a}\n")



    # if operator == "x":
    #     max_val = 10 ** max_digits - 1
    #     filename = os.path.join(os.getcwd(), "cramming-data", "data", f"dataset_mult_{num_pairs}_digit.txt")


    #     with open(filename, 'w') as f:
    #         for _ in range(num_pairs):
    #             a = random.randint(1, max_val)
    #             b = random.randint(1, max_val)
    #             c = a * b
    #             f.write(f"{a} {b} {c}\n")
    #             f.write(f"{b} {a} {c}\n")

generate_symmetric_pairs(max_digits=8, num_pairs=1000)
print("Dataset generated successfully")