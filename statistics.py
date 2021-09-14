def first_stat(stat,infitive=None,third_from=None,praeteritum=None,perfect_haben_sein=None,perfect=None,level=None):
	if infitive is None or third_from is None or praeteritum is None or perfect_haben_sein is None or perfect is None or level is None:
		import verbs_loader
		buffer=verbs_loader.load_n_split('text.txt.txt')
		infitive=buffer[0]
		third_from=buffer[1]
		praeteritum=buffer[2]
		perfect_haben_sein=buffer[3]
		perfect=buffer[4]
		del buffer
	file = open('statistics.txt', 'w', encoding='utf-8')
	percentage_of_correct_answers=0
	verbs_amount_counter=0
	correct_verbs_counter=0
	wrong_answers_pool=[]
	for b in range(len(stat)):
		for i in range(len(stat[0])):
			verbs_amount_counter=verbs_amount_counter+1
			if stat[b][i]==True:
				correct_verbs_counter=correct_verbs_counter+1
			else:
				if i==0:
					wrong_answers_pool.append(f'Third form for {infitive[b]} - {third_from[b]}')
				elif i==1:
					wrong_answers_pool.append(f'Präteritum for {infitive[b]} - {praeteritum[b]}')
				elif i==2:
					wrong_answers_pool.append(f'Perfect for {infitive[b]} - {perfect_haben_sein[b]} {perfect[b]}')
				else:
					pass
	percentage_of_correct_answers=(100*correct_verbs_counter)/verbs_amount_counter

	output=f'''Starke und unregelmäßige Verben, Niveau - {level}\n\nThe total percentage of correct answers: {percentage_of_correct_answers}
Amount of mistakes:{(verbs_amount_counter-correct_verbs_counter)}\n\nWrong answers(to learn):'''
	for elem in wrong_answers_pool:
		output = output + f'\n{elem}'
	file.write(output)
	file.close()

