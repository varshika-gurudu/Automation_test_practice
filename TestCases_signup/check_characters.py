import string

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



    