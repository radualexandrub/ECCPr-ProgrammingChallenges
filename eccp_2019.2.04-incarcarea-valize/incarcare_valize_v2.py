# D = greutate maxima incarcare valiza
# k = nr de greutati ce contin pachete diferite ce urmeaza sa fie aranjate in valiza
# pe urmatoarele k linii
# n, p = n pachete de greutate p fiecare
D, k_greutati = [int(_) for _ in input().split()]
pachete = []
for _ in range(k_greutati):
	# Fiecare greutate/linie pe care o citim contine n pachete cu greutate p fiecare
	n_pachete, p = [int(_) for _ in input().split()]
	for _ in range(n_pachete):
		pachete.append(p)

# Prelucrare date: punere pachete in valize:
valize = []
total_pachete = len(pachete)

while total_pachete > 0:
	spatiu_ramas = D
	o_valiza = []

	for i in range(len(pachete)):
		if spatiu_ramas - pachete[i] >= 0 and pachete[i] != 0:
			o_valiza.append(pachete[i])
			spatiu_ramas -= pachete[i]
			# In loc sa sterg pachetul din lista, il trec cu zero
			# si ma asigur ca nu le iau in considerare (pun conditie ^^)
			pachete[i] = 0

	valize.append(o_valiza)
	total_pachete -= len(o_valiza)

# Afisare: valiza e lista de liste, continutul unei liste se poate afisa cu print(*lista)
for i in range(len(valize)):
	print(*valize[i])
