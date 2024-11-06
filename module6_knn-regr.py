import numpy as np


class Knn_regr:
    def __init__(self, k, points):
        self.k = k
        self.points = np.array(points)

    def predict(self, x_value):
        distances = np.abs(self.points[:, 0] - x_value)

        k_nearest_indices = np.argsort(distances)[:self.k]

        k_nearest_y = self.points[k_nearest_indices, 1]
        k_nearest_distances = distances[k_nearest_indices]

        if np.any(k_nearest_distances == 0):
            return k_nearest_y[k_nearest_distances == 0][0]

        weights = 1 / k_nearest_distances
        weighted_y = np.sum(weights * k_nearest_y) / np.sum(weights)

        return weighted_y


def main():
    N = int(input("Enter a positive integer N: "))
    if N <= 0:
        print("N must be a positive integer.")
        return

    k = int(input("Enter a positive integer as the number of nearest neighbors k: "))
    if k <= 0:
        print("k must be a positive integer.")
        return
    elif k > N:
        print("Error: k cannot be greater than N.")
        return

    points = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        points.append([x, y])

    X = float(input("Enter the X value to predict Y: "))

    regression = Knn_regr(k, points)
    y_pred = regression.predict(X)
    print(f"The predicted Y value for X = {X} is: {y_pred}")


if __name__ == "__main__":
    main()
