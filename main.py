# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer # método para treinar o chatbot
from chatterbot import ChatBot # importar o chatbot
import os

bot = ChatBot('Teste') #, read_only=True) # criar o chatbot

bot.set_trainer(ListTrainer) # definir o "treinador"

for arq in os.listdir('arq'): # procurar na pasta dos arquivos
	chats = open('arq/' + arq, 'r').readlines() # ler os ficheiros
	bot.train(chats) # treinar os ficheiros

while True:
	resq = input('Você: ')
	resp = bot.get_response(resq)

	if float (resp.confidence) > 0.5:
		print('Bot: ' + str(resp))
	else:
		print('Bot: Não entendi.')