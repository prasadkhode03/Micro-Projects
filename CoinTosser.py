import random
print("Welcome to Coin Toss")
toss = random.randint(0, 1)
if toss == 1:
    print("We got Head")
else:
    print("We got Tails")