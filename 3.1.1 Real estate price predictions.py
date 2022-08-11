# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms,
# proximity of neighbors
X = [[66, 5, 15, 2, 500], [21, 3, 50, 1, 100], [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]  # coefficient values


def predict(X, c):
    for cabin in X:
        price = 0
        for i in range(len(c)):
            price += cabin[i] * c[i]
        print(price)


predict(X, c)
