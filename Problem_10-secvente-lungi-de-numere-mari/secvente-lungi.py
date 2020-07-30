#### CITIRE DATE ####
len_lista = int(raw_input())
lista = []
for i in range(len_lista):
    lista.append(float(raw_input()))
prag = float(raw_input())

#### PRELUCRARE DATE ####
lista_binar = ""
for i in range(len_lista):
    if lista[i] > prag:
        lista_binar += "1"
    else:
        lista_binar += "0" # obtinem: "1111101110"

lista_binar = lista_binar.split('0') # obtinem lista: ["11111", "111", ""] care contine Nones din cauza zerourilor din capete
lista_binar2 = [lista_binar[i] for i in range(len(lista_binar)) if lista_binar[i] != ""] # obtinem lista2: ["11111", "111"]
print(len(lista_binar2)) # lungimea listei ne va da numarul de secvente de 1