import unittest
from unittest.mock import patch
from contactlist import process_user_contacts

class TestProcessUserContacts(unittest.TestCase):

    def test_contact_found(self):
        user_input = "Joe,123-5432 Linda,983-4123 Frank,867-5309"
        with patch('builtins.input', side_effect=["Frank"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("867-5309")

    def test_contact_not_found(self):
        user_input = "Jasmin,312-3145 Scooby-Doo,093-1212"
        with patch('builtins.input', side_effect=["Jasmin"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("312-3145")

    def test_additional_case(self):
        user_input = "Mo,391-0993 Rachel,019-1265 Ruby,010-8712 Steve,312-3318 Maria,871-0091"
        with patch('builtins.input', side_effect=["Rachel"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("019-1265")

    def test_four(self):
        user_input = "Sally,190-1214 Sue,119-6442"
        with patch('builtins.input', side_effect=["Sue"]):
            with patch('builtins.print') as mock_print:
                process_user_contacts(user_input)
                mock_print.assert_called_once_with("119-6442")

if __name__ == '__main__':
    unittest.main()
