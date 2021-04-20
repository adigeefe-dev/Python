alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
if (direction != "encode") and (direction != "decode"):
    print("Invalid choose")
    exit()

text = input("Type your message:").lower()

try:
    shift = int(input("Type the shift number:"))
except:
    print("Give an integer")
    exit()



def encrypt(text,shift):
    cipher_text=""
    for letter in text:
        position=(alphabet.index(letter))
        new_position=position+shift
        
        #Debugging
        while new_position>=26:
            new_position -=26

        new_letter=alphabet[new_position]
        cipher_text+=new_letter
            
    print(f"\nYour Crypted Text:{cipher_text}")

def decode(text,shift):
    cipher_text=""
    for letter in text:
        position=(alphabet.index(letter))
        new_position=position-shift
        
        #Debugging
        while new_position<0:
            new_position +=26
            
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"\nYour Decrypted Text:{cipher_text}")


if direction.lower()=="encode":
    encrypt(text,shift)
elif direction.lower()=="decode":
    decode(text,shift)
