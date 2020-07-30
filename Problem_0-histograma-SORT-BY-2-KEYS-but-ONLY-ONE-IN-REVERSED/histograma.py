class Cuvant:
    def __init__(self, cuv, nr):
        self.cuv = cuv
        self.nr = nr
    
text = raw_input().lower().split()
lista = []
lista_obj = []
for i in range(len(text)):
    if text[i] not in lista:
        lista.append(text[i])
        lista_obj.append(Cuvant(text[i], 0))

for i in range(len(lista_obj)):
    nr = text.count(lista_obj[i].cuv)
    lista_obj[i].nr = nr
    
##### IN PYTHON POTI SORTA O LISTA DUPA 2 ATRIBUTE, DAR NU POTI SORTA O LISTA CU UN ATRIBUT DESCRESCATOR SI ALTUL DESCRESCATOR.
#### WORKAROUD? Negi unul din atribute (preferabil numarul): daca sortezi in ordine crescatoare un atribut NEGAT, il vei sorta de fapt in ordine DEScrescatoare
lista_obj.sort(key = lambda c: (-c.nr, c.cuv))

for i in range(len(lista_obj)):
    print(lista_obj[i].cuv+" "+str(lista_obj[i].nr))
