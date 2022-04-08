print("welcome to lucky unicorn. each game costs $1")
play = input("press 'Y' to play and 'N' to exit")
if play == 'Y':
    print("you can play from 1 to 10 games.")
    money = int(input("please pay here:"))
    while money > 10:
        print("The maximum amount of turns is 10.")
        money = int(input("Please enter a number between 1-10:"))
    if money < 1:
        print("You cannot play 0 or less games.")
        money = int(input("Please enter a number between 1-10:"))
    else:
        print(f"you have payed for {money} amount of games")
elif play == 'N':
    print("bye")
else:
    print("system cannot read your input. please enter 'Y' or 'N'")
    play = input("press 'Y' to play and 'N' to exit:")

