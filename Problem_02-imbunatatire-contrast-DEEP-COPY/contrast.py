import copy
nr_lin = int(raw_input())
nr_col = int(raw_input())

## Citire matrice intr-o lista de liste
linie = []
matrice = []
for i in range(nr_lin):
    linie = []
    for j in range(nr_col):
        linie.append(int(raw_input()))
    matrice.append(linie)

## Filtrare matrice: aplicare ficarui element 
matrice_nemodif = copy.deepcopy(matrice) ### !!!!! daca facem matrice_nemodif = matrice => se face referinta, nu un obiect nou
                                        ### idem pentru matrice_nemodif = copy.copy(matrice) => tot referinta !!!
for i in range(nr_lin):
    for j in range(nr_col):
        matrice[i][j] = int(matrice[i][j]*0.9+2)

matrice_dif = copy.deepcopy(matrice_nemodif)
for i in range(nr_lin):
    for j in range(nr_col):
        matrice_dif[i][j] = float(matrice[i][j]) - float(matrice_nemodif[i][j])

suma = 0.0
for i in range(len(matrice_dif)):
    suma = suma + sum(matrice_dif[i])
medie = round(suma / (nr_lin*nr_col),2)

print(medie)















# ## Afisare matrice in randuri string
# print("Matrice_nemodif")
# for i in range(len(matrice_nemodif)):
#     s = ""
#     for j in range(len(matrice_nemodif[i])):
#         s = s + str(matrice_nemodif[i][j]) + " "
#     print(s)

# # Afisare matrice_2 in randuri string
# print("Matrice_modificata")
# for i in range(len(matrice)):
#     s = ""
#     for j in range(len(matrice[i])):
#         s = s + str(matrice[i][j]) + " "
#     print(s)
    
# # Afisare matrice_2 in randuri string
# print("Matrice_diferente")
# for i in range(len(matrice_dif)):
#     s = ""
#     for j in range(len(matrice_dif[i])):
#         s = s + str(matrice_dif[i][j]) + " "
#     print(s)
    
