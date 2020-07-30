# ordine corecta: M, N, S, D (doar intre doua si patru)
# Adica doar combinatiile:
# MN, MS, MD, MNS, MND, MNSD, MSD
# NS, ND, NSD
# SD
# Trebuie afisate:
# linie 1: Nr obiecte corect slefuite (ce resepcta ordinea)
# linie 2: Nr obiecte ce pot fi corect slefuite dar contin o eticheta 0
# linie 3: Nr benzi ce nu pot fi fol (nu respecta ordinea)
lista_tmp = input().split()
sir = ''.join([tmp[0] for tmp in lista_tmp])
nr = ''.join([str(tmp[1]) for tmp in lista_tmp])

# Prelucrare date
nr_corect = 0
nr_necunosc = 0
nr_incorect = 0

# print(sir)
# print(nr)

i = 0
while i in range(0, len(sir)):

	if sir[i:i + 4] in "MNSD" and i != len(sir) - 1:
		nr_corect += 1
		if '0' in nr[i:i + 4]:
			nr_necunosc += 1
		i += 4

	elif sir[i:i + 3] in ["MNS", "MND", "MSD", "NSD"]:
		nr_corect += 1
		if '0' in nr[i:i + 3]:
			nr_necunosc += 1
		i += 3

	elif sir[i:i + 2] in ["MN", "MS", "MD", "NS", "ND", "SD"]:
		nr_corect += 1
		if '0' in nr[i:i + 2]:
			nr_necunosc += 1
		i += 2

	else:
		i += 1
		nr_incorect += 1

print(nr_corect)
print(nr_necunosc)
print(nr_incorect)
