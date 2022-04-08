import random
animal_list = ["zebra", "horse", "donkey", "unicorn"]
animal = random.choice(animal_list)
print("welcome to lucky unicorn. each game costs $1")
play = input("press 'Y' to play and 'E' to exit")
if play == 'Y':
    print("you can play from 1 to 10 games.")
elif play == 'E':
    print("bye")
money = int(input("please pay here:"))
while money > 10:
    print("The maximum amount of turns is 10.")
    money = int(input("Please enter a number between 1-10:"))
    if money < 1:
        print("You cannot play 0 or less games.")
        money = int(input("Please enter a number between 1-10:"))
    else:
        print(f"you have payed for {money} amount of games")
while money > 0:
    if animal == "unicorn":
        print("your animal is unicorn and you won $5")
        money -= 1
    elif animal == "zebra":
        print("your animal is zebra and you won $0.50")
    elif animal == "donkey":
        print("your animal is donkey and you didn't win anything")
    elif animal == "horse":
        print("your animal is horse and you won $0.50")
