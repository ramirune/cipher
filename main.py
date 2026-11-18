from logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text,shift,encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = (alphabet.index(letter) + shift) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Your {encode_or_decode}ed text is {output_text}")

should_continue = True

while should_continue == True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type your shift number:\n"))

    cipher(text=text,shift=shift,encode_or_decode=direction)

    restart = input("Type 'yes' to go again. Otherwise, type 'no':\n")
    if restart == "no":
        should_continue = False
        print("Goodbye!!!")