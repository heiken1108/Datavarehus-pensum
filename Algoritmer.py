import numpy as np
import Beregningsfunksjoner as Bf
from itertools import product
import random
def Apriori_Itemset_Generator(items, transactions, minsup, General_to_specific = True, mergeMethod = "k-1 and 1"): #Blir basicly prefix tree på latticen
    frequentItemsets = {i: [] for i in range(1, len(items)+1)} #Nøkkel: k (størrelse på itemsettet), verdi: liste med itemsets av størrelse k
    k = 1
    Candidateitemsets = items
    for i in range(len(Candidateitemsets)):
        if Bf.supportCount(Candidateitemsets[i], transactions) >= minsup:
            frequentItemsets[1].append([Candidateitemsets[i]])

    while k < len(items):
        k += 1
        Candidateitemsets = []
        if mergeMethod == "k-1 and 1":
            for i in range(len(frequentItemsets[k-1])):
                for j in range(len(frequentItemsets[1])):
                    possibleSet = list(set(frequentItemsets[k-1][i] + frequentItemsets[1][j]))
                    possibleSet.sort()
                    if possibleSet in Candidateitemsets or len(possibleSet) != k:
                        continue
                    else:
                        Candidateitemsets.append(possibleSet)
        for itemset in Candidateitemsets:
            if Bf.supportCount(itemset, transactions) >= minsup:
                frequentItemsets[k].append(itemset)


    return frequentItemsets


def KMeans(punkter, k, d): #Returnerer koordinatene til klusterne
    MAXITERATIONS = 50
    randomIndeces = random.sample(range(0, len(punkter)), k)
    Centroids = {i: [] for i in range(1, k+1)}
    ClusterPoints = {i: [] for i in range(1, k+1)}
    for i, index in enumerate(randomIndeces):
        Centroids[i+1] = punkter[index]
    iteration = 1
    while iteration <= MAXITERATIONS:
        for punkt in punkter:
            minDist = float("inf")
            closestCentroid = 0
            for key, value in Centroids.items():
                dist = Bf.distanse(punkt, value, 2)
                if dist < minDist:
                    minDist = dist
                    closestCentroid = key
            ClusterPoints[closestCentroid].append(punkt)
        for key, value in ClusterPoints.items():
            for j in range(d):
                sum = 0
                for punkt in value:
                    sum += punkt[j]
                Centroids[key][j] = sum/len(value)
        iteration += 1
    Cluster2d = []
    for key, value in Centroids.items():
        l = list(value)
        Cluster2d.append(l)
    arrayPoints = np.array(Cluster2d)
    return arrayPoints
