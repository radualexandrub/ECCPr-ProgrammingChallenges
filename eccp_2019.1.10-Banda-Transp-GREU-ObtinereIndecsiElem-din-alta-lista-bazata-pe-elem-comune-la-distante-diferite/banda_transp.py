# Problema: Obtinere Indecsi Elem-din-alta-lista-bazata-pe-elem-comune-la-distante-diferite. Ex:
# i:0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
#  1  0  1  0  1  0  0  0  1  0  1  1  0  1  1  0  0  1  0  0
#  0  1  0  0  1  0  0  0  1  0  1  0  1  1  0  0  1  1  0  1
# [0     2     4           8    10       13          17]
# [1     4     8          10    12       16          19]

# n = nr_esantioane
# s1 s2 = senzor stanga dreapta, fiecare contine amprenta timp si 1/0 daca s-a activat sau nu

# Citire date
n = int(input())
s1 = []
s2 = []

s1x = ''
s2x = ''
for i in range(n):
	x = [int(x) for x in input().split()]
	s1.append([x[0], x[1]])
	s1x += str(x[1])
for i in range(n):
	x = [int(x) for x in input().split()]
	s2.append([x[0], x[1]])
	s2x += str(x[1])

# print(s1x)
# print(s2x)

# Prelucrare date
# Cautam primul index de 1 in fiecare din cele 2 liste
indecsi1 = []
indecsi2 = []

nr_colete = 0

i = 0
i2 = 1
while i in range(len(s1x)):
	if s1x[i] == '1':
		indecsi1.append(i)

		# Cat de lunga e secv de 1 gasita? (trb sa sar dupa cu contorul)
		j = i + 1
		lung = 1
		while j < len(s1x) and s1x[j] == '1':
			lung += 1
			j += 1

		# Cauta in sir2 secventa de 1 de aceeasi lungime lung
		# O sa restrang cautarea doar la o zona de aceeasi lungime lung
		de_cautat = lung * '1'
		j = i2
		while j in range(len(s2x)):
			if de_cautat in s2x[j:j + lung]:
				indecsi2.append(j)
				i2 = j + lung
				break
			else:
				j += 1

		i += lung
		nr_colete += 1
	else:
		i += 1

# print(indecsi1)
# print(indecsi2)

# Avand indecsii la dispozitie, putem calcula fiecare viteza in parte
viteze = []
for i in range(len(indecsi1)):
	vit = (20 * 0.01) / ((s1[indecsi1[i]][0] - s2[indecsi2[i]][0]) * 0.001)
	viteze.append(abs(vit))
medie = int(round(sum(viteze) / len(viteze)))

# print(viteze)

print(medie, nr_colete)
