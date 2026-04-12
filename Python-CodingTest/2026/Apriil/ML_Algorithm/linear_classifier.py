import numpy as np

def linear_classifier(x, w):
    score = np.dot(w, x)
    if score >= 0:
        return 1
    else:
        return -1

x = np.array([2, 1])      # input feature vector
w = np.array([1, -2])     # weight vector

pred = linear_classifier(x, w)

print("score:", np.dot(w, x))
print("prediction:", pred)