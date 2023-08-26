import random

# making random number
Computer_num = random.randint(1, 3)
if Computer_num == 1:
    Computer = "stone"
elif Computer_num == 2:
    Computer = "paper"
else:
    Computer ="scissors"
    
 # choosing num by player   
player_num = int(input("1:stone, 2:paper 3:scissors  Enter a number:"))
if player_num == 1:
    Player ="stone"
elif Computer_num == 2:
    Player ="paper"
else:
    Player ="scissors"
    
# creating rules
if Player == Computer:
    print("play again")
elif  Player == 'stone':
    if Computer == 'paper':
        print('player win!!')
    else:
        print('computer win!!')
elif Player == "paper":
    if Computer == 'stone':
        print('player win!!')
    else:
        print('computer win!!')
elif Player == "scissors":
    if Computer == 'paper':
        print('player win!!')
    else:
        print('computer win!!')
    

    