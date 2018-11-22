import numpy as np

def next_intent(intent):
	
	matrix = open('matrix.txt').read()
	matrix = [item.split() for item in matrix.split('\n')]

	next_i = [""]*10
	prob = [""]*10
	fl = 0
	fla = 0
	flag = 0

	for i in matrix:
		if intent in matrix[flag][0]:
			next_i[fla] = matrix[flag][1]
			prob[fla] = matrix[flag][2]
			fla = fla + 1
		flag = flag + 1

	next_i = list(filter(None, next_i))
	prob = list(filter(None, prob))

	s = np.random.choice(
		next_i,
		1,
		p=prob
	)

	for i in next_i:
		if s[0] in next_i[fl]:
			pr = prob[fl]
		fl = fl + 1

	return [s[0], pr]