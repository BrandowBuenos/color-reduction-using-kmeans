import numpy as np
import random
import math
import cv2


def euclidean_distance(a, b):
    return np.linalg.norm(a - b)


def init_centroids(X, k):
    n_samples, n_features = X.shape
    centroids = np.zeros((k, n_features))
    for i in range(k):
        centroid = X[random.randint(0, n_samples - 1)]
        centroids[i] = centroid
    return centroids


def closest_centroid(sample, centroids):
    closest, min_distance = -1, math.inf
    for i, centroid in enumerate(centroids):
        distance = euclidean_distance(sample, centroid)
        if distance < min_distance:
            closest, min_distance = i, distance
    return closest


def k_means_clustering(X, k, max_iterations=100):

    # Initialize the centroids randomly.
    centroids = X[np.random.randint(0, X.shape[0], size=k), :]

    old_centroids = np.zeros(centroids.shape)
    labels = np.zeros(X.shape[0])
    distances = np.zeros((X.shape[0], k))

    iteration = 0

    # Repeat until the centroids stop moving or the maximum number of iterations is reached.
    while np.linalg.norm(centroids - old_centroids) > 0 and iteration < max_iterations:
        # Assign the datapoints to the nearest centroids.
        for i in range(k):
            distances[:, i] = np.linalg.norm(X - centroids[i], axis=1)
        labels = np.argmin(distances, axis=1)

        # Save the old centroids.
        old_centroids = centroids.copy()

        # Update the centroids.
        for i in range(k):
            centroids[i] = np.mean(X[labels == i], axis=0)

        iteration += 1

    # Return the final centroids and cluster assignments.
    return centroids, labels


def reduce_colors(image, k):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pixels = np.float32(image.reshape(-1, 3))

    centroids, labels = k_means_clustering(pixels, k)

    new_pixels = np.uint8(centroids[labels].reshape(image.shape))

    return cv2.cvtColor(new_pixels, cv2.COLOR_RGB2BGR)


def main():
    image = cv2.imread('examples/lenna.jpg')

    reduced_color_image = reduce_colors(image, k=16)

    cv2.imwrite('original.jpg', image)
    cv2.imwrite('reduced.jpg', reduced_color_image)


if __name__ == '__main__':
    main()
