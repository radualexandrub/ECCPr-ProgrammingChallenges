###### Citim de la tastatura o matrice 9x9:
matrice = []
for i in range(9):
    matrice.append( [int(x) for x in raw_input().split()] )

gresit = False
linie_coloana = [1, 2, 3, 4, 5, 6, 7, 8, 9]

### Verificam liniile 
for i in range(9):
    if sorted(matrice[i]) != linie_coloana:
        gresit = True
        break
        
### Verificam coloanele
for i in range(9):
    coloana = []
    for j in range(9):
        coloana.append(matrice[j][i])
    if sorted(coloana) != linie_coloana:
        gresit = True
        break

### Verificam patratele 3x3
### prima linie
patrat = []
for i in range(3):
    for j in range(3):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True
    
patrat = []
for i in range(3):
    for j in range(3,6):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

patrat = []
for i in range(3):
    for j in range(6,9):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

### a doua linie
patrat = []
for i in range(3,6):
    for j in range(3):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

    
patrat = []
for i in range(3,6):
    for j in range(3,6):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

patrat = []
for i in range(3,6):
    for j in range(6,9):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

### a treia linie
patrat = []
for i in range(6,9):
    for j in range(3):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

patrat = []
for i in range(6,9):
    for j in range(3,6):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

patrat = []
for i in range(6,9):
    for j in range(6,9):
        patrat.append(matrice[i][j])
if sorted(patrat) != linie_coloana:
    gresit = True

### Afisare
if gresit == True:
    print("Gresit")
else:
    print("Corect")

