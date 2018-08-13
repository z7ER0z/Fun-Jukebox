import random
import sys



while True:
    print(" (1) Dice with input range \n (2) Guess The Number \n (3) Determine your faith with the magic 8ball! \n (4) Caesar Cipher! (encode and decode fun messages)")
    choice = int(input())
    if choice == 1:
        # Dice Sim
        bolo = "ye"
        print("Pick your range!")
        range_min = int(input("From: "))
        range_max = int(input("To: "))
        while 1 == 1:
            if bolo == "ye":
                roll = int(random.randint(range_min, range_max))
                print(roll)
                print("Wanna' roll again? ye if you wanna'!")
                bolo = input()
            else:
                break
    elif choice == 2:
        # Guess the number
        i = 0
        while i == 0:
            print("Pick the range for the number")
            range_min = int(input("Min: "))
            range_max = int(input("Max: "))
            print("Your number is between", range_min, " and ", range_max)
            number = int(random.randint(range_min, range_max))
            guess = int(input("Guess!: "))
            if guess == number:
                print("You somehow got it! \n The number was ", number)
                i = 1
            else:
                print("Awh. Too bad! \n The number was ", number)
                i = 1
    elif choice == 3:
        # Magic 8Ball
        while True:
            question = input("Ask away! The magic 8ball is wating. \n [~~Hit enter to exit~~] \n")
            replies = random.randint(1, 8)
            if question == "":
                break
            elif replies == 1:
                print("For certain")
            elif replies == 2:
                print("Outlook looks good!")
            elif replies == 3:
                print("The gods say no")
            elif replies == 4:
                print("Try again later")
            elif replies == 5:
                print("You may rely on it")
            elif replies == 6:
                print("No!")
            elif replies == 7:
                print("Hmmm. Concentrate and ask again")
            elif replies == 8:
                print("My answer is hazy. Try again")
    elif choice == 4:
        # Caesar Cipher
        while True:
            symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            key_range = len(symbols)
            def get_mode():
                while True:
                    print("Do you please to encrypt or decrypt a message?")
                    mode = input().lower()
                    if mode in ["encrypt", "e", "decrypt", "d"]:
                        return mode
                    else:
                        print('Type either "encrypt" or "e" or "decrypt" or "d" then hit enter!')

            def get_message():
                return input("Enter your message: ")

            def get_key():
                key = 0
                while True:
                    key = int(input("Enter your super duper secret key (1-26): " ))
                    if key >= 1 and key <= key_range:
                        return key
                    else:
                        print("The key range is between 1 and 26, 1 and 26 included")

            def get_translated_message(mode, message, key):
                translated = ""
                if mode[0] == "d":
                    key = -key
                translated = ""
                for symbol in message:
                        if symbol.isalpha():
                            num = ord(symbol)
                            num += key
                            if symbol.isupper():
                                if num > ord("Z"):
                                   num -= 26
                                elif num < ord("A"):
                                   num += 26
                            elif symbol.islower():
                                if num > ord("z"):
                                   num -= 26
                                elif num < ord("a"):
                                   num += 26       
                            translated += chr(num)
                        else:
                            translated += symbol
                return translated

            mode = get_mode()
            message = get_message()
            key = get_key()
            print("Your translated text is: ", get_translated_message(mode, message, key), "\n\n")
            break
        
                
