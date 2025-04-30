import random

def generate_symmetric_pairs(filename: str, max_digits: int, num_pairs: int, seed: int = 42) -> None:
    """
    Generate `num_pairs` random number pairs (a b and b a) and write to a dataset.txt.
    Each number has up to `max_digits` digits.

    Args:
        filename (str): Output text file name.
        max_digits (int): Maximum number of digits for each number.
        num_pairs (int): Number of random pairs to generate.
        seed (int): Random seed for reproducibility.
    """
    random.seed(42)
    max_val = 10 ** max_digits - 1

    with open(filename, 'w') as f:
        for _ in range(num_pairs):
            a = random.randint(1, max_val)
            b = random.randint(1, max_val)
            f.write(f"{a} {b}\n")
            f.write(f"{b} {a}\n")


generate_symmetric_pairs("dataset.txt", max_digits=8, num_pairs=1000)
print("Dataset generated successfully.")