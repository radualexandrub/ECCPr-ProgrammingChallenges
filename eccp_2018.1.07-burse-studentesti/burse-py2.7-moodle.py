nr_stud, nr_disc, nr_burse = raw_input().split()
nr_stud = int(nr_stud)
nr_disc = int(nr_disc)
nr_burse = int(nr_burse)

class student:
    nume = ""
    note = []
    media = 0.0
    def __init__(obj, nume, note, media):
        obj.nume = nume
        obj.note = note
        obj.media = media

########## CITIRE DATE ############# CALCULARE media #################
obj_stud = []
note_per_student = []
media_calc = 0.0
for i in range(nr_stud):
    note_per_student = []
    nume_studenti = raw_input()
    note_studenti = raw_input().split()
    for j in range(nr_disc):
        note_per_student.append(int(note_studenti[j]))
    media_calc = round(sum(note_per_student)/float(nr_disc),2)
    
    obj_stud.append(student(nume_studenti, note_per_student, media_calc))

############ PRELUCRARE DATE #########################################
obj_stud.sort(key = lambda c: c.media, reverse=True) #sortare obiecte/studenti dupa medie

# ~~~ Bursa de performanta ~~~
integralist = True
for i in range(nr_stud):
    for j in range(nr_disc):
        if (obj_stud[i].note[j]) < 5:
            integralist = False
    if integralist == True:
        performanta = obj_stud[i]
        index = i
        break
del obj_stud[index] ## Elimin stud cu performanta

# ~~ Burse de merit ~~
nr_merite = 0
for i in range(len(obj_stud)):
    integralist = True
    for j in range(nr_disc):
        if (obj_stud[i].note[j]) < 5:
            integralist = False
    if integralist == True and obj_stud[i].media >= 8 and nr_burse != 0:
        nr_merite += 1
        nr_burse -= 1

# ~ afisare nr burse de merit
print(nr_merite)
# ~ afisare bursa perfomanta ~
print(performanta.nume+" %.2f" % performanta.media)
# se va afisa: Ana Croitoru 10.00
# se va afisa: Irina 8.50
# practic am adaugat spatiul si numarul de zecimale dupa virgula, urmand operatorul % pentru valoarea numerica































## functie afisare obiecte separata de clasa
def afisar(obj_stud):
    for i in range(len(obj_stud)):
        print(obj_stud[i].nume, obj_stud[i].note, obj_stud[i].media)
#afisar(obj_stud)


