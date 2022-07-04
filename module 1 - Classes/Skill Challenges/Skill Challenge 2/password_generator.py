import string
import random

class PasswordGenerator:

    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    password_values = {'lowercase': lowercase,
                       'uppercase': uppercase,
                       'digits': digits,
                       'punctuation': punctuation}

    def __init__(self,strength='mid',length=12):
        if strength not in ['low','mid','high']:
            raise 'Strength contains not valid attribute: Use [low,mid,high]'
        if not isinstance(length,int):
            raise 'Length is not an integer value'

        if not length:
            if strength == 'low':
                self.length = 4
            elif strength == 'mid':
                self.length = 12
            elif strength == 'high':
                self.strength = 16

        else:
            self.strength = strength
            self.length = length

    @staticmethod
    def show_input_universe():
        return PasswordGenerator.password_values

    def generate_random_password(self):
        if self.strength == 'low':
            password_attributes = ['lowercase', 'uppercase']
        elif self.strength == 'mid':
            password_attributes = ['lowercase', 'uppercase','digits']
        else:
            password_attributes = ['lowercase', 'uppercase','digits','punctuation']

        password = ''
        for i in range(self.length):
            attribute = random.choice(password_attributes)
            password += random.choice(PasswordGenerator.password_values[attribute])

        return password

m1 = PasswordGenerator('mid')
print(m1.generate_random_password())



