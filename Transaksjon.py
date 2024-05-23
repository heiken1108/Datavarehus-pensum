import secrets
import random

Items = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def GenererTransaksjon(antallTransaksjoner, antallItems, tilfeldig):
    transaksjoner = dict()

    if antallItems <= 0 or antallItems > len(Items) or antallTransaksjoner <= 0:
        raise ValueError("Ugyldige verdier for antallItems eller antallTransaksjoner")
    if not tilfeldig:
        transaksjoner[1] = ["A", "B", "D", "E"]
        transaksjoner[2] = ["B", "C", "E"]
        transaksjoner[3] = ["A", "B", "D", "E"]
        transaksjoner[4] = ["A", "B", "C", "E"]
        transaksjoner[5] = ["A", "B", "C", "D", "E"]
        transaksjoner[6] = ["B", "C", "D"]
    elif tilfeldig:
        for i in range(antallTransaksjoner):
            antall = secrets.randbelow(antallItems) + 1
            transaksjoner[i+1] = random.sample(Items[0:antallItems], antall)
    sorterItems(transaksjoner)
    return Items[0:antallItems], transaksjoner



def sorterItems(transaksjoner):
    for key, value in transaksjoner.items():
        value.sort()

def printTransaksjoner(transaksjoner):
    for key in transaksjoner:
        print(key, ":", transaksjoner[key]) 

def VerticalDatalayout(items, transactions):
    VerticalDataLayout = {item: [] for item in items}
    for item in items:
        for key, value in transactions.items():
            if item in value:
                VerticalDataLayout[item].append(key)   
    return VerticalDataLayout
