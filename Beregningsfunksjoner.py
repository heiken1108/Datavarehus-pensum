def support(X, Y, transaksjoner):
    supCount = supportCount(list(set(X+Y)), transaksjoner)
    N = len(transaksjoner)
    return supCount/N

def confidence(X, Y, transaksjoner):
    supXY = supportCount(list(set(X+Y)), transaksjoner)
    supX = supportCount(X, transaksjoner)
    return supXY/supX

def supportCount(itemset, transaksjoner): #Liten sigma
    n = 0
    for key, value in transaksjoner.items():
        if set(itemset).issubset(set(value)):
            n += 1
    return n

def distanse(punkt1, punkt2, r): #r=1 betyr Manhattan, r=2 betyr Eukledisk, r=inf betyr Chebyshev som gir maksimal avstand
    if r < 1 or len(punkt1) != len(punkt2):
        raise ValueError("Ugyldig verdi for r eller punktene har ulik dimensjon")
    SquaredDistance = 0
    for i in range(len(punkt1)):
        SquaredDistance += abs(punkt1[i]-punkt2[i])**r
    return SquaredDistance**(1/r)

def SimpleMatchingCoefficient(X, Y): #Antall indekser med 0,0 eller 1,1 delt på antall alle indekser
    if len(X) != len(Y):
        raise ValueError("X og Y må ha samme dimensjon")
    f_00 = 0
    for i in range(len(X)):
        if X[i] == 0 and Y[i] == 0:
            f_00 += 1

    f_11 = 0
    for i in range(len(Y)):
        if X[i] == 1 and Y[i] == 1:
            f_11 += 1
    
    return (f_00 + f_11)/len(X)

def JaccardCoefficient(X,Y): #Antall indekser med 1,1 delt på antall indekser med 1 i en av vektorene
    if len(X) != len(Y):
        raise ValueError("X og Y må ha samme dimensjon") 
    f_11 = 0
    for i in range(len(X)):
        if X[1] == 1 and Y[1] == 1:
            f_11 += 1

    n = 0
    for i in range(len(X)):
        if X[i] == 1 or Y[i] == 1:
            n += 1
    
    return f_11/n

def CosineSimilarity(X,Y): #Prikkprodukt delt på produktet av lengdene
    prikkprodukt = Prikkprodukt(X,Y)
    Lengde_X = Vektorlengde(X)
    Lengde_Y = Vektorlengde(Y)
    return prikkprodukt/(Lengde_X*Lengde_Y)

def Prikkprodukt(X,Y):
    if len(X) != len(Y):
        raise ValueError("X og Y må ha samme dimensjon")
    prikkprodukt = 0
    for i in range(len(X)):
        prikkprodukt += X[i]*Y[i]
    return prikkprodukt

def Vektorlengde(X):
    s = 0
    for i in range(len(X)):
        s += X[i]**2
    return s**(1/2)

def Corrolation(X,Y):
    return Covariance(X,Y)/(StandardDeviation(X)*StandardDeviation(Y))

def Covariance(X,Y):
    s = 0
    meanX = Mean(X)
    meanY = Mean(Y)
    for i in range(len(X)):
        s += (X[i]-meanX)*(Y[i]-meanY)
    return s/(len(X)-1)

def StandardDeviation(X):
    s = 0
    mean = Mean(X)
    for k in range(len(X)):
        s += (X[k] - mean)**2
    return (s/(len(X)-1))**(1/2)

def Mean(X):
    s = 0
    for i in range(len(X)):
        s += X[i]
    return s/len(X)

def Lift(X, Y, transaksjoner):
    return confidence(X,Y,transaksjoner)/supportCount(Y, transaksjoner)
