import numpy as np


def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    return np.random.choice([0, 1], p=[1 - p1, p1], size=10000)


def count(seq):
    count = 0
    for i in range(len(seq)):
        if sum(seq[i:i + 5]) == 5:
            count += 1
    return count


def main(p1):
    seq = generate(p1)
    return count(seq)


print(main(2 / 3))
