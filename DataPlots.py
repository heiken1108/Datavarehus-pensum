import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

data_points, clusterInformation = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)

def genererData(antallPunkter = 300, antallDimensjoner = 2, antallKlynger = 4, tilfeldig = True):
    if not tilfeldig:
        data_points, clusterInformation = make_blobs(n_samples=antallPunkter, centers=antallKlynger, n_features=antallDimensjoner, random_state=42)
    else:
        data_points, clusterInformation = make_blobs(n_samples=antallPunkter, centers=antallKlynger, n_features=antallDimensjoner)
    return data_points

def plotDataPunkter(data_punkter, centroids):
    plt.figure(figsize=(6, 4))
    plt.scatter(data_punkter[:, 0], data_punkter[:, 1], s=50, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], s=50, cmap='viridis', c='red', marker='x')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Data')
    plt.show()
