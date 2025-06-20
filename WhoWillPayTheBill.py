import random
friends = ["Aditya", "Piyush", "Jayesh", "Prasad", "Om", "Atharva", "Anuj", "Sumedh"]

# 1st Option
random_index = random.randint(0, len(friends)-1)
print(f"{friends[random_index]} will pay the bill.")

# 2nd Option
print(f"{random.choice(friends)} will pay the bill.")