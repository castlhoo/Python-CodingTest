import numpy as np
import random

def k_means(k, i, points):
    # k-means++
    centroids = [random.choice(points)]

    for _ in range(1, k):
        distances = []

        for point in points:
            point_distances = []
            for center in centroids:
                d = np.linalg.norm(np.array(point) - np.array(center))
                point_distances.append(d)

            min_distance = min(point_distances)
            distances.append(min_distance ** 2)

        total = sum(distances)
        probs = [distance / total for distance in distances]

        r = random.random()
        cumulative = 0

        for idx, point in enumerate(points):
            cumulative += probs[idx]
            if r < cumulative:
                centroids.append(point)
                break

    # k-means
    for _ in range(i):
        clusters = [[] for _ in range(k)]

        for point in points:
            distances = []
            for centroid in centroids:
                d = np.linalg.norm(np.array(point) - np.array(centroid))
                distances.append(d)

            idx = distances.index(min(distances))
            clusters[idx].append(point)

        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_centroids.append(np.mean(cluster, axis=0))
            else:
                new_centroids.append(random.choice(points))

        centroids = new_centroids

    return centroids, clusters