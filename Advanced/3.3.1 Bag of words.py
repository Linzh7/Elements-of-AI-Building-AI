import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)

    data_array = np.array(data)

    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = np.inf
            else:
                dist[i][j] = sum(abs(data_array[i] - data_array[j]))

    # print(dist)
    print(np.unravel_index(np.argmin(dist), dist.shape))


find_nearest_pair(data)