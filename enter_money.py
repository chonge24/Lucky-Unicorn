money = int(input("please pay here:"))
while money > 10:
    print("The maximum amount of turns is 10.")
    money = int(input("Please enter a number between 1-10:"))
    if money < 1:
        print("You cannot play 0 or less games.")
        money = int(input("Please enter a number between 1-10:"))
else:
    print(f"you have payed for {money} amount of games")
