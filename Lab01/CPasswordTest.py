import unittest
from CPassword import character
from CPassword import lower
from CPassword import upper
from CPassword import digit
from CPassword import special

# Class to test all the functions of the CPassword that check the validity of password
class validatePassword(unittest.TestCase):

    # Tests the valid lenth of characters in a password
    def test_password_character_length_failure(self):
        self.assertFalse(character('P@ss'))

    def test_password_character_length_success(self):
        self.assertTrue(character('P@ssw0rd'))

    # Tests the lower case in a password
    def test_password_lowercase_failure(self):
        self.assertFalse(lower('P@SSW0RD'))

    def test_password_lowercase_success(self):
        self.assertTrue(lower('P@ssw0rd'))

    # Tests the upper case in a password
    def test_password_uppercase_failure(self):
        self.assertFalse(upper('p@ssw0rd'))

    def test_password_uppercase_success(self):
        self.assertTrue(upper('P@ssw0rd'))

    # Tests digit in a password
    def test_password_digit_failure(self):
        self.assertFalse(digit('P@sswOrD'))

    def test_password_digit_success(self):
        self.assertTrue(digit('P@ssw0rd'))

    # Tests special characters in a password
    def test_password_special_characters_failure(self):
        self.assertFalse(special('Passw0rd'))

    def test_password_special_characters_success(self):
        self.assertTrue(special('P@ssw0rd'))

if __name__ == '__main__':
    unittest.main()