#Mia Hakkarainen
def encode(password):
    new_password = ""
    for i in range(len(password)):
        new_password += str((int(password[i]) + 3) % 10)
    return new_password
