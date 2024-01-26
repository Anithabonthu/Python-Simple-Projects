# rock,paper=paper
# rock,scissor=rock
#paper,scissor=scissor
import random
l=["rock","scissor","paper"]
player1=random.choice(l)
player2=input("rock,scissor,paper")
score1,score2=0,0
print(player1)
if player1==player2:
    score1+=0
    score2+=0
elif player1=="rock":
    if player2=="paper":
        score2+=1
    else:
        score1+=1
elif player1=="scissor":
    if player2=="paper":
        score2+=1
    else:
        score1+=1
elif player1=="paper":
    if player2=="scissor":
        score2+=1
    else:
        score1+=1
else:
    print("wrong choice")
print(score1,score2)
    
