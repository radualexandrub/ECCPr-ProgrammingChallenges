# Intr-o permutare CIRCULARA, toate cifrele secventei date exceptand-o pe ultima, sunt mutate cu o pozitie spre dreapta, ultima cifra devenind prima.

nr_binar = bin(int(raw_input()))[2:] # type(nr_binar) -> string

permutari = []
for i in range(len(nr_binar)):
    nr_binar = nr_binar[-1] + nr_binar[0:len(nr_binar)-1]
    permutari.append(nr_binar)

maxim = max(permutari)
print(int(maxim, 2)) # convertire din binar(string only) in decimal(int)