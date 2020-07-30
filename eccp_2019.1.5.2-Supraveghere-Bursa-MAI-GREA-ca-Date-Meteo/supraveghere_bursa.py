# Problema e asemanatoare cu DateMeteo doar ca acolo deja aveai variatiile in lista
# Aici dupa ce calculeezi variatiile trebuie sa te folosesti de indecsii variatiilor
# Pentru a ajunge inapoi valorile listei originale date

def find_index_sublist(l, sl):
	'''Gaseste indexul unei subliste in lista'''
	for ind in (i for i, e in enumerate(l) if e == sl[0]):
		if l[ind:ind + len(sl)] == sl:
			return ind


N_zile = int(input())
lista_burse = [int(_) for _ in input().split()]

variatii = []
for i in range(len(lista_burse) - 1):
	variatii.append(lista_burse[i + 1] - lista_burse[i])

# ##### PRELUCRARE DATE 1: Afisare cea mai recenta lunga lista ######
lista = []
i = 0
while i in range(len(variatii)):
	tmp = []
	j = i
	while j in range(len(variatii) - 1):
		# un fel de treceri prin zero ...
		if variatii[j] < 0 and variatii[j + 1] >= 0 or variatii[j] >= 0 and variatii[j + 1] < 0:
			tmp.append(variatii[j])
			j += 1
			# daca se intampla ca cel mai mare sir sa contina si ultimul element, il adaug
			if j == len(variatii) - 1:
				tmp.append(variatii[j])
		else:
			tmp.append(variatii[j])
			i = j
			break

	lista.append(tmp)
	i += 1

# Caut lista de lungime maxima a variatiilor, daca sunt doua de aceeasi lugime maxima o pastrez pe ultima (>=max_len)
max_len = 0
for i in range(len(lista)):
	if len(lista[i]) >= max_len:
		lista_max = lista[i]
		max_len = len(lista[i])

if (max_len == 1):
	print(0)
else:
	# Acum trebuie sa preluam indexul+1 la lista de lungime maxima a variatiilor
	index = find_index_sublist(variatii, lista_max)

	print(len(lista_max))
	listaa = lista_burse[index + 1:index + 1 + len(lista_max)]
	# print(listaa)
	print(" ".join((str(x) for x in listaa)))

	# ##### PRELUCRARE DATE 2: Procente pentru variatia pozitiva/negativa DINTRE TOATE VARIATIILE
	# nu din aia cu lungime maxima gasita ...
	count_poz = 0
	count_neg = 0
	for i in range(len(variatii)):
		if variatii[i] < 0:
			count_neg += 1
		else:
			count_poz += 1

	raport_poz = round(float(count_poz) / len(variatii) * 100, 2)
	raport_neg = round(float(count_neg) / len(variatii) * 100, 2)
	print("+:{:.2f}%".format(raport_poz) + " -:{:.2f}%".format(raport_neg))
