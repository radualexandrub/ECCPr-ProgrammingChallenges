# aperitiv (A), ciorbă (C), fel principal (P), desert(D)
# ACPD

# Se consideră meniul cu cele mai multe feluri (adică un meniu ACP este corect, dar,
# dacă pe bandă după P urmează un D, atunci se va considera meniul ACPD)

# Iesire:
# numărul de meniuri corecte realizate (deci formate cu 2 până la 4 feluri, sosite în ordinea corectă)
# numărul de meniuri corecte realizate în care apare un fel de mâncare ce nu a fost recunoscut
# numărul de farfurii care sunt în plus (fac parte din meniuri incorect realizate).

# C1 A2 C6 P1 D7 D0 A0 C3 D2 C1 D2 P7
# lista_tmp = "C1 A2 C6 P1 D7 D0 A0 C3 D2 C1 D2 P7".split()
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

	if sir[i:i + 4] in "ACPD" and i != len(sir) - 1:
		nr_corect += 1
		if '0' in nr[i:i + 4]:
			nr_necunosc += 1
		i += 4

	elif sir[i:i + 3] in ["ACP", "ACD", "APD", "CPD"]:
		nr_corect += 1
		if '0' in nr[i:i + 3]:
			nr_necunosc += 1
		i += 3

	elif sir[i:i + 2] in ["AC", "AP", "AD", "CP", "CD", "PD"]:
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
