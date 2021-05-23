import string
import re

class check_char:

    @staticmethod
    def check_special_char(name):

        invalid_char = set(string.punctuation)
        if any(char in invalid_char for char in name):
            print('string has special characters')
        else:
            print('string is good')


    @staticmethod
    def check_numeric(name):

        new = [i for i in name if i.isdigit()]
        print('it has digits')

    @staticmethod
    def check_characters(phone):

        if phone.isalnum():
            print('it has numbers')
        else:
            print('it has characters too')

    @staticmethod
    def check_email(email):

        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):  # if the email is valid
            print("That's a valid email!")
        else:
            print("That's an invalid email!")







