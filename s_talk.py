def s_talk():

	s_talk = open('s_talk.txt').read().splitlines()

	small_talk = [""]*20
	flag = 0

	for i in s_talk:
		small_talk[flag] = i
		flag = flag + 1

	return small_talk