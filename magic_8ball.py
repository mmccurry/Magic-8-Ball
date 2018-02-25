import random

print("Welcome to the all-knowing magic 8-ball program.")

while True:	
	
	responses = ["It is certain.", "As I see it, yes.", "Reply hazy. Try again.", "Don't count on it.", 
	"It is decidedly so.", "Most likely.", "Most likely.", "Ask again later.", "My reply is no.", "Without a doubt.", 
	"Outlook good.", "Better not tell you now.", "My sources say no.", "Yes, definitely.", "Yes", "Cannot predict now.", 
	"Outlook not so good.", "You may rely on it.", "Signs point to yes.", "Concentrate and ask again.", "Very doubtful."]
	
	input("Press enter to shake the ball or control-c to quit.")
	print(responses[random.randint(0,20)])
