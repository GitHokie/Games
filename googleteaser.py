#Google Pyramid BrainTeaser

#Print first X lines
#Ask for User Input
#Check User Input vs Correct Answer
	#If TRUE then display answer 
		#OPT ask for next line & Check User Input
	#IF FALSE say 'Incorrect' and let the user try again

#OPT Create Algorithm to calculate Correct Answer

#Iniital Sequence
seq = ['1', '11', '21', '1211', '111221', '312211']


characters = len(seq[len(seq)-1]) - 1 #Find Length of last element of list and subtract 1 since _ only go in the middle of characters
#print characters 

def printseq():
	for lines in seq:
		charInStr = len(lines)
		interior = charInStr * 2 - 1
		numberSpaces = characters * 2 + 1 - interior
		#print numberSpaces, " ", interior
		print (numberSpaces / 2) * " ", " ".join(lines), (numberSpaces / 2) * " "
		#" ".join(s)

		#print ' ' * characters, lines, ' ' * characters
		#characters -= 1



nextanswer = '13112221'


def attempt():
	answer = raw_input('What is the next line? ')
	#TODO remove spaces from answer	
	answer = answer.translate(None, ' ')
	
	if answer == nextanswer:
		print 'Congrats!'
		playagain = raw_input("Do you want to try another line? (Y / N) ")
		if playagain	== 'Y' or playagain == 'y' or playagain == 'yes' or playagain == 'YES':
			seq.append(nextanswer)
			printseq()
			charseq = 2

			for i in xrange (0,len(seq[len(seq)-1]),2):
				#Check to see if next character equals the previous character
				#If yes keep going and count number of loops
				#if not print out the number of loops and the value being checked
				
				
				#NOT CORRECT
				#newseq = seq[len(seq)-1][charseq-2:charseq]
				#charseq += 2


		#TODO Calculate nextanswer
		


	else:
		tryagain = raw_input('Try again? (Y / N) ')
		if tryagain	== 'Y' or tryagain == 'y' or tryagain == 'yes' or tryagain == 'YES':
			printseq()
			attempt()

printseq()
attempt()





