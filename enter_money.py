print(" welcome to lucky unicorn. each game costs $1")
payment = 0
play = input("press 'Y' to play and 'E' to exit")
if play == 'Y':
    game_amount = int(input("you can play from 1 to 10 games. please enter how many games you would like to play:"))
    print(f"you need to pay ${game_amount * 1}")
    payment = int(input("enter payment here e.g '7':"))
    if payment < game_amount:
        print(f"you are {game_amount - payment} dollars short")
    elif payment >
