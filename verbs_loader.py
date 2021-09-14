def load_n_split(textfile):
	tmp = open(textfile, 'r', encoding='utf-8')
	all_verbs=tmp.read()
	tmp.close()
	del tmp
	#splitting words by arrayss

	

	rows=[]
	rows.append(all_verbs[0:(all_verbs.find('\n'))])
	end_point=all_verbs.find('\n')
	while True:
		end_point=all_verbs.find('\n',(end_point+1))
		if end_point==-1:
			break
		rows.append(all_verbs[(end_point+1):(all_verbs.find('\n', end_point+1))])

	infitive=[]
	third_form=[]
	praeteritum=[]
	perfect_haben_sein=[]
	perfect=[]
	niveau=[]

	for verb in rows:
		end_point=verb.find(' ', 0)
		infitive.append(verb[0:(verb.find(' '))])
		third_form.append((verb[(end_point+1):(verb.find(' ', (end_point+1)))]).translate(str.maketrans('', '', '()'))) 
		end_point=verb.find(' ', end_point+1)
		praeteritum.append(verb[(end_point+1):(verb.find(' ', (end_point+1)))])
		end_point=verb.find(' ', end_point+1)
		perfect_haben_sein.append(verb[(end_point+1):(verb.find(' ', (end_point+1)))])
		end_point=verb.find(' ', end_point+1)
		perfect.append(verb[(end_point+1):(verb.find(' ', (end_point+1)))])
		end_point=verb.find(' ', end_point+1)
		niveau.append(verb[(end_point+1):len(verb)])
	del end_point

	return infitive, third_form, praeteritum, perfect_haben_sein, perfect, niveau