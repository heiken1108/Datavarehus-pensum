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