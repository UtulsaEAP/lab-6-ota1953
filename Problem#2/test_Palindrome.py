import unittest
from Palindrome import check_palindrome
import io
import unittest.mock

class TestCheckPalindrome(unittest.TestCase):

    def test_one(self):
        user_input = "sees"
        expected_output = "palindrome: sees"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_two(self):
        user_input = "never odd or even"
        expected_output = "palindrome: never odd or even"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_three(self):
        user_input = "dr awkward"
        expected_output = "palindrome: dr awkward"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
            
    def test_four(self):
        user_input = "evil is alive"
        expected_output = "not a palindrome: evil is alive"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_five(self):
        user_input='no lemon no melon'
        expected_output = "palindrome: no lemon no melon"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)  

    def test_six(self):
        user_input = "taco cat"
        expected_output = "palindrome: taco cat"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_seven(self):
        user_input = "seems"
        expected_output = "not a palindrome: seems"
        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)
    def test_palindrome(self):
        user_input = "bob"
        expected_output = "palindrome: bob"

        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_not_palindrome(self):
        user_input = "statistics"
        expected_output = "not a palindrome: statistics"

        # Redirect stdout to capture print statements
        with self.subTest(input=user_input):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                check_palindrome(user_input)
                self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
