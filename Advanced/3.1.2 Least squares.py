import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], [21, 3, 50, 1, 100], [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200, -50, 5000, 100], [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])


def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    ys_predict = []
    for coeff in c:
        ys_predict.append(X @ coeff)

    errors = []
    for y_predict in ys_predict:
        errors.append([(m - n)**2 for m, n in zip(y, y_predict)])
    for error in errors:
        current_error_sum = sum(error)
        if current_error_sum < smallest_error:
            smallest_error = current_error_sum
            best_index = errors.index(error)
    print("the best set is set %d" % best_index)


find_best(X, y, c)
