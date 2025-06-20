import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '@', '$', '%', '&', '*', '+']

print("Welcome to PyPassword Generator!")
total_alphas = int(input("How many alphabets would you like in your password?\n"))
total_nums = int(input("How many numbers would you like?\n"))
total_symbs = int(input("How many symbols would you like?\n"))

# 1. Easy Level
password = ""
for char in range(1, total_alphas + 1):
    password += random.choice(alphabets)
    
for num in range(1, total_nums + 1):
    password += random.choice(number)

for symbol in range(1, total_symbs + 1):
    password += random.choice(symbols)

print("Password : ", password) 
#Output : TTgEu29$& OR tHDVr53@& , etc.

password = ""
# 2. Complex Level

password = []
for char in range(1, total_alphas + 1):
    password.append(random.choice(alphabets))
    
for num in range(1, total_nums + 1):
    password.append(random.choice(number))

for symbol in range(1, total_symbs + 1):
    password.append(random.choice(symbols))

random.shuffle(password)
passw = ""
for char in password:
    passw += char

print(passw)