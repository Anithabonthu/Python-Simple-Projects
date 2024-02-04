import random
EASY=10
DIFFICULTY=5
def set_difficulty(chosen_level):
	if chosen_level=="easy":
		return EASY;
	elif chosen_level=="hard":
		return DIFFICULTY
	else:
		return
def check_answer(guessed_number,answer,attempts):
	if guessed_number<answer:
		print("Your guess is too low.")
		return attempts-1
	elif guessed_number>answer:	
		print("Your guess is too high.")
		return attempts-1
	else:
		print(f"Your guess is right....The answer {answer}")		
def GuessTheNumber():	
	print("Let me think of a number between 1 to 100")
	answer=random.randint(1,100)
	level=input("choose level of difficulty.....type easy or hard: ").lower()
	attempts=set_difficulty(level)
	if(attempts!=EASY and attempts!=DIFFICULTY):
		print("You have entered wrong difficulty level...Play again!!")
		return
	guessed_number=0
	while guessed_number!=answer:
		print(f"you have {attempts} attempts remaining to guess the number.")
		guessed_number=int(input("Guess a number:"))
		attempts=check_answer(guessed_number,answer,attempts)
		if(attempts==0):
			print("You are out of guesses...You lose!!")
			return
		elif(guessed_number!=answer):
			print("Guess again!")

GuessTheNumber()