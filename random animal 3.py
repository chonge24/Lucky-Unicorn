import random
animal_list = ["zebra", "Horse", "Donkey", "Unicorn"]
random.choice(animal_list)
while random.choice(animal_list) == "Donkey":
    print("Your animal was Donkey and you won nothing")
if random.choice(animal_list) == "Horse":
    print("Your animal was Horse and you won $0.50")
if random.choice(animal_list) == "zebra":
    print("Your animal was zebra and you won $0.50")
if random.choice(animal_list) == "Unicorn":
    print("Your animal was Unicorn and you won $5")
