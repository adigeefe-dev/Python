



print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88         

           88             88                                 
           ""             88                                                               
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                                         
-----------------------------------------------------------------
''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Double for (26+shift_amount)
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt [encode|decode]:")
    if (direction != "encode") and (direction != "decode"):
        print("Invalid choose")
        exit()

    text = input("Type your message:").lower()

    try:
        shift = int(input("Type the shift number:"))
    except:
        print("Give an integer!")
        exit()

    def cipher(start_text,shift_amount,cipher_direction):
        end_text=""

        if cipher_direction == "decode":
            shift_amount *= -1

        for letter in start_text:
            if letter in alphabet:
                position=(alphabet.index(letter))
                new_position= position+shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(f"\nYour {cipher_direction}d text: {end_text}\n")

    shift = shift % 26
    cipher(start_text=text,shift_amount=shift,cipher_direction=direction)
    shall_continue=input("Do you want to shall_continue? [yes|no]:")
    if shall_continue == "no":
        should_continue=False
        print("Veni, vidi, utor cipher...")
        print("Good Bye!")
