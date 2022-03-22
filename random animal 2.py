import random
animal_list = ["zebra", "horse", "donkey", "unicorn"]
print(f"your animal is {random.choice(animal_list)}")
animal = random.choice(animal_list)
if animal == "unicorn":
    print("congratulations you won $5")
elif animal == "zebra":
    print("you won $0.50")
elif animal == "horse":
    print("you won $0.50")
elif animal == "donkey":
    print("go cry")
