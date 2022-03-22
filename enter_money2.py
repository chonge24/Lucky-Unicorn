print("welcome to lucky unicorn. each game costs $1")
play = input("press 'Y' to play and 'E' to exit")
if play == 'Y':
    print("you can play from 1 to 10 games.")
    payment = int(input("please pay here:"))
    print(f"you have payed for {payment} amount of games")
