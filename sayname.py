from ent import ent
from db import create_account

def sayname(r, conta, ex):

	nome = ent(r)[3]

	if nome == "":
		nome = ex

	create_account(conta, 0, nome)
	print("ChatBanco: Abri uma conta " + conta + " em nome de " + nome.title() + " com 0 euros.\n")