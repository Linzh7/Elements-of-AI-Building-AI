import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# calculate the output of the sigmoid for x with all three coefficients
def main():
    c = np.concatenate(
        [c1[:, np.newaxis], c2[:, np.newaxis], c3[:, np.newaxis]], axis=1).T
    # c = np.concatenate(np.concatenate(c1,c2),c3)
    for i in range(3):
        print(sigmoid(c[i].reshape(1, 3) @ x.reshape(3, 1)))


main()