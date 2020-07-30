nr_stud, nr_disc, nr_burse = input().split()
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
        
########## CITIRE DATE ###############
obj_stud = []
nume_studenti = ""
note_studenti = ""
note_studenti2 = []
media_calc = 0.0
for i in range(nr_stud):
    note_studenti2 = []
    nume_studenti=input()
    note_studenti=input().split()
    for j in range(len(note_studenti)):
        note_studenti2.append(int(note_studenti[j]))
    media_calc = round(sum(note_studenti2) / float(len(note_studenti2)),2)
    obj_stud.append(student(nume_studenti, note_studenti2, media_calc))
    
####### PRELUCRARE DATE #############################
obj_stud.sort(key = lambda c: c.media, reverse=True)