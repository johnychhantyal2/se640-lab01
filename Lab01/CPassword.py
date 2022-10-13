# CPassword class that takes user's input for password and checks
# the validity of password using functions below
class CPassword:
    def __init__(self):
        self.input = input('Please enter the password: ')
        self.character = character(self.input)
        self.lower = lower(self.input)
        self.upper = upper(self.input)
        self.digit = digit(self.input)
        self.special = special(self.input)

# Function that checks the length of the characters in a password
def character(password):
    if len(password) >= 6:
        return True
    print('FAILED:  must be at least 6 characters long.')
    return False

# Function that checks the lower case letter in a password
def lower(password):
    for char in password:
        if char.islower():
            return True
    print('FAILED:  must contain at least one lowercase letter.')
    return False

# Function that checks the upper case letter in a password
def upper(password):
    for char in password:
        if char.isupper():
            return True
    print('FAILED:  must contain at least one uppercase letter.')
    return False

# Function that checks the digit in a password
def digit(password):
    for char in password:
        if char.isnumeric():
            return True
    print('FAILED:  must contain at least one digit.')
    return False

# Function that checks the special characters in a password
def special(password):
    specialChars = '~!@#$%^&*()+'
    for char in password:
        if char in specialChars:
            return True
    print('FAILED:  must contain at least one special character.')
    return False

# Main function
def main():
    isTrying = True

    while isTrying:
        password = CPassword()
        validPassword = True
        if (not password.character) or (not password.lower) or (not password.upper) or (not password.digit) or (not password.special):
            validPassword = False
            print('Invalid password. Please try again...')

        if validPassword:
            print('Valid password')
            isTrying = False

if __name__ == "__main__":
    main()