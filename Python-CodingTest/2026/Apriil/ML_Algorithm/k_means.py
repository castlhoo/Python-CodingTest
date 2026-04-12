import numpy as np
import random

def k_means(k, i,points):
    centroids = random.sample(points, k)

    for _ in range(i):
        clusters = [ [] for _ in range(k)]
        for point in points:
            distances = []
            for centroid in centroids:
                distances.append(np.linalg.norm(np.array(point) - np.array(centroid)))
            
            idx = distances.index(min(distances))
            clusters[idx].append(point)

        new_centroids = []
        for cluster in clusters:
            if clusters:
                new_centroids.append(np.mean(cluster, axis=[0]))
            else:
                new_centroids.append(random.choice(points))
        centroids = new_centroids
        
    return centroids, clusters