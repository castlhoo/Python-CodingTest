import numpy as np

def train_perceptron(X, y, epochs = 10, lr = 0.31):
    w = np.zeros(X.shape[1])
    b = 0

    for _ in range(epochs):
        for i in range(len(X)):
            score = np.dot(w, X[i]) + b

            if y[i] * score <= 0:
                w = w + (lr * y[i] * X[i])
                b = b + (lr * y[i])

    return w, b

def predict(X, w, b):
    score = w @ X + b
    return np.where(score >= 0, 1, -1)