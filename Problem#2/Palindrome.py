'''
Name: Owen Anderson 
Lab Time: THUR 2:00 - 3:15
'''
def check_palindrome(user_input):
    new_string = ""
    index = len(user_input)
    while index > 0:
        new_string += user_input[index-1]
        index -= 1
    if user_input == new_string:
        return "palindrome: " + new_string
    else:
        return "not a palindrome: " + user_input

if __name__ == "__main__":
    user_input = input()
    print(check_palindrome(user_input))
