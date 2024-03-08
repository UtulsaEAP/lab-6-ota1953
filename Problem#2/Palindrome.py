'''
Name: Owen Anderson 
Lab Time: THUR 2:00 - 3:15
'''
def check_palindrome(user_input):
    reverse = user_input.replace(" ","")
    if reverse == reverse[::-1]:
        print("palindrome: " + user_input)
    else:
        print("not a palindrome: " + user_input)
    return

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
