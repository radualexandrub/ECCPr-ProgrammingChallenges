# ##### CITIRE DATE ######
N_zile = int(raw_input())
temperaturi = [int(x) for x in raw_input().split()]

# ##### PRELUCRARE DATE 1 ######
lista = []
i = 0
while i in range(N_zile):
	tmp = []
	j = i
	while j in range(N_zile - 1):
		# un fel de treceri prin zero ...
		if temperaturi[j] < 0 and temperaturi[j + 1] >= 0 or temperaturi[j] >= 0 and temperaturi[j + 1] < 0:
			tmp.append(temperaturi[j])
			j += 1
			if j == N_zile - 1:  # daca se intampla ca cel mai mare sir sa contina si ultimul element, il adaug
				tmp.append(temperaturi[j])
		else:
			tmp.append(temperaturi[j])
			i = j
			break

	lista.append(tmp)
	i += 1

max_len = 0
index = i
for i in range(len(lista)):
	if len(lista[i]) >= max_len:
		max_len = len(lista[i])
		index = i
if max_len == 1:
	print(0)
else:
	print(max_len)
	# lolz ce mod creativ mi-a venit in minte sa afisez lista [1, -2, 3] ca string: am eliminat parantezele si virgulele
	print(str(lista[index])[1:-1].replace(',', ''))

	# ##### PRELUCRARE DATE 2 ######
	count_neg = 0
	count_poz = 0
	for i in range(len(temperaturi)):
		if temperaturi[i] < 0:
			count_neg += 1
		elif temperaturi[i] >= 0:
			count_poz += 1
	raport_poz = round(float(count_poz) / N_zile * 100, 2)
	raport_neg = round(float(count_neg) / N_zile * 100, 2)
	print("+:{0:.2f}%".format(raport_poz) + " -:{0:.2f}%".format(raport_neg))
