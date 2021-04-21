alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Double for (26+shift_amount)
should_continue=True
while should_continue:
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
    contuine=input("Do you want to contuine?")
    if contuine == "no":
        should_continue=False
    print("Veni, vidi, utor cipher...")
    print("Good Bye!")
