nr_decodari = int(raw_input())

texte_decodate = []
for k in range(nr_decodari):
    
    text = raw_input().split(',')
    text_decodat = []
    
    for i in range(len(text)):
        if text[i] in "0123456789":
            text_decodat.append(text[i]+',')
            
        elif text[i][0] == '(' and len(text[i]) == 2:
            nr = text[i][1]
            
            if len(text[i+1]) == 3:
                zeros = int(text[i+1][0]+text[i+1][1])
            else:
                zeros = int(text[i+1][0])
            
            text_decodat.append(nr+',')
            for j in range(zeros):
                text_decodat.append('0,')
      
        elif text[i][0] == '(' and len(text[i]) == 3:
            nr = text[i][1]+text[i][2]
            zeros = int(text[i+1][0])
            
            text_decodat.append(nr+',')
            for j in range(zeros):
                text_decodat.append('0,')
                
    text_decodat[-1] = text_decodat[-1][0] #'elimin' ultima virgula de la final
    texte_decodate.append("".join(text_decodat))
    
for i in range(nr_decodari):
    print(texte_decodate[i])