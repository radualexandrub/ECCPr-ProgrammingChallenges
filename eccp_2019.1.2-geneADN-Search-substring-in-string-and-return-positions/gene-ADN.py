# A <-> T
# C <-> G
# S = secventa data de aparat 2 <= len(S) <= 1024
# G = secventa de cautat 1 <= len(G) <= len(S)
S = input()
G = input()

# inversam si oglindim stringul de cautat s
G2 = [x for x in reversed(list(G))]
for i in range(len(G)):
    if G2[i] == 'A':
        G2[i] = 'T'
    elif G2[i] == 'T':
        G2[i] = 'A'
    elif G2[i] == 'C':
        G2[i] = 'G'
    elif G2[i] == 'G':
        G2[i] = 'C'
G2 = ''.join(x for x in G2)

# cautam pozitiile
pozitii = []
for i in range(len(S)):
    if G in S[i:i + len(G)] or G2 in S[i:i + len(G)]:
        pozitii.append(i)

print(len(pozitii))
if len(pozitii) != 0:
    print(' '.join(str(x) for x in pozitii))

# Explicatii simple -- Cautare substring in string si afisare toate pozitiile unde se regaseste
# string = "Happy pypy day"
# substring = "py"
# indecsi = []
# for i in range(len(string)):
#     if substring in string[i:i+len(substring)]:
#         indecsi.append(i)
# print(indecsi) # se gaseste pe poz 3, 6, 8
