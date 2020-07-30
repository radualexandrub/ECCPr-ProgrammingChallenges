# n = nr zile din trecut
# p = nr zile pentru care se face prognoza
n, p = [int(_) for _ in input().split()]
n_preturi = [float(_) for _ in input().split()]

# print(n_preturi[-n:]) # -> Taking n last elements of a list

p_preturi = [] # Adaug zilele cu prognoza intr-o noua lista separata
while p != 0:
    medie = round(sum(n_preturi[-n:]) / n, 2)
    n_preturi.append(medie)
    p_preturi.append(medie)

    p -= 1

print(' '.join(str(x) for x in p_preturi))
print(max(p_preturi), min(p_preturi))

# DATE INTRARE:
# 4 3
# 1.13 2.1 3.68 4.5
# DATE IESIRE:
# 2.85 3.28 3.58
# 3.58 2.85
# EXPLICATII:
# Se vor folosi preţurile din ultimele 4 zile pentru a prognoza preţurile pentru următoarele 3 zile.
# Preţul din ziua 5 se obţine făcând media preţurilor din zilele 1, 2, 3 şi 4: (1.13+2.1+3.68+4.5)/4 = 2.85.
# Preţul din ziua 6 se obţine făcând media preţurilor din zilele 2, 3, 4 şi 5: (2.1+3.68+4.5+2.85)/4 = 3.28.
# Preţul din ziua 7 se obţine făcând media preţurilor din zilele 3, 4, 5 şi 6: (3.68+4.5+2.85+3.28)/4 = 3.58.
# Maximul şi minimul pentru perioada prognozată sunt 3.58, respectiv 2.85.
