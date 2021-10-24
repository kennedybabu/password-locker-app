#!/usr/bin/env python3.8
from unittest import result
from user import User
from credentials import Credentials
import random
import string
import sys


def create_user(fname, lname, password):
    """
    Function that will create a new user
    """
    new_user = User(fname, lname,password)
    return new_user

def save_user(user):
    """
    Function to save user
    """
    user.save_user()


def create_user_credentials(platform_name, platform_username, platform_password):
    """
    Function that will create a new credential
    """
    new_user_credentials = Credentials(platform_name, platform_username, platform_password)
    return new_user_credentials

def save_user_credentials(credential):
    """
    Function to save user credentials
    """
    Credentials.save_credentials(credential)


def display_credentials():
    """
    A function that will return the credential list
    """
    return Credentials.display_credentials()

def find_user(username):
    """
    Function that will find a user by their username and return the user
    """
    return User.find_by_username(username)

def delete_credentials(credential):
    """
    Function that will delete a user credential
    """
    Credentials.delete_credentials() 

def find_credentials(credential):
    """
    Function that will look for a specific account in the stored credentials
    """

    return Credentials.find_credentials(credential)


def check_existing_credentials(platform):
    """
    Function that will check for a credential
    """
    return Credentials.credential_exists(platform)

@classmethod
def password_gen(length):
    """
    generate random password
    """
    letters = string.ascii_lowercase
    result1 = ''.join((random.sample(letters, length)))  
    platform_password = result1
    return platform_password  


def main():
    print("\n")
    print("\u001b[35mJambo(Hello, in Swahili)!Welcome to Password-Locker!.\u001b[0m")
    print("\n")

    user_name = input("\u001b[36mEnter your user name: \u001b[0m")


    print(f"What would you like to do? A. Login | B. Create an account")

    short_code = input().lower()

    while True:
        if short_code == "a":
            print()
           
            platform_search = input("Enter the platform you want to search for: ")
            if check_existing_credentials(platform_search):
                search_credential = find_credentials(platform_search)

            else:
                print("\u001b[31;1mThe credential was not found, Try Again\u001b[0m")
                
                sys.exit()

        elif short_code == "b":

            print("Create an Account")

            new_user_first_name = input("Enter your first name: ")
            new_user_last_name = input("Enter your last name: ")
            print("Would you like to create your password or generate one, A. Create | B. Generate")
            create_password_option = input().lower()

            if create_password_option == "a":
                create_password = input("Enter your password: ")
                confirmed_password = input("\u001b[33mConfirm password: \u001b[0m")
                if confirmed_password == create_password:
                    print("\u001b[32mAccount Created Succesfully.\u001b[0m")
                    new_user_password = confirmed_password
                    save_user(create_user(new_user_first_name, new_user_last_name,new_user_password))

if __name__ == "__main__":
    main()