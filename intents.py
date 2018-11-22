from table import table
from ent import ent
from s_talk import s_talk
from db import create_account
from db import saber_saldo
from db import atualizar_valores

nome_ = ""

def intents(intent, r, ex, score):

    montante = ent(r)[0]
    conta = ent(r)[1]
    dest = ent(r)[2]
    nome = ent(r)[3]
    small_talk = s_talk()

    # Certeza do reconhecimento no intent
    if score > 0.5:

        # Tratamento dos intents regulares
        if intent in small_talk:
            table(intent)

        elif intent in "DizerNome":
            # Se não reconhecer o nome
            if nome == "":
                global nome_
                nome_ = ex
            else:
                nome_ = nome
            print("ChatBanco: Bem-vindo " + nome_.title() + ". Que posso fazer por si?\n")

        elif intent in "AbrirConta":
            if nome_ == "":
                print("ChatBanco: Diga-me o seu nome, por favor.\n")
            elif conta != "":
                create_account(conta, 0, nome_)
                print("ChatBanco: Abri uma conta " + conta + " em nome de " + nome_.title() + " com 0€.\n")
            else:
                print("ChatBanco: Que tipo de conta deseja abrir (corrente/poupança)?\n")

        elif intent in "TipoConta":
            if nome_ == "":
                print("ChatBanco: Diga-me o seu nome, por favor.\n")
            else:
                create_account(conta, 0, nome_)
                print("ChatBanco: Abri uma conta " + conta + " em nome de " + nome_.title() + " com 0€.\n")

        elif intent in 'SaberSaldo':
            '''
            SELECT DISTINCT conta.id, tipo, montante, utilizador_id
                FROM utilizador, conta
                WHERE utilizador_id =
                    (SELECT utilizador.id
                        FROM utilizador, conta
                        WHERE nome LIKE "Pedro");
            '''
            if nome_ == "":
                print("ChatBanco: Diga-me o seu nome, por favor.\n")
            else:
                sal = saber_saldo(nome_)
                print("ChatBanco: Tem " + str(sal) + "€ na Conta.\n")

        elif intent in 'TransferirDinheiro':
            '''
            UPDATE conta
            SET montante = 50
            WHERE utilizador_id =
            (SELECT utilizador.id
                FROM utilizador, conta
                WHERE nome = "Pedro");

            UPDATE conta
            SET montante = 100
            WHERE utilizador_id =
            (SELECT utilizador.id
                FROM utilizador, conta
                WHERE nome = "Carlos");
            '''

            if nome_ == "":
                print("ChatBanco: Diga-me o seu nome, por favor.\n")
            else:
                sal1 = int(saber_saldo(nome_))
                sal2 = int(saber_saldo(dest))

                if sal1 >= int(montante.split(' ', 1)[0]):
                    sal1 = sal1 - int(montante.split(' ', 1)[0])
                    atualizar_valores(nome, sal1)
                    print("ChatBanco: Tem agora " + str(sal1) + "€ na Conta.\n")

                    sal2 = sal2 + int(montante.split(' ', 1)[0])
                    atualizar_valores(dest, sal2)

                else:
                    print("Não tem dinheiro suficiente na Conta.\n")
            
        elif intent in 'LevantarDinheiro':
            '''
            UPDATE conta
            SET montante = 50
            WHERE utilizador_id =
            (SELECT utilizador.id
                FROM utilizador, conta
                WHERE nome = "Pedro");
            '''

            if nome_ == "":
                print("ChatBanco: Diga-me o seu nome, por favor.\n")
            else:
                sal = int(saber_saldo(nome_))
                if sal >= int(montante.split(' ', 1)[0]):
                    montante = sal - int(montante.split(' ', 1)[0])
                    atualizar_valores(nome, montante)
                    print("ChatBanco: Tem agora " + str(montante) + "€ na Conta.\n")
                else:
                    print("Não tem dinheiro suficiente na Conta.\n")

        elif intent in 'FazerDepósito':
            '''
            UPDATE conta
            SET montante = 50
            WHERE utilizador_id =
            (SELECT utilizador.id
                FROM utilizador, conta
                WHERE nome = "Pedro");
            '''
            if nome_ == "":
                print("ChatBanco: Diga-me o seu nome, por favor.\n")
            else:
                sal = int(saber_saldo(nome_))
                montante = int(montante.split(' ', 1)[0]) + sal
                atualizar_valores(nome, montante)
                print("ChatBanco: Tem agora " + str(montante) + "€ na Conta.\n")

    else:
        print("ChatBanco: Desculpe, não percebi.\n")