import csv
import random

with open('res.txt') as f:
	    reader = csv.reader(f, delimiter="\t")
	    falas = list(reader)

def table(intent):

	array = [""]*10
	flag = 0
	fla = 0

	for i in falas:
		if intent in falas[flag][0]:
			array[fla] = falas[flag][1]
			fla = fla + 1
		flag = flag + 1

	array = list(filter(None, array))
	print("ChatBanco: " + str(random.choice(array)) + '\n')