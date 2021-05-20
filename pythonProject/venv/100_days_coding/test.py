alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift,alphabet):
  encrypted_text = []
  for letters in  text :

    index = alphabet.index(letters)
    new_position = index + shift
    if(new_position>26):
        extra = new_position - 26
        new_text = alphabet[extra]
        encrypted_text.append(new_text)
    else:
        new_text = alphabet[new_position]
        encrypted_text.append(new_text)
  print(encrypted_text)



def decrypt(text,shift,alphabet):
    decrypted_text =[]
    for letters in text :
        index = alphabet.index(letters)
        new_position =  index - shift
        if (new_position < 1):
            extra =
        new_text = alphabet[new_position]
        decrypted_text.append(new_text)
        print(decrypted_text)




if(direction == 'encode'):
  encrypt(text,shift,alphabet)

if(direction == 'decode'):
    decrypt(text,shift,alphabet)








