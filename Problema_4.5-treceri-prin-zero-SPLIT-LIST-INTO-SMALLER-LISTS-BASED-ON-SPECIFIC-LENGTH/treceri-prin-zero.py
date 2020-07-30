# ###### Citire date #######
nr_numere = int(raw_input())
lista = []

for i in range(nr_numere):
	lista.append(float(raw_input()))

lungime_fereastra = int(raw_input())

# ###### Prelucrare date #######
# separam numerele pe ferestre
# https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists
# practic, din lista mare facem subgrupuri de liste de cate N elemente -> split list in smaller list based on specific length

lista2 = []
for i in range(0, nr_numere, lungime_fereastra):
	lista2.append(lista[i: i + lungime_fereastra])

for i in range(len(lista2)):
	medie = sum(lista2[i]) / float(len(lista2[i]))
	for j in range(len(lista2[i])):
		lista2[i][j] = lista2[i][j] - medie

	nr_treceri_zero = 0
	for j in range(len(lista2[i])):
		if j != len(lista2[i]) - 1:
			# un element trece prin zero daca: element_curent * element_urmator < 0
			if(lista2[i][j] * lista2[i][j + 1] < 0):
				nr_treceri_zero += 1
	print(nr_treceri_zero)
