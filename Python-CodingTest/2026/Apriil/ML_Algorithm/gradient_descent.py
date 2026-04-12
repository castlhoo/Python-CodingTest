import numpy as np

def train_logistic(X, y, epochs=10, lr=0.31):
    w = np.zeros(X.shape[1])
    b = 0.0

    for _ in range(epochs):
        for i in range(len(X)):
            z = np.dot(w, X[i]) + b
            p = 1 / (1 + np.exp(-z))

            w = w - lr * (p - y[i]) * X[i]
            b = b - lr * (p - y[i])

    return w, b

def predict(X, w, b):
    z = X @ w + b
    p = 1 / (1 + np.exp(-z))
    return np.where(p >= 0.5, 1, 0)