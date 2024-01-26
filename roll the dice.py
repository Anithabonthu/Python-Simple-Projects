import random
min_value,max_value=1,6
game_start=True
while(game_start):
    num=random.randint(min_value,max_value+1)
    print(num)
    roll_again=input("if you want to roll the dice again yes or no:").lower()
    if roll_again=="yes":
        game_start=True
    else:
        game_start=False
