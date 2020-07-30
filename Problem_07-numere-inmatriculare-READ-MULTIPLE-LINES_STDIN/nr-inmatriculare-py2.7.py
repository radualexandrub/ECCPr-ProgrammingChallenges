#########################################################################################
############### TREBUIE SA CITIM UN NUMAR NECUNOSCUT DE LINII DE LA TASTATURA:
############### Cele 2 metode presupun finalizarea citirii de la tastatura prin CTRL+D
##### METODA 1 --- Vom obtine o lista cu string-ul de pe fiecare linie introdusa.
# while True:
#     try:
#         line = raw_input("")
#     except EOFError:
#         break
#     lista.append(line)
#
##### METODA 2 --- Vom obtine tot o lista cu string-ul de pe fiecare linie introdusa. CTRL+D
# import sys
# lista = sys.stdin.read().splitlines()
#########################################################################################

class Numar:
    def __init__(self, judet, cifre, litere):
        self.judet = judet
        self.cifre = cifre
        self.litere = litere

########### Citire de la tastatura - salvam intr-o lista de obiecte    
import sys
lista_old = sys.stdin.read().splitlines()

lista = []
for i in range(len(lista_old)-1): #### FACEM -1 PENTRU CA DATELE DE INTRARE AU UN FUKING NEW LINE IN PLUS PUS DEGEABA IN PNM...
    x = lista_old[i].split()
    lista.append(Numar(x[0],x[1],x[2]))


########### Salvam liste cu cifre, alfabet, judete
judete = ['AB', 'AR', 'AG', 'B', 'BC', 'BH', 'BN', 'BT', 'BV', 'BR', 'BZ', 'CS', 'CL', 'CJ', 'CT', 'CV', 'DB', 'DJ', 'GL', 'GR', 'GJ', 'HR', 'HD', 'IL', 'IS', 'IF', 'MM', 'MH', 'MS', 'NT', 'OT', 'PH', 'SM', 'SJ', 'SB', 'SV', 'TR', 'TM', 'TL', 'VS', 'VL', 'VN']
alfabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
numere = "1234567890"

########### Rezolvare...
for i in range(len(lista)):
    if lista[i].judet in judete:
        if len(lista[i].cifre) == 2:
            if lista[i].cifre[0] in numere and lista[i].cifre[1] in numere:
                
                if len(lista[i].litere) == 3: ## EXISTA IN TESTE SI NR INMATRICULARE CU CATE 2 LITERE LA FINAL IN LOC DE 3.
                    if lista[i].litere[0] in alfabet and lista[i].litere[1] in alfabet and lista[i].litere[2] in alfabet:
                        print(str(lista[i].judet)+" "+str(lista[i].cifre)+" "+str(lista[i].litere))
                
        elif len(lista[i].cifre) == 3:
            if lista[i].cifre[0] in numere and lista[i].cifre[1] in numere and lista[i].cifre[2] in numere:
                
                if len(lista[i].litere) == 3:
                    if lista[i].litere[0] in alfabet and lista[i].litere[1] in alfabet and lista[i].litere[2] in alfabet:
                        print(str(lista[i].judet)+" "+str(lista[i].cifre)+" "+str(lista[i].litere))



