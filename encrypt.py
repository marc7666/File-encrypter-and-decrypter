from cryptography.fernet import Fernet
from colorama import Fore

def create_key():
    key = Fernet.generate_key() 
  
    with open('filekey.key', 'wb') as filekey: 
        filekey.write(key)
  
def encryption():

    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 

    fernet = Fernet(key)

    with open('example.csv', 'rb') as file: 
        original = file.read() 
      
    encrypted = fernet.encrypt(original) 
  
    with open('example.csv', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted) 

def decryption():

    with open('filekey.key', 'rb') as filekey: 
        key = filekey.read() 

    fernet = Fernet(key) 
  
    with open('example.csv', 'rb') as enc_file: 
        encrypted = enc_file.read() 
  
    decrypted = fernet.decrypt(encrypted) 
  
    with open('example.csv', 'wb') as dec_file: 
        dec_file.write(decrypted)


if __name__ == "__main__":
    action = input(Fore.MAGENTA + "Encrypt (write 1) or decrypt (write 2)? " + Fore.RESET)
    if action == "1":
        print(Fore.BLUE + "Creating the encryption key..." + Fore.RESET)
        create_key()
        print(Fore.BLUE + "Encrypting..." + Fore.RESET)
        encryption()
        print(Fore.GREEN + "Encryption process complete!" + Fore.RESET)
    if action == "2":
        print(Fore.BLUE + "Reading the key file..." + Fore.RESET)
        print(Fore.BLUE + "Decrypting..." + Fore.RESET)
        decryption()
        print(Fore.GREEN + "Decryption process complete!" + Fore.RESET)