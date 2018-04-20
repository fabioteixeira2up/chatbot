# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer # método para treinar o chatbot
from chatterbot import ChatBot # importar o chatbot
import os
import io
import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use("TkAgg")

bot = ChatBot(
	'Teste', # , read_only=True) # criar o chatbot
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': 'Desculpe, não percebi.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer',
)

for arq in os.listdir('arq'): # procurar na pasta dos arquivos
    chats = io.open('arq/' + arq, 'r').readlines() # ler os ficheiros
    bot.train(chats) # treinar os ficheiros

def add_text(mw,st,imsg):
    resq=''
    resp=''
    if(imsg.get().strip()==''):
        pass
    else:
        resq='Eu: '+imsg.get()+'\n'
        resp='Bot: '+str(bot.get_response(imsg.get()))+'\n'
        mw.config(state='normal')
        mw.insert('end',resq)
        mw.insert('end',resp)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

window = tk.Tk()
input_message=tk.StringVar(window)
input_message.set("")
window.bind('<Return>',lambda x:add_text(message_window,input_entry,input_message))
window.title('ChatBot')
window.geometry('600x600')
window['bg'] = 'white'
fram1 = tk.Frame(height=400, width=100, bg='blue')
fram2 = tk.Frame(height=80, width=100, bg='red')

input_entry=tk.Entry(fram2,width=10,
                     bg='white',textvariable=input_message)
input_entry.pack(side='left',expand='YES',fill='both')

message_window=tk.Text(fram1,bg='white',yscrollcommand='YES')
message_window.insert('end','Bot: ' + 'Bem-vindo!' + '\n')
message_window.config(state='disabled')
message_window.pack(side='top',expand='YES',fill='both')

send_button = tk.Button(fram2,text='Responder',
                        width=10,
                        height=2,
                        relief='groove',
                        bg='white',
                        state='active',
                        command=lambda :add_text(message_window,input_entry,input_message)
                        )
send_button.pack(side='right')
fram1.pack(fill='both', expand='YES')
fram2.pack(fill='x', side='bottom')

window.mainloop()

#https://www.eslfast.com/robot/topics/bank/bank.htm
#http://english-the-international-language.com/edbnk.php