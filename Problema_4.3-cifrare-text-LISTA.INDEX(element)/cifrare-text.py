alfabetM = sorted("QWERTYUIOPASDFGHJKLZXCVBNM")
alfabetm = sorted("qwertyuiopasdfghjklzxcvbnm")

text = raw_input()
nr_chei = int(raw_input())
chei = []
for i in range(nr_chei):
    chei.append(int(raw_input()))

j = 0
text_cifrat = ""
for i in range(len(text)):

    if text[i] in alfabetM:

        index = alfabetM.index(text[i]) + chei[j]
        if index >= len(alfabetM):
            index = index - len(alfabetM)

        text_cifrat = text_cifrat + alfabetM[index]
        j += 1
        if j == nr_chei:
            j = 0

    elif text[i] in alfabetm:

        index = alfabetm.index(text[i]) + chei[j]
        if index >= len(alfabetm):
            index = index - len(alfabetm)

        text_cifrat = text_cifrat + alfabetm[index]
        j += 1
        if j == nr_chei:
            j = 0

    else:
        text_cifrat = text_cifrat + text[i]

print(text_cifrat)
