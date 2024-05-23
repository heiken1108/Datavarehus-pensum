import Beregningsfunksjoner as Bf

def distanseMatrise(punkter): 
    matrise = lagTomMatrise(len(punkter), len(punkter)) #Kvadriatisk matrise, med antall rader og kolonner = antall punkter
    for i in range(len(matrise)):
        for j in range(len(matrise[0])):
            matrise[i][j] = round(Bf.distanse(punkter[i], punkter[j], 2), 3) #Rad i, kolonne j
    return matrise

def lagTomMatrise(antallRader, antallKolonner):
    return [[0 for _ in range(antallKolonner)] for _ in range(antallRader)]

def printMatrise(matrise):
    for i in range(len(matrise)):
        print(matrise[i])