import numpy as np
from io import StringIO

train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''


def main():
    np.set_printoptions(
        precision=1
    )  # this just changes the output settings for easier reading

    train_data = np.genfromtxt(StringIO(train_string), skip_header=1)
    test_data = np.genfromtxt(StringIO(test_string), skip_header=1)

    x_train = np.asarray(train_data[:, :-1])
    y_train = np.asarray(train_data[:, -1])

    x_test = np.asarray(test_data[:, :-1])

    c = np.linalg.lstsq(x_train, y_train)[0]

    print(c)
    print(x_test @ c)


main()