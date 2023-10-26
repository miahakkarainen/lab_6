#Mia Hakkarainen
def encode(password):
    new_password = ""
    for i in range(len(password)):
        new_password += str((int(password[i]) + 3) % 10)
    return new_password

def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        decoded_digit = (int(digit) - 3) % 10
        decoded_password += str(decoded_digit)
    return decoded_password


if __name__ == "__main__":

    passwords = []

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option_number = int(input("Please enter an option:"))

        if option_number == 3:
            exit()
        elif option_number == 1:
            password = str(input("Please enter your password to encode:"))
            new_password = encode(password)
            passwords.append(new_password)
            print(f"Your password has been encoded and stored!")
        elif option_number == 2:
            last_encoded_password = passwords[-1]
            last_original_password = decode(last_encoded_password)
            print(f"The encoded password is {last_encoded_password}, and the original password is {last_original_password}.")
