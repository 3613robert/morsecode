MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

while True:
    options = input('Would you like to (e)ncrypt or (d)ecrypt a message?: \n')
    if options == 'e':
        message_encrypted = []
        message_user = input('What is the message?: \n').upper()
        message = [char for char in message_user]

        for char in message:
            char = MORSE_CODE_DICT[char]
            message_encrypted.append(char)

        print(message_encrypted)
    if options == 'd' :
        message_morse = []
        message_user = input('What is the message?: \n')
        message_code = [morse.strip() for morse in message_user.split(',')]
        print(message_code)
        for morse in message_code:
            for key, value in MORSE_CODE_DICT.items():
                if value == morse:
                    message_morse.append(key)
        message = ''.join(message_morse)
        print(message.capitalize())