from table import table
from ent import ent
from sayname import sayname
#from db import saber_saldo

def intents(intent, r, ex):

    conta = ent(r)[1]
    nome = ent(r)[3]

    # Tratamento dos intents regulares
    if intent in ["Agradecimentos", "Apresentações", "Confirmações", "Despedidas", "None"]:
        table(intent)

    elif intent in "AbrirConta":
        if ent(r)[1] != "":
            print("ChatBanco: Diga-me o seu nome, por favor.\n")
        else:
            print("ChatBanco: Que tipo de conta deseja abrir (corrente/poupança)?\n")

    elif intent in "TipoConta":
        print("ChatBanco: Diga-me o seu nome, por favor.\n")

    elif intent in "DizerNome":
        sayname(r, conta, ex)

    elif intent in 'SaberSaldo':
        # RASCUNHO
        print("ChatBanco: Tem 3 213,34€ na Conta.\n")

    elif intent in 'TransferirDinheiro':
        # RASCUNHO
        print("ChatBanco: Tem a certeza que deseja transferir dinheiro?\n")

    elif intent in 'FazerDepósito':
        # RASCUNHO
        print("ChatBanco: Tem a certeza que deseja fazer um depósito?\n")

    elif intent in 'LevantarDinheiro':
        # RASCUNHO
        print("ChatBanco: Tem a certeza que deseja levantar dinheiro?\n")

    else:
        print("ChatBanco: Desculpe, não percebi.\n")