import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define your ceaser function without the loop
def ceaser(plain_text, shift_amount, direction):
    message = ''
    for letter in plain_text:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            if direction == 'encode':
                new_index = (current_index + shift_amount) % 26
            elif direction == 'decode':
                new_index = (current_index - shift_amount) % 26
            shifted_letter = alphabet[new_index]
            message += shifted_letter
        else:
            message += letter
    print(f'Your {direction}d message: {message}')

# Use a while loop here to keep asking the user if they want to continue
run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)

    replay = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if replay != 'yes':
        run = False
        print('Goodbye!')
