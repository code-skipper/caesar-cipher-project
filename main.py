alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(plain_text, shift_amount, direction):
  message = ''
  for letter in plain_text:
      if letter in alphabet:
          current_index = alphabet.index(letter)
          # Apply the shift
          if direction == 'encode':
              new_index = (current_index + shift_amount) % 26
          elif direction == 'decode':
              new_index = (current_index - shift_amount) % 26
          shifted_letter = alphabet[new_index]
          message += shifted_letter
      else:
          # Directly add the character if it's not in the alphabet
          message += letter
  print(f'Your {direction}d message: {message}')

# Now calling the ceaser function with direction as an argument as well
ceaser(text, shift, direction)
