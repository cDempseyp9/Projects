from cryptography.fernet import Fernet
import bcrypt
import getpass
import json
import os

class PasswordManager:
    def __init__(self):
        self.master_password_hash = None
        self.passwords = {}
        self.key = None
        self.load_master_password()

    def generate_key(self):
        return Fernet.generate_key()

    def load_key(self):
        try:
            with open("secret.Key", "rb") as key_file:
                self.key = key_file.read()
        except FileNotFoundError:
            self.key = self.generate_key()
            with open("secret.key", "wb") as key_file:
                key_file.write(self.key)

    def encrypt_data(self, data):
        cipher = Fernet(self.key)
        encrypted_data = cipher.encrypt(json.dumps(data).encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        cipher = Fernet(self.key)
        decrypted_data = json.loads(cipher.decrypt(encrypted_data).decode())
        return decrypted_data

    def load_master_password(self):
        try:
            with open("master_password_hash.txt", "rb") as password_file:
                self.master_password_hash = password_file.read()
        except FileNotFoundError:
            self.create_master_password()

    def create_master_password(self):
        print("Create a master password: ")
        while True:
            master_password = getpass.getpass("Enter your master password: ")
            confirm_password = getpass.getpass("Confirm your master password: ")

            if master_password == confirm_password:
                self.master_password_hash = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())
                with open("master_password_hash.txt", "wb") as password_file:
                    password_file.write(self.master_password_hash)
                print("Master password set successfully!")
                break
            else:
                print("Passwords do not match. Please try again") 

    def verify_master_passwords(self, entered_password):
        return bcrypt.checkpw(entered_password.encode(), self.master_password_hash)

    def add_password(self):
        if not self.verify_master_password(getpass.getpass("Enter your password to proceed: ")):
            print("Incorrect master password. Access denied.  ")
            return

        website = input("Enter the website or service name: ")
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        self.passwords[website] = {"username": username, "password": password}
        print("Password added successfully!")

    def view_passwords(self):
        if not self.verify_master_password(getpass.getpass("Enter your master password to proceed: ")):
            print("Incorrect master password. Access denied. ")
            return

        if not self.passwords:
            print(" No passwords stored. ")
            return

        print("Stored passwords:")
        for website, data in self.passwords.items():
            print(f"- Websites: {website}")
            print(f"  Username: {data['username']}")
            print(f"  Passwords: *********")

    def load_data(self):
        try:
            with open("Passwords.dat", "rb") as data_file:
                encrypted_data = data_file.read()
                decrypted_data = self.decrypt_data(encrypted_data)
                self.master_password_hash = decrypted_data["master_password_hash"]
                self.passwords = decrypted_data["passwords"]
        except FileNotFoundError:
            print("No existing data found. Starting with an empty password manager.")


if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.load_key()
    password_manager.load_data()

    while True:
        print("\nSecure Password Manager")
        print("1.  Add Password")
        print("2.  View Passwords")
        print("3.  Save and Exit")
        choice = input("Enter your choice:  ")

        if choice == "1":
            password_manager.add_password()
        elif choice == "2":
            password_manager.view_passwords()
        elif choice == "3":
            password_manager.save_data()
            print("Exiting the password manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again. ")
  
           
                
     
            