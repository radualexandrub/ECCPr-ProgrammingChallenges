from math import sqrt
class Fruct:
    def __init__(self, tip, M, R, G, B, dist):
        self.tip = tip
        self.M = M
        self.R = R
        self.G = G
        self.B = B
        self.dist = dist

nr_fructe, nr_tip, M, R, G, B = [int(x) for x in raw_input().split()]
fruct_cantarit = Fruct(-1, M, R, G, B, 0)

lista_fructe = []
for i in range(nr_fructe):
    tip, M, R, G, B = [int(x) for x in raw_input().split()]
    
    dist = round(sqrt( (fruct_cantarit.M-M)**2 + (fruct_cantarit.R-R)**2 + (fruct_cantarit.G-G)**2 + (fruct_cantarit.B-B)**2 ), 2)
    
    lista_fructe.append(Fruct(tip, M, R, G, B, dist))

min = 99999.0
index = 0
for i in range(nr_fructe):
    if lista_fructe[i].dist < min:
        min = lista_fructe[i].dist
        index = i

print(lista_fructe[index].tip)