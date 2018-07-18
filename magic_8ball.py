import random
import os

def screen():
	responses = ["It is certain.", "As I see it, yes.", "Reply hazy. Try again.", "Don't count on it.", 
	"It is decidedly so.", "Most likely.", "Ask again later.", "My reply is no.", "Without a doubt.", 
	"Outlook good.", "Better not tell you now.", "My sources say no.", "Yes, definitely.", "Yes", "Cannot predict now.", 
	"Outlook not so good.", "You may rely on it.", "Signs point to yes.", "Concentrate and ask again.", "Very doubtful."]
	
	os.system('clear')
	print('''
		-----------------------------------------------------
					Magic 8-Ball
		-----------------------------------------------------
		''')
	print("                " + responses[random.randint(0,19)])
	print("\n\n\n\n               Press enter to shake ball. Press q to quit.")
	choice = input('> ')

	if choice == 'q':
		os.system('clear')
		exit(0)
	else:
		screen()	


screen()
