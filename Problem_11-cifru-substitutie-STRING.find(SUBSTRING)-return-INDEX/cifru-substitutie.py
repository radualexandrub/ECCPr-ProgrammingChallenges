text_in = raw_input()
text_out = ""
c1 = ""
c2 = ""

tabel = raw_input().split()
for i in range(len(tabel)):
    c1 = c1 + tabel[i][0]
    c2 = c2 + tabel[i][2]

for i in range(len(text_in)):
    if text_in[i] in c1:
        index_in_c2 = c1.find(text_in[i])
        text_out += c2[index_in_c2]
    else:
        text_out += text_in[i]

print(text_out)

#### EXPLICATII #####
#   Noi avem la intrare: a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G s,n t,N u,e v,B w,r x,U y,p z,A A,8 B,X C,S D,P E,T F,a G,M H,d I,K J,L K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y 2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y
#   Vom salva in c1 toate caracterele care pot fi inlocuite, iar in c2 caracterele cu care sunt inlocuite.
# Pentru asta, vom pune in lista tabel toate perechile ["a,H", "b,j", "c,6"] etc.. 
# deci, fiecare element din lista are pe pozitia [0] - litera, pe pozitia [1] - virgula, pe pozitia[2] - litera de inlocuit, astfel obtinem:
# c1 = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
# c2 = Hj6I2R5thkmfDF10cGnNeBrUpA8XSPTaMdKL3Ci9Ewoz4OqVJxZulyWsQgv7bY
# avantajul e ca vom avea acelasi index pentru litera de inlocuit si litera cu care e inlocuita
#
#   Functia find returneaza pozitia la care se gaseste un substring(poate fi si un singur caracter) intr-un string, exemplu:
# s = "Happy Birthday"
# s2 = "py"
# print s.find(s2) #VA RETURNA 3 !!
#   Deci putem salva indexul la care se aflata caracterul de inlocuit SI cu trebuie inlocuit !! (index_in_c2)
#
#   In final, in loc sa facem replace la fiecare caracter din textul initial de intrare (in timp ce il si parcurgem...), construim un nou string text_out
# pe principiul: daca trebuie inlocuit, pune in text_out cu ce trebuie inlocuit caracterul curent
#               daca nu, pune in text_out caracterul curent din text_in



