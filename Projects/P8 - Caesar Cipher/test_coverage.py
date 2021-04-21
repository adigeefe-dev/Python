alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Double for (26+shift_amount)

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    text = input("Type your message:").lower() if (direction == "encode") or (direction == "decode") else exit("Invalid Choose")
    shift = int(input("Type the shift number:")) if text else exit("Empty input!")

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
        
        print(f"\nYour {cipher_direction}d text:{end_text}")

    shift = shift % 26
    cipher(start_text=text,shift_amount=shift,cipher_direction=direction)
    
    shall_continue=input("Do you want to continue? [yes|no]:")
    exit("Good Bye!\nVeni, vidi, utor cipher...") if  shall_continue == "no" else 1
