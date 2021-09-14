NIVEAU=input("Enter your niveau -> ")

from statistics import first_stat
from verbs_loader import load_n_split

buffer=load_n_split("text.txt.txt")
infitive=buffer[0]
third_form=buffer[1]
praeteritum=buffer[2]
perfect_haben_sein=buffer[3]
perfect=buffer[4]
niveau=buffer[5]
del buffer

#First testing 
statistics=[]
niveau_indexing=[]
for i in range(len(niveau)):
	if niveau[i]==NIVEAU:
		niveau_indexing.append(i)
	else:
		pass

for elem in niveau_indexing:
	tmp=[]
	print(f"\nEnter the third form for {infitive[elem]}")
	if input("-> ")==third_form[elem]:
		print(f"Correct!")
		tmp.append(True)
	else:
		print(f"Incorrect, it is {third_form[elem]}. Enter the correct answer below")
		tmp.append(False)
		while input("-> ")!=third_form[elem]:
			print("Try one more time")
		print("Good!")
	print(f"\nEnter präteritum for {infitive[elem]}")
	if input("-> ")==praeteritum[elem]:
		print(f"Correct!")
		tmp.append(True)
	else:
		print(f"Incorrect, it is {praeteritum[elem]}. Enter the correct answer below")
		tmp.append(False)
		while input("-> ")!=praeteritum[elem]:
			print("Try one more time")
		print("Good!")


	print(f"\nEnter perfect for {infitive[elem]}")
	answer_perfect=input('-> ')
	if answer_perfect.find('hat')==-1 and answer_perfect.find('ist')==-1:
		print(f"Perfect should contain hat or ist. Answer is {(str(perfect_haben_sein[elem]+' '+perfect[elem]))}. Enter the correct answer below")
		tmp.append(False)
		answer_second=input("->")
		while answer_second!=(str(perfect_haben_sein[elem]+' '+perfect[elem])) and answer_second!=('ist '+perfect[elem]) and answer_second!=('hat '+perfect[elem]):
			print("Try one more time")
		print("Good!")
	else:
		if perfect_haben_sein[elem]=='hat/ist':
			if answer_perfect[(answer_perfect.find(' ')+1):]==perfect[elem]:
				print("Correct!")
				tmp.append(True)
			else:
				print(f"Incorrect, it is {(str(perfect_haben_sein[elem]+' '+perfect[elem]))}. Enter the correct answer below")
				tmp.append(False)
				while input("-> ")!=(str(perfect_haben_sein[elem]+' '+perfect[elem])):
					print("Try one more time")
				print("Good!")
		else:
			if answer_perfect[0:(answer_perfect.find(' '))]==perfect_haben_sein[elem]:
				if answer_perfect[(answer_perfect.find(' ')+1):]==perfect[elem]:
					print(f"Correct!")
					tmp.append(True)
				else:
					print(f"Incorrect, it is {(str(perfect_haben_sein[elem]+' '+perfect[elem]))}. Enter the correct answer below")
					tmp.append(False)
					while input("-> ")!=(str(perfect_haben_sein[elem]+' '+perfect[elem])):
						print("Try one more time")
					print("Good!")
			else:
				print(f"Incorrect, it is {(str(perfect_haben_sein[elem]+' '+perfect[elem]))}. Enter the correct answer below")
				tmp.append(False)
				while input("-> ")!=(str(perfect_haben_sein[elem]+' '+perfect[elem])):
					print("Try one more time")
				print("Good!")

	statistics.append(tmp)

del tmp
first_stat(statistics, level=NIVEAU)


