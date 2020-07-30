
# Output:
# 1. Pe prima linie două valori numerice întregi pozitive, reprezentând numărul total de
# obiecte ce vor lovi Pământul și câte din ele reprezintă un pericol.
# 2. Pe a doua linie se vor afișa trei numere reprezentând numărul de asterioizi, numărul de
# comete și numărul de obiecte neidentificare.
# 3. Pe a treia linie se vor afișa numărul de asteriozi, comete și obiecte identificate care vor
# lovi Pământul
# 4. Pe a patra linie se vor afișa numărul de de asteroizi, comete și obiecte neidentificate
# care vor lovi pământul și care reprezintă un pericol.

# Clasificare
# 1. Asteroizii au masa mai mare sau egală cu 2000 de tone și viteza de maxim 100 km/s.
# 2. Cometele au masa sub 2000 de tone și viteza mai mare sau egală 150 km/s.
# 3. Orice nu este asteroid sau cometă este un corp neidentificat.

# (pt pericol) Energie = mv^2 / 2

# n = nr obiecte
# d0 = distanta; m1 = masa; u2 = unghiul de incidenta; v3 = viteza
# raza_pamant = 6371 km

# ## Citire date
from math import asin

class Ob:
	def __init__(self, d, m, u, v, u_max):
		self.d = d
		self.m = m
		self.u = u
		self.v = v
		self.u_max = u_max

	def __repr__(self):
		return("[d:{} m:{} u:{} v:{} u_max:{}]".format(self.d, self.m, self.u, self.v, self.u_max))


n = int(input())
lista = []
for _ in range(n):
	tmp = [float(_) for _ in input().split()]
	u_max = asin(6371 / (6371 + tmp[0]))
	lista.append(Ob(tmp[0], tmp[1], tmp[2], tmp[3], u_max))
# print(lista)


# ## Prelucrare date
# ast = asteroizi, com = comete, nan = neindentificate

# Calcul unghi incidenta maxim ca medie a unghiurilor tuturor obiectelor
nr_ob_lovi = 0
nr_ob_lovi_pericol = 0

nr_ast = 0
nr_com = 0
nr_nan = 0

nr_ast_lovi = 0
nr_com_lovi = 0
nr_nan_lovi = 0

nr_ast_lovi_pericol = 0
nr_com_lovi_pericol = 0
nr_nan_lovi_pericol = 0

# Linia1: nr obiecte/obiecte_pericol ce vor lovi pamantul
for i in range(len(lista)):
	if lista[i].u <= lista[i].u_max:
		nr_ob_lovi += 1
		energie = (lista[i].m * (lista[i].v**2)) / 2000  # m/km
		# print("energie", energie)
		if energie > 2e+7:
			nr_ob_lovi_pericol += 1

# Linia2,3,4 Clasificari
for i in range(len(lista)):

	# Daca e asteroid
	if lista[i].m >= 2000 and lista[i].v <= 100:
		nr_ast += 1
		# Verificam daca va lovi pamant
		if lista[i].u <= lista[i].u_max:
			nr_ast_lovi += 1
			# Verificam daca e periculos
			energie = (lista[i].m * (lista[i].v**2)) / 2000
			if energie > 2e+7:
				nr_ast_lovi_pericol += 1

	# Daca e cometa
	elif lista[i].m < 2000 and lista[i].v >= 150:
		nr_com += 1
		# Verificam daca va lovi pamant
		if lista[i].u <= lista[i].u_max:
			nr_com_lovi += 1
			# Verificam daca e periculos
			energie = (lista[i].m * (lista[i].v**2)) / 2000
			if energie > 2e+7:
				nr_com_lovi_pericol += 1

	# Daca e neindentificat
	else:
		nr_nan += 1
		# Verificam daca va lovi pamant
		if lista[i].u <= lista[i].u_max:
			nr_nan_lovi += 1
			# Verificam daca e periculos
			energie = (lista[i].m * (lista[i].v**2)) / 2000
			if energie > 2e+7:
				nr_nan_lovi_pericol += 1

print(nr_ob_lovi, nr_ob_lovi_pericol)
print(nr_ast, nr_com, nr_nan)
print(nr_ast_lovi, nr_com_lovi, nr_nan_lovi)
print(nr_ast_lovi_pericol, nr_com_lovi_pericol, nr_nan_lovi_pericol)
