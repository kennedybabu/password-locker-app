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