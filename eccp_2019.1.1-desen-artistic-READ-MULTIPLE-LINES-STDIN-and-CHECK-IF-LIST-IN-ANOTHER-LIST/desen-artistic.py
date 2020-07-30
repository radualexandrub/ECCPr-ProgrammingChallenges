# C = nr culori
# Citire date
C = int(input())
culori = input().split()
lista = []

class Copil:
    def __init__(self, nume, lst_culori):
        self.nume = nume
        self.lst_culori = lst_culori

    def __repr__(self):
        return("{} {}".format(self.nume, self.lst_culori))


# !!! CITIRE LINII PANA LA SFARSIT STREAM INTRARE (CTRL+D):
import sys
lista_tmp = sys.stdin.read().splitlines()
for i in range(len(lista_tmp)):
    tmp = lista_tmp[i].split()
    # print(tmp[2:2+int(tmp[1])])
    lista.append(Copil(tmp[0], tmp[2:2 + int(tmp[1])]))

# for i in range(len(lista)):
#     print(lista[i])

# Prelucrare date
# Adaugare combinatii de culori in lista de culori
if 'red' in culori and 'blue' in culori and 'purple' not in culori:
    culori.append('purple')
if 'yellow' in culori and 'red' in culori and 'orange' not in culori:
    culori.append('orange')
if 'yellow' in culori and 'blue' in culori and 'green' not in culori:
    culori.append('green')
if 'yellow' in culori and 'red' in culori and 'blue' in culori and 'brown' not in culori:
    culori.append('brown')

# # Verificare si afisare care copii pot termina desenele:
for i in range(len(lista)):
    if all(c in culori for c in lista[i].lst_culori):
        print(lista[i].nume)

# (Exemplu) Verificare daca o lista este in alta lista:
# if all(c in ['a', 'b', 'c'] for c in ['a', 'b']):
#     print("da")
# else:
#     print('nu')
