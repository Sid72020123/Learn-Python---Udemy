# --- Project 8 ---

from string import ascii_uppercase, ascii_lowercase

logo = """
 ▄████▄   ▄▄▄      ▓█████   ██████  ▄▄▄       ██▀███  
▒██▀ ▀█  ▒████▄    ▓█   ▀ ▒██    ▒ ▒████▄    ▓██ ▒ ██▒
▒▓█    ▄ ▒██  ▀█▄  ▒███   ░ ▓██▄   ▒██  ▀█▄  ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒▓█  ▄   ▒   ██▒░██▄▄▄▄██ ▒██▀▀█▄  
▒ ▓███▀ ░ ▓█   ▓██▒░▒████▒▒██████▒▒ ▓█   ▓██▒░██▓ ▒██▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
  ░  ▒     ▒   ▒▒ ░ ░ ░  ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░
░          ░   ▒      ░   ░  ░  ░    ░   ▒     ░░   ░ 
░ ░            ░  ░   ░  ░      ░        ░  ░   ░     
░                                                     
 ▄████▄   ██▓ ██▓███   ██░ ██ ▓█████  ██▀███          
▒██▀ ▀█  ▓██▒▓██░  ██▒▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒        
▒▓█    ▄ ▒██▒▓██░ ██▓▒▒██▀▀██░▒███   ▓██ ░▄█ ▒        
▒▓▓▄ ▄██▒░██░▒██▄█▓▒ ▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄          
▒ ▓███▀ ░░██░▒██▒ ░  ░░▓█▒░██▓░▒████▒░██▓ ▒██▒        
░ ░▒ ▒  ░░▓  ▒▓▒░ ░  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░        
  ░  ▒    ▒ ░░▒ ░      ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░        
░         ▒ ░░░        ░  ░░ ░   ░     ░░   ░         
░ ░       ░            ░  ░  ░   ░  ░   ░             
░\n     
"""

print(logo)

ALPHABETS = list(ascii_uppercase + ascii_lowercase)


def caesar(convert_type, msg, shift):
    result = ""
    if convert_type == "decode":
        shift *= -1
    for letter in msg:
        try:
            idx = ALPHABETS.index(letter)
        except ValueError:
            result += letter
            continue
        new_index = idx + shift
        new_index %= len(ALPHABETS)
        result += ALPHABETS[new_index]

    return result


confirm = "yes"

while confirm == "yes":
    choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip().lower()

    if choice == "encode":
        msg = input("Enter your message: ")
        shift_num = int(input("Enter the shift number: "))
        print(f"\nHere's your ENCODED result: {caesar("encode", msg, shift_num)}")

    elif choice == "decode":
        enc_msg = input("Enter your ENCODED message: ")
        shift_num = int(input("Enter the shift number: "))
        print(f"\nHere's your DECODED result: {caesar("decode", enc_msg, shift_num)}")

    else:
        print("Invalid input given! Please try again...")

    confirm = (
        input(
            "\nType 'yes' if you want to go again, otherwise type 'no' or any input & press enter: "
        )
        .strip()
        .lower()
    )
