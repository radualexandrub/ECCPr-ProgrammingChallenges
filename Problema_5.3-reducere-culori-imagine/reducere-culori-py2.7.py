m_lin = int(raw_input())
n_col = int(raw_input())
s = int(raw_input())

###### CITIRE MATRICE A (ca lista de liste de liste)
#### [  [ [R1,G1,B1],[R2,G2,B2],[R3,G3,B3] ], [4, 5, 6]  ] 
A = []
for i in range(m_lin):
    linie = []
    for j in range(n_col):
        linie.append( [int(x) for x in raw_input().split()] )
    A.append(linie)

##### PRELUCRARE DATE ######### (in python nu exista switch case :( )
#### s = {2, 4, 8, 16} unde s == nr de intervale egale pentru [0, 255]
A_new = []
if s == 2:
    for i in range(m_lin):
        linie = []
        for j in range(n_col):
            pixel = []
            for k in range(3):
                if 0 <= A[i][j][k] <= 128:
                    pixel.append(0)
                elif 128 < A[i][j][k] <= 255:
                    pixel.append(1)
            linie.append(pixel)
        A_new.append(linie)

elif s == 4:
    for i in range(m_lin):
        linie = []
        for j in range(n_col):
            pixel = []
            for k in range(3):
                if 0 <= A[i][j][k] <= 256/s:
                    pixel.append(0)
                elif 256/s < A[i][j][k] <= 2*256/s:
                    pixel.append(1)
                elif 2*256/s < A[i][j][k] <= 3*256/s:
                    pixel.append(2)
                elif 3*256/s < A[i][j][k] <= 255:
                    pixel.append(3)
            linie.append(pixel)
        A_new.append(linie)
        
elif s == 8:
    for i in range(m_lin):
        linie = []
        for j in range(n_col):
            pixel = []
            for k in range(3):
                if 0 <= A[i][j][k] <= 256/s:
                    pixel.append(0)
                elif 256/s < A[i][j][k] <= 2*256/s:
                    pixel.append(1)
                elif 2*256/s < A[i][j][k] <= 3*256/s:
                    pixel.append(2)
                elif 3*256/s < A[i][j][k] <= 4*256/s:
                    pixel.append(3)
                elif 4*256/s < A[i][j][k] <= 5*256/s:
                    pixel.append(4)
                elif 5*256/s < A[i][j][k] <= 6*256/s:
                    pixel.append(5)
                elif 6*256/s < A[i][j][k] <= 7*256/s:
                    pixel.append(6)
                elif 7*256/s < A[i][j][k] <= 255:
                    pixel.append(7)
            linie.append(pixel)
        A_new.append(linie)

elif s == 16:
    for i in range(m_lin):
        linie = []
        for j in range(n_col):
            pixel = []
            for k in range(3):
                if 0 <= A[i][j][k] <= 256/s:
                    pixel.append(0)
                elif 256/s < A[i][j][k] <= 2*256/s:
                    pixel.append(1)
                elif 2*256/s < A[i][j][k] <= 3*256/s:
                    pixel.append(2)
                elif 3*256/s < A[i][j][k] <= 4*256/s:
                    pixel.append(3)
                elif 4*256/s < A[i][j][k] <= 5*256/s:
                    pixel.append(4)
                elif 5*256/s < A[i][j][k] <= 6*256/s:
                    pixel.append(5)
                elif 6*256/s < A[i][j][k] <= 7*256/s:
                    pixel.append(6)
                elif 7*256/s < A[i][j][k] <= 8*256/s:
                    pixel.append(7)
                elif 8*256/s < A[i][j][k] <= 9*256/s:
                    pixel.append(8)
                elif 9*256/s < A[i][j][k] <= 10*256/s:
                    pixel.append(9)
                elif 10*256/s < A[i][j][k] <= 11*256/s:
                    pixel.append(10)
                elif 11*256/s < A[i][j][k] <= 12*256/s:
                    pixel.append(11)
                elif 12*256/s < A[i][j][k] <= 13*256/s:
                    pixel.append(12)
                elif 13*256/s < A[i][j][k] <= 14*256/s:
                    pixel.append(13)
                elif 14*256/s < A[i][j][k] <= 15*256/s:
                    pixel.append(14)
                elif 15*256/s < A[i][j][k] <= 255:
                    pixel.append(15)
            linie.append(pixel)
        A_new.append(linie)

####### AFISARE (lista de liste de liste) #####################
for i in range(m_lin):
    for j in range(n_col):
        s = ""
        s = str(A_new[i][j][0]) + " " + str(A_new[i][j][1]) + " " + str(A_new[i][j][2])
        print s
