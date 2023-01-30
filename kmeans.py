import cv2
import numpy as np
import matplotlib.pyplot as plt


file_path = "examples/pexels.jpg"
img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def resize(image, width=None, height=None, scale=1):
    # Resizes an RGB image.
    if width is None or height is None:
        width, height = image_width_height(image)
        width = int(width * scale)
        height = int(height * scale)
    return cv2.resize(image, (width, height))


def image_width_height(image):
    # Get an RGB image's width and height.
    width = image.shape[1]
    height = image.shape[0]
    return width, height


def image2X(image, width, height, channels=3):
    # Converts an RGB image to an array X for use with sklearn.
    return image.reshape([width * height, channels])


def X2image(X, width, height, channels=3):
    # Converts an array X from sklearn to an RGB image.
    return X.reshape([height, width, channels])


# Resize the image to a 400 x 600 resolution.
img = resize(img, width=400, height=600)
width, height = image_width_height(img)

X = image2X(img, width, height, 3)


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


# Convert the numpy array into an RGB image.
centroids, labels = k_means_clustering(X, 16)
img_segmented = X2image(centroids[labels], width, height, 3)

# Visualize the original image with the segmented one.
plt.figure(figsize=[10, 10])
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.imshow(img_segmented)
plt.show()
