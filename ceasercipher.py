import mail

cipher_graphic = '''
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    
'''
print('\n\n', cipher_graphic, '\n\n\n')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

shift = int(input("Type the shift number:\n")) % 26
print('\n')
cipher_alphabets = []
for i in range(0, 26):
    cipher_alphabets.append('')

for i in range(0, 26):

    if i + shift >= 26:
        cipher_alphabets[i] = alphabet[(i + shift) - 26]
    else:
        cipher_alphabets[i] = alphabet[i + shift]


def encrypt(message):
    str = ""
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            str += cipher_alphabets[index]
        else:
            str += char
    return str


def decrypt(message):
    str = ""
    for char in message:
        if char in cipher_alphabets:
            index = cipher_alphabets.index(char)
            str += alphabet[index]
        else:
            str += char
    return str


turn_off = False

# emailing cipher code-start
# emailing cipher code-end

while not turn_off:

    try:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\nEnter 'e' to exit\n\n")

        if direction == 'encode':
            text = input("Type your message:\n").lower()
            encrypted_text = encrypt(text)
            print("Encrypted Message: " + encrypted_text + '\n')
            send_mail = input(
                "Do you want to send the encrypted message through mail? Enter 'Y' or press any key and enter to cancel.")

            if send_mail == 'Y':
                # send mail
                receiver_name = input("Receiver's email address: ")
                mail.send_mail(receiver_name, encrypted_text)

        elif direction == 'decode':
            text = input("Type your message:\n").lower()
            print("Decrypted Message: " + decrypt(text) + '\n')
        elif direction == 'e':
            turn_off = True
            print("Thank You for using Cipher Encryption.")
        else:
            print("Error")
            break

    except:
        print("An exception occurred")
