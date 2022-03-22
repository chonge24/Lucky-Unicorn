import random
animal_list = ["zebra", "horse", "donkey", "unicorn"]
if random.choice(animal_list) == "unicorn":
    print("your animal is unicorn and you won $5")
elif random.choice(animal_list) == "zebra":
    print("your animal is zebra and you won $0.50")
elif random.choice(animal_list) == "donkey":
    print("your animal is donkey and you didn't win anything")
elif random.choice(animal_list) == "horse":
    print("your animal is horse and you won $0.50")
