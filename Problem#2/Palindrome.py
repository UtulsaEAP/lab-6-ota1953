'''
Name: Owen Anderson 
Lab Time: THUR 2:00 - 3:15
'''
def check_palindrome(user_input):
    new_string =""
    for i in user_input:
        new_string += i[::-1]
    
    if user_input == new_string:
        return "palindrome: " + new_string
    else:
        return "not a palindrome: " + user_input

if __name__ == "__main__":
    user_input = input()
    print(check_palindrome(user_input))
