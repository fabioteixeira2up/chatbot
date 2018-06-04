tipo_conta = ""
nome_ = ""

def ent(r):   

    montante = ""
    conta = ""
    destinatario = ""
    nome = ""
    flag = 0

    if r.json()['entities'] != []:
        r_type = r.json()['entities'][flag]['type']
        r_entity = r.json()['entities'][flag]['entity']

    for i in r.json()['entities']:

        if r.json()['entities'] != "":
            if r_type in "Montante":
                montante = r_entity
            
            elif r_type in "Conta":
                conta = r_entity
                if conta != "":
                    global tipo_conta
                    tipo_conta = conta
            
            elif r_type in "Destinatário":
                destinatario = r_entity
            
            elif r_type in "Nome":
                nome = r_entity
                if nome != "":
                    global nome_
                    nome_ = nome
            
            flag = flag + 1

    return [montante, tipo_conta, destinatario, nome_]