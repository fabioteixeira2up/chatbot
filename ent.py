montante_ = ""
tipo_conta = ""
dest = ""
nome_ = ""

def ent(r):   

    montante = ""
    conta = ""
    destinatario = ""
    nome = ""
    flag = 0

    for i in r.json()['entities']:

        if r.json()['entities'] != []:
            r_type = r.json()['entities'][flag]['type']
            r_entity = r.json()['entities'][flag]['entity']

        if r.json()['entities'] != "":
            if r_type in "Montante":
                montante = r_entity
                if montante != "":
                    global montante_
                    montante_ = montante
            
            elif r_type in "Conta":
                conta = r_entity
                if conta != "":
                    global tipo_conta
                    tipo_conta = conta
            
            elif r_type in "Destinatário":
                destinatario = r_entity
                if destinatario != "":
                    global dest
                    dest = destinatario
            
            elif r_type in "Nome":
                nome = r_entity
                if nome != "":
                    global nome_
                    nome_ = nome
            
            flag = flag + 1
 
    return [montante_, tipo_conta, dest, nome_]