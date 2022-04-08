import random
animal_list = ["zebra", "horse", "donkey", "unicorn"]


# testing loop to generate 20 tokens
for item in range(20):
   token = random.choice(animal_list)
   print(token, end='\t') # can wrap output making it easier to screenshot
