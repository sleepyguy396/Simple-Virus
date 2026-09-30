from cryptography.fernet import Fernet
import os


# Generate a key for encryption and decryption
def generate_key():
    key = Fernet.generate_key() # Creating a unique encryption key
    with open("random_key.key", "wb") as key_file: # Storing the key in a file
        key_file.write(key)


# Load the encryption key from the file
def load_key():
    return open("random_key.key", "rb").read() #Reading the key from the file


# Encrypt file
def encrypt_file(file_path, key):
    fernet = Fernet(key) # initailize the encryption method with the key
    with open(file_path, "rb") as file: 
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data) # Encrypting the content
    with open(file_path, "wb") as file: # Writing the encrypted content back to the file
        file.write(encrypted_data)
    print(f"File '{file_path}' has been encrypted successfully.")


# Decrypt file
def decrypt_file(file_path, key):
    fernet = Fernet(key) # initailize the decryption method with the key
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data) # Decrypting the content
    with open(file_path, "wb") as decrypted_file: # Writing the decrypted content back to the file
        decrypted_file.write(decrypted_data)
    print(f"File '{file_path}' has been decrypted successfully.")

# Encrypt files in a directory
def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path): # Traversing/Scanning through the directory
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key) # Encrypting each file

# Main function
def main():
    target_directory = input("Enter the directory path to encrypt: ")  
    
    # Generate a key if it doesn't exist
    if not os.path.exists("random_key.key"):
        generate_key()
        print("Encryption key generated.")

    key = load_key() # Load the generated key
    print("Key loaded successfully, encrypting files...")

    # Encrypt the files in the specified directory
    encrypt_directory(target_directory, key)

    # Decrypt the files in the specified directory
    print("Decrypting files...")
    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key) # Decrypting each file


if __name__ == "__main__":
    main()
