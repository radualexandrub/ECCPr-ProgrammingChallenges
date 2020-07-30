nr_aruncari = int(raw_input())
aruncari = []
for i in range(nr_aruncari):
    aruncari.append(int(raw_input()))

aparitii_fata = []
for i in range(1,7):
    aparitii_fata.append( aruncari.count(i) )

if max(aparitii_fata) - min(aparitii_fata) > nr_aruncari*0.1:
    print(1)
else:
    print(0)
    