import Beregningsfunksjoner as Bf
from itertools import product

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