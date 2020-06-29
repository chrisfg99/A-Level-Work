def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print ('Enter your message:')
    return input()


def getKeyword():
    Keyword = str(input("What is your chosen Keyword"))
    chris = len(Keyword) * 10
    getMessage = New_Message
    letter_inc = 0
    for letter in Keyword:
        if letter_inc == chris:
            letter_inc = 0
        Keyword = Keyword + Keyword[letter_inc]
        letter_inc = letter_inc + 1
        return Keyword

def getTranslatedMessage(Keyword, mode, message):
    if mode[0] == 'd''decrypt''Decrypt':
        number = 0
        for symbol in New_Message:
            MessageValue = ord(New_Message[number])
            KeywordValue = ord(Keyword[number])
            EncryptedValue =  MessageValue + KeywordValue
            EncryptedLetter = chr(EncryptedValue)
            number = number + 1
            a.apend(EncryptedLetter)
        return a

    if mode [1] == 'e' 'encrypt' 'Encrypt':
        number = 0
        for symbol in New_Message:
            MessageValue = ord(New_Message[number])
            KeywordValue = ord(Keyword[number])
            EncryptedValue =  MessageValue - KeywordValue
            EncryptedLetter = chr(EncryptedValue)
            number = number + 1
            a.apend(EncryptedLetter)
        return a
        
mode = getMode()
New_Message = getMessage()
Keyword = getKeyword()

print('your translated text is:')
print(getTranslatedMessage(Keyword, mode, New_Message))
