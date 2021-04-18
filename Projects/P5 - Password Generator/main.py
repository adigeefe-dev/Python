#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PRIMITIVE 2X-HARD PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password:")) 
nr_symbols = int(input(f"How many symbols would you like in your password:"))
nr_numbers = int(input(f"How many numbers would you like in your password:"))

#   PASSED X
#--------------------------------------------------
#   Eazy Level - Order not randomised:
#       e.g. 4 letter, 2 symbol, 2 number = JduE&!91



#   DONE +
#--------------------------------------------------
#   Hard Level - Order of characters randomised:
#       e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# PRIMITIVE 2X-HARD
password=""
random_letters=[]
random_numbers=[]
random_symbols=[]
total=(nr_letters+nr_symbols+nr_numbers)

#Randomize
for x in range(0,nr_letters):
    random_letters+=letters[random.randint(0,len(letters)-1)]
for y in range(0,nr_numbers):
    random_numbers+=numbers[random.randint(0,len(numbers)-1)]
for z in range(0,nr_symbols):
    random_symbols+=symbols[random.randint(0,len(symbols)-1)]

#Char pool
newlist=(random_letters+random_numbers+random_symbols)

#Select from char pool and add to password
for i in range(0,total):
    indexoflist=newlist[random.randint(0,len(newlist)-1)]
    password+=indexoflist
    newlist.remove(indexoflist)
    
if nr_letters <= 5 and nr_symbols <= 4 and nr_numbers <= 5:
    print("Your NOT secure password is: "+password)
elif (nr_letters >= 5 and nr_symbols >= 5 and nr_numbers >= 5):
    print("Your ULTRA, CRAZY, PSYCHO, SUPER, DUPER, SECURE PASSWORD is: "+password)
else:
    print("Your ULTRA SECURE PASSWORD is: "+password)

## HARD LEVEL

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password:")) 
# nr_symbols = int(input(f"How many symbols would you like in your password:"))
# nr_numbers = int(input(f"How many numbers would you like in your password:"))

# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is: {password}")