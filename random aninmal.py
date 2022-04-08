import random
animal_list = ["zebra", "horse", "donkey", "unicorn"]
animal = random.choice(animal_list)
if animal == "unicorn":
    print("your animal is unicorn and you won $5")
elif animal == "zebra":
    print("your animal is zebra and you won $0.50")
elif animal == "donkey":
    print("your animal is donkey and you didn't win anything")
elif animal == "horse":
    print("your animal is horse and you won $0.50")
