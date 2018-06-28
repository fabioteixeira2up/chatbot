import requests
import json
from intents import intents
from next_intent import next_intent
import db_create

# Chave de subscrição
headers = {
    'Ocp-Apim-Subscription-Key': '401282c903fb4f65878ff1dfd16db098',
}

# Frase de abertura
print('\nSou um bot construído para realizar serviços bancários (abrir uma conta, consultar o saldo, realizar transferências). Diga-me o seu nome, por favor.\n')

# Iniciar variáveis necessárias
next_i_p = 0

# Criar tabelas se não existirem
db_create.main()

while True:
    # Input do utilizador
    ex = input('Eu: ')

    # Parâmetros da query
    params = {
        # Adicionar input aos paâmetros
        'q': ex,
        # Parâmetros opcionais. Valores default
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:

        # Request da query
        r = requests.get(
            'https://westeurope.api.cognitive.microsoft.com/luis/v2.0/apps/31e88306-ab6d-475f-979b-a2d8920a1664',
            headers = headers,
            params = params)

        # Intent da query
        intent = r.json()['topScoringIntent']['intent']
        # Score do intent
        score = r.json()['topScoringIntent']['score']

        # Ver se o próximo intent gerado anteriormente é mais preciso do que o atual
        if score < float(next_i_p):
            intent = next_i

        # Função com as respostas
        intents(intent, r, ex, score)

        # Próximo intent e a sua probabilidade
        next_i, next_i_p = next_intent(intent)

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))